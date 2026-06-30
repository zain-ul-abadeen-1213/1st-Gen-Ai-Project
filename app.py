import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Page Global Setup
st.set_page_config(page_title="Zain Tech", page_icon="💻", layout="wide")

# 2. Premium Cyber Dark CSS Style (Fixed Universal Text Contrast)
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

# 3. Sidebar Configuration Setup (Strict 3 Pages Layout)
st.sidebar.markdown("## 💻 ZAIN TECH ENGINES")
page = st.sidebar.radio("Corporate Directory:", ["🏠 Headquarters Showcase", "⚙️ Real-World Services Portfolio", "🤖 AI Support Agent Chat"])

st.sidebar.markdown("---")
groq_key = st.sidebar.text_input("Enter Groq Access Token:", type="password")
st.sidebar.info("Official Support:\n📞 Call/WhatsApp: 03221837390")

# Persistent Memory Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Universal Direct Contact WhatsApp Redirection Link
wa_link = "https://wa.me."

# ==================== PAGE 1: HOME SHOWCASE ====================
if page == "🏠 Headquarters Showcase":
    st.title("🚀 ZAIN TECH AUTOMATION SOLUTIONS")
    st.write("We engineer mission-critical cloud configurations, multi-layer computational machine architectures, predictive learning models, and secure full-stack backend platforms designed to automate operations flawlessly.")
    st.info("👈 Use the Corporate Directory Matrix Menu inside the left sidebar panel to switch sections directly.")
    st.link_button("📞 Schedule Enterprise Consultation Now", wa_link)

# ==================== PAGE 2: REAL-WORLD PORTFOLIO ====================
if page == "⚙️ Real-World Services Portfolio":
    st.title("⚡ Premium Engineering Services Matrix (Basic to Advance)")
    st.write("Review our real-world tech stack catalog below. Every implementation node scales from basic local scripts up to deep advance global cloud structures.")
    
    # DevOps Vertical
    st.markdown("---")
    st.markdown("### ⚙️ DevOps & Cloud Computing Operations")
    st.write("🟢 **Level 1 (Basic):** Local Server Environment Config (Dockerized) • Static Web App Cloud Static Hosting Setup • Linux Server Shell Command Script Automation")
    st.write("🟡 **Level 2 (Intermediate):** Core GitHub Actions CI/CD Pipeline Automation • Centralized Database Automated Replication Strategy • Basic Terraform Resource Scripting")
    st.write("🔴 **Level 3 (Advance):** Production-Grade Kubernetes Elastic Auto-Scaling Clusters • High-Availability Multi-Region AWS / Google Cloud Global Pipelines")
    st.link_button("📞 Order Cloud Frameworks via WhatsApp Live", wa_link)

    # Cyber Security Vertical
    st.markdown("---")
    st.markdown("### 🛡️ Cyber Security Cloud Matrix")
    st.write("🟢 **Level 1 (Basic):** SSL/TLS Certificate System Configuration • Basic WordPress/Shopify Site Security Hardening • Server Firewall Access Rules Tuning")
    st.write("🟡 **Level 2 (Intermediate):** Automated Source Code Dependency Vulnerability Audits • Secure API Token Validation & Routing Protocols • Multi-Factor Authentication (MFA)")
    st.write("🔴 **Level 3 (Advance):** Full-Scope Professional Black-Box Network Penetration Hacking Scans • Automated Zero-Trust Enterprise Key Server Configurations")
    st.link_button("📞 Order Cyber Security Packages via WhatsApp Live", wa_link)

    # AI & Machine Learning Vertical
    st.markdown("---")
    st.markdown("### 🧠 Data Science & Generative AI Matrix")
    st.write("🟢 **Level 1 (Basic):** Automated Lead Generation Bot Web Processing • Basic Excel Sheet Formula Analytics Script Automation • Customer Feedback Sentiment Parsers")
    st.write("🟡 **Level 2 (Intermediate):** Predictive Time-Series Revenue Forecasting Data Models • Corporate Documents OCR Intelligent Data Retrieval Pipelines")
    st.write("🔴 **Level 3 (Advance):** Custom Autonomous LangChain Chat Agent Architectures • Real-Time Spatial Object Tracking Neural Computer Vision Nodes")
    st.link_button("📞 Order AI Engines via WhatsApp Live", wa_link)

    # Web Systems & Automation Vertical
    st.markdown("---")
    st.markdown("### 🌐 Web Systems & Headless Crawlers")
    st.write("🟢 **Level 1 (Basic):** Landing Page Web Interface UI Responsive Deployments • Local Python Automation Web-Scraping Scripts • Local Database SQLite Data Backup Pipelines")
    st.write("🟡 **Level 2 (Intermediate):** Secure RESTful API Backend Architectures with Python FastAPI • High-Speed Multi-Threaded Headless Selenium Automation Scrapers")
    st.write("🔴 **Level 3 (Advance):** Next.js Enterprise Software Single-Page Application Interfaces • Scalable Distributed PostgreSQL Database Structuring Optimization")
    st.link_button("📞 Order App Frameworks via WhatsApp Live", wa_link)

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
                system_rule = "Aap Zain Tech Automation Solutions ke official ai representative assistant hain. Hamari services DevOps, Security audits, Neural Network Machine Learning Models aur Web Apps hain. Pricing ya deployment deal ki baat ho toh kahein ke complete execution strategy ke liye founder Zain Ul Abadeen se direct call ya WhatsApp rabta karein: +923221837390."
                messages_pipeline = [SystemMessage(content=system_rule)] + st.session_state.chat_history
                llm_engine = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_key)
                execution_response = llm_engine.invoke(messages_pipeline)
                st.write(execution_response.content)
                st.session_state.chat_history.append(AIMessage(content=execution_response.content))
