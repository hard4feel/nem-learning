import streamlit as st
import random
from datetime import date

# --- 1. ПРЕМИАЛЬНАЯ КОНФИГУРАЦИЯ СТРАНИЦЫ ---
st.set_page_config(page_title="NEM Lexicon | C2 Engine", page_icon="⬛", layout="centered")

# --- 2. CSS (Стиль "Erryssence": Минимализм, Dark Mode, Типографика) ---
st.markdown("""
    <style>
    /* Основной фон */
    .stApp {
        background-color: #050505;
        color: #F0F0F0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Скрытие стандартных элементов Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Карточка слова */
    .nem-card {
        background: linear-gradient(145deg, #0a0a0a, #111111);
        border: 1px solid #222222;
        border-radius: 12px;
        padding: 40px 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .nem-category {
        color: #666666;
        font-size: 12px;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    .nem-word {
        color: #FFFFFF;
        font-size: 48px;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }
    .nem-phonetic {
        color: #888888;
        font-size: 18px;
        font-family: monospace;
        margin-bottom: 25px;
    }
    .nem-context {
        color: #CCCCCC;
        font-size: 20px;
        font-style: italic;
        line-height: 1.5;
        border-left: 3px solid #333333;
        padding-left: 15px;
        text-align: left;
    }
    .nem-meaning {
        color: #00FFAA;
        font-size: 24px;
        font-weight: 500;
        margin-top: 25px;
        padding-top: 20px;
        border-top: 1px solid #222222;
    }
    
    /* Статистика */
    .stat-box {
        border: 1px solid #333;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #0a0a0a;
    }
    .stat-value { font-size: 28px; font-weight: bold; color: #FFF; }
    .stat-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. БАЗА ДАННЫХ (Уровень C1/C2 Elite) ---
vocabulary = {
    "⚙️ NEM Engineering": [
        {"word": "Telemetry", "phonetic": "/təˈlemətrē/", "meaning": "Телеметрия, удаленный сбор данных.", "context": "The ESP32 processes real-time telemetry from the AWD sensors."},
        {"word": "Bespoke", "phonetic": "/bəˈspōk/", "meaning": "Сделанный на заказ (особенно о технологиях и авто).", "context": "This isn't a factory part; it's a bespoke electric motor control unit."},
        {"word": "Redundancy", "phonetic": "/rəˈdəndənsē/", "meaning": "Избыточность (в инженерии - дублирование систем для надежности).", "context": "We built redundancy into the L298 code to prevent system failure."},
        {"word": "Latency", "phonetic": "/ˈlātnsē/", "meaning": "Задержка, время отклика.", "context": "Minimizing signal latency is crucial for all-wheel-drive traction."}
    ],
    "🧵 Erryssence Fashion": [
        {"word": "Sartorial", "phonetic": "/särˈtôrēəl/", "meaning": "Относящийся к мужской одежде, портновский.", "context": "Erryssence offers a minimalist, yet profound sartorial experience."},
        {"word": "Monochromatic", "phonetic": "/ˌmänəkrəˈmadik/", "meaning": "Монохромный, в оттенках одного цвета.", "context": "The new heavy cotton tee features a sleek, monochromatic aesthetic."},
        {"word": "Tactile", "phonetic": "/ˈtaktl/", "meaning": "Тактильный, осязательный.", "context": "The tactile quality of the embroidery speaks of its premium nature."},
        {"word": "Avant-garde", "phonetic": "/ˌaväntˈɡärd/", "meaning": "Авангардный, опережающий время.", "context": "It's not just streetwear; it's an avant-garde approach to daily wear."}
    ],
    "💼 US Boardroom": [
        {"word": "Bootstrapping", "phonetic": "/ˈbo͞otˌstrap/ing/", "meaning": "Создание бизнеса без внешних инвестиций, на свои средства.", "context": "I spent 8 months bootstrapping this project with 500k tenge."},
        {"word": "Equity", "phonetic": "/ˈekwədē/", "meaning": "Доля в капитале компании.", "context": "I'm offering you a partnership, but I retain the majority equity."},
        {"word": "Paradigm Shift", "phonetic": "/ˈperəˌdīm SHift/", "meaning": "Смена парадигмы, кардинальное изменение ситуации.", "context": "NEM E AWD represents a paradigm shift in how we control traction."},
        {"word": "Leverage", "phonetic": "/ˈlev(ə)rij/", "meaning": "Рычаг влияния, использование ресурсов.", "context": "We will leverage your retail experience to scale the brand."}
    ],
    "🐺 Street Stoicism": [
        {"word": "Resilience", "phonetic": "/rəˈzilyəns/", "meaning": "Жизнестойкость, способность быстро восстанавливаться.", "context": "Betrayal didn't break me; it forged my resilience."},
        {"word": "Equanimity", "phonetic": "/ˌekwəˈnimədē/", "meaning": "Хладнокровие, невозмутимость (особенно в стрессе).", "context": "Despite the lies and hate, he maintained total equanimity."},
        {"word": "To Sever", "phonetic": "/ˈsevər/", "meaning": "Разорвать (отношения), отрезать.", "context": "I had to sever ties with toxic blood to protect my vision."},
        {"word": "Vindicate", "phonetic": "/ˈvindəˌkāt/", "meaning": "Оправдать, доказать правоту фактами.", "context": "The success of Erryssence will vindicate my silent grind."}
    ]
}

# --- 4. СОСТОЯНИЕ (Session State) ---
if 'mastered' not in st.session_state: st.session_state.mastered = 0
if 'reviewed' not in st.session_state: st.session_state.reviewed = 0
if 'current_cat' not in st.session_state: st.session_state.current_cat = "💼 US Boardroom"
if 'current_word' not in st.session_state: st.session_state.current_word = random.choice(vocabulary[st.session_state.current_cat])
if 'show_meaning' not in st.session_state: st.session_state.show_meaning = False

# --- 5. ФУНКЦИИ ---
def next_card(status):
    if status == "mastered":
        st.session_state.mastered += 1
    else:
        st.session_state.reviewed += 1
    
    st.session_state.current_word = random.choice(vocabulary[st.session_state.current_cat])
    st.session_state.show_meaning = False

# --- 6. ИНТЕРФЕЙС ПРИЛОЖЕНИЯ ---

# Шапка
st.markdown("<h3 style='color:#FFF; font-weight:300; letter-spacing: 3px;'>NEM <span style='color:#00FFAA;'>|</span> LEXICON</h3>", unsafe_allow_html=True)
st.markdown("---")

# Панель статистики
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='stat-box'><div class='stat-value'>{st.session_state.mastered}</div><div class='stat-label'>Mastered</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='stat-box'><div class='stat-value'>{st.session_state.reviewed}</div><div class='stat-label'>Reviewed</div></div>", unsafe_allow_html=True)

# Выбор категории
st.write("")
selected_cat = st.selectbox("SELECT MODULE:", list(vocabulary.keys()), label_visibility="collapsed")
if selected_cat != st.session_state.current_cat:
    st.session_state.current_cat = selected_cat
    st.session_state.current_word = random.choice(vocabulary[selected_cat])
    st.session_state.show_meaning = False
    st.rerun()

# Отрисовка карточки
word_data = st.session_state.current_word

card_html = f"""
<div class='nem-card'>
    <div class='nem-category'>{st.session_state.current_cat}</div>
    <div class='nem-word'>{word_data['word']}</div>
    <div class='nem-phonetic'>{word_data['phonetic']}</div>
    <div class='nem-context'>"{word_data['context']}"</div>
"""

if st.session_state.show_meaning:
    card_html += f"<div class='nem-meaning'>{word_data['meaning']}</div>"

card_html += "</div>"
st.markdown(card_html, unsafe_allow_html=True)

# Кнопки управления
if not st.session_state.show_meaning:
    if st.button("DECRYPT MEANING", use_container_width=True):
        st.session_state.show_meaning = True
        st.rerun()
else:
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        if st.button("NEEDS REVIEW", use_container_width=True):
            next_card("reviewed")
            st.rerun()
    with b_col2:
        # Зеленая кнопка для Mastered (через Streamlit type="primary" и CSS)
        if st.button("MASTERED", type="primary", use_container_width=True):
            next_card("mastered")
            st.rerun()

st.markdown("<br><center><p style='color:#444; font-size:12px; letter-spacing:1px;'>ERRRYSENCE C2 ENGINE • DESIGNED IN KZ</p></center>", unsafe_allow_html=True)