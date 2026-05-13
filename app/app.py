import streamlit as st
import pickle
import pandas as pd
import os

# =========================
# LOAD MODEL (SAFE PATH)
# =========================
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# =========================
# UI
# =========================
st.set_page_config(page_title="Admission Predictor")

st.title("🎓 Graduate Admission Predictor")

st.markdown("### Enter your academic profile")

col1, col2 = st.columns(2)

with col1:
    gre = st.slider("GRE Score", 260, 340, 300)
    toefl = st.slider("TOEFL Score", 0, 120, 100)
    rating = st.slider("University Rating", 1, 5, 3)
    research = st.selectbox("Research Experience", [0, 1])

with col2:
    sop = st.slider("SOP Strength", 1.0, 5.0, 3.0)
    lor = st.slider("LOR Strength", 1.0, 5.0, 3.0)
    gpa = st.slider("GPA", 0.0, 10.0, 7.5)
    
if st.button("Predict Admission Chance"):

    input_data = pd.DataFrame(
        [[gre, toefl, rating, sop, lor, gpa, research]],
        
      columns=[
    "GRE Score",
    "TOEFL Score",
    "University Rating",
    "SOP",
    "LOR",
    "GPA",
    "Research"
]
    )

    prediction = model.predict(input_data)[0]

    st.subheader("Result")

    st.metric(label="Admission Probability", value=f"{prediction:.2f}")

    if prediction > 0.75:
        st.success("High chance of admission")
    elif prediction > 0.5:
        st.warning("Moderate chance")
    else:
        st.error("Low chance")