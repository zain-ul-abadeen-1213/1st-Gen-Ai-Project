import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# 1. Page Config (Futuristic Icon aur Title)
st.set_page_config(page_title="Zain Tech AI", page_icon="⚡", layout="centered")

# 2. Advanced AI Styling (Custom CSS for perfect contrast)
st.markdown("""
    <style>
    /* Main Background aur Font Setting */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3 !important;
    }
    
    /* Chat Messages ke Text ko bilkul saaf aur bright dikhane ke liye */
    div[data-testid="stChatMessage"] p, 
    div[data-testid="stChatMessage"] li, 
    div[data-testid="stChatMessage"] span,
    div[data-testid="stChatMessage"] {
        color: #e6edf3 !important;
        font-size: 16px;
        line-height: 1.6;
    }
    
    /* Futuristic Header Banner */
    .ai-banner {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        font-size: 38px;
        margin-bottom: 5px;
        letter-spacing: 2px;
        text-shadow: 0px 0px 20px rgba(0, 242, 254, 0.4);
    }
    
    .ai-sub {
        text-align: center;
        color: #8b949e;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 14px;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Branding (Zain Tech Automation Solutions)
st.markdown('<div class="ai-banner">ZAIN TECH</div>', unsafe_allow_html=True)
st.markdown('<div class="ai-sub">Automation Solutions • Next-Gen AI</div>', unsafe_allow_html=True)

# 4. Groq API Key Setup (Sidebar)
st.sidebar.markdown("### 🛠️ CONTROL PANEL")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
st.sidebar.info("Designed & Developed by Zain Tech.")

# 5. Chat History System
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 6. Chat Messages Interface (Custom Avatars)
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.write(message.content)

# 7. User Input Field
user_query = st.chat_input("Ask Zain Tech AI anything...")

if user_query:
    if not groq_api_key:
        st.info("⚠️ Please enter your Groq API Key in the sidebar control panel.")
        st.stop()

    # User Message Box
    with st.chat_message("user", avatar="👤"):
        st.write(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    # AI (Groq Engine) Message Box
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("⚡ Processing via Zain Tech Automation Engines..."):
            try:
                # Super-fast Llama Model
                llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)
                
                ai_response = llm.invoke(st.session_state.chat_history)
                
                st.write(ai_response.content)
                st.session_state.chat_history.append(AIMessage(content=ai_response.content))
                
            except Exception as e:
                st.error(f"System Error: {e}")
