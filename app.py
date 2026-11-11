import streamlit as st
import pickle
import pandas as pd

# वेबसाइट की सेटिंग्स और टाइटल
st.set_page_config(page_title="Tip Predictor", page_icon="💵")
st.title("💵 Restaurant Tip Predictor")
st.write("नीचे दी गई जानकारी भरें और जानें कि कितनी टिप (Tip) मिल सकती है:")

# मॉडल लोड करें
model = pickle.load(open("model.pkl", "rb"))

# सुंदर Frontend फॉर्म (Inputs)
col1, col2 = st.columns(2)

with col1:
    total_bill = st.number_input("Total Bill ($)", min_value=1.0, value=20.0, step=0.5)
    sex = st.selectbox("Gender (Sex)", ["Male", "Female"])
    day = st.selectbox("Day", ["Sun", "Sat", "Thur", "Fri"])

with col2:
    size = st.number_input("Group Size (लोगों की संख्या)", min_value=1, max_value=20, value=2)
    smoker = st.selectbox("Smoker", ["No", "Yes"])
    time = st.selectbox("Time", ["Dinner", "Lunch"])

# भविष्यवाणी करने का बटन
if st.button("Predict Tip 💰", use_container_width=True):
    # डेटा को मॉडल के फॉर्मेट में बदलें
    input_data = pd.DataFrame({
        "total_bill": [total_bill],
        "sex": [sex],
        "smoker": [smoker],
        "day": [day],
        "time": [time],
        "size": [size]
    })
    
    # मॉडल से रिजल्ट निकालें
    prediction = model.predict(input_data)
    st.success(f"### अनुमानित टिप (Predicted Tip): ${prediction[0]:.2f}")
