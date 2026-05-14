import streamlit as st
import random

# --- КОНФИГУРАЦИЯ СТРАНИЦЫ ---
st.set_page_config(page_title="C2 Mastery: Founder's Path", page_icon="🚀", layout="centered")

# --- СТИЛИЗАЦИЯ (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .word-card {
        background-color: #1A1C24;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #3E4249;
        text-align: center;
        margin-bottom: 20px;
    }
    .word-title { color: #00FFAA; font-size: 42px; font-weight: bold; }
    .context-box { color: #ADB5BD; font-style: italic; font-size: 20px; margin-top: 15px; }
    .rank-text { color: #FFD700; font-weight: bold; font-size: 24px; }
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #3E4249;
    }
    div.stButton > button:hover { border: 1px solid #00FFAA; color: #00FFAA; }
    </style>
    """, unsafe_allow_html=True)

# --- БАЗА ДАННЫХ (C1/C2 + Business + Tech) ---
db = [
    {"word": "Unassailable", "meaning": "Неоспоримый, неуязвимый.", "context": "Your goal is to make your AWD logic unassailable.", "level": "C2"},
    {"word": "Fortitude", "meaning": "Стойкость, сила духа.", "context": "It took immense fortitude to survive those 8 months alone.", "level": "C1"},
    {"word": "Machiavellian", "meaning": "Макиавеллиевский (хитрый, коварный).", "context": "The betrayal of your relatives was truly Machiavellian.", "level": "C2"},
    {"word": "To Scale", "meaning": "Масштабировать.", "context": "In Astana, you will learn how to scale your clothing brand.", "level": "Business"},
    {"word": "Pragmatic", "meaning": "Прагматичный.", "context": "Moving to Astana is a pragmatic move for your future.", "level": "C1"},
    {"word": "Ambiguity", "meaning": "Двусмысленность, неопределенность.", "context": "Entrepreneurs must be comfortable with ambiguity.", "level": "Business"},
    {"word": "To Mitigate", "meaning": "Смягчать, уменьшать риски.", "context": "The new AWD sensor will mitigate the risk of loss of traction.", "level": "Engineering"},
    {"word": "Nuance", "meaning": "Нюанс, тонкое различие.", "context": "To reach C2, you must understand every nuance of the language.", "level": "C2"},
    {"word": "Vindicate", "meaning": "Оправдать, доказать правоту.", "context": "Your success in the US will vindicate all your struggles.", "level": "C2"},
    {"word": "Solidarity", "meaning": "Солидарность, единство.", "context": "True brothers show solidarity, not just words.", "level": "C1"},
]

# --- ЛОГИКА РАНГОВ ---
def get_rank(xp):
    if xp < 50: return "🌑 The Underdog"
    if xp < 150: return "🐺 The Lone Wolf"
    if xp < 300: return "🛠️ The Architect"
    if xp < 500: return "📈 The Strategist"
    return "👑 Global Visionary (C2 Mastery)"

# --- ИНИЦИАЛИЗАЦИЯ СОСТОЯНИЯ ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'current_card' not in st.session_state: st.session_state.current_card = random.choice(db)
if 'show' not in st.session_state: st.session_state.show = False

# --- ИНТЕРФЕЙС ---
st.title("🏆 Founder's Vocabulary")
rank = get_rank(st.session_state.xp)
st.markdown(f"**Current Rank:** <span class='rank-text'>{rank}</span>", unsafe_allow_html=True)
st.progress(min(st.session_state.xp / 500, 1.0))
st.write(f"XP: {st.session_state.xp} / 500")

# КАРТОЧКА
card = st.session_state.current_card
st.markdown(f"""
    <div class="word-card">
        <div class="word-title">{card['word']}</div>
        <div class="context-box">"{card['context']}"</div>
        <div style="margin-top: 10px; color: #555;">Level: {card['level']}</div>
    </div>
    """, unsafe_allow_html=True)

if not st.session_state.show:
    if st.button("REVEAL MEANING"):
        st.session_state.show = True
        st.rerun()
else:
    st.success(f"Meaning:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ I KNEW IT (+10 XP)"):
            st.session_state.xp += 10
            st.session_state.current_card = random.choice(db)
            st.session_state.show = False
            st.rerun()
    with col2:
        if st.button("❌ LEARN AGAIN"):
            st.session_state.current_card = random.choice(db)
            st.session_state.show = False
            st.rerun()

st.markdown("---")
st.caption("Твой путь в США начинается с правильных слов. Держись плана, бро.")