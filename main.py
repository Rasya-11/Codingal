import streamlit as st
from constants import APP_TITLE
from student_logic import get_sentinel_mood
from ui import inject_styles, render_mood_card, render_rules_legend

st.set_page_config(page_title=APP_TITLE, layout="wide")
inject_styles()

st.title(APP_TITLE)

if "trust_score" not in st.session_state:
    st.session_state.trust_score = 50

left_panel, right_panel = st.columns(2)

with left_panel:
    st.subheader("Interactive Controls")
    
    st.slider(
        "Adjust Trust Score:", 
        min_value=0, 
        max_value=100, 
        key="trust_score"
    )
    
    st.write("Quick Presets:")
    b1, b2, b3, b4, b5 = st.columns(5)
    
    if b1.button("🚨 Critical (10)"):
        st.session_state.trust_score = 10
        st.rerun()
    if b2.button("⚠️ Warning (35)"):
        st.session_state.trust_score = 35
        st.rerun()
    if b3.button("🙂 Good (65)"):
        st.session_state.trust_score = 65
        st.rerun()
    if b4.button("🌟 Excellent (95)"):
        st.session_state.trust_score = 95
        st.rerun()
    if b5.button("🔄 Reset Option", type="primary"):
        st.session_state.trust_score = 50
        st.rerun()

with right_panel:
    st.subheader("Visual Status")
    
    active_mood = get_sentinel_mood(st.session_state.trust_score)
    
    render_mood_card(active_mood)
    render_rules_legend()
