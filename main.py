import io
import requests
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Mountain Scenery Generator", page_icon="🏔️", layout="centered")

OPTIONS = {
    "Mountain type": ["Snowy Alps", "Volcanic Peaks", "Rocky Canyons", "Green Highlands", "Mystic Floating Mountains"],
    "Weather": ["Clear Sky", "Stormy Thunderstorm", "Dense Fog", "Golden Hour Sunshine", "Northern Lights (Aurora)"],
    "Time of day": ["Sunrise", "Midday", "Sunset", "Midnight", "Twilight"],
    "Mood": ["Peaceful and Serene", "Epic and Dramatic", "Mysterious and Eerie", "Bright and Cheerful"],
    "Art style": ["Photorealistic", "Fantasy Oil Painting", "Anime Landscape Style", "Minimalist Vector Art", "Watercolor"]
}

st.session_state.setdefault("generated_scenery", None)

st.title("🏔️ AI Mountain Scenery Generator")
st.write("Design breathtaking mountain landscapes using artificial intelligence!")
st.markdown("Select your preferences below to build your dynamic custom prompt, then click **Generate Scenery**.")

st.subheader("Customize Your Landscape")

selections = {}
for label, items in OPTIONS.items():
    selections[label] = st.selectbox(f"Choose {label.lower()}", items)

extra_details = st.text_area(
    "Extra details", 
    placeholder="Example: A small wooden cabin by a crystal-clear lake..."
).strip()

prompt_parts = [
    f"A breathtaking view of {selections['Mountain type']}",
    f"with {selections['Weather']}",
    f"during {selections['Time of day']}",
    f"creating a {selections['Mood']} atmosphere",
    f"in {selections['Art style']} art style",
    "highly detailed, masterpiece, 8k resolution"
]
base_prompt = ", ".join(prompt_parts)
final_prompt = f"{base_prompt}, {extra_details}" if extra_details else base_prompt

with st.expander("👀 See the AI prompt"):
    st.write(final_prompt)

if st.button("✨ Generate Scenery"):
    with st.spinner("Generating your mountain masterpiece..."):
        try:
            cleaned_prompt = requests.utils.quote(final_prompt)
            image_url = f"https://image.pollinations.ai/prompt/{cleaned_prompt}"
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                st.session_state.generated_scenery = image
                st.success("Your landscape scenery is ready!")
            else:
                st.error(f"Server responded with status code: {response.status_code}")
        except Exception as e:
            st.error(f"Something went wrong during generation: {e}")

if st.session_state.generated_scenery:
    st.image(st.session_state.generated_scenery, caption="Your AI Mountain Scenery", use_container_width=True)
    buffer = io.BytesIO()
    st.session_state.generated_scenery.save(buffer, format="PNG")
    st.download_button(
        label="📥 Download Mountain Scenery",
        data=buffer.getvalue(),
        file_name="mountain_scenery.png",
        mime="image/png"
    )

#cd "c:\Users\Prashant\Desktop\Codingal1\Codingal\Module10\Lesson54\Homework"
#streamlit run main.py