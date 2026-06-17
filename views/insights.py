import streamlit as st

st.title("🔍 Deep-Dive Semantic Analytics")
st.markdown("<p style='color:#8B8BAE; font-size:1.2rem; margin-top:-15px;'>Granular Competency Matrix Breakdown</p>", unsafe_allow_html=True)
st.markdown("---")

# Custom structural card styles
st.markdown("""
    <style>
    .metric-card-good {
        background: #18182C;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(0, 230, 118, 0.3);
        margin-bottom: 15px;
    }
    .metric-card-bad {
        background: #18182C;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 105, 180, 0.3);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.get("analysis_results"):
    res = st.session_state.analysis_results
    col_matched, col_missing = st.columns(2)
    
    with col_matched:
        st.markdown("### ✅ Verified Core Competencies")
        matched_skills = res.get("matched_skills", [])
        if matched_skills:
            for skill in matched_skills:
                st.markdown(f"<div class='metric-card-good'><b style='color:#00E676;'>✔ Verified:</b> {skill}</div>", unsafe_allow_html=True)
        else:
            st.info("No matching structural keywords identified for this target profile.")
            
    with col_missing:
        st.markdown("### ⚠️ Identified Structural Skill Gaps")
        missing_skills = res.get("missing_skills", [])
        if missing_skills:
            for skill in missing_skills:
                st.markdown(f"<div class='metric-card-bad'><b style='color:#FF69B4;'>⚡ Gap:</b> {skill}</div>", unsafe_allow_html=True)
        else:
            st.success("Zero capability gaps detected. Profile matches technical constraints perfectly.")
else:
    st.info("No active matrix data available. Please upload a profile and run the pipeline from the Executive Dashboard.")