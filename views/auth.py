import streamlit as st
from supabase import create_client, Client

# Initialize database credentials directly
url: str = "https://wilqyyjakhbnxrkuhul.supabase.co"
key: str = "sb_publishable_BNpYfeGJAlvXpjROMx7nlg_SKzq9XMp"
supabase: Client = create_client(url, key)

st.markdown("""
    <style>
    .auth-container {
        background: #18182C;
        border: 1px solid #29294D;
        border-radius: 14px;
        padding: 35px;
        max-width: 480px;
        margin: 40px auto;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="auth-container">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #FFFFFF; margin-top: 0; text-align: center;">🔑 COGNITO AUTH GATE</h2>', unsafe_allow_html=True)

email = st.text_input("Enter Email ID", placeholder="user@domain.com")
password = st.text_input("Secure Password", type="password")
role = st.selectbox("Select Account Designation", ["Corporate HR Recruiter", "Tech Candidate Track"])

st.markdown("<br>", unsafe_allow_html=True)
if st.button("INITIALIZE SECURE APPLICANT SSN", use_container_width=True):
    if email and password:
        st.session_state.is_authenticated = True
        st.session_state.user_email = email
        st.session_state.user_role = role
        st.success("Session Verified Successfully!")
        st.switch_page("views/dashboard.py")
    else:
        st.error("Please insert valid profile entry credentials.")

if st.button("« Return to Landing Page", use_container_width=True):
    st.switch_page("views/landing.py")

st.markdown('</div>', unsafe_allow_html=True)