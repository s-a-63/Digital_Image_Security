# Digital Image Privacy Protection Tool

A Streamlit-based adversarial image transformation tool that reduces AI image classification confidence by applying localized, gradient-based pixel perturbations while maintaining perceptual image quality.

- Live Demo (Streamlit): https://digitalimagesecurity-mbehygmmyuwgmqfklvbrr2.streamlit.app/
- Demo Video: https://youtu.be/QfHy34D6Ths  

---

## Overview

As AI vision models become increasingly powerful, images shared online can be analyzed and classified automatically. This project explores how small, controlled pixel-level perturbations can reduce the confidence of pretrained image classification models without significantly altering how the image appears to humans.

Developed during **HackSRM 7.0 – AI/ML Track (24-hour National Hackathon)**.

This project demonstrates practical adversarial machine learning concepts through an interactive web application.

---

## Key Features

- Upload images through an interactive Streamlit interface
- Detect face regions using MediaPipe for localized modification
- Apply iterative gradient-based adversarial perturbations
- Reduce prediction confidence of a pretrained ResNet18 model
- Preserve perceptual similarity using Gaussian smoothing
- Real-time transformation and confidence visualization

---

## Technical Architecture
1. Face Localization
- Uses MediaPipe Face Detection to identify face regions
- Generates a smooth mask for localized perturbation

2️. Classification Model
- Uses pretrained ResNet18 (PyTorch)
- Computes original prediction label and confidence

3️. Adversarial Optimization
- Applies iterative gradient-based perturbations
- Constrains perturbation magnitude using epsilon bounds
- Monitors softmax confidence reduction during iterations
- Stops early when confidence drops below threshold

4️. Output
- Displays transformed image
- Shows final AI confidence score
- Reports success based on confidence reduction threshold

## Methodology

The pipeline:

1. User uploads an image
2. Image is resized and passed to ResNet18
3. Original prediction label is computed
4. Face region is detected and masked
5. Iterative gradient-based updates modify pixels within mask
6. Model confidence is re-evaluated
7. Transformed image and final confidence are displayed
The goal is to experimentally reduce model confidence while maintaining visual similarity.
---

## Results

- Successfully reduced AI recognition accuracy during evaluation  
- Demonstrated model evasion capability under controlled settings  
- Observed perceptual trade-offs at higher perturbation strengths  

---

## Live Application

**Access the live tool here:**  
https://digitalimagesecurity-mbehygmmyuwgmqfklvbrr2.streamlit.app/

---

## Evaluation

Tested against a pretrained ResNet18 classification model to measure:

- Reduction in softmax prediction confidence
- Iterative confidence tracking
- Visual distortion trade-offs at varying perturbation strengths

Note: The system reduces classification confidence under controlled conditions and does not claim universal evasion of production-grade facial recognition systems.

---

## Use Cases

- Adversarial machine learning demonstrations
- AI robustness experimentation
- Educational projects on model vulnerability
- Privacy-focused AI research prototypes

---

## Team Members

Team name: M.A.P.S

- Danthuluri Kiranmai Meghana
- Mojjada Sahiti
- Vemireddy Anjali Devi
- Gedda Padma Sree

---

## Disclaimer

This project is developed strictly for educational and research purposes in adversarial machine learning and AI robustness. It is not intended for misuse, malicious evasion, or deceptive applications.

---
