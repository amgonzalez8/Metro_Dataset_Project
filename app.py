import streamlit as st
import pickle
import numpy as np
import pandas as pd

model=pickle.load(open('model_metro.pkl','rb'))

st.set_page_config(page_title="Operational Status Prediction", layout="centered")
st.markdown("<h1 style='text-align: center;'>🔧 Prediction of the Operating Status of Equipment</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Complete the following fields to predict the status of the equipment:</p>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("🌡️ Pressure & Temperature")
col1, col2, col3 = st.columns(3)

with col1:
    TP2 = st.number_input('TP2', min_value=-1.0, max_value=50.0, value=50.0)
    DV_pressure = st.number_input('DV_pressure', min_value=-1.0, max_value=10.0, value=5.0)
    Oil_temperature = st.number_input('Oil_temperature (°C)', min_value=0.0, max_value=100.0, value=60.0)

with col2:
    TP3 = st.number_input('TP3', min_value=0.0, max_value=50.0, value=50.0)
    Reservoirs = st.number_input('Reservoirs', min_value=0.0, max_value=20.0, value=20.0)
    Oil_level = st.number_input('Oil_level (%)', min_value=0.0, max_value=1.0, value=0.5)

with col3:
    H1 = st.number_input('H1', min_value=-1.0, max_value=50.0, value=25.0)
    MPG = st.number_input('MPG', min_value=0.0, max_value=1.0, value=0.5)
    Caudal_impulses = st.number_input('Caudal_impulses', min_value=0.0, max_value=1.0, value=0.5)

st.subheader("⚡ Electrical and Control Parameters")
col4, col5, col6 = st.columns(3)

with col4:
    Motor_current = st.number_input('Motor_current', min_value=0.0, max_value=10.0, value=10.0)

with col5:
    COMP = st.number_input('COMP', min_value=0.0, max_value=1.0, value=0.5)

with col6:
    DV_eletric = st.number_input('DV_eletric', min_value=0.0, max_value=1.0, value=0.5)

st.subheader("🧠 Sensors and Actuators")
col7, col8, col9 = st.columns(3)

with col7:
    Towers = st.number_input('Towers', min_value=0.0, max_value=1.0, value=0.5)

with col8:
    LPS = st.number_input('LPS', min_value=0.0, max_value=1.0, value=0.5)

with col9:
    Pressure_switch = st.number_input('Pressure_switch', min_value=0.0, max_value=1.0, value=0.5)


st.markdown("---")
if st.button("🚀 Predict Operating Status"):
    input_array = np.array([[TP2, TP3, H1, DV_pressure, Reservoirs, Oil_temperature,
                             Motor_current, COMP, DV_eletric, Towers, MPG,
                             LPS, Pressure_switch, Oil_level, Caudal_impulses]])
    
    prediction = model.predict(input_array)
    
    status = {
        0: "🔴 Off",
        1: "🟡 No load",
        2: "🟢 Load",
        3: "🔵 Start",
        4: "⚪ Unknown"
    }
    
    result = status.get(prediction[0], "Unidentified value")
    
    st.success(f"✅ The predicted operating status is: **{result}**")
