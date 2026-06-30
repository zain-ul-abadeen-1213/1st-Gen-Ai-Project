import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Real-World Page Configurations
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="💻", layout="wide")

# 2. Premium Deep Cyber Dark Interface Styling (Advanced Custom CSS)
st.markdown("""
    <style>
    /* Main Background & Base Typography Settings */
    .stApp {
        background-color: #030712 !important;
        color: #f3f4f6 !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Left Sidebar Panel Modern Contrast Override */
    section[data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid #1f2937 !important;
    }
    div[data-testid="stSidebarUserContent"] div.stRadio label p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    div[data-testid="stSidebarUserContent"] h1, 
    div[data-testid="stSidebarUserContent"] h2, 
    div[data-testid="stSidebarUserContent"] h3, 
    div[data-testid="stSidebarUserContent"] h4, 
    div[data-testid="stSidebarUserContent"] label {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* Fixed Chat Input Visibility - High Deep Contrast Text */
    textarea[data-testid="stChatInputTextArea"] {
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        background-color: #ffffff !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 8px !important;
    }
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #64748b !important;
    }

    /* Stylish Premium Containers Layout */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, #0f172a, #0b0f19) !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 25px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4) !important;
    }

    /* Global Streamlit Buttons Custom Polish */
    div.stButton > button, div.stDownloadButton > button, .stLinkButton > a {
        color: #ffffff !important;
        background: linear-gradient(135deg, #1e3a8a, #2563eb) !important;
        border: 1px solid #3b82f6 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100% !important;
        text-align: center !important;
        padding: 10px 0 !important;
        display: inline-block !important;
        text-decoration: none !important;
    }
    div.stButton > button:hover, .stLinkButton > a:hover {
        background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
        box-shadow: 0px 0px 15px rgba(59, 130, 246, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Secure Core Dataset (Real Corporate Technical Services Portfolio)
services_matrix = {
    "⚙️ DevOps Infrastructure": [
        {"title": "Zero-Downtime AWS/GCP Multi-Region Pipeline", "desc": "Enterprise level high-availability scaling configuration layout, orchestrated via custom automated scripts.", "price": "$1,200", "scope": "Enterprise Cloud Setup"},
        {"title": "Kubernetes Production Multi-Tenant Clustering", "desc": "Production-grade auto-scaling infrastructure, integrated traffic proxy mesh node parameters deployment.", "price": "$1,500", "scope": "Container Orchestration"},
        {"title": "Infrastructure-as-Code (Terraform & Ansible)", "desc": "Complete environment cloning automation blocks setup for programmatic execution routines.", "price": "$800", "scope": "Cloud Automation"}
    ],
    "🛡️ Cyber Security Cloud": [
        {"title": "Full-Scope Penetration Testing & Source Auditing", "desc": "Deep blackbox system scans, enterprise network breach simulation, logic validation patch reporting.", "price": "$2,500", "scope": "VAPT Audit Security"},
        {"title": "Zero-Trust Identity Multi-Layered Access Architecture", "desc": "Automated authentication servers configuration setups, secure API data pipeline hashing blocks.", "price": "$1,100", "scope": "Enterprise Access"},
        {"title": "Ransomware Defense Shield & Server Hardening", "desc": "Kernel configuration locks, firewall matrices deployment, automatic server intrusion backup scripts.", "price": "$950", "scope": "Server Hardening"}
    ],
    "🧠 AI, ML & Deep Learning": [
        {"title": "Predictive Time-Series Data Forecasting Model", "desc": "Custom computational analytical algorithms architecture deployed for corporate transaction monitoring scaling.", "price": "$1,800", "scope": "Business ML Analytics"},
        {"title": "Computer Vision Real-Time Detection Node", "desc": "Intelligent neural scanning frame matrices for spatial object tracking, semantic boundary analysis.", "price": "$2,200", "scope": "Neural Vision Engine"},
        {"title": "Custom Autonomous LangChain Chat Agent Setup", "desc": "Corporate vector database connections architecture config, advanced Llama tuning logic layers setup.", "price": "$1,400", "scope": "Generative AI Systems"}
    ],
    "🌐 Apps & Automation Web": [
        {"title": "Full-Stack Enterprise Software Web Dashboard", "desc": "Modern secure application layout built with Next.js interface, fast asynchronous FastAPI data backends.", "price": "$2,000", "scope": "Next-Gen Software"},
        {"title": "High-Speed Multi-Threaded Headless Selenium Scraper", "desc": "Programmatic anti-bot bypass crawler automation blocks config, data capture indexing engines execution.", "price": "$650", "scope": "Data Scraping Automation"},
        {"title": "Distributed Caching and Database Tuning Architecture", "desc": "PostgreSQL layout structural optimization configurations setup, optimized Redis storage structures deployment.", "price": "$700", "scope": "Database Performance"}
    ]
}

# 4. Professional Sidebar Corporate Menu Layout
st.sidebar.markdown("<h2 style='color:#60a5fa;'>💻 ZAIN TECH ENGINES</h2>", unsafe_allow_html=True)
selected_section = st.sidebar.radio("Corporate Directory Matrix:", [
    "🏢 Headquarters Showcase",
    "⚙️ DevOps Infrastructure Solutions",
    "🛡️ Enterprise Cyber Security Matrix",
    "🧠 Machine & Deep Learning Engines",
    "🌐 Cloud Applications & Web Automation",
    "🤖 Interactive Autonomous AI Support Agent"
])

st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color:#a78bfa;'>🛠¾ ACCESS SECURITY</h4>", unsafe_allow_html=True)
groq_api_entry = st.sidebar.text_input("Enter Groq Access Token:", type="password")
st.sidebar.info("Zain Tech Escalation Desk:\n📞 Call/WhatsApp: 03221837390")

# Universal Direct Contact WhatsApp Core Link
base_whatsapp_link = "https://wa.me"

# ==================== PAGE 1: HEADQUARTERS SHOWCASE ====================
if selected_section == "🏢 Headquarters Showcase":
    st.markdown("<h1 style='color:#60a5fa; text-align:center;'>🚀 ZAIN TECH AUTOMATION SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#9ca3af; letter-spacing:2px; text-transform:uppercase; margin-bottom:40px;'>Enterprise Engineering & Systemic Architectures Matrix</p>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.write("Zain Tech Automation Solutions engineers mission-critical cloud configurations, multi-layer computational machine architectures, predictive learning models, and secure full-stack backend platforms designed to automate enterprise operations flawlessly.")
        st.info("👈 Use the Corporate Directory Matrix Menu inside the left side sidebar panel to explore our specialized premium technology sectors directly.")
        st.link_button("📞 Schedule Enterprise Consultation Now", f"{base_whatsapp_link}General%20Enterprise%20Consultation")
    with col_right:
        st.image("https://unsplash.com", caption="Zain Tech Infrastructure Management Node")

# ==================== GENERIC SERVICES RENDER ====================
elif selected_section != "🤖 Interactive Autonomous AI Support Agent":
    target_key = ""
    if "DevOps" in selected_section: target_key = "⚙️ DevOps Infrastructure"
    elif "Cyber" in selected_section: target_key = "🛡️ Cyber Security Cloud"
    elif "Machine" in selected_section: target_key = "🧠 AI, ML & Deep Learning"
    elif "Cloud" in selected_section: target_key = "🌐 Apps & Automation Web"
    
    if target_key:
        st.title(target_key)
        st.write("Review our live commercial technical service line packages below. Every deployment node contains full operations documentation support.")
        st.markdown("---")
        
        # Core Matrix Render Loops
        for service in services_matrix[target_key]:
            with st.container():
                st.subheader(f"🔹 {service['title']}")
                st.caption(f"Domain Focus Matrix: {service['scope']}")
                st.write(service['desc'])
                st.metric(label="Base Implementation Cost", value=service['price'])
                
                if st.button(f"🛒 Add Framework to Queue System ({service['title']})", key=f"cart_{service['title']}"):
                    st.toast(f"System Matrix Pipeline Initialized for: {service['title']}")
                    
                custom_wa_text = f"{base_whatsapp_link}{service['title'].replace(' ', '%20')}"
                st.link_button("📞 Purchase / Deploy on WhatsApp Live", custom_wa_text)

# ==================== PAGE 6: LIVE AI CHATBOT AGENT ====================
if selected_section == "🤖 Interactive Autonomous AI Support Agent":
    st.title("🤖 Zain Tech Autonomous Enterprise Operations Agent")
