import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Real-World Page Configurations
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="💻", layout="wide")

# 2. Premium Cyber Agency Design (Advanced CSS for Perfect High-Contrast Text)
st.markdown("""
    <style>
    /* Dark Cyber Professional Base Theme */
    .stApp {
        background-color: #030712;
        color: #f3f4f6;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* LEFT SIDEBAR PANEL TEXT CONTRAST FIX */
    section[data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid #1f2937 !important;
    }
    /* Making Sidebar Text Bright White and Bold */
    div[data-testid="stSidebarUserContent"] div.stRadio label p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    div[data-testid="stSidebarUserContent"] h2, 
    div[data-testid="stSidebarUserContent"] h4,
    div[data-testid="stSidebarUserContent"] label {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    
    /* Fixed Chat Input Visibility - Deep Crisp Contrast Text */
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
    
    /* Corporate Tech Cards Architecture */
    .agency-card {
        background: linear-gradient(145deg, #1f2937, #111827);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .service-badge {
        background-color: #1e3a8a;
        color: #60a5fa;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }
    .service-price {
        font-size: 24px;
        color: #10b981;
        font-weight: 700;
        margin: 12px 0;
    }
    
    /* Premium Header */
    .agency-header {
        text-align: center;
        padding: 40px 0;
        background: radial-gradient(circle, rgba(30,58,138,0.2) 0%, rgba(3,7,18,0) 70%);
    }
    .agency-title {
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(to right, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Real World Buttons Styling */
    div.stButton > button {
        color: #030712 !important;
        background-color: #ffffff !important;
        font-weight: bold !important;
        border: 1px solid #3b82f6 !important;
        padding: 10px !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        background-color: #3b82f6 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Secure Core Dataset (Real Industry Technical Frameworks & Live Pricing structures)
services_matrix = {
    "⚙️ DevOps Infrastructure": [
        {"id": "d1", "title": "Zero-Downtime AWS/GCP Multi-Region Pipeline", "desc": "Enterprise level high-availability scaling configuration layout, orchestrated via custom automated scripts.", "price": "$1,200", "scope": "Enterprise Cloud Setup"},
        {"id": "d2", "title": "Kubernetes Production Multi-Tenant Clustering", "desc": "Production-grade auto-scaling infrastructure, integrated traffic proxy mesh node parameters deployment.", "price": "$1,500", "scope": "Container Orchestration"},
        {"id": "d3", "title": "Infrastructure-as-Code (Terraform & Ansible)", "desc": "Complete environment cloning automation blocks setup for programmatic execution routines.", "price": "$800", "scope": "Cloud Automation"}
    ],
    "🛡️ Cyber Security Cloud": [
        {"id": "s1", "title": "Full-Scope Penetration Testing & Source Auditing", "desc": "Deep blackbox system scans, enterprise network breach simulation, logic validation patch reporting.", "price": "$2,500", "scope": "VAPT Audit Security"},
        {"id": "s2", "title": "Zero-Trust Identity Multi-Layered Access Architecture", "desc": "Automated authentication servers configuration setups, secure API data pipeline hashing blocks.", "price": "$1,100", "scope": "Enterprise Access"},
        {"id": "s3", "title": "Ransomware Defense Shield & Server Hardening", "desc": "Kernel configuration locks, firewall matrices deployment, automatic server intrusion backup scripts.", "price": "$950", "scope": "Server Hardening"}
    ],
    "🧠 AI, ML & Deep Learning": [
        {"id": "a1", "title": "Predictive Time-Series Data Forecasting Model", "desc": "Custom computational analytical algorithms architecture deployed for corporate transaction monitoring scaling.", "price": "$1,800", "scope": "Business ML Analytics"},
        {"id": "a2", "title": "Computer Vision Real-Time Detection Node", "desc": "Intelligent neural scanning frame matrices for spatial object tracking, semantic boundary analysis.", "price": "$2,200", "scope": "Neural Vision Engine"},
        {"id": "a3", "title": "Custom Autonomous LangChain Chat Agent Setup", "desc": "Corporate vector database connections architecture config, advanced Llama tuning logic layers setup.", "price": "$1,400", "scope": "Generative AI Systems"}
    ],
    "🌐 Apps & Automation Web": [
        {"id": "w1", "title": "Full-Stack Enterprise Software Web Dashboard", "desc": "Modern secure application layout built with Next.js interface, fast asynchronous FastAPI data backends.", "price": "$2,000", "scope": "Next-Gen Software"},
        {"id": "w2", "title": "High-Speed Multi-Threaded Headless Selenium Scraper", "desc": "Programmatic anti-bot bypass crawler automation blocks config, data capture indexing engines execution.", "price": "$650", "scope": "Data Scraping Automation"},
        {"id": "w3", "title": "Distributed Caching and Database Tuning Architecture", "desc": "PostgreSQL layout structural optimization configurations setup, optimized Redis storage structures deployment.", "price": "$700", "scope": "Database Performance"}
    ]
}

# 4. Multi-Page Layout Structure (Real World Left Navigation Panel)
st.sidebar.markdown("## 💻 ZAIN TECH ENGINES")
selected_section = st.sidebar.radio("Corporate Directory:", [
    "🏢 Headquarters Showcase",
    "⚙️ DevOps Infrastructure Solutions",
    "🛡️ Enterprise Cyber Security Matrix",
    "🧠 Machine & Deep Learning Engines",
    "🌐 Cloud Applications & Web Automation",
    "🤖 Interactive Autonomous AI Support Agent"
])

st.sidebar.markdown("---")
st.sidebar.markdown("#### 🛠️ SECURITY CONFIG")
groq_api_entry = st.sidebar.text_input("Enter Groq Cloud Access Token:", type="password")
st.sidebar.info("Zain Tech Official Escalation Desk:\n📞 Call/WhatsApp: +92 322 1837390")

# Universal Direct Action Communication Route String
base_whatsapp_link = "https://wa.me"

# ==================== PAGE 1: HEADQUARTERS SHOWCASE ====================
if selected_section == "🏢 Headquarters Showcase":
    st.markdown('<div class="agency-header"><div class="agency-title">ZAIN TECH</div><p style="color:#9ca3af; letter-spacing:2px; font-size:14px; text-transform:uppercase; margin-top:10px;">Enterprise Engineering • Automated Architectures</p></div>', unsafe_allow_html=True)
    
    c_left, c_right = st.columns([1.2, 1])
    with c_left:
        st.markdown("### Next-Gen System Engineering For Modern Enterprise Scales")
        st.write("Zain Tech Automation Solutions engineers mission-critical cloud configurations, multi-layer computational machine architectures, predictive learning models, and secure full-stack backend platforms designed to automate operations flawlessly.")
        st.write("👈 Use the **Corporate Directory Matrix Menu** inside the left side command interface to explore our modular premium technology sectors directly.")
        st.markdown(f'<a href="{base_whatsapp_link}General%20Enterprise%20Consultation" target="_blank"><button style="background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border: none; padding: 14px 28px; font-weight: bold; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 14px 0 rgba(59,131,246,0.4); width:100%;">📞 Schedule System Infrastructure Consultation</button></a>', unsafe_allow_html=True)
    with c_right:
        st.image("https://unsplash.com", caption="Zain Tech Mainframe Data Operations Nodes")

# ==================== GENERIC CARD RENDER FOR CORES ====================
elif selected_section != "🤖 Interactive Autonomous AI Support Agent":
    target_key = ""
    if "DevOps" in selected_section: target_key = "⚙️ DevOps Infrastructure"
    elif "Cyber" in selected_section: target_key = "🛡️ Cyber Security Cloud"
    elif "Machine" in selected_section: target_key = "🧠 AI, ML & Deep Learning"
    elif "Cloud" in selected_section: target_key = "🌐 Apps & Automation Web"
    
    if target_key:
        st.title(target_key)
        st.write("Review our live commercial technical service line packages below. Every deployment node contains full operations documentation support.")
        
        # Real-World Looped Matrix Generation Elements
        for service in services_matrix[target_key]:
            st.markdown
            <div class="agency-card">
                <span class="service-badge">{service['scope']}</span>
