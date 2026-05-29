import io
import streamlit as st
from huggingface_hub import InferenceClient
import config

st.set_page_config(page_title="AI Avatar Creator", page_icon="🎨", layout="centered")


OPTIONS = {
"avatar type": ["boy hero", "girl hero", "wizard", "robot explorer", "space warrior", "animal adventurer"],
"hairstyle": ["short spiky hair", "curly hair", "long straight hair", "ponytail", "glowing hair", "helmet"],
"outfit": ["superhero suit", "magical robe", "space armor", "casual hoodie", "battle costume", "royal outfit"],
"expression": ["happy", "confident", "excited", "brave", "mysterious", "playful"],
"background": ["forest", "space station", "magic castle", "city skyline", "rainbow world", "cloud kingdom"],
"art style": ["cartoon style", "anime style", "3D game style", "fantasy illustration", "comic style"],
}

client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0"
    token=config.HF_TOKEN)
st.session_state.setdefault("generated_image", None)

st.title("🎨 AI Avatar Creator")
st.write("Create your own avatar with AI!")
st.markdown("Choose your avatar details or write your own custom prompt, then click **Generate Avatar**.")
st.subheader("Create you Avatar")

mode = st.selectbox("Choose prompt mode", ["Use Avatar Builder", "Write Custom Prompt"])

