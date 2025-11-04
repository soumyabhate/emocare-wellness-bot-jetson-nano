import streamlit as st

# Page config
st.set_page_config(page_title="EmoCare Therapy Bot", layout="centered")

# Title and header
st.markdown("<h1 style='text-align: center;'>🌟 EmoCare Therapy Bot</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-bottom: 60px;'>Welcome to your interactive therapy space</h3>", unsafe_allow_html=True)

# Irregular animated blob using CSS
blob_html = """
<style>
.irregular-blob {
  width: 220px;
  height: 220px;
  background: #00f0ff;
  border-radius: 60% 40% 55% 45% / 50% 60% 40% 50%;
  animation: morph 4s infinite ease-in-out;
  margin: auto;
  box-shadow: 0 0 30px #00f0ff;
}

@keyframes morph {
  0% {
    border-radius: 60% 40% 55% 45% / 50% 60% 40% 50%;
  }
  50% {
    border-radius: 50% 60% 40% 60% / 60% 40% 60% 40%;
  }
  100% {
    border-radius: 60% 40% 55% 45% / 50% 60% 40% 50%;
  }
}
</style>
<div class="irregular-blob"></div>
"""
st.markdown(blob_html, unsafe_allow_html=True)

# Centered Recording button (non-neon)
st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 40px;'>
        <form action='#' method='post'>
            <button style='margin: 40px; padding: 10px 20px; font-size: 16px; background-color: #0055aa; border: none; border-radius: 8px; color: white; cursor: pointer;'>
                🎙️ Recording
            </button>
        </form>
    </div>
""", unsafe_allow_html=True)