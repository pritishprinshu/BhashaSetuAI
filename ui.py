import streamlit as st

def load_ui():

    st.markdown("""
    <style>

    .main .block-container {
        max-width: 1300px;
        padding-top: 1rem;
    }

    .hero {
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        border-left: 8px solid #2E7D32;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    .hero h1,
    .hero h2,
    .hero h3,
    .hero p {
        color: var(--text-color) !important;
    }

    .info-card {
        background-color: var(--secondary-background-color);
        color: var(--text-color) !important;

        padding: 15px;
        border-radius: 12px;
        text-align: center;

        border: 1px solid rgba(128,128,128,0.2);

        box-shadow: 0 2px 8px rgba(0,0,0,0.05);

        font-size: 18px;
        font-weight: 600;

        transition: all 0.3s ease;
    }

    .info-card:hover {
        transform: translateY(-4px);
    }

    .info-card b,
    .info-card div,
    .info-card span {
        color: var(--text-color) !important;
    }

    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        background-color: #2E7D32;
        color: white;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """, unsafe_allow_html=True)

def hero():

    st.markdown("""
    <div class="hero">

    <h1>🌐 BhashaSetu AI</h1>

    <h3>Empowering Multilingual Communication</h3>

    <p>
    Supporting Education, Agriculture,
    Healthcare and Government Services
    through Offline AI Translation.
    </p>

    </div>
    """, unsafe_allow_html=True)

def feature_cards():

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="info-card">
        📚<br><b>Education</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
        🌾<br><b>Agriculture</b>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
        🏥<br><b>Healthcare</b>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="info-card">
        🏛<br><b>Government</b>
        </div>
        """, unsafe_allow_html=True)

def footer():

    st.markdown("---")

    st.markdown("""
    <center>

    <b>BhashaSetu AI</b>

    Bridging Language Barriers for
    Education, Agriculture,
    Healthcare and Government Services

    </center>
    """, unsafe_allow_html=True)