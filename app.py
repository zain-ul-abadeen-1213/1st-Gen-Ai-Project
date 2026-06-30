import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Page Configuration
st.set_page_config(page_title="Zain Tech Automation Solutions", page_icon="⚡", layout="wide")

# 2. Perfect Text Visibility & Styling CSS (Guarantees deep text contrast inside input box)
st.markdown("""
    <style>
    /* Absolute fix for the Streamlit Chat Input Box Text Contrast */
    textarea[data-testid="stChatInputTextArea"] {
        color: #111111 !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        background-color: #ffffff !important;
    }
    /* Fixing placeholder text color visibility inside input box */
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #555555 !important;
    }
    /* Standard Button Styling */
    div.stButton > button {
        color: #111111 !important;
        background-color: #ffffff !important;
        font-weight: bold !important;
        border: 2px solid #ff4b4b !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #ff4b4b !important;
        color: #ffffff !important;
    }
    /* Service Box Structure layout */
    .service-container {
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-bottom: 12px;
        background-color: #f9f9f9;
        color: #222222;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Persistent Memory Configurations
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# WhatsApp API Trigger Redirect String Helper
whatsapp_url = "https://wa.me."

# 4. Sidebar 5 Pages Navigation Interface Matrix
st.sidebar.title("⚡ ZAIN TECH PLATFORM")
page = st.sidebar.radio("Navigate Sections:", [
    "🏠 Agency Home Showcase", 
    "⚙️ DevOps Infrastructure (25 Services)", 
    "🛡️ Cyber Security Cloud (25 Services)", 
    "🧠 AI, ML & Deep Learning (25 Services)", 
    "🌐 Apps & Automation Web (25 Services)",
    "🤖 Talk to Live AI Agent"
])

st.sidebar.markdown("---")
groq_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
st.sidebar.info("Direct Contact Support:\n📞 03221837390")

# ==================== PAGE 1: HOME ====================
if page == "🏠 Agency Home Showcase":
    st.title("🚀 Zain Tech Automation Solutions")
    st.subheader("Automated Tech Infrastructure Engineering Portal")
    st.write("We build extreme performance systems scaling business operations dynamically. Use the sidebar directory matrix to look inside individual service deployment pages.")
    st.markdown(f'[![Contact on WhatsApp](https://shields.io)]({whatsapp_url})')

# ==================== PAGE 2: DEVOPS (25 SERVICES) ====================
elif page == "⚙️ DevOps Infrastructure (25 Services)":
    st.title("⚙️ Custom Enterprise DevOps Architecture")
    st.write("Browse our granular DevOps scalable sub-modules below:")
    
    for i in range(1, 26):
        st.markdown(f"""
        <div class="service-container">
            <h4>🔹 DevOps Microservice Package Node #{i}</h4>
            <p>Automated Pipeline scaling, custom CI/CD execution node config, server security layer, and container provisioning cluster index layout part {i}.</p>
        </div>
        """, unsafe_allow_html=True)
        col_c, col_w = st.columns(2)
        with col_c:
            st.button(f"🛒 Add Node #{i} to Cart", key=f"cart_devops_{i}")
        with col_w:
            # Action Link to open WhatsApp directly with custom redirection anchors
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; padding:10px; font-weight:bold; background-color:#25D366; color:white; border:none; border-radius:4px; cursor:pointer;">📞 Contact Now / Buy on WhatsApp</button></a>', unsafe_allow_html=True)

# ==================== PAGE 3: CYBER SECURITY (25 SERVICES) ====================
elif page == "🛡️ Cyber Security Cloud (25 Services)":
    st.title("🛡️ Penetration Testing & Core Asset Hardening")
    st.write("Explore our cyber defense modules configuration layers:")
    
    for i in range(1, 26):
        st.markdown(f"""
        <div class="service-container">
            <h4>🔹 Cyber Security Defense Module #{i}</h4>
            <p>Source auditing pipeline patch, logic validation protocol, blackbox testing sequence engine, security clearance certificate deployment layer {i}.</p>
        </div>
        """, unsafe_allow_html=True)
        col_c, col_w = st.columns(2)
        with col_c:
            st.button(f"🛒 Add Security Module #{i} to Cart", key=f"cart_cyber_{i}")
        with col_w:
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; padding:10px; font-weight:bold; background-color:#25D366; color:white; border:none; border-radius:4px; cursor:pointer;">📞 Contact Now / Buy on WhatsApp</button></a>', unsafe_allow_html=True)

# ==================== PAGE 4: AI & ML (25 SERVICES) ====================
elif page == "🧠 AI, ML & Deep Learning (25 Services)":
    st.title("🧠 Neural Computation Models & Agent Blocks")
    st.write("Examine our specialized predictive algorithms clusters:")
    
    for i in range(1, 26):
        st.markdown(f"""
        <div class="service-container">
            <h4>🔹 Intelligent Cognitive Core Structure #{i}</h4>
            <p>Time-series regression matrix, custom computer vision classifier, transformers multi-vector database model processing engine version {i}.</p>
        </div>
        """, unsafe_allow_html=True)
        col_c, col_w = st.columns(2)
        with col_c:
            st.button(f"🛒 Add AI Engine #{i} to Cart", key=f"cart_ai_{i}")
        with col_w:
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; padding:10px; font-weight:bold; background-color:#25D366; color:white; border:none; border-radius:4px; cursor:pointer;">📞 Contact Now / Buy on WhatsApp</button></a>', unsafe_allow_html=True)

# ==================== PAGE 5: APPS & AUTOMATION (25 SERVICES) ====================
elif page == "🌐 Apps & Automation Web (25 Services)":
    st.title("🌐 Full-Stack Applications & High-Speed Automated Bots")
    st.write("Deploy secure backend interfaces and scraper engines:")
    
    for i in range(1, 26):
        st.markdown(f"""
        <div class="service-container">
            <h4>🔹 Scalable Software Application Dashboard Component #{i}</h4>
            <p>Asynchronous runtime execution platform setup, automated multi-threaded headless Selenium bot matrix router element {i}.</p>
        </div>
        """, unsafe_allow_html=True)
        col_c, col_w = st.columns(2)
        with col_c:
            st.button(f"🛒 Add Application Component #{i} to Cart", key=f"cart_app_{i}")
        with col_w:
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; padding:10px; font-weight:bold; background-color:#25D366; color:white; border:none; border-radius:4px; cursor:pointer;">📞 Contact Now / Buy on WhatsApp</button></a>', unsafe_allow_html=True)

# ==================== PAGE 6: LIVE AI CHATBOT AGENT ====================
elif page == "🤖 Talk to Live AI Agent":
    st.title("🤖 Zain Tech Autonomous System Sales Agent")
    st.write("Discuss service pricing and systemic integrations instantly.")
    
    # Rendering message boards logs
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"): st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant"): st.write(msg.content)
            
    user_query = st.chat_input("Ask Zain Tech Assistant Anything...")
    
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        if not groq_key:
            st.warning("⚠️ Enter your Groq API Key inside the sidebar control dashboard.")
        else:
            with st.chat_message("assistant"):
                with st.spinner("⚡ Processing operations data..."):
                    system_instruction = "Aap Zain Tech Automation Solutions ke official ai assistant hain. DevOps, Security, AI, Full Stack platforms ke baray mein baat karein. Agar koi price poochaey toh kahen custom design ke liye founder Zain Ul Abadeen se is number par direct contact karein Call/WhatsApp: 03221837390."
                    messages_to_send = [SystemMessage(content=system_instruction)] + st.session_state.chat_history
                    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_key)
                    ai_response = llm.invoke(messages_to_send)
                    st.write(ai_response.content)
                    st.session_state.chat_history.append(AIMessage(content=ai_response.content))
