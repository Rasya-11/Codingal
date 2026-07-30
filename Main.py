import base64
import io
import json
import streamlit as st
from PIL import Image, ImageDraw
from groq import Groq
import config

# 1. Page Configuration
st.set_page_config(page_title="AI Visual Report Generator", page_icon="📊", layout="wide")

# Initialize the Groq client using config values
client = Groq(api_key=config.GROQ_API_KEY)

# 2. Responsible AI Structured JSON System Prompt
PROMPT = """Analyze this image and return ONLY valid JSON.
Identify all clearly visible important objects in the image.
For each object, return: name, short_label, fun_metadata, confidence, box
The "box" must use percentages 0 to 100 with x, y, w, h.

Responsible AI Safety Rules:
- Include all clearly visible important objects.
- Do not guess hidden or unclear objects. If unsure, skip the object.
- Keep labels short and kid-friendly.
- Confidence must be one of: high, medium, low.
- Never identify a real person by name. If a person appears, use generic labels like "person", "smiling adult", "child", or "seated person".
- Do not guess identity, age, profession, or relationship.

Format:
{"scene_title":"short futuristic title","objects":[{"name":"person","short_label":"smiling adult","fun_metadata":"person detected near the center","confidence":"high","box":{"x":20,"y":10,"w":25,"h":60}}]}"""

# 3. Helper Functions
def analyze_image(file):
    """Encodes the uploaded image and sends it to the Groq Vision model."""
    encoded = base64.b64encode(file.getvalue()).decode()
    response = client.chat.completions.create(
        model=config.GROQ_VISION_MODEL,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": PROMPT},
                {"type": "image_url", "image_url": {"url": f"data:{file.type};base64,{encoded}"}}
            ],
        }],
        temperature=0.2,
        max_completion_tokens=1200,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)

def get_pixel_coords(box, img_w, img_h):
    """Parses and converts percentage-based bounding box dictionary data into pixel integers."""
    x_min = int((box["x"] / 100) * img_w)
    y_min = int((box["y"] / 100) * img_h)
    x_max = int(((box["x"] + box["w"]) / 100) * img_w)
    y_max = int(((box["y"] + box["h"]) / 100) * img_h)
    
    # Clip coordinates inside image dimensions to avoid clipping crashes
    return (
        max(0, min(x_min, img_w - 1)),
        max(0, min(y_min, img_h - 1)),
        max(0, min(x_max, img_w - 1)),
        max(0, min(y_max, img_h - 1))
    )

# 4. User Interface
st.title("📊 AI Visual Report Generator")
st.write("Upload an image to generate annotated outputs, structured analytics, and object data tables.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read the file directly into a PIL image object
    original_img = Image.open(uploaded_file).convert("RGB")
    w, h = original_img.size
    
    # Display the file inside the web layout immediately
    st.image(original_img, caption="Target Image Source", width=400)
    
    if st.button("Generate Report"):
        with st.spinner("Processing vision model data..."):
            try:
                # Retrieve parsed structured JSON
                data = analyze_image(uploaded_file)
                st.success("Analysis Complete!")
                
                # Setup PIL RGBA Transparency canvas layers
                annotated_img = original_img.copy()
                overlay = Image.new("RGBA", annotated_img.size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(overlay)
                
                objects = data.get("objects", [])
                table_rows = []
                
                # Loop through objects to composite the transparency vectors
                for obj in objects:
                    box = obj.get("box")
                    if box:
                        coords = get_pixel_coords(box, w, h)
                        
                        # Composite transparent fills and outline borders onto overlay channel
                        draw.rectangle(coords, outline=(255, 0, 0, 255), fill=(255, 0, 0, 45), width=3)
                        draw.text((coords[0] + 5, coords[1] + 5), obj.get("short_label"), fill=(255, 255, 255, 255))
                        
                        # Format elements directly for clean data table rendering
                        table_rows.append({
                            "Object Name": obj.get("name"),
                            "Label Provided": obj.get("short_label"),
                            "Confidence Level": obj.get("confidence"),
                            "Metadata Details": obj.get("fun_metadata")
                        })
                
                # Multi-layer image alpha compositing step
                final_img = Image.alpha_composite(annotated_img.convert("RGBA"), overlay)
                
                # Display multiple output sections across clean UI layout divisions
                st.subheader(f"Report Summary: {data.get('scene_title', 'Generic Scene')}")
                
                tab1, tab2, tab3 = st.tabs(["🖼️ Annotated Image Output", "📊 Summary Data Table", "⚙️ Raw Parsed JSON"])
                
                with tab1:
                    st.image(final_img, caption="Processed Image Overlay", use_container_width=True)
                
                with tab2:
                    if table_rows:
                        st.table(table_rows)
                    else:
                        st.warning("No clear structured object arrays detected to index inside table rows.")
                        
                with tab3:
                    st.json(data)
                    
            except Exception as error:
                st.error(f"Failed to execute structural runtime pipeline: {error}")
