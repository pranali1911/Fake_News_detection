import streamlit as st
import joblib

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

vectorizer = joblib.load("vectorizer.jb")
model_lr = joblib.load("lr_model.jb")
model_dtc = joblib.load("DTC_model.jb")

st.title("Fake News Detector")
st.write("Enter a news Article below to check whether it is fake or Real.")

news_input = st.text_area("News Article:", "", placeholder="Paste your news article here...")

if st.button("check News"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model_dtc.predict(transform_input)
        # prediction = model_lr.predict(transform_input)

        if prediction[0] == 1:
            st.success("✅ The News is Real!")
        else:
            st.error("❌ The News is Fake!")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
