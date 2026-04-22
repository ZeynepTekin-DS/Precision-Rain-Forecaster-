🌿 CassavaGuard AI: Mobile-Compatible Deep Learning-Based Plant Disease Diagnosis System

APPLICATION LINK (Hugging Face / GitHub): 

https://huggingface.co/spaces/zeynepptkn/cassava-leaf-disease-classifier  ----https://github.com/ZeynepTekin-DS/-cassava-leaf-disease-classifier

PROJECT SUMMARY: 📖 This study was developed to automatically diagnose viral and bacterial diseases in the Cassava (Manihot esculenta) plant—a primary food source in developing countries—through leaf photographs. By utilizing deep learning techniques to enhance agricultural productivity, the project offers a mobile solution capable of distinguishing between 4 different disease types and healthy leaves with over 77% accuracy.
METHODS USED:

Transfer Learning (MobileNetV2): 🧠 Google's MobileNetV2 architecture was utilized to achieve maximum efficiency with limited data and computational power. This model, pre-trained with ImageNet weights, was specialized to capture plant pathology features.

Strategic Fine-Tuning: ⚙️ The training was conducted in two stages: in the first stage, the base model was frozen while the classifier layers (Head) were trained. In the second stage, all layers were unfrozen, and a low learning rate (1e-5) was applied to allow the model to learn micro-details on the plants, such as spots and discoloration.

Optimization & Callbacks: ⚖️ During training, the learning rate was dynamically optimized using ReduceLROnPlateau, and EarlyStopping was employed to prevent overfitting. The best weights were sealed in .keras format using ModelCheckpoint.
DATA PREPROCESSING & IMAGE ENGINEERING:

Standardization & Scaling: 🛠️ All input images were resized to 224x224 according to MobileNetV2 standards, and pixel values were normalized to the [0, 1] range.

Robust Preprocessing: 🧹 To ensure the model remains accurate under real-world conditions (varying light and angles), 4-channel (RGBA) images were stabilized using a .convert('RGB') filter.

Validation Strategy: 📊 The dataset was split into training and validation sets for unbiased evaluation and cross-checking.
KEY RESULTS:

High Diagnostic Performance: 🏆 The model achieved a validation accuracy of 77.34% among complex and visually similar leaf diseases. A training accuracy of 90.16% was reached, proving the model's high learning capacity.

Balanced Classification: 📊 Analysis showed that the model demonstrates high sensitivity, particularly in identifying CMD (Mosaic Disease) and Healthy classes.

Edge AI Readiness: 📱 By selecting the MobileNetV2 architecture, the model was optimized for low-latency performance, allowing for diagnosis in seconds even on low-end mobile devices.
NOTES:

Interactive Web Interface: 🎨 Thanks to the user interface developed with Streamlit, farmers and agricultural engineers can upload leaf photos and receive "instant diagnosis" within seconds.

Global Accessibility: ☁️ The trained model has been deployed live on Hugging Face Spaces, serving as an end-to-end AI product contributing to the digital transformation of agriculture.

📂 Model Storage Notice

    [!IMPORTANT]

    Due to GitHub's file size limits, the trained model file (Final_Model.keras) could not be uploaded here. However, you can access the model file and the fully functional application via the Hugging Face link provided at the top of this page.

Prepared By: Zeynep Tekin

Date: April 4, 2026