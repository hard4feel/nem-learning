import streamlit as st
import random

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="NEM Lexicon | C2 Engine v2", page_icon="⬛", layout="centered")

# --- 2. PREMIUM CSS (Erryssence Aesthetic) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #F0F0F0; }
    #MainMenu, footer, header {visibility: hidden;}
    
    .nem-card {
        background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%);
        border: 1px solid #222;
        border-radius: 15px;
        padding: 45px 35px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.9);
        margin-bottom: 25px;
    }
    .nem-category { color: #666; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 20px; }
    .nem-word { color: #FFF; font-size: 52px; font-weight: 800; letter-spacing: -2px; margin-bottom: 5px; }
    .nem-phonetic { color: #00FFAA; font-size: 18px; font-family: 'Courier New', monospace; margin-bottom: 30px; opacity: 0.8; }
    .nem-context {
        color: #BBB;
        font-size: 19px;
        font-style: italic;
        line-height: 1.6;
        background: #0f0f0f;
        padding: 20px;
        border-radius: 10px;
        border-left: 2px solid #00FFAA;
        text-align: left;
    }
    .nem-meaning {
        color: #FFFFFF;
        font-size: 26px;
        font-weight: 600;
        margin-top: 30px;
        padding-top: 25px;
        border-top: 1px solid #222;
    }
    .stat-label { color: #555; font-size: 10px; text-transform: uppercase; letter-spacing: 2px; }
    .stat-value { color: #FFF; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- 3. EXPANDED DATABASE (C1/C2 Elite) ---
vocabulary = {
    "⚙️ NEM Engineering": [
        {"word": "Propulsion", "phonetic": "/prəˈpəlSHən/", "meaning": "Тяга, движение вперед, пропульсия.", "context": "The NEM E AWD system optimizes propulsion on any surface."},
        {"word": "Calibration", "phonetic": "/ˌkaləˈbrāSHən/", "meaning": "Калибровка, точная настройка.", "context": "Precise calibration of the ESP32 is essential for motor sync."},
        {"word": "Friction", "phonetic": "/ˈfrikSHən/", "meaning": "Трение, сцепление.", "context": "We need to calculate the friction coefficient for the carbon fiber parts."},
        {"word": "Robustness", "phonetic": "/rōˈbəstnəs/", "meaning": "Надежность, устойчивость системы.", "context": "The software architecture must ensure total robustness under load."},
        {"word": "Integration", "phonetic": "/ˌin(t)əˈɡrāSHən/", "meaning": "Интеграция, объединение частей.", "context": "Seamless integration of L298 drivers into the AWD prototype."},
        {"word": "Traction", "phonetic": "/ˈtrakSHən/", "meaning": "Тяга, сцепление с дорогой.", "context": "All-wheel drive provides superior traction in Astana's winter."}
    ],
    "🧵 Erryssence Fashion": [
        {"word": "Craftsmanship", "phonetic": "/ˈkraf(t)smənˌSHip/", "meaning": "Мастерство, искусство ручной работы.", "context": "Erryssence focuses on flawless craftsmanship and heavy cotton."},
        {"word": "Aesthetic", "phonetic": "/esˈTHedik/", "meaning": "Эстетика, внешний вид.", "context": "A minimalist aesthetic is the core of our brand identity."},
        {"word": "Versatility", "phonetic": "/ˌvərsəˈtilədē/", "meaning": "Универсальность.", "context": "Our hoodies offer versatility for both street and high-end looks."},
        {"word": "Durability", "phonetic": "/ˌd(y)o͝orəˈbilədē/", "meaning": "Долговечность, износостойкость.", "context": "High-density fabric ensures the durability of our prototypes."},
        {"word": "Silhouette", "phonetic": "/ˌsiləˈwet/", "meaning": "Силуэт, очертания.", "context": "The brand's silhouette is defined by clean lines and boxy fits."},
        {"word": "Exclusivity", "phonetic": "/ˌeksklo͞oˈsivədē/", "meaning": "Эксклюзивность.", "context": "We maintain exclusivity by producing limited embroidery drops."}
    ],
    "💼 US Boardroom": [
        {"word": "Disruptive", "phonetic": "/disˈrəptiv/", "meaning": "Прорывной, разрушающий старые стандарты.", "context": "NEM aims to be a disruptive force in the EV market."},
        {"word": "Scalability", "phonetic": "/ˌskāləˈbilədē/", "meaning": "Масштабируемость бизнеса.", "context": "When we move to the US, scalability will be our top priority."},
        {"word": "Valuation", "phonetic": "/ˌvalyəˈwāSHən/", "meaning": "Оценка стоимости компании.", "context": "A working prototype significantly increases our seed valuation."},
        {"word": "Stakeholder", "phonetic": "/ˈstākˌhōldər/", "meaning": "Заинтересованная сторона, партнер.", "context": "Your brother in Astana is a key stakeholder in our summer plan."},
        {"word": "Venture", "phonetic": "/ˈven(t)SHər/", "meaning": "Предприятие, рискованное начинание.", "context": "This venture requires courage and capital to succeed."},
        {"word": "Revenue", "phonetic": "/ˈrevəˌn(y)o͞o/", "meaning": "Выручка, доход.", "context": "We need to project our Q4 revenue before applying to US schools."}
    ],
    "🐺 Street Stoicism": [
        {"word": "Fortitude", "phonetic": "/ˈfôrdəˌt(y)o͞od/", "meaning": "Сила духа, стойкость в беде.", "context": "Mental fortitude is what kept me going when I was alone."},
        {"word": "Conviction", "phonetic": "/kənˈvikSHən/", "meaning": "Твердая убежденность.", "context": "I have the conviction that Erryssence will go global."},
        {"word": "Unyielding", "phonetic": "/ˌənˈyēldiNG/", "meaning": "Непреклонный, несгибаемый.", "context": "Stay unyielding when others doubt your vision."},
        {"word": "Adversity", "phonetic": "/ədˈvərsədē/", "meaning": "Невзгоды, тяжелые обстоятельства.", "context": "True leaders are forged in the fires of adversity."},
        {"word": "Authenticity", "phonetic": "/ˌôˌTHenˈtisədē/", "meaning": "Подлинность, искренность.", "context": "Your authenticity is why high-level people respect you."},
        {"word": "Aloof", "phonetic": "/əˈlo͞of/", "meaning": "Отстраненный, холодный (в хорошем смысле).", "context": "Stay aloof from toxic relatives; focus only on the grind."}
    ]
}

# --- 4. LOGIC ---
if 'mastered' not in st.session_state: st.session_state.mastered = 0
if 'total' not in st.session_state: st.session_state.total = 0
if 'current_cat' not in st.session_state: st.session_state.current_cat = "💼 US Boardroom"
if 'current_word' not in st.session_state: st.session_state.current_word = random.choice(vocabulary[st.session_state.current_cat])
if 'show' not in st.session_state: st.session_state.show = False

def update_card(success):
    if success: st.session_state.mastered += 1
    st.session_state.total += 1
    st.session_state.current_word = random.choice(vocabulary[st.session_state.current_cat])
    st.session_state.show = False

# --- 5. UI ---
st.markdown("<h2 style='text-align: center; letter-spacing: 5px; font-weight: 200;'>NEM LEXICON</h2>", unsafe_allow_html=True)

# Stats
c1, c2 = st.columns(2)
with c1: st.markdown(f"<center><div class='stat-label'>Mastered</div><div class='stat-value'>{st.session_state.mastered}</div></center>", unsafe_allow_html=True)
with c2: st.markdown(f"<center><div class='stat-label'>Progress</div><div class='stat-value'>{st.session_state.total}</div></center>", unsafe_allow_html=True)

st.markdown("---")

# Category Selector
cat = st.selectbox("MODULE", list(vocabulary.keys()), label_visibility="collapsed")
if cat != st.session_state.current_cat:
    st.session_state.current_cat = cat
    st.session_state.current_word = random.choice(vocabulary[cat])
    st.session_state.show = False
    st.rerun()

# Card Rendering
word = st.session_state.current_word
st.markdown(f"""
    <div class='nem-card'>
        <div class='nem-category'>{cat}</div>
        <div class='nem-word'>{word['word']}</div>
        <div class='nem-phonetic'>{word['phonetic']}</div>
        <div class='nem-context'>"{word['context']}"</div>
        {"<div class='nem-meaning'>" + word['meaning'] + "</div>" if st.session_state.show else ""}
    </div>
""", unsafe_allow_html=True)

# Controls
if not st.session_state.show:
    if st.button("DECRYPT MEANING", use_container_width=True):
        st.session_state.show = True
        st.rerun()
else:
    col_l, col_r = st.columns(2)
    with col_l:
        if st.button("NEEDS REVIEW", use_container_width=True):
            update_card(False)
            st.rerun()
    with col_r:
        if st.button("MASTERED", type="primary", use_container_width=True):
            update_card(True)
            st.rerun()

st.markdown("<br><center><p style='color:#333; font-size:10px; letter-spacing:2px;'>ERRRYSENCE DESIGN SYSTEM • PROTOTYPE 2.0</p></center>", unsafe_allow_html=True)