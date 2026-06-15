import streamlit as st
from core.parser import extract_text_from_pdf
from core.engine import calculate_semantic_match

# 1. Comprehensive Cyberpunk UI Styling Engine + Moving Radar Animations
st.markdown("""
    <style>
    /* Force premium app canvas container padding rules */
    .block-container {
        padding: 2rem 3rem !important;
        max-width: 100% !important;
    }
    
    /* Clean out native widget block backgrounds */
    div[data-testid="stColumn"] > div {
        padding: 0px !important;
    }
    
    /* Executive Structural Metric Cards */
    .metric-container-row {
        display: flex;
        gap: 20px;
        margin-bottom: 25px;
        width: 100%;
    }
    
    .executive-card {
        flex: 1;
        background: #18182C;
        border: 1px solid #29294D;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
    }
    
    /* Neon Status Pill Badges */
    .pill-badge {
        font-size: 0.8rem;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
        margin-left: 8px;
        vertical-align: middle;
    }
    .badge-purple {
        background: rgba(163, 112, 247, 0.15);
        color: #A370F7;
        border: 1px solid #A370F7;
    }
    .badge-green {
        background: rgba(0, 230, 118, 0.15);
        color: #00E676;
        border: 1px solid #00E676;
    }
    
    /* Bottom Insight Dynamic Response Cards */
    .insight-card {
        background: #18182C;
        border: 1px solid #29294D;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
    }

    /* --- ADVANCED MOVING RADAR ICON ANIMATION --- */
    .radar-panel {
        background: #131324;
        border: 1px solid #29294D;
        border-radius: 16px;
        padding: 40px 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
        position: relative;
        overflow: hidden;
        height: 240px;
        box-shadow: inset 0 0 20px rgba(163, 112, 247, 0.1);
    }

    /* Sweeping Laser Line Animation */
    .scanning-laser {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, transparent, #A370F7, #FF69B4, #A370F7, transparent);
        box-shadow: 0 0 15px #A370F7, 0 0 30px #FF69B4;
        animation: laser-sweep 3.5s infinite ease-in-out;
    }

    @keyframes laser-sweep {
        0% { top: 0%; opacity: 0; }
        5% { opacity: 1; }
        95% { opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }

    /* Rotating Radar Circle Grid */
    .radar-circle {
        width: 110px;
        height: 110px;
        border: 2px dashed rgba(163, 112, 247, 0.4);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: radar-spin 10s infinite linear;
        position: relative;
    }

    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Glowing Core Pulse Icon */
    .radar-core {
        position: absolute;
        width: 24px;
        height: 24px;
        background: #A370F7;
        border-radius: 50%;
        box-shadow: 0 0 20px #A370F7, 0 0 40px #FF69B4;
        animation: core-pulse 1.5s infinite ease-in-out;
    }

    @keyframes core-pulse {
        0% { transform: scale(0.8); opacity: 0.7; }
        50% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 30px #FF69B4, 0 0 50px #A370F7; }
        100% { transform: scale(0.8); opacity: 0.7; }
    }

    .radar-text {
        margin-top: 20px;
        color: #E0E0FF;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 1px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Page Typography Header Matrix
st.markdown('<h1 style="color:#FFFFFF; font-size:2.3rem; font-weight:700; margin:0;">Cognito JobFit Analytics</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B8BAE; font-size:1.1rem; margin-top:4px; margin-bottom:24px;">💼 Enterprise Profile Alignment Matrix</p>', unsafe_allow_html=True)

# 3. Safely Retrieve State Cache Values
res = st.session_state.get("analysis_results")
score = res.get("match_percentage", 0) if res else 0
summary = res.get("alignment_summary", "Ingest a target profile and corresponding job specifications on the right side panel to generate the evaluation matrix.") if res else "Ingest a target profile and corresponding job specifications on the right side panel to generate the evaluation matrix."
matched_skills = res.get("matched_skills", []) if res else []
missing_skills = res.get("missing_skills", []) if res else []

# 4. Generate Main Two-Column Side-by-Side Application Layout Grid
col_layout_left, col_layout_right = st.columns([1.6, 1], gap="large")

with col_layout_left:
    # Top KPI Metrics row block components
    badge_type = "badge-green" if score >= 80 else "badge-purple"
    status_label = "Pass" if score >= 80 else "Review Required" if res else "Pending Ingestion"
    
    st.markdown(f"""
        <div class="metric-container-row">
            <div class="executive-card">
                <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600;">💜 Overall Match Profile</p>
                <h1 style="color:#FFFFFF; margin:6px 0 0 0; font-size:2.6rem; font-weight:700;">{f"{score}%" if res else "--%"} <span style="font-size:0.85rem; color:#00E676; background:rgba(0,230,118,0.1); padding:2px 8px; border-radius:4px; font-weight:600; margin-left:6px;">+12%</span></h1>
                <p style="color:#5C5C8A; margin:6px 0 0 0; font-size:0.78rem;">Target threshold constraint: >85%</p>
            </div>
            <div class="executive-card">
                <p style="color:#8B8BAE; margin:0; font-size:0.88rem; font-weight:600;">🧡 Critical Gaps Detected</p>
                <h1 style="color:#FFFFFF; margin:6px 0 0 0; font-size:2.6rem; font-weight:700;">{len(missing_skills) if res else "--"} <span class="pill-badge {badge_type}">{status_label}</span></h1>
                <p style="color:#5C5C8A; margin:6px 0 0 0; font-size:0.78rem;">Missing operational target key-insights</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # --- CHART COMPLETELY REMOVED & REPLACED WITH HIGH-TECH MOVING ICON PANEL ---
    st.markdown("<p style='font-weight:600; font-size:1.05rem; color:#E0E0FF; margin-top:5px; margin-bottom:5px;'>🔮 Real-Time Semantic Neural Scanner</p>", unsafe_allow_html=True)
    
    scanning_text = "MATRIX SCANNING ACTIVE..." if res else "AWAITING PROFILE INGESTION..."
    st.markdown(f"""
        <div class="radar-panel">
            <div class="scanning-laser"></div>
            <div class="radar-circle">
                <div class="radar-core"></div>
            </div>
            <div class="radar-text" style="color: {'#00E676' if res else '#A370F7'}; text-shadow: 0 0 10px {'rgba(0,230,118,0.5)' if res else 'rgba(163,112,247,0.5)'};">
                {scanning_text}
            </div>
            <p style="color: #5C5C8A; font-size: 0.75rem; margin: 5px 0 0 0;">Cognito Intelligence Vector Pipeline v3.3</p>
        </div>
    """, unsafe_allow_html=True)

with col_layout_right:
    # Right panel control wrapper container housing identity cards and input fields
    st.markdown("""
        <div style="background:#131324; padding:18px; border-radius:14px; border:1px solid #22223D; margin-bottom:20px;">
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:38px; height:38px; border-radius:50%; background:linear-gradient(135deg, #A370F7, #FF69B4); display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:1rem;">H</div>
                <div>
                    <p style="margin:0; font-size:0.9rem; color:#FFFFFF; font-weight:600;">Candidate Profile: Hafsa</p>
                    <p style="margin:0; font-size:0.75rem; color:#00E676; font-weight:500;">🟢 Active Engineering Track</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Functional Form Component Fields
    uploaded_file = st.file_uploader("Upload Target Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Target Job Specifications", height=150, placeholder="Paste requirement criteria constraints description text here...")
    
    execute_pipeline = st.button("RUN ENGINE EVALUATION MATRIX", use_container_width=True)

    if execute_pipeline:
        if uploaded_file and job_desc:
            with st.spinner("Processing core match vector data..."):
                try:
                    resume_text = extract_text_from_pdf(uploaded_file)
                    results = calculate_semantic_match(resume_text, job_desc)
                    st.session_state.analysis_results = results
                    st.rerun()
                except Exception as e:
                    st.error(f"Engine Processing Pipeline Failure: {str(e)}")
        else:
            st.warning("Please upload a profile document and target criteria to initialize the analytical engine matrix.")

# 5. Bottom Segment Layout Container Rows
st.markdown("<p style='font-weight:600; font-size:1.15rem; color:#E0E0FF; margin-top:25px; margin-bottom:15px;'>🔍 Strategic Engine Insight Readouts</p>", unsafe_allow_html=True)
col_inf1, col_inf2, col_inf3 = st.columns(3, gap="medium")

with col_inf1:
    st.markdown(f"""
        <div class="insight-card" style="border-left: 4px solid #00E676;">
            <p style="color:#00E676; font-weight:700; margin:0 0 6px 0; font-size:0.92rem;">✅ Matched Competencies</p>
            <p style="color:#E0E0FF; margin:0; font-size:0.85rem; line-height:1.4;">{', '.join(matched_skills[:4]) if matched_skills else 'No current application matrix data loaded.'}</p>
        </div>
    """, unsafe_allow_html=True)

with col_inf2:
    st.markdown(f"""
        <div class="insight-card" style="border-left: 4px solid #FF69B4;">
            <p style="color:#FF69B4; font-weight:700; margin:0 0 6px 0; font-size:0.92rem;">⚡ Identified Skill Gaps</p>
            <p style="color:#E0E0FF; margin:0; font-size:0.85rem; line-height:1.4;">{', '.join(missing_skills[:4]) if missing_skills else 'No current application matrix data loaded.'}</p>
        </div>
    """, unsafe_allow_html=True)

with col_inf3:
    st.markdown(f"""
        <div class="insight-card" style="border-left: 4px solid #A370F7;">
            <p style="color:#A370F7; font-weight:700; margin:0 0 6px 0; font-size:0.92rem;">💡 Executive Summary</p>
            <p style="color:#E0E0FF; margin:0; font-size:0.82rem; line-height:1.4;">{summary}</p>
        </div>
    """, unsafe_allow_html=True)