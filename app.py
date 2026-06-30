import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Enterprise Page Global Settings
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="🏢", layout="wide")

# 2. Premium Cyber Dark Base Theme with Network Grid Background Image Injection
st.markdown("""
    <style>
    /* Professional Tech Blueprint Background Wallpaper Injection */
    .stApp {
        background-image: linear-gradient(rgba(3, 7, 18, 0.85), rgba(3, 7, 18, 0.95)), url('https://unsplash.com') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: #f3f4f6 !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Left Sidebar Command Matrix Overhaul */
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
    
    /* Fixed Chat Input Control Contrast Fix */
    textarea[data-testid="stChatInputTextArea"] {
        color: #000000 !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
    }
    
    /* Trust-Metric Block Configurations */
    .trust-badge-container {
        background: rgba(17, 24, 39, 0.75) !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Corporate Navigation (Strict 3 Pages Layout Element)
st.sidebar.markdown("## 💻 ZAIN TECH ENGINES")
page = st.sidebar.radio("Corporate Directory Matrix:", ["🏢 Corporate Overview", "⚙️ Enterprise Services Matrix", "🤖 Autonomous AI Support Agent"])

st.sidebar.markdown("---")
groq_key = st.sidebar.text_input("Enter Groq Cloud Access Token:", type="password")
st.sidebar.info("Zain Tech Escalation Desk:\n📞 Call/WhatsApp: 03221837390")

# Persistent Memory Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Global Official Corporate Communication Routing Endpoint
wa_link = "https://wa.me."

# ==================== PAGE 1: CORPORATE OVERVIEW ====================
if page == "🏢 Corporate Overview":
    st.title("🚀 ZAIN TECH AUTOMATION SOLUTIONS")
    st.subheader("Global Technology Consulting & Enterprise Software Transformation Mainframe")
    st.write("Zain Tech Automation Solutions is a premier next-generation technology engineering corporation. We help modern enterprises scale operations globally by architecting highly-scalable distributed cloud networks, provisioning multi-tenant computing pipelines, designing data science neural matrices, and implementing zero-trust cyber security frameworks.")
    
    st.markdown("---")
    st.markdown("### 🏆 Enterprise Operations Integrity (Trust & Credibility Matrix)")
    
    # 3 Column Real-World Trust Metric Display
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="System Architecture SLA", value="99.99% Uptime", delta="Guaranteed Active")
    with m_col2:
        st.metric(label="Global Security Audit Pass", value="ISO 27001 Ready", delta="Zero Vulnerabilities")
    with m_col3:
        st.metric(label="Production Frameworks", value="100+ Enterprise Nodes", delta="Fully Documented")
        
    st.markdown("---")
    st.info("👈 Use the Corporate Directory Menu inside the left sidebar panel to navigate our specialized engineering capabilities.")
    st.link_button("📞 Schedule Enterprise Consultation Now", wa_link)

# ==================== PAGE 2: REAL-WORLD SYSTEMS PORTFOLIO ====================
if page == "⚙️ Enterprise Services Matrix":
    st.title("⚙️ Global Engineering Capabilities & Core Technology Verticals")
    st.write("Review our high-performance technical service catalog engineered to power modern enterprise infrastructure scales seamlessly (Systems Limited & 10Pearls Corporate Grade).")
    
    # DevOps Vertical
    st.markdown("---")
    st.markdown("### ☁️ Cloud Infrastructure & Enterprise DevOps Automation")
    st.write("We design resilient multi-cloud strategies and zero-downtime microservices orchestration loops built to manage massive computational processing loads efficiently.")
    st.write("🔹 **Infrastructure as Code (IaC):** Automated single-command deployment configurations using standard enterprise HashiCorp Terraform modules.")
    st.write("🔹 **High-Availability Cloud Design:** Multi-region load balancing failovers, continuous backup replication channels on AWS, Azure, and Google Cloud.")
    st.write("🔹 **Microservices Orchestration Mesh:** Production-grade Kubernetes auto-scaling clusters provisioning and multi-tenant container management.")
    st.write("🔹 **Automated Delivery Channels:** Advanced continuous integration and continuous deployment (CI/CD) pipelines built via GitHub Actions and GitLab Runners.")
    st.write("🔹 **System Optimization & Cost Audits:** Real-time computational node analysis and metrics tracking to minimize corporate cloud billing variables.")
    st.link_button("🚀 Deploy Production Cloud Architecture via WhatsApp", wa_link)

    # Cyber Security Vertical
    st.markdown("---")
    st.markdown("### 🛡️ Cyber Security Hardening & Vulnerability Assessments (VAPT)")
    st.write("We safeguard mission-critical digital assets by deploying multi-layer defense perimeters and auditing application software logics comprehensively.")
    st.write("🔹 **Full-Scope Penetration Testing:** Deep black-box and white-box network breach simulations to discover hidden infrastructure vulnerabilities.")
    st.write("🔹 **Zero-Trust Access Identity Architecture:** Centralized secure credential rotation infrastructure integration leveraging modern secret vaults.")
    st.write("🔹 **Application Logic Hardening:** Intercepting cross-site scripting (XSS), software code exploitation layers, and SQL injections completely.")
    st.write("🔹 **Server Core Defense Hardening:** Linux kernel configuration access locks, secure cryptographic key enforcements, and strict firewall proxies.")
    st.write("🔹 **Compliance & Source Auditing:** Real-time software dependency vulnerability analysis and formatting architecture for international safety clearance audits.")
    st.link_button("🚀 Procure High-End Security Audits via WhatsApp", wa_link)

    # Data Science & AI Vertical
    st.markdown("---")
    st.markdown("### 🧠 Predictive Analytics, Data Science & Generative AI")
    st.write("We build sophisticated custom language modules and train state-of-the-art neural computation matrices that turn raw corporate data sets into operational value.")
    st.write("🔹 **Autonomous Language Agents:** Engineering custom LangChain bot architectures capable of executing complex business processes programmatically.")
    st.write("🔹 **Knowledge Bases & Retrieval (RAG):** Connecting large language models directly with enterprise PDF and Excel files via semantic vector databases.")
    st.write("🔹 **Neural Computer Vision Systems:** Real-time convolutional camera frame scanning loops deployed for spatial object tracking and facial metrics analysis.")
    st.write("🔹 **Predictive Revenue Forecasting:** Data science time-series mathematical models trained to project accurate business transactional flow trends.")
    st.write("🔹 **Intelligent Document Processing (OCR):** High-speed multi-threaded parsing pipelines that interpret and classify complex data logs automatically.")
    st.link_button("🚀 Build Custom Autonomous AI Agents via WhatsApp", wa_link)

    # Application Software Vertical
    st.markdown("---")
    st.markdown("### 🌐 Full-Stack Web Dashboards & High-Speed Crawler Automation")
    st.write("We develop secure enterprise application layers and automated data miners fueled by asynchronous data processing processing backend units.")
    st.write("🔹 **Full-Stack Cloud Software:** High-performance single-page responsive web applications engineered with Next.js frontends and async Python FastAPI backends.")
    st.write("🔹 **High-Scale Web Crawlers:** Multi-threaded headless Selenium browser automation bots built to bypass advanced anti-bot proxy firewalls.")
    st.write("🔹 **Data Speed Caching Systems:** Distributed memory storage and low-latency database performance tuning optimized with advanced Redis caching setups.")
    st.write("🔹 **Database Structuring Optimization:** Query index optimization and table partitioning designed to scale PostgreSQL databases handling millions of active logs.")
    st.write("🔹 **Microservices Overhaul:** Seamless structural migration refactoring legacy applications into modern decoupled secure API micro-units.")
    st.link_button("🚀 Order Production Software Platforms via WhatsApp", wa_link)

# ==================== PAGE 3: AI CHAT AGENT ====================
if page == "🤖 Autonomous AI Support Agent":
    st.title("🤖 Zain Tech Autonomous Enterprise Operations Agent")
    st.write("Talk instantly with our system framework automation representative regarding technical metrics or deployment prices.")
    
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"): st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant"): st.write(msg.content)
            
    user_input = st.chat_input("Ask Zain Tech Assistant Anything...")
