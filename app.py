import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import mediapipe as mp

# --- STREAMLIT FRONTEND SETUP ---
st.set_page_config(page_title="AI Face Cloaker", layout="wide")
st.title("🛡️ Instagram-Friendly AI Face Cloaker")
st.write("Upload a high-res photo to make it undetectable to AI while keeping it post-ready.")

# --- YOUR ORIGINAL PARAMETERS ---
START_EPS = 0.10
MAX_EPS = 0.25
MAX_ITERATIONS = 1000
FEATHER_AMOUNT = 45

# --- BACKEND INITIALIZATION ---
@st.cache_resource
def load_models():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.resnet18(pretrained=True).to(device).eval()
    
    # Updated import for newer MediaPipe versions
    import mediapipe as mp
    mp_face_detection = mp.solutions.face_detection
    
    face_detector = mp_face_detection.FaceDetection(
        model_selection=1, 
        min_detection_confidence=0.5
    )
    
    return device, model, face_detector

device, model, face_detector = load_models()

# --- YOUR ORIGINAL LOGIC FUNCTIONS (Unchanged) ---
def create_ultra_smooth_mask(image_pil):
    img_np = np.array(image_pil)
    h, w, _ = img_np.shape
    mask = np.zeros((h, w, 3), dtype=np.float32)
    results = face_detector.process(img_np)
    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y = int(bbox.xmin * w), int(bbox.ymin * h)
            mw, mh = int(bbox.width * w), int(bbox.height * h)
            mask[max(0, y-20):min(h, y+mh+20), max(0, x-20):min(w, x+mw+20)] = 1.0
    
    mask_tensor = torch.from_numpy(mask).permute(2, 0, 1).unsqueeze(0).to(device)
    return transforms.GaussianBlur(kernel_size=91, sigma=FEATHER_AMOUNT)(mask_tensor)

def apply_high_res_cloak(model, images, mask, original_label, status_placeholder):
    images = images.clone().detach().to(device)
    adv_images = images.clone().detach() + (torch.rand_like(images) * 2 - 1) * START_EPS
    
    loss_fn = nn.CrossEntropyLoss()
    current_eps = START_EPS

    for i in range(MAX_ITERATIONS):
        adv_images.requires_grad = True
        outputs = model(adv_images)
        loss = -loss_fn(outputs, original_label) 
        grad = torch.autograd.grad(loss, adv_images)[0]

        adv_images = adv_images.detach() - (0.01 * grad.sign())
        delta = torch.clamp(adv_images - images, min=-current_eps, max=current_eps)
        adv_images = torch.clamp(images + (delta * mask), 0, 1).detach()
        
        if i % 100 == 0:
            conf = torch.softmax(model(adv_images), dim=1).max().item()
            status_placeholder.text(f"Processing: Iteration {i} | AI Confidence: {conf:.2%}")
            
            if conf > 0.90 and current_eps < MAX_EPS:
                current_eps += 0.02
            
            if conf < 0.40: break

    return adv_images

# --- STREAMLIT INTERACTION LOGIC ---
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    raw_img = Image.open(uploaded_file).convert('RGB')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(raw_img, use_container_width=True)

    if st.button("🚀 Apply Cloak"):
        status = st.empty()
        status.text("Initializing Attack...")
        
        # Preprocessing
        transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
        img_tensor = transform(raw_img).unsqueeze(0).to(device)
        
        with torch.no_grad():
            original_label = torch.argmax(model(img_tensor), dim=1)
        
        # Processing
        soft_mask = create_ultra_smooth_mask(raw_img.resize((224, 224)))
        protected_img_tensor = apply_high_res_cloak(model, img_tensor, soft_mask, original_label, status)
        
        # Output Display
        with col2:
            st.subheader("Cloaked Result")
            protected_img_np = protected_img_tensor.squeeze().cpu().permute(1, 2, 0).numpy()
            st.image(protected_img_np, use_container_width=True)
            
            with torch.no_grad():
                final_conf = torch.softmax(model(protected_img_tensor), dim=1).max().item()
            
            st.metric("Final AI Confidence", f"{final_conf:.2%}")
            
            if final_conf < 0.50:
                st.success("✅ SUCCESS: High-Res Face is now UNDETECTABLE!")
            else:
                st.error("❌ FAILURE: Image is too stubborn. Try resizing down.")