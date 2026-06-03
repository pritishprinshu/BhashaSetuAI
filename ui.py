import streamlit as st

def load_ui():

    st.markdown("""
    <style>

    .stApp {
        background-color: #F5F7FA;
    }

    .main .block-container {
        max-width: 1300px;
        padding-top: 1rem;
    }

    .hero {
        background: white;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        border-left: 8px solid #2E7D32;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    .hero h1 {
        color: #1565C0;
    }

    .hero h3 {
        color: #2E7D32;
    }

    .hero p {
        color: #555;
    }

    .info-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #E5E7EB;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
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