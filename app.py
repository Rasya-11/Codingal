
import random
import streamlit as st
from constants import (
    APP_TITLE, MAX_TRUST, TRUST_TO_OPEN, TRUST_TO_ENTER,
    RIDDLES, REPEAT_REPLIES,
)
from ui import inject_styles, render_hud, render_gate_scene, render_chat_log, render_rules_popup


try:
    from student_logic import analyze_player_tone, get_sentinel_mood, process_player_message, process_riddle_answer
    _STUDENT_LOADED = True
except Exception as e:
    _STUDENT_LOADED = False
    _LOAD_ERROR = str(e)

st.set_page_config(page_title=APP_TITLE, page_icon="⚔", layout="wide", initial_sidebar_state="collapsed")

def init_state():
    defaults = {
        "player_name":          "",
        "trust_score":          0,
        "sentinel_mood":        "Suspicious",
        "riddle":               random.choice(RIDDLES),
        "riddle_solved":        False,
        "sentinel_messages":    [
            "[SYSTEM]: Dimensional breach detected...",
            "[SENTINEL]: Stop where you are, Traveler...",
        ],
        "latest_clue":          "The outer gate is silent, but it is listening.",
        "streak":               0,
        "banished":             False,
        "messages_sent":        0,
        "player_messages":      [],
        "rules_accepted":       False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_game():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    init_state()

def get_phase_label() -> str:
    t = st.session_state.trust_score
    if t >= TRUST_TO_ENTER: return "VAULT THRESHOLD"
    if t >= TRUST_TO_OPEN:  return "GATE OPENING"
    return "TRUST GATE"

def _on_msg_change():
    msg = st.session_state.get("msg_input", "").strip()
    if msg:
        if _STUDENT_LOADED:
            process_player_message(msg)
        else:
            st.toast("⚠️ Finish student_logic.py first!", icon="⚠️")
        st.session_state["_clear_msg"] = True

def _on_riddle_change():
    ans = st.session_state.get("riddle_input", "").strip()
    if ans:
        if _STUDENT_LOADED:
            process_riddle_answer(ans)
        else:
            st.toast("⚠️ Finish student_logic.py first!", icon="⚠️")
        st.session_state["_clear_riddle"] = True

def main():
    inject_styles()
    init_state()
    s = st.session_state

    if not s.rules_accepted:
        render_rules_popup()
        return
    

if not _STUDENT_LOADED:
    st.error(f"⚠️ Could not load student_logic.py - fix the error and refresh.\n\n'{_LOAD_ERROR}'")

render_hud(s.player_name, s.trust_score, s.sentinel_mood, s.streak, get_phase_label())


latest = s.sentinel_messages[-1] if s.sentinel_messages else "[SENTINEL]: ..."
render_gate_scene(s.trust_score, s.sentinel_mood, latest, s.player_name, s.latest_clue)


if s.banished:
    st.error(" You have been banished. The Sentinel remembers your disrespect.")
    if st.button(" Try again", key="reset_banish"):
        reset_game(); st.rerun()
        return
    
