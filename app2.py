import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

st.set_page_config(page_title="Plant Disease Expert", page_icon="🌿")

st.title("🌿 Plant Disease Diagnostic System")
st.write("Professional AI-based classification for 5 types of Cassava diseases.")

@st.cache_resource
def load_my_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'Final_Model.keras')
    return tf.keras.models.load_model(model_path)

# Load the model and handle errors
try:
    model = load_my_model()
except Exception as e:
    st.error("Model file not found! Make sure 'Final_Model.keras' is in the folder.")
    st.stop()

# ALL 5 CLASSES (0, 1, 2, 3, 4)
class_names = [
    'Cassava Bacterial Blight (CBB)',        # 0
    'Cassava Brown Streak Disease (CBSD)',   # 1
    'Cassava Green Mottle (CGM)',            # 2
    'Cassava Mosaic Disease (CMD)',          # 3
    'Healthy Leaf'                           # 4
]

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # CRITICAL FIX: Convert image to RGB to handle 4th channel (Alpha) errors
    # This ensures the model sees exactly (224, 224, 3)
    display_img = image.convert('RGB')
    
    st.image(display_img, caption='Processed Image', use_container_width=True)
    
    # Preprocessing
    img_resized = display_img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prediction logic for all classes
    st.write("### 🔍 AI Analysis in Progress...")
    predictions = model.predict(img_array)
    result_index = np.argmax(predictions) # Finds the best match among 0,1,2,3,4
    
    # Final Result Output
    st.success(f"**Final Diagnosis:** {class_names[result_index]}")
    st.info("Note: Please consult an agricultural expert for definitive action plans.")