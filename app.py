import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Real-World Page Configurations
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="💻", layout="wide")

# 2. Base Dark/Light Universal Text Contrast Sync via Config Settings
st.markdown("""
    <style>
    /* Absolute Input Field Text Contrast Fix */
    textarea[data-testid="stChatInputTextArea"] {
        color: #000000 !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
    }
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #555555 !important;
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
st.sidebar.title("💻 ZAIN TECH ENGINES")
selected_section = st.sidebar.radio("Corporate Directory Matrix:", [
    "🏢 Headquarters Showcase",
    "⚙️ DevOps Infrastructure Solutions",
    "🛡️ Enterprise Cyber Security Matrix",
    "🧠 Machine & Deep Learning Engines",
    "🌐 Cloud Applications & Web Automation",
    "🤖 Interactive Autonomous AI Support Agent"
])

st.sidebar.markdown("---")
st.sidebar.markdown("#### 🛠️ ACCESS SECURITY")
groq_api_entry = st.sidebar.text_input("Enter Groq Access Token:", type="password")
st.sidebar.info("Zain Tech Escalation Desk:\n📞 Call/WhatsApp: 03221837390")

# Universal Direct Contact WhatsApp Core Link
base_whatsapp_link = "https://wa.me"

# ==================== PAGE 1: HEADQUARTERS SHOWCASE ====================
if selected_section == "🏢 Headquarters Showcase":
    st.title("🚀 ZAIN TECH AUTOMATION SOLUTIONS")
    st.subheader("Enterprise Engineering & Systemic Architectures Matrix")
    
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.write("Zain Tech Automation Solutions engineers mission-critical cloud configurations, multi-layer computational machine architectures, predictive learning models, and secure full-stack backend platforms designed to automate enterprise operations flawlessly.")
        st.info("👈 Use the Corporate Directory Matrix Menu inside the left side sidebar panel to explore our specialized premium technology sectors directly.")
        
        # Safe URL Link Action Button
        st.link_button("📞 Schedule Enterprise Consultation Now", f"{base_whatsapp_link}General%20Enterprise%20Consultation", type="primary")
    with col_right:
        st.image("https://unsplash.com", caption="Zain Tech Infrastructure Management Node")

# ==================== GENERIC SERVICES RENDER (ERROR FREE CORE INTERFACE) ====================
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
        
        # Completely Pure Streamlit Block (Zero risk of HTML or brace formatting errors)
        for service in services_matrix[target_key]:
            st.subheader(f"🔹 {service['title']}")
            st.caption(f"Domain Focus Matrix: {service['scope']}")
            st.write(service['desc'])
            
            # Rendering live clean text pricing data
            st.metric(label="Base Implementation Cost", value=service['price'])
            
            # Interactive System Buttons using clean Streamlit definitions
            if st.button(f"🛒 Add Framework to Queue System ({service['title']})", key=f"cart_{service['title']}"):
                st.toast(f"System Matrix Pipeline Initialized for: {service['title']}")
                
            custom_wa_text = f"{base_whatsapp_link}{service['title'].replace(' ', '%20')}"
            st.link_button("📞 Purchase / Deploy on WhatsApp Live", custom_wa_text)
            st.markdown("---")

# ==================== PAGE 6: LIVE AI CHATBOT AGENT ====================
if selected_section == "🤖 Interactive Autonomous AI Support Agent":
    st.title("🤖 Zain Tech Autonomous Enterprise Operations Agent")
    st.write("Talk instantly with our system framework automation representative regarding technical metrics or deployment prices.")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"): st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant"): st.write(msg.content)
            
    user_input = st.chat_input("Ask Zain Tech Automation Solutions Matrix Agent...")
    
    if user_input:
        with st.chat_message("user"): st.write(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        
        if not groq_api_entry:
            st.warning("⚠️ High security cloud access credential required. Please type your Groq Cloud Access Token inside the sidebar control dashboard.")
        else:
            with st.chat_message("assistant"):
                with st.spinner("⚡ Running programmatic pipeline lookup matrix..."):
                    try:
                        system_rule = "Aap Zain Tech Automation Solutions ke official enterprise ai representative assistant hain. Hamari services DevOps, Security audits, Neural Network Machine Learning Models aur Web Apps hain. Pricing ya deployment deal ki baat ho toh kahein ke complete execution strategy ke liye founder Zain Ul Abadeen se direct call ya WhatsApp rabta karein: +923221837390."
                        messages_pipeline = [SystemMessage(content=system_rule)] + st.session_state.chat_history
                        llm_engine = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_entry)
                        execution_response = llm_engine.invoke(messages_pipeline)
                        st.write(execution_response.content)
                        st.session_state.chat_history.append(AIMessage(content=execution_response.content))
                    except Exception as system_crash_error:
                        st.error(f"Operational Exception Triggered: {system_crash_error}")
