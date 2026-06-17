import streamlit as st
from core.parser import extract_text_from_pdf
from core.engine import calculate_semantic_match

# 1. System Window Architecture Configuration
st.set_page_config(
    page_title="Cognito JobFit Engine",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Isolated CSS Injection Template Variables (Error Free Matrix Layout)
CYBERPUNK_THEME = """
<style>
    /* Global Base High-Contrast Deep Dark Canvas */
    .stApp {
        background-color: #0A0A12 !important;
    }
    
    /* Sleek Dark Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0F0F1D !important;
        border-right: 2px solid #2B1B4D !important;
    }
    
    /* --- INTENSE NEON PURPLE GLOW PANELS --- */
    .executive-panel {
        background: #141126 !important;
        border: 1px solid #6236FF !important;
        border-radius: 12px;
        padding: 26px;
        margin-bottom: 22px;
        box-shadow: 0 0 20px rgba(98, 54, 255, 0.2) !important;
    }
    
    /* Dynamic Bottom Insight Matrix Cards */
    .insight-card {
        background: #141126 !important;
        border: 1px solid #4426A3 !important;
        border-radius: 10px;
        padding: 22px;
        height: 100%;
        box-shadow: 0 0 15px rgba(98, 54, 255, 0.1) !important;
    }
    
    /* Input field elements text layout */
    input, textarea, select { 
        color: #FFFFFF !important; 
        background-color: #0F0F1D !important;
    }
    
    /* Brand Identity Header inside sidebar */
    .sidebar-brand {
        font-size: 1.6rem;
        font-weight: 800;
        color: #A370F7;
        text-shadow: 0 0 10px rgba(163, 112, 247, 0.6);
        letter-spacing: 0.8px;
        margin-bottom: 3px;
    }
    
    /* --- REAL-TIME MOVING PURPLE LASER SCANNER --- */
    .radar-panel {
        background: #0B0914; 
        border: 2px dashed #6236FF; 
        border-radius: 14px; 
        padding: 40px 20px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        position: relative; overflow: hidden; height: 190px;
        box-shadow: inset 0 0 20px rgba(98, 54, 255, 0.15);
    }
    .scanning-laser {
        position: absolute; top: 0; left: 0; width: 100%; height: 4px;
        background: linear-gradient(90deg, transparent, #FF69B4, #A370F7, #FF69B4, transparent);
        animation: laser-sweep 3.5s infinite ease-in-out;
    }
    @keyframes laser-sweep {
        0% { top: 0%; opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }
    
    /* Font override rule styling */
    h1, h2, h3, p, span {
        font-family: 'Inter', sans-serif !important;
    }
</style>
"""

# Safe execution of dynamic custom theme
st.markdown(CYBERPUNK_THEME, unsafe_allow_html=True)

# 3. Persistent Memory Matrix Initialization
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None

# =====================================================================
# SIDEBAR NAVIGATION ROUTING GATEWAY
# =====================================================================
with st.sidebar:
    st.markdown('<div class="sidebar-brand">🔮 Cognito.AI</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #6C6C9C; font-size: 0.85rem; margin-top:-5px; margin-bottom: 35px;">Neural Filter System v3.3</p>', unsafe_allow_html=True)
    
    if not st.session_state.is_authenticated:
        navigation_menu = st.radio(
            "Navigation",
            ["🏠 Welcome Screen", "🔑 Access Portal ID"],
            label_visibility="collapsed"
        )
    else:
        navigation_menu = st.radio(
            "Navigation",
            ["📊 Executive Workspace", "🏠 Welcome Screen"],
            label_visibility="collapsed"
        )
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("🔴 Logout Session", use_container_width=True):
            st.session_state.is_authenticated = False
            st.session_state.user_email = None
            st.session_state.analysis_results = None
            st.rerun()

# =====================================================================
# INTERFACE MAIN COMPONENT SWITCH DISPATCH
# =====================================================================

# SCREEN 1: THE WELCOME SCREEN
if navigation_menu == "🏠 Welcome Screen":
    st.markdown('<h1 style="color:#FFFFFF; font-size:2.8rem; font-weight:800; margin-top:10px; letter-spacing:-0.5px;">Intelligence Library Matrix</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8B8BAE; font-size:1.05rem; margin-bottom:40px;">Bypass legacy constraints. Map technical talent streams with raw multi-layered semantic context filters.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
            <div class="executive-panel">
                <h3 style="color: #FF69B4; margin-top:0; font-weight:700;">🛸 Profile Performance Analysis</h3>
                <p style="color: #BAC2DE; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
                Ingest applicant resume parameters to parse complex data blocks against real-time target operational constraints instantly.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="executive-panel">
                <h3 style="color: #A370F7; margin-top:0; font-weight:700;">💼 Corporate Mapping Filters</h3>
                <p style="color: #BAC2DE; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
                Establish complex positional requirements vectors and extract architectural candidate alignment ratios in seconds.
                </p>
            </div>
        """, unsafe_allow_html=True)

# SCREEN 2: ACCESS PORTAL LOGIN GATEWAY
elif navigation_menu == "🔑 Access Portal ID":
    st.markdown('<div style="max-width: 520px; margin: 40px auto;" class="executive-panel">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #FFFFFF; margin-top: 0; font-weight:700;">🔑 Secure Access Gate</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #8B8BAE; font-size:0.88rem; margin-top:-10px; margin-bottom:25px;">Enter your workspace verification parameters token below.</p>', unsafe_allow_html=True)
    
    email = st.text_input("Corporate Email ID", placeholder="name@company.com")
    password = st.text_input("Secure Vault Password", type="password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("INITIALIZE SECURE SYSTEM SESSION", use_container_width=True):
        if email and password:
            st.session_state.is_authenticated = True
            st.session_state.user_email = email
            st.success("Credentials verified! Access Granted.")
            st.rerun()
        else:
            st.error("Invalid sequence values. Complete all input fields.")
    st.markdown('</div>', unsafe_allow_html=True)

# SCREEN 3: HIGH-CONTRAST DATA RUNTIME ANALYSIS DASHBOARD
elif navigation_menu == "📊 Executive Workspace" and st.session_state.is_authenticated:
    st.markdown('<h1 style="color:#FFFFFF; font-size:2.5rem; font-weight:800; margin:0;">JobFit Analysis Dashboard</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#A370F7; font-size:0.95rem; font-weight:600; margin-top:5px; margin-bottom:30px;">🔮 MATRIX CORE OPERATIONAL // ID: {st.session_state.user_email}</p>', unsafe_allow_html=True)
    
    res = st.session_state.analysis_results
    score = res.get("match_percentage", 0) if res else 0
    summary = res.get("alignment_summary", "Awaiting ingestion streams. Upload target layout profile variables inside the panel matrix setup to evaluate metrics.") if res else "Awaiting ingestion streams. Upload target layout profile variables inside the panel matrix setup to evaluate metrics."
    matched_skills = res.get("matched_skills", []) if res else []
    missing_skills = res.get("missing_skills", []) if res else []

    col_l, col_r = st.columns([1.5, 1], gap="large")

    with col_l:
        # Glow Output Metrics Columns
        st.markdown(f"""
            <div style="display: flex; gap: 20px; margin-bottom: 25px; width: 100%;">
                <div class="executive-panel" style="flex:1; margin-bottom:0;">
                    <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600; text-transform: uppercase;">Overall Profile Match</p>
                    <h1 style="color:#A370F7; margin:8px 0 0 0; font-size:3rem; font-weight:800; text-shadow: 0 0 10px rgba(163,112,247,0.3);">{f"{score}%" if res else "--%"}</h1>
                </div>
                <div class="executive-panel" style="flex:1; margin-bottom:0;">
                    <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600; text-transform: uppercase;">Core Competency Gaps</p>
                    <h1 style="color:#FF69B4; margin:8px 0 0 0; font-size:3rem; font-weight:800; text-shadow: 0 0 10px rgba(255,105,180,0.3);">{len(missing_skills) if res else "--"}</h1>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Cyber laser scan graphic element
        st.markdown("<p style='font-weight:600; font-size:0.98rem; color:#BAC2DE; margin-top:12px; margin-bottom:8px;'>🔮 Neural Cluster Scan Vector Status</p>", unsafe_allow_html=True)
        scanning_text = "NEURAL COMPILATION COMPLETE // READY" if res else "AWAITING INBOUND APPLICANT DATA STREAM"
        st.markdown(f"""
            <div class="radar-panel">
                <div class="scanning-laser"></div>
                <div style="color: {'#A370F7' if res else '#6C6C9C'}; font-size:1.05rem; font-weight:700; letter-spacing:1px; text-shadow: {'0 0 8px rgba(163,112,247,0.5)' if res else 'none'};">
                    {scanning_text}
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_r:
        uploaded_file = st.file_uploader("Upload Target Profile Resume (PDF)", type=["pdf"])
        job_desc = st.text_area("Paste Corporate Requirement Constraints", height=135, placeholder="Insert explicit job description specifications text data...")
        
        if st.button("RUN EVALUATION MATRIX ENGINE", use_container_width=True):
            if uploaded_file and job_desc:
                with st.spinner("Analyzing semantic vectors..."):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    st.session_state.analysis_results = calculate_semantic_match(resume_text, job_desc)
                    st.rerun()

    # Strategic Bottom Insight Fields
    st.markdown("<br><p style='font-weight:700; font-size:1.15rem; color:#FFFFFF; margin-bottom:15px;'>🔍 Neural Extraction Readouts</p>", unsafe_allow_html=True)
    col_inf1, col_inf2, col_inf3 = st.columns(3, gap="medium")
    with col_inf1:
        st.markdown(f'<div class="insight-card" style="border-left: 4px solid #A370F7;"><b style="color:#A370F7;">✅ Matched Competencies</b><br><br><span style="color:#BAC2DE; font-size:0.92rem;">{", ".join(matched_skills) if matched_skills else "No current data profile parsed."}</span></div>', unsafe_allow_html=True)
    with col_inf2:
        st.markdown(f'<div class="insight-card" style="border-left: 4px solid #FF69B4;"><b style="color:#FF69B4;">⚡ Detected Skill Gaps</b><br><br><span style="color:#BAC2DE; font-size:0.92rem;">{", ".join(missing_skills) if missing_skills else "No current data profile parsed."}</span></div>', unsafe_allow_html=True)
    with col_inf3:
        st.markdown(f'<div class="insight-card" style="border-left: 4px solid #6236FF;"><b style="color:#6236FF;">💡 Alignment Executive Summary</b><br><br><span style="color:#BAC2DE; font-size:0.9rem; line-height:1.55;">{summary}</span></div>', unsafe_allow_html=True)
