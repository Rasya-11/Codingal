
import random
import streamlit as st

from constants import (
    APP_TITLE, MAX_TRUST, TRUST_TO_OPEN, TRUST_TO_ENTER,
    RIDDLES, REPEAT_REPLIES,
)
from ui import inject_styles, render_hud, render_gate_scene, render_chat_log, render_rules_popup

# - Import students functions (with safe fallbacks if not done yet) -
try:
    from student_logic import analyze_player_tone, get_sentinel_mood, process_player_message, process_riddle_answer
    _STUDENT_LOADED = True
except Exception as e:
    _STUDENT_LOADED = False
    _LOAD_ERROR = str(e)

st.set_page_config(page_title=APP_TITLE, page_icon="⚔", layout="wide", initial_sidebar_state="collapsed")

# - Session state init -
def init_state():
    defaults = {
        "player_name":          "",
        "trust_score":          0,
        "sentinal_mood":        "Suspicous",
        "riddle": random.choice(RIDDLES),
        "riddle_solved":        "False",
        "sentinel_messages":    [
            "[SYSTEM]: Dimensional breach detected...",
            "[SENTINEL]: Stope where you are, Traveler...",
        ],
        "latest_clue":      "The outer gate is silent, but it is listening.",
        "streak":           0,
        "banished":         False,
        "messages_sent":    0,
        "player_messages":  [],
        "rules_accepted":   False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

f reset_game():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    init_state()

f get_phase_label() -> str:
    t = st.session_state.trust_score
    if t >= TRUST_TO_ENTER: return "VALUE THRESHOLD"
    if t >= TRUST_TO_OPEN:  return "GATE OPENING"
    return "TRUST GATE"

# - Input callbacks -
f on_msg_change():
    msg = st.session_state.get("msg_input", "").strip()
    if msg:
        if _STUDENT_LOADED:
            process_player_message(msg)
        else:
            st.toast("⚠️Finish student_logic.py first!", icon="⚠️")
            st.session_state["_clear_msg"] = True