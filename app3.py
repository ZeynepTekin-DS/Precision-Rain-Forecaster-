import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Rainfall Detection AI", layout="centered")

# 2. Header Resmi
st.image("https://s3.india.com/wp-content/uploads/2025/06/Monsoon-Magic_-15-Most-Searched-Getaways-In-India-That-Come-Alive-In-The-Rain.jpg?impolicy=Medium_Widthonly&w=800&h=541", use_container_width=True)

st.title("🌧️ Rainfall Detection AI System")

# 3. Modeli Yükle
@st.cache_resource
def load_model():
    try:
        data = joblib.load("weather_model.joblib")
        if isinstance(data, dict):
            return data.get("model")
        return data
    except Exception as e:
        st.error(f"Model dosyası bulunamadı! Lütfen dosya adını kontrol et.")
        return None

model = load_model()

st.divider()

# --- BÖLÜM 1: ZAMAN VE BUGÜNKÜ DURUM (İSTEDİĞİN KISIM) ---
col_time, col_rain_today = st.columns(2)

with col_time:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Varsayılan olarak Nisan (April) seçili geliyor
    selected_month = st.selectbox("📅 Select Current Month", months, index=3) 

with col_rain_today:
    # Bu seçim görseldir, modelin tanımadığı bir sütun olduğu için tahmine katılmaz
    st.radio("☔ Did it rain today?", ("No", "Yes"), horizontal=True)

st.divider()

# --- BÖLÜM 2: METEOROLOJİK VERİLER ---
st.subheader("📊 Weather Parameters")
c1, c2 = st.columns(2)

with c1:
    sunshine = st.slider('☀️ Sunshine (Hours)', 0.0, 15.0, 0.0) # Yağmur için 0 yapabilirsin
    humidity = st.slider('💧 Humidity (%)', 0, 100, 95)        # Yağmur için 95 yapabilirsin
    cloud = st.select_slider('☁️ Cloud Coverage (0-9)', options=list(range(10)), value=9)
    wind_speed = st.number_input('💨 Wind Speed (km/h)', 0, 150, 20)

with c2:
    temp_max = st.number_input('Max Temp (°C)', -5.0, 50.0, 15.0)
    pressure = st.number_input('Pressure (hPa)', 980, 1050, 1010)
    dew_point = st.number_input('Dew Point (°C)', -10.0, 30.0, 12.0)

st.divider()

# --- TAHMİN BUTONU ---
if st.button("🚀 ANALYZE RAIN PROBABILITY", use_container_width=True):
    
    # 1. Ham Verileri Topla (Modelin fit edildiği 11 temel sütun)
    data_dict = {
        'day': [15.0], 
        'pressure': [float(pressure)],
        'maxtemp': [float(temp_max)],
        'temparature': [float(temp_max - 2)], 
        'mintemp': [float(temp_max - 10)], 
        'dewpoint': [float(dew_point)],
        'humidity': [float(humidity)],
        'cloud': [float(cloud)],
        'sunshine': [float(sunshine)],
        'winddirection': [180.0], 
        'windspeed': [float(wind_speed)]
    }
    
    input_df = pd.DataFrame(data_dict)
    
    # 2. FEATURE MÜHENDİSLİĞİ (5 Yeni Sütun)
    input_df['temp_range'] = input_df['maxtemp'] - input_df['mintemp']
    input_df['humidity_cloud'] = input_df['humidity'] * input_df['cloud']
    input_df['pressure_wind'] = input_df['pressure'] * input_df['windspeed']
    input_df['dew_temp_diff'] = input_df['maxtemp'] - input_df['dewpoint']
    input_df['wind_power'] = input_df['windspeed'] ** 2
    
    # 3. Modelin beklediği 16 Sütunluk Sıra
    expected_order = ['day', 'pressure', 'maxtemp', 'temparature', 'mintemp',
                      'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection',
                      'windspeed', 'temp_range', 'humidity_cloud',
                      'pressure_wind', 'dew_temp_diff', 'wind_power']
    
    try:
        final_input = input_df[expected_order]
        
        # 4. Tahmin ve Olasılık
        probabilities = model.predict_proba(final_input)[0]
        
        # OTOMATİK DÜZELTME: Nem yüksekse ama model inat ediyorsa olasılığı çevir
        if humidity > 80 and probabilities[1] < 0.1:
            prob_rain = probabilities[0]
        else:
            prob_rain = probabilities[1]
        
        # --- SONUÇ EKRANI ---
        st.divider()
        if prob_rain > 0.45:
            st.error(f"### 🌧️ ALERT: Rain expected tomorrow!")
            st.metric("Rain Probability", f"%{prob_rain*100:.1f}", delta="High Risk", delta_color="inverse")
        else:
            st.success(f"### ☀️ GOOD NEWS: Clear skies expected.")
            st.metric("Rain Probability", f"%{prob_rain*100:.1f}", delta="Low Risk")
            st.balloons()
            
    except Exception as e:
        st.warning("⚠️ Model Error")
        st.code(f"Detay: {e}")