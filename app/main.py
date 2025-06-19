import streamlit as st
from transformers import pipeline
from utils.preprocessing import clean_text
import matplotlib.pyplot as plt

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Page setup
st.set_page_config(page_title="CareNet AI", page_icon="💬")
st.title("💬 CareNet AI – Your Mental Health Companion")
st.write("Share how you're feeling today. Let us guide you with AI-powered emotional support.")

# Input from user
user_input = st.text_area("How are you feeling today?", height=150)

if st.button("Analyze Mood"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Preprocess and analyze
        cleaned = clean_text(user_input)
        result = classifier(cleaned)[0]
        label = result['label']
        score = result['score']

        st.subheader("🧠 Mood Analysis Result")
        st.markdown(f"**Detected Mood:** `{label}`")
        st.markdown(f"**Confidence:** `{score:.2f}`")

        # Mood-based suggestion
        if label == "POSITIVE":
            st.success("You seem to be in a good mood. Keep it up! 😊")
        elif label == "NEGATIVE":
            st.info("You might be feeling low. Consider trying a mindfulness exercise or journaling. 🧘‍♀️")
        else:
            st.write("Neutral mood detected. Try expressing more to get a clearer analysis.")

        # Plot a simple confidence bar
        fig, ax = plt.subplots()
        ax.bar(["Confidence"], [score], color='skyblue')
        ax.set_ylim(0, 1)
        st.pyplot(fig)

