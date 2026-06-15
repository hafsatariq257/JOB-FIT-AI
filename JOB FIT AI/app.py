import streamlit as st

# Initialize Global Executive Page Configurations
st.set_page_config(
    page_title="Cognito JobFit Analytics",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Instantiate Global Session State Matrix to pass data across different pages
if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None

# Updated paths pointing to the 'views' directory
pages = {
    "Talent Workspace": [
        st.Page("views/dashboard.py", title="Executive Dashboard", icon="📊"),
    ],
    "Deep-Dive Analytics": [
        st.Page("views/insights.py", title="Semantic Insights", icon="🔍"),
    ]
}

# Run Routing Management Engine
pg = st.navigation(pages)
pg.run()