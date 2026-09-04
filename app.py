# ===== LESSON 1 — Build the Magic Gesture Recognizer =========================
# Goal : Load a Teachable Machine model, capture a gesture, detect it,
#        and map it to a spell name.
# Run  : streamlit run lesson1_boilerplate/app.py
# =============================================================================

# ---------- PROVIDED — do not edit below this line ---------------------------
import streamlit as st
from PIL import Image
import Module12.Lesson67.tensorflow310_env.config as config
from Module12.Lesson67.tensorflow310_env.gesture_utils import load_local_teachable_machine_model, predict_gesture_from_image

st.set_page_config(page_title=config.APP_TITLE, page_icon=config.APP_ICON, layout="wide")

# Cleans raw model labels into friendly names
LABEL_MAP = {
    "Open Palm": "Palm", "Palm": "Palm", "Peace": "Peace",
    "Pointer": "Pointer", "Point": "Pointer",
    "Thumbs Up": "Thumbs Up", "Thumbsup": "Thumbs Up", "No Gesture": "No Gesture",
}

# Dark fantasy CSS — pre-built for you
def render_styles():
    st.markdown("""
        <style>
        .stApp { background: radial-gradient(circle at top, #241339 0%, #100914 42%, #07070b 100%); color: #f5efff; }
        .hero  { padding: 22px; border-radius: 22px; border: 1px solid rgba(191,158,255,.20);
                 background: linear-gradient(135deg,rgba(44,24,70,.92),rgba(15,12,30,.96)); margin-bottom: 1rem; }
        .panel { padding: 20px; border-radius: 22px; border: 1px solid rgba(191,158,255,.18);
                 background: rgba(255,255,255,.03); box-shadow: 0 0 32px rgba(118,80,255,.10); margin-bottom: 1rem; }
        .card  { padding: 14px; border-radius: 16px; background: rgba(94,67,170,.14);
                 border: 1px solid rgba(186,163,255,.18); margin-bottom: 10px; text-align: center; }
        .pill  { display: inline-block; padding: 7px 14px; border-radius: 999px;
                 background: rgba(108,75,214,.18); border: 1px solid rgba(193,170,255,.18);
                 color: #efe7ff; margin-bottom: 12px; }
        </style>""", unsafe_allow_html=True)
# ---------- END PROVIDED ------------------------------------------------------


# TODO 1 — Gesture → Spell mapping  (~4 lines)
# Create a dict called GESTURE_SPELLS mapping:
#   "Palm" → "Shield of Light"
#   "Peace" → "Healing Aura"
#   "Pointer" → "Lightning Strike"
#   "Thumbs Up" → "Phoenix Blessing"

# GESTURE_SPELLS = { ... }

GESTURE_SPELLS = {
"Palm": "Shield of Light",
"Peace": "Healing Aura",
"Pointer": "Lightning Strike",
"Thumbs Up": "Phoenix Blessing",
}

# TODO 2 — Cached model loader  (~3 lines)
# Decorate with @st.cache_resource(show_spinner=False)
# Call load_local_teachable_machine_model(str(config.MODEL_PATH), str(config.LABELS_PATH))
# Return the result.

# @st.cache_resource(show_spinner=False)
# def get_model():
#     ...
@st.cache_resource(show_spinner=False)
def get_model():
    return load_local_teachable_machine_model(
    str(config.MODEL_PATH),
    str(config.LABELS_PATH)
    )

# TODO 3 — Label normalizer  (~2 lines)
# Use LABEL_MAP.get(label.strip(), label.strip()) to return the cleaned label.

# def normalize(label: str) -> str:
#     ...
def normalize(label: str) -> str:
    return LABEL_MAP.get(label.strip(), label.strip())


def prediction_panel(image: Image.Image, source: str):
    st.image(image, caption='Gesture image', width='content')
    st.markdown(f'<div class="pill">Source: {source.title()}</div>',
                unsafe_allow_html=True)
    try:
        model, labels = get_model()
        pred = predict_gesture_from_image(model, labels, image)
        pred['label'] = normalize(pred['label'])
        for item in pred['top_predictions']:
            item['label'] = normalize(item['label'])
        st.success(f"Detected gesture: **{pred['label']}**")
        st.progress(float(pred['confidence']),
                    text=f"Confidence: {pred['confidence']:.1%}")
        spell = GESTURE_SPELLS.get(pred['label'], 'Arcane Pulse')
        c1, c2 = st.columns(2)
        c1.markdown(f'<div class="card"><b>Detected Gesture</b><br><br>{pred["label"]}</div>',
                    unsafe_allow_html=True)
        c2.markdown(f'<div class="card"><b>Mapped Spell</b><br><br>{spell}</div>',
                    unsafe_allow_html=True)
        with st.expander('All prediction scores'):
            for item in pred['top_predictions']:
                st.progress(float(item['confidence']),
                            text=f"{item['label']} — {item['confidence']:.1%}")
    except Exception as e:
        st.error(f'Model error: {e}\n\nTip: use Python 3.10/3.11 and tensorflow==2.15.0')


# TODO 5 — Main app layout  (~20 lines)
# def main():
#   render_styles()
#   st.markdown hero div with config.APP_ICON + config.APP_TITLE
#   st.expander with info about the 4 gestures
#   st.markdown '<div class="panel">'
#   tabs = st.tabs(["📷 Webcam Capture", "🖼️ Upload Image"])
#   tab[0]: cam = st.camera_input(...)
#           if cam: prediction_panel(Image.open(cam).convert("RGB"), "webcam")
#           else: st.info(...)
#   tab[1]: up = st.file_uploader(..., type=["png","jpg","jpeg"])
#           if up: prediction_panel(Image.open(up).convert("RGB"), "upload")
#           else: st.info(...)
#   st.markdown '</div>'

# def main():
#     ...
def main():
    render_styles()
    st.markdown(f'''
        <div class="hero">
            <h1 style="margin:0 0 6px 0;">{config.APP_ICON} {config.APP_TITLE}</h1>
            <p style="margin:0;">Show a hand gesture via webcam or upload an image.
            The app detects the sign and maps it to a magical spell.</p>
        </div>''', unsafe_allow_html=True)
    with st.expander('ℹ️ Detected gestures: Palm · Peace · Pointer · Thumbs Up'):
        st.markdown('Show one of these gestures clearly in the camera or image.')
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    tabs = st.tabs(['📷 Webcam Capture', '🖼️ Upload Image'])
    with tabs[0]:
        cam = st.camera_input('Capture gesture from webcam', help=config.CAMERA_HELP)
        if cam:
            prediction_panel(Image.open(cam).convert('RGB'), 'webcam')
        else:
            st.info('Take a photo with your webcam to detect a gesture.')
    with tabs[1]:
        up = st.file_uploader('Upload a gesture image', type=['png', 'jpg', 'jpeg'])
        if up:
            prediction_panel(Image.open(up).convert('RGB'), 'upload')
        else:
            st.info('Upload a hand gesture image to detect a gesture.')
    st.markdown('</div>', unsafe_allow_html=True)




# ---------- PROVIDED — do not edit -------------------------------------------
if __name__ == "__main__":
    main()
# ===== END LESSON 1 ===========================================================
