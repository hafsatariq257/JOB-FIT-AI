import streamlit as st
from core.parser import extract_text_from_pdf
from core.engine import calculate_semantic_match

st.markdown("""
    <style>
    .block-container { padding: 2rem 3rem !important; max-width: 100% !important; }
    .executive-card { background: #18182C; border: 1px solid #29294D; border-radius: 14px; padding: 22px; flex: 1; }
    .radar-panel {
        background: #131324; border: 1px solid #29294D; border-radius: 16px; padding: 40px 20px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        position: relative; overflow: hidden; height: 240px;
    }
    .scanning-laser {
        position: absolute; top: 0; left: 0; width: 100%; height: 4px;
        background: linear-gradient(90deg, transparent, #A370F7, #FF69B4, #A370F7, transparent);
        animation: laser-sweep 3.5s infinite ease-in-out;
    }
    @keyframes laser-sweep {
        0% { top: 0%; opacity: 0; }
        5% { opacity: 1; }
        95% { opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }
    .radar-circle {
        width: 110px; height: 110px; border: 2px dashed rgba(163, 112, 247, 0.4);
        border-radius: 50%; display: flex; align-items: center; justify-content: center; animation: radar-spin 10s infinite linear;
    }
    @keyframes radar-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .radar-core { width: 24px; height: 24px; background: #A370F7; border-radius: 50%; animation: core-pulse 1.5s infinite ease-in-out; }
    @keyframes core-pulse { 0%, 100% { transform: scale(0.8); } 50% { transform: scale(1.2); } }
    .insight-card { background: #18182C; border: 1px solid #29294D; border-radius: 12px; padding: 20px; height: 100%; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color:#FFFFFF; font-size:2.3rem; font-weight:700; margin:0;">Cognito JobFit Analytics</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#8B8BAE; font-size:1.1rem; margin-top:4px; margin-bottom:24px;">💼 Profile Engine Matrix // Active Session: {st.session_state.user_email}</p>', unsafe_allow_html=True)

res = st.session_state.analysis_results
score = res.get("match_percentage", 0) if res else 0
summary = res.get("alignment_summary", "Ingest a target profile and corresponding job specifications on the right side panel to generate the evaluation matrix.") if res else "Ingest a target profile and corresponding job specifications on the right side panel to generate the evaluation matrix."
matched_skills = res.get("matched_skills", []) if res else []
missing_skills = res.get("missing_skills", []) if res else []

col_layout_left, col_layout_right = st.columns([1.6, 1], gap="large")

with col_layout_left:
    st.markdown(f"""
        <div style="display: flex; gap: 20px; margin-bottom: 25px; width: 100%;">
            <div class="executive-card">
                <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600;">💜 Overall Match Profile</p>
                <h1 style="color:#FFFFFF; margin:6px 0 0 0; font-size:2.6rem; font-weight:700;">{f"{score}%" if res else "--%"}</h1>
            </div>
            <div class="executive-card">
                <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600;">🧡 Critical Gaps Detected</p>
                <h1 style="color:#FFFFFF; margin:6px 0 0 0; font-size:2.6rem; font-weight:700;">{len(missing_skills) if res else "--"}</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-weight:600; font-size:1.05rem; color:#E0E0FF; margin-bottom:5px;'>🔮 Real-Time Semantic Neural Scanner</p>", unsafe_allow_html=True)
    scanning_text = "MATRIX SCANNING ACTIVE..." if res else "AWAITING PROFILE INGESTION..."
    st.markdown(f"""
        <div class="radar-panel">
            <div class="scanning-laser"></div>
            <div class="radar-circle"><div class="radar-core"></div></div>
            <div class="radar-text" style="color: #A370F7; margin-top:15px; font-weight:600;">{scanning_text}</div>
        </div>
    """, unsafe_allow_html=True)

with col_layout_right:
    uploaded_file = st.file_uploader("Upload Target Profile Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Corporate Requirement Constraints", height=120)
    
    if st.button("RUN ENGINE EVALUATION MATRIX", use_container_width=True):
        if uploaded_file and job_desc:
            with st.spinner("Processing..."):
                resume_text = extract_text_from_pdf(uploaded_file)
                st.session_state.analysis_results = calculate_semantic_match(resume_text, job_desc)
                st.rerun()

    st.markdown("<br><hr style='border-color:#22223D;'>", unsafe_allow_html=True)
    if st.button("🚪 TERMINATE SECURE SESSION", use_container_width=True):
        st.session_state.is_authenticated = False
        st.session_state.user_email = None
        st.session_state.user_role = None
        st.session_state.analysis_results = None
        st.switch_page("views/landing.py")

st.markdown("<br><p style='font-weight:600; font-size:1.15rem; color:#E0E0FF;'>🔍 Strategic Engine Insight Readouts</p>", unsafe_allow_html=True)
col_inf1, col_inf2, col_inf3 = st.columns(3, gap="medium")
with col_inf1:
    st.markdown(f'<div class="insight-card" style="border-left: 4px solid #00E676;"><b>✅ Matched Skills</b><br>{", ".join(matched_skills) if matched_skills else "No data"}</div>', unsafe_allow_html=True)
with col_inf2:
    st.markdown(f'<div class="insight-card" style="border-left: 4px solid #FF69B4;"><b>⚡ Gaps</b><br>{", ".join(missing_skills) if missing_skills else "No data"}</div>', unsafe_allow_html=True)
with col_inf3:
    st.markdown(f'<div class="insight-card" style="border-left: 4px solid #A370F7;"><b>💡 Exec Summary</b><br>{summary}</div>', unsafe_allow_html=True)