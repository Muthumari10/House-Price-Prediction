import pandas as pd
import streamlit as st
import pickle
import time

with open ("house_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="House Price Predictor", layout="centered")


st.markdown("""
<style>

/* ===== FULL PAGE INTERACTIVE BACKGROUND ===== */
.stApp {
    min-height: 100vh;
    background: linear-gradient(
        -45deg,
        #0f172a,
        #1e3a8a,
        #020617,
        #38bdf8
    );
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== REMOVE STREAMLIT DEFAULT WHITE AREAS ===== */
header, footer, [data-testid="stToolbar"] {
    background: transparent !important;
}

/* ===== GLASS MAIN CARD ===== */
.block-container {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    padding: 2.5rem;
    box-shadow: 0 30px 60px rgba(0,0,0,0.35);
}

/* ===== INTERACTIVE TITLE ===== */
.title-container {
    text-align: center;
    margin-bottom: 30px;
}

.app-title {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #0f172a;
    transition: all 0.4s ease;
    cursor: pointer;
}

.app-title:hover {
    transform: scale(1.06);
    color: #1e3a8a;
    text-shadow: 0px 10px 30px rgba(30,58,138,0.6);
}

/* ===== INPUT STYLES ===== */
input {
    border-radius: 12px !important;
    border: 2px solid #e5e7eb !important;
    padding: 10px !important;
    transition: all 0.3s ease-in-out !important;
}

input:hover {
    border-color: #38bdf8 !important;
}

input:focus {
    border-color: #1e3a8a !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,0.35) !important;
}

/* ===== NUMBER INPUT BUTTONS ===== */
button[kind="secondary"] {
    border-radius: 10px !important;
    background: linear-gradient(135deg, #1e3a8a, #38bdf8) !important;
    color: white !important;
}

/* ===== PREDICT BUTTON ===== */
.stButton > button {
    background: linear-gradient(135deg, #1e3a8a, #38bdf8);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.6rem 1.8rem;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.35s ease;
    box-shadow: 0 10px 25px rgba(56,189,248,0.4);
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 20px 40px rgba(56,189,248,0.6);
}

/* ===== ALERT BOX ===== */
.stAlert {
    border-radius: 16px !important;
}

</style>

<div class="title-container">
    <div class="app-title">
        Property Cost Estimation System
    </div>
</div>

""", unsafe_allow_html=True)



feature_name = ['TotalBathrooms','BedroomAbvGr','GrLivArea']

bathroom = st.number_input("Enter Total No. of Bathroom:", min_value = 0.0, max_value=7.0)
bedroom = st.number_input("Enter Total No. of Bedroom:", min_value=0.0, max_value=10.0)
area = st.number_input("Enter the living area (in sq ft):", min_value=0.0, max_value=6000.0)

st.info(
    f"""
    **Your selection**
    - 🛁 Bathrooms: {bathroom}
    - 🛏 Bedrooms: {bedroom}
    - 📐 Area: {area} sq ft
    """
)
if st.button("PREDICT"):
    with st.spinner("Predicting Price"):
        time.sleep(1)
    house = pd.DataFrame([[bathroom, bedroom, area]], columns=feature_name)
    price=model.predict(house)
    st.success(f"🏠 Predicted Price: ₹ {price[0]:,.2f}")
    if price[0] < 150000:
        st.warning("💰 Budget House")
    elif price[0] < 300000:
        st.info("🏡 Mid-range House")
    else:
        st.success("🏰 Premium House")




