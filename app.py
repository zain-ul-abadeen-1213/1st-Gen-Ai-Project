import streamlit as st

# 1. Page Global Setup
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="⚡", layout="wide")

# 2. Advanced Neon Dark Custom CSS
st.markdown("""
    <style>
    .stApp { background-color: #0b0f17; color: #e6edf3; }
    div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] li { color: #e6edf3 !important; font-size: 16px; }
    .main-title {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-family: 'Courier New', monospace; font-weight: bold; font-size: 42px;
        text-shadow: 0px 0px 25px rgba(0, 242, 254, 0.5); margin-bottom: 5px;
    }
    .sub-title { text-align: center; color: #8b949e; font-size: 14px; letter-spacing: 3px; margin-bottom: 30px; }
    .page-header { color: #00f2fe; font-family: 'Courier New', monospace; font-weight: bold; font-size: 28px; margin-bottom: 20px; border-bottom: 2px solid #30363d; padding-bottom: 10px; }
    div.stButton > button { color: #0d1117 !important; background-color: #ffffff !important; font-weight: bold !important; border: 1px solid #00f2fe !important; width: 100%; transition: all 0.3s ease; }
    div.stButton > button:hover { background-color: #00f2fe !important; box-shadow: 0px 0px 15px rgba(0, 242, 254, 0.6); }
    .service-box { background-color: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .service-name { color: #00f2fe; font-size: 22px; font-weight: bold; margin-bottom: 10px; }
    .service-details { color: #c9d1d9; font-size: 15px; line-height: 1.6; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# 3. Persistent State Maintenance
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""

# 4. Sidebar Dynamic Menu Selector
st.sidebar.markdown("## 🌐 NAVIGATION MENU")
selected_page = st.sidebar.selectbox(
    "Choose a Platform Section:",
    ["🏠 Home Showcase", "⚙️ DevOps Pipelines", "🛡️ Cyber Security Matrix", "🧠 ML & Neural Networks", "🌐 Apps & Automation", "🤖 Talk to AI Agent"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛠️ CONTROL PANEL")
input_key = st.sidebar.text_input("Enter Groq API Key:", value=st.session_state.groq_api_key, type="password")
st.session_state.groq_api_key = input_key
st.sidebar.info("Official Support:\n📞 03221837390")

# 5. Core Content Engine
if selected_page == "🏠 Home Showcase":
    st.markdown('<div class="main-title">🚀 ZAIN TECH</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">AUTOMATION SOLUTIONS • NEXT-GEN AI MARKETPLACE</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Welcome to the Future of Tech")
        st.write("Zain Tech Automation Solutions provides elite-tier enterprise architecture engineered to scale your computational pipelines, data analytics, and full-stack security infrastructures.")
        st.write("👈 Use the **Navigation Menu in the Left Sidebar** to explore our separate specialized service sections seamlessly.")
    with col2:
        st.image("https://unsplash.com", caption="Zain Tech Next-Gen Systems")

if selected_page == "⚙️ DevOps Pipelines":
    st.markdown('<div class="page-header">⚙️ DevOps Cloud Pipelines Infrastructure</div>', unsafe_allow_html=True)
    st.write("We build automated scaling architecture designed to manage massive computation tasks across multiple networks.")
    devops_items = [
        {"title": "Automated CI/CD Deployment Pipelines", "desc": "Continuous Integration & Deployment via GitHub Actions, Jenkins, and GitLab Runners. Zero-downtime application updates."},
        {"title": "Kubernetes Orchestration & Auto-Scaling", "desc": "Enterprise container provisioning, multi-tenant cluster management, and horizontal load balancing."},
        {"title": "Cloud Architecture & Infrastructure as Code (IaC)", "desc": "Automated resource setup on AWS, Google Cloud, and Azure platforms using specialized HashiCorp Terraform modules."}
    ]
    for item in devops_items:
        st.markdown(f'<div class="service-box"><div class="service-name">{item["title"]}</div><div class="service-details">{item["desc"]}</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("🛒 Add to Cart", key=f"cart_{item['title']}")
        with c2:
            if st.button("📞 Get Service", key=f"get_{item['title']}"): st.success("Rabta karein: 03221837390")

if selected_page == "🛡️ Cyber Security Matrix":
    st.markdown('<div class="page-header">🛡️ High-End Cyber Security Matrix</div>', unsafe_allow_html=True)
    st.write("We protect enterprise assets by finding application backdoors before malicious entities can discover them.")
    cyber_items = [
        {"title": "Full-Scope Penetration Testing (VAPT)", "desc": "Deep black-box and white-box network architecture scanning, custom API logic vulnerability assessment, and server exploit validation."},
        {"title": "Automated DevSecOps Vulnerability Scanners", "desc": "Integrating automatic real-time source code dependency scanners inside active deployment triggers to detect leak pipelines."},
        {"title": "Identity Access Management & Encryption", "desc": "Deploying zero-trust configurations, secure server key generation nodes, and end-to-end multi-layered database encryption layouts."}
    ]
    for item in cyber_items:
        st.markdown(f'<div class="service-box"><div class="service-name">{item["title"]}</div><div class="service-details">{item["desc"]}</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("🛒 Add to Cart", key=f"cart_{item['title']}")
        with c2:
            if st.button("📞 Get Service", key=f"get_{item['title']}"): st.success("Rabta karein: 03221837390")

if selected_page == "🧠 ML & Neural Networks":
    st.markdown('<div class="page-header">🧠 Machine Learning & Deep Learning Matrices</div>', unsafe_allow_html=True)
    st.write("We train state-of-the-art predictive structures to turn raw enterprise data sets into highly accurate automated forecasting models.")
    ai_items = [
        {"title": "Custom Analytical Forecasting Architectures", "desc": "Predictive regression engines, customer behaviour time-series projection algorithms, and multi-variable analytical data streams."},
        {"title": "Intelligent Computer Vision Models", "desc": "Advanced convolutional neural networks for object tracking, multi-point facial recognition configurations, and semantic pixel classification engines."},
        {"title": "Natural Language Networks & Agents", "desc": "LangChain autonomous agent execution setups, dynamic dataset vectors retrieval structures, and custom Llama tuning architectures."}
    ]
    for item in ai_items:
        st.markdown(f'<div class="service-box"><div class="service-name">{item["title"]}</div><div class="service-details">{item["desc"]}</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("🛒 Add to Cart", key=f"cart_{item['title']}")
        with c2:
            if st.button("📞 Get Service", key=f"get_{item['title']}"): st.success("Rabta karein: 03221837390")

if selected_page == "🌐 Apps & Automation":
    st.markdown('<div class="page-header">🌐 Full-Stack Application Solutions</div>', unsafe_allow_html=True)
    st.write("We build fast, secure full-stack software dashboards using robust backend frameworks capable of handling hundreds of client transactions smoothly.")
    web_items = [
        {"title": "High-Performance Cloud Web Apps", "desc": "Modern responsive application layouts built using Next.js, interactive Streamlit architectures, and fast asynchronous Python FastAPI backends."},
        {"title": "Automated Web Processing Engines (Scrapers)", "desc": "High-speed multi-threaded headless Selenium bots, automated pricing tracker modules, and programmatic API integrations."},
        {"title": "Database Optimization Solutions", "desc": "Setting up PostgreSQL databases, designing secure query execution nodes, and deploying memory caching systems using Redis pipelines."}
    ]
    for item in web_items:
        st.markdown(f'<div class="service-box"><div class="service-name">{item["title"]}</div><div class="service-details">{item["desc"]}</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("🛒 Add to Cart", key=f"cart_{item['title']}")
        with c2:
            if st.button("📞 Get Service", key=f"get_{item['title']}"): st.success("Rabta karein: 03221837390")

if selected_page == "🤖 Talk to AI Agent":
    from langchain_groq import ChatGroq
    from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
    st.markdown('<div class="page-header">🤖 Zain Tech Autonomous AI Assistant</div>', unsafe_allow_html=True)
    st.write("Talk directly with our live sales agent module regarding system integration specifications.")
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user", avatar="👤"): st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar="🤖"): st.write(msg.content)
    user_query = st.chat_input("Ask Zain Tech AI Agent...")
    if user_query:
        with st.chat_message("user", avatar="👤"): st.write(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("⚡ System thinking..."):
                try:
