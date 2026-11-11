import time
from google import genai
from dotenv import load_dotenv
import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Sarvesh App",  # Changes the browser tab title
    page_icon="🚀",  # Changes the tab icon (can be an emoji or a file path to an image)
    layout="wide",  # Optional: sets page layout to wide
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(BASE_DIR, "travel_bg.png")

with open(image_path, "rb") as f:
    image = base64.b64encode(f.read()).decode()

load_dotenv()
client = genai.Client()

#st.title("Travel assistant")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        min-height: 100vh;
    }}

    /* Make Streamlit main area transparent */
    .main {{
        background: transparent;
    }}

    /* Hide default Streamlit header */
    header {{
        background: transparent !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<div style="
    background: rgba(10, 30, 65, 0.72);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
    backdrop-filter: blur(8px);
    margin-bottom: 25px;
">

<h1 style="font-size: 45px; margin-bottom: 5px;">
✈️ Travel Buddy
</h1>

<p style="font-size: 22px; margin-top: 5px;">
🌍 Your Intelligent Travel Companion
</p>

<p style="font-size: 16px;">
Plan • Explore • Discover • Travel
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: rgba(15, 35, 70, 0.75);
    padding: 25px;
    border-radius: 20px;
    color: white;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
">

<h2>🤖 Hello, Traveler! 👋</h2>

<p style="font-size:18px;">
I'm your AI Travel Assistant. Ask me anything about your next adventure.
</p>

<p style="
    background: rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 12px;
">
✈️ <b> "Got a destination? Let's make it legendary.” 🔥</b>
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
/* Caption colour */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}


/* All question labels */
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stRadio label,
.stMultiSelect label {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Radio button options */
.stRadio div[role="radiogroup"] label {
    color: white !important;
}

/* Multiselect options */
.stMultiSelect div[data-baseweb="tag"] {
    color: black !important;
}

/* Input text */
.stTextInput input,
.stNumberInput input {
    color: #222222 !important;
}

/* Input backgrounds */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
}

</style>
""", unsafe_allow_html=True)


st.caption("This is a travel assistant that helps you plan your trips and find the best destinations.")

location= st.text_input("where do you want to  go?")
days = st.number_input("Enter the number of days for your trip:", min_value=1, max_value=30)
budget = st.selectbox("Select your budget", ["Luxury", "Moderate", "Budgeted"])
travel_type = st.radio("who are you travelling with", [ "Family", "Alone","Friends"])
intrest = st.multiselect("Select your interests", ["Adventure ", "Cultural", "Relaxation"])


prompt =f"""you are an travel planner user is saying he/she is going to {location} for {days} days,
he is on a {budget} budget and he is travelling with {travel_type} 
and has interests in {intrest}
and share answer in bullet format"""

if st.button("plan my trip"):
    interaction = client.interactions.create(
     model="gemini-3.5-flash-lite",
    input=prompt,
     system_instruction="You are an experienced travel planner.",
    stream=True,
    generation_config={"temperature": 0.7,
                          "top_K": 20,
                          "max output tokens": 400},)
    with st.spinner("Wait for a sec..", show_time =True):
        time.sleep(5)
    st.success("Here are some fantastic suggestions ")
    st.write(interaction.output_text)