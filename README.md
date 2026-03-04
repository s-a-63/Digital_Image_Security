# Digital Image Privacy Protection Tool

A privacy-preserving image transformation tool designed to mitigate AI-based facial recognition and deepfake misuse by applying adversarial perturbations that reduce AI model detection accuracy while maintaining perceptual image quality.

Live Demo (Streamlit): (https://digitalimagesecurity-mbehygmmyuwgmqfklvbrr2.streamlit.app/)
Demo Video: https://youtu.be/QfHy34D6Ths  

---

## Overview

With the rise of AI-powered facial recognition and deepfake technologies, publicly shared images can be exploited without user consent. This project introduces an adversarial image transformation pipeline that modifies uploaded images to disrupt AI-based feature extraction while preserving human-visible content.

Developed during **HackSRM 7.0 – AI/ML Track (24-hour National Hackathon)**.

---

## Key Features

- Upload images through an interactive Streamlit web interface  
- Apply controlled adversarial perturbations to reduce AI recognition confidence  
- Balance privacy protection with perceptual quality preservation  
- Real-time image transformation and visualization  

---

## Methodology

The system applies controlled pixel-level perturbations designed to interfere with feature embeddings used in pretrained computer vision models.  

The pipeline:
1. Accepts user-uploaded image
2. Applies adversarial noise / parameter modifications
3. Evaluates impact on model inference confidence
4. Outputs privacy-enhanced image

We experimentally analyzed the trade-off between:
- Perturbation strength
- Recognition accuracy reduction
- Visual distortion

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

Tested against pretrained computer vision models to measure:
- Recognition confidence reduction
- Structural similarity preservation
- Visual distortion levels

---

## Use Cases

- Social media privacy enhancement
- Adversarial machine learning research
- AI security experimentation
- Deepfake risk mitigation studies

---

## Team Members

Team name: M.A.P.S

- Danthuluri Kiranmai Meghana
- Mojjada Sahiti
- Vemireddy Anjali Devi
- Gedda Padma Sree

---

## Disclaimer

This project is intended for educational and research purposes in AI privacy and adversarial robustness. It should not be used for malicious or deceptive activities.

---
