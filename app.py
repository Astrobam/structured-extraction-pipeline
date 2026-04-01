import streamlit as st
import pdfplumber

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 Resume Analyzer")
st.caption("Upload a resume and ask a question about it.")

uploaded_file = st.file_uploader("Upload a resume", type=["pdf", "txt"])


def extract_text(file) -> str:
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    return file.read().decode("utf-8")


if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        raw_text = extract_text(uploaded_file)

    st.success("Resume uploaded and text extracted.")

    with st.expander("Extracted Text", expanded=False):
        st.text(raw_text)

    st.divider()

    st.text_input(
        "Your question about this resume",
        placeholder="e.g. How many years of experience does this candidate have?",
        key="user_query",
        disabled=True,
        help="Gemini-powered analysis coming in the next step.",
    )
    st.caption("Query analysis will be enabled in the next update.")
