import base64
from io import BytesIO

import streamlit as st
from PIL import Image
from groq import Groq
import config

# App configuration
st.set_page_config(page_title="AI Visionary", page_icon="🕵️", layout="centered")

# Review styles dictionary matching project requirements
STYLES = {
    "Normal": (
        "Look at this food image carefully and write a clear, detailed culinary report. "
        "Describe the dish, ingredients, presentation, and overall vibe."
    ),
    "Funny": (
        "Look at this food image carefully and write a funny review. "
        "Mention elements, plating flaws, and make it highly playful and humorous, "
        "but still accurately describe the dish."
    ),
    "Detective": (
        "Look at this food image like a culinary detective. "
        "Write an investigation-style report looking for clues about how it was made, "
        "freshness observations, and smart chef deductions."
    ),
    "Dramatic": (
        "Look at this food image and describe it in a dramatic, cinematic way. "
        "Make the flavors sound epic, the plating legendary, and the text expressive."
    ),
    "Story Mode": (
        "Look at this food image and write a short story-like review. "
        "Set a fictional scene around who is eating it, where they are, and the mood."
    ),
}

# Initialize Groq client
client = Groq(api_key=config.GROQ_API_KEY)

st.title("🍽️ AI Food Image Reviewer")
st.write("Upload a food photo and let AI create a stylized critique!")
st.markdown(
    "Choose an image, pick a review style, and click **Analyse Image**. "
    "The AI will study the image and write a detailed report."
)

def analyze_image(uploaded_file, style):
    # Encode the uploaded image file to base64
    encoded = base64.b64encode(uploaded_file.getvalue()).decode("utf-8")
    
    # Request completion from Groq vision model
    response = client.chat.completions.create(
        model=config.GROQ_VISION_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": STYLES.get(style, STYLES["Normal"])},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{uploaded_file.type};base64,{encoded}"
                        },
                    },
                ],
            }
        ],
        temperature=0.8,
        max_completion_tokens=500,
    )
    # Fixed the response access syntax error (.choices[0] instead of choice[0])
    return response.choices[0].message.content

# File uploader widget
uploaded_file = st.file_uploader(
    "Upload a food image",
    type=["png", "jpg", "jpeg", "webp"],
)

# Style picker dropdown
report_style = st.selectbox("Choose review style", list(STYLES))

# Display the uploaded image
if uploaded_file:
    st.image(
        Image.open(BytesIO(uploaded_file.getvalue())),
        caption="Uploaded Image",
        use_container_width=True,
    )

# Execution trigger button
if st.button("Analyse Image"):
    if not config.GROQ_API_KEY:
        st.error("Groq API key is missing. Please add it to your .env file.")
    elif not uploaded_file:
        st.warning("Please upload an image first.")
    else:
        with st.spinner("The AI is studying your dish..."):
            try:
                report_content = analyze_image(uploaded_file, report_style)
                st.success("Report ready!")
                st.subheader("AI Food Report")
                st.write(report_content)
            except Exception as error:
                st.error(f"Something went wrong: {error}")