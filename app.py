import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Page Global Setup
st.set_page_config(page_title="Zain Tech", page_icon="💻", layout="wide")

# 2. Premium Cyber Dark CSS Style (Fixed Contrast Text Elements)
st.markdown("""
    <style>
    .stApp {
        background-color: #030712 !important;
        color: #f3f4f6 !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid #1f2937 !important;
    }
    div[data-testid="stSidebarUserContent"] label, 
    div[data-testid="stSidebarUserContent"] p,
    div[data-testid="stSidebarUserContent"] h2 {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    textarea[data-testid="stChatInputTextArea"] {
        color: #000000 !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration Setup
st.sidebar.markdown("## 💻 ZAIN TECH ENGINES")
page = st.sidebar.radio("Corporate Directory Matrix:", ["🏠 Headquarters Showcase", "⚙️ Technical Services Portfolio", "🤖 AI Support Agent Chat"])

st.sidebar.markdown("---")
groq_key = st.sidebar.text_input("Enter Groq Access Token:", type="password")
st.sidebar.info("Official Support:\n📞 Call/WhatsApp: 03221837390")

# Persistent Memory Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Universal Direct Contact Route
wa_link = "https://wa.me."

# ==================== PAGE 1: HOME SHOWCASE ====================
if page == "🏠 Headquarters Showcase":
    st.title("🚀 ZAIN TECH AUTOMATION SOLUTIONS")
    st.write("We engineer mission-critical cloud configurations, multi-layer computational machine architectures, predictive learning models, and secure full-stack backend platforms designed to automate operations flawlessly.")
    st.info("👈 Use the Corporate Directory Matrix Menu inside the left side sidebar panel to switch sections directly.")
    st.link_button("📞 Schedule Enterprise Consultation Now", wa_link)

# ==================== PAGE 2: REAL-WORLD PORTFOLIO ====================
if page == "⚙️ Technical Services Portfolio":
    st.title("⚡ Premium Engineering Services Matrix")
    st.write("Review our live commercial technical service line packages below. Every deployment node contains full operations documentation support.")
    
    # Block 1: DevOps
    st.markdown("---")
    st.subheader("⚙️ Enterprise DevOps Infrastructure")
    st.write("Zero-Downtime AWS/GCP Multi-Region Pipelines, Kubernetes Production Multi-Tenant Clustering, and automated Terraform infrastructure environment scaling loops.")
    st.metric(label="Base Implementation Cost", value="$1,200")
    st.link_button("📞 Purchase / Deploy on WhatsApp Live", wa_link)

    # Block 2: Security
    st.markdown("---")
    st.subheader("🛡️ Enterprise Cyber Security Matrix")
    st.write("Full-Scope Penetration Testing (VAPT), Zero-Trust Identity Multi-Layered Access Architecture, source code dependency vulnerability auditing, and server hardening shields.")
    st.metric(label="Base Implementation Cost", value="$2,500")
    st.link_button("📞 Purchase / Deploy on WhatsApp Live", wa_link)

    # Block 3: AI/ML
    st.markdown("---")
    st.subheader("🧠 Machine & Deep Learning Engines")
    st.write("Predictive Time-Series Data Forecasting Models, Computer Vision Real-Time Detection Nodes, and Custom Autonomous LangChain Chat Agent Setup with corporate vector databases.")
    st.metric(label="Base Implementation Cost", value="$1,800")
    st.link_button("📞 Purchase / Deploy on WhatsApp Live", wa_link)

    # Block 4: Web Apps
    st.markdown("---")
    st.subheader("🌐 Cloud Applications & Web Automation")
    st.write("Full-Stack Enterprise Software Web Dashboards built with Next.js & FastAPI, high-speed multi-threaded headless Selenium scrapers, and distributed Redis memory storage systems.")
    st.metric(label="Base Implementation Cost", value="$2,000")
    st.link_button("📞 Purchase / Deploy on WhatsApp Live", wa_link)

# ==================== PAGE 3: AI CHAT AGENT ====================
if page == "🤖 AI Support Agent Chat":
    st.title("🤖 Zain Tech Autonomous Enterprise Operations Agent")
    st.write("Talk instantly with our system framework automation representative regarding technical metrics or deployment prices.")
    
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"): st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant"): st.write(msg.content)
            
    user_input = st.chat_input("Ask Zain Tech Assistant Anything...")
    if user_input:
        with st.chat_message("user"): st.write(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        
        if not groq_key:
            st.warning("⚠️ High security cloud access credential required. Please type your Groq Cloud Access Token inside the sidebar dashboard.")
        else:
            with st.chat_message("assistant"):
                system_rule = "Aap Zain Tech Automation Solutions ke official enterprise ai representative assistant hain. Hamari services DevOps, Security audits, Neural Network Machine Learning Models aur Web Apps hain. Pricing ya deployment deal ki baat ho toh kahein ke complete execution strategy ke liye founder Zain Ul Abadeen se direct call ya WhatsApp rabta karein: +923221837390."
                messages_pipeline = [SystemMessage(content=system_rule)] + st.session_state.chat_history
                llm_engine = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_key)
                execution_response = llm_engine.invoke(messages_pipeline)
                st.write(execution_response.content)
                st.session_state.chat_history.append(AIMessage(content=execution_response.content))
