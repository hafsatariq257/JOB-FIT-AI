import os
import streamlit as st
from supabase import create_client, Client

# 1. Clean Direct String Assignment (No syntax errors)
url: str = "https://wilqyyjakhbnxrkuhul.supabase.co"
key: str = "sb_publishable_BNpYfeGJAlvXpjROMx7nlg_SKzq9XMp"  
supabase: Client = create_client(url, key)

# 3. Secure Portal View Entry Point Layout
st.subheader("🔑 Access Portal")

email = st.text_input("Corporate Email ID", placeholder="name@domain.com")
password = st.text_input("Password", type="password")
account_type = st.selectbox("Account Role", ["Candidate", "HR Recruiter"])

if st.button("Initialize Secure Session"):
    if email and password:
        with st.spinner("Verifying credentials against cloud data clusters..."):
            try:
                # Abhi temporary logic session state save karne ke liye
                st.session_state.is_authenticated = True
                st.session_state.user_email = email
                st.session_state.user_role = account_type
                st.session_state.current_route = "dashboard"
                st.success(f"Authenticated successfully as {account_type}!")
                st.rerun()
            except Exception as e:
                st.error(f"Authentication Failure: {str(e)}")
    else:
        st.warning("Please insert valid profile entry credentials.")