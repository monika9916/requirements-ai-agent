import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from core.requirements_generator import generate_requirements

st.set_page_config(page_title="AI Requirements Engineer", layout="wide")

st.title("🧠 AI Requirements Engineering Agent")

uploaded_file = st.file_uploader("Upload your code file", type=["py", "js", "java", "txt"])

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Code")
    st.code(code)

    if st.button("Generate Requirements"):

        with st.spinner("Analyzing code using AI..."):
            result = generate_requirements(code)

        st.subheader("📋 Generated Requirements")
        st.markdown(result)

        with open("outputs/requirements.md", "w") as f:
            f.write(result)

        st.success("Saved to outputs/")