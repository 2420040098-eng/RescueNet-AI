import streamlit as st

st.set_page_config(
    page_title="RescueNet AI",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 RescueNet AI")
st.subheader(
    "Multi-Agent Disaster Prediction, Emergency Coordination "
    "and Resource Allocation Framework"
)

st.write(
    "RescueNet AI helps analyze disaster risk and support "
    "emergency response decisions."
)

st.divider()

st.header("🌍 Disaster Information")

location = st.text_input("Location", "Chennai")

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    value=100.0
)

temperature = st.number_input(
    "Temperature (°C)",
    value=30.0
)

population = st.number_input(
    "Population",
    min_value=0,
    value=100000
)

if st.button("🔍 Analyze Disaster Risk"):

    risk_score = (
        rainfall * 0.5
        + temperature * 0.2
        + (population / 10000) * 0.3
    )

    if risk_score >= 70:
        risk = "🔴 HIGH"
    elif risk_score >= 40:
        risk = "🟠 MEDIUM"
    else:
        risk = "🟢 LOW"

    st.success(f"Location: {location}")

    st.metric("Disaster Risk", risk)
    st.metric("Risk Score", round(risk_score, 2))

    st.info(
        "Coordinator Agent: Disaster analysis completed."
    )
