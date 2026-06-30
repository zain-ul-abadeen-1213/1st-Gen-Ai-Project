import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# 1. Page Config
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="⚡", layout="wide")

# 2. Advanced AI Neon Glow Styling (Custom CSS with perfect contrast fixes)
st.markdown("""
    <style>
    /* Main Background aur Font Setting */
    .stApp {
        background-color: #0b0f17;
        color: #e6edf3;
    }
    
    /* Chat Messages Text Contrast */
    div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] li {
        color: #e6edf3 !important;
        font-size: 16px;
    }
    
    /* White Boxes / Streamlit Buttons Text Contrast Fix */
    div.stButton > button {
        color: #0d1117 !important; /* Dark text for light/white buttons */
        background-color: #ffffff !important;
        font-weight: bold !important;
        border: 1px solid #00f2fe !important;
        transition: all 0.3s ease;
    }
    
    /* Button Hover Effect */
    div.stButton > button:hover {
        background-color: #00f2fe !important;
        color: #0d1117 !important;
        box-shadow: 0px 0px 15px rgba(0, 242, 254, 0.6);
    }
    
    /* Main Brand Title */
    .main-title {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 42px;
        text-shadow: 0px 0px 25px rgba(0, 242, 254, 0.5);
    }
    
    /* Subtitle Styling */
    .sub-title {
        text-align: center;
        color: #8b949e;
        font-size: 14px;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }
    
    /* Service Cards Layout */
    .service-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .service-title {
        color: #00f2fe;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 8px;
    }
    
    .service-desc {
        color: #8b949e;
        font-size: 13px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Headers Branding
st.markdown('<div class="main-title">🚀 ZAIN TECH</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AUTOMATION SOLUTIONS • AUTOMATED ENTERPRISE MARKETPLACE</div>', unsafe_allow_html=True)

# 4. Layout Columns (Left Marketplace Matrix, Right AI Agent)
col_market, col_chat = st.columns([1.2, 1])

with col_market:
    st.markdown("### 🛠️ Our Core Tech Services Matrix")
    
    # 5. Core Services Dataset
    services_data = [
        {"name": "⚙️ Enterprise DevOps Pipelines", "desc": "CI/CD setups, AWS/Azure Cloud management, Kubernetes cluster scaling & Dockerization."},
        {"name": "🛡️ Cyber Security Assessment & Hardening", "desc": "Penetration testing, source code auditing, security compliance & vulnerability patches."},
        {"name": "🧠 Predictive Machine Learning Engines", "desc": "Custom business forecasting data models, regression, cluster analysis & analytical pipelines."},
        {"name": "👁️ Deep Learning & Neural Architectures", "desc": "Computer Vision systems, NLP processing networks, and intelligent OCR data models."},
        {"name": "🤖 Hyper-Automation Core Bots", "desc": "Custom LangChain engine configurations, Selenium web scrapers & automated API processes."},
        {"name": "🌐 Full-Stack Cloud Web Architecture", "desc": "Secure, high-traffic Enterprise web applications built using Next.js, Python FastAPI, & Streamlit."}
    ]
    
    # Rendering Service Cards & Interactive Buttons
    for service in services_data:
        st.markdown(f"""
        <div class="service-card">
            <div class="service-title">{service['name']}</div>
            <div class="service-desc">{service['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("🛒 Add to Cart", key=f"cart_{service['name']}"):
                st.toast(f"Added to queue: {service['name']}")
        with btn_col2:
            if st.button("📞 Get Service / Contact Now", key=f"contact_{service['name']}"):
                st.success("Direct Contact: 📞 Call/WhatsApp: 03221837390")

    st.markdown("---")
    st.caption("⚡ Dynamically loading +100 granular technical sub-modules (Microservices) inside the core systemic index matrix.")

with col_chat:
    st.markdown("### 🤖 Zain Tech Autonomous Agent")
    
    # Sidebar control configurations
    st.sidebar.markdown("### 🛠️ CONTROL PANEL")
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
    st.sidebar.info("Designed & Developed by Zain Tech.\n📞 Official Line: 03221837390")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat Log Stream Render
    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message("user", avatar="👤"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🤖"):
                st.write(message.content)

    user_query = st.chat_input("Ask Zain Tech AI Agent...")

    if user_query:
        if not groq_api_key:
            st.info("⚠️ Please enter your Groq API Key in the sidebar control panel.")
            st.stop()

        with st.chat_message("user", avatar="👤"):
            st.write(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("⚡ Processing system engine knowledge..."):
                try:
                    # AI System Persona Configurations
                    system_instruction = """
                    Aap Zain Tech Automation Solutions ke official enterprise system agent hain. 
                    Aapka main core job user ko business solutions guide karna aur services deal karna hai.

                    Core Expert Services Provided by Zain Tech:
                    1. DevOps Cloud Architecture & Automation
                    2. Cyber Security Vulnerability Assessments & Audits
                    3. Machine Learning (ML) Data Pipelines & Processing
                    4. Deep Learning Neural Networks & Multi-Modal AI Solutions
                    5. Robotic Process Automation Tools & Scrapers
                    6. Full-Stack Secure Custom Website & App Applications

                    CRITICAL SALES RULES:
                    - Agar user price poochaey, deal ki baat karey, ya custom pricing mangey, toh usey kahen: 
                      'Pricing and custom design discussion ke liye aap direct humaray founder (Zain Ul Abadeen) se direct call ya WhatsApp par rabta karein: 03221837390.'
                    - Hamesha isi configuration dataset ke mutabiq professional and helping tareeqay se Urdu/Hindi/English mix mein jawab dein.
                    """

                    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key).bind(system=system_instruction)
                    ai_response = llm.invoke(st.session_state.chat_history)
                    
                    st.write(ai_response.content)
                    st.session_state.chat_history.append(AIMessage(content=ai_response.content))
                    
                except Exception as e:
                    st.error(f"System Error: {e}")
