import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Page Title and Clean Theme
st.set_page_config(page_title="Zain Tech", page_icon="⚡")
st.title("🚀 Zain Tech Automation Solutions")
st.write("Welcome to Next-Gen Technical Services Platform.")

# 2. Sidebar Navigation and Control Panel
st.sidebar.markdown("## 🌐 Navigation Menu")
page = st.sidebar.radio("Go to Page:", ["🏠 Home", "⚙️ Services Portfolio", "🤖 AI Agent Chat"])

st.sidebar.markdown("---")
groq_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
st.sidebar.info("Support / Call / WhatsApp: 03221837390")

# Initialize Chat Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 3. PAGE 1: Home Showcase
if page == "🏠 Home":
    st.header("Welcome to Zain Tech Systems")
    st.write("We deliver elite computational pipelines, cloud environments, application software, and full-stack automated operations built to transform business performance scales.")
    st.write("Use the left sidebar navigation menu to switch between portfolio panels or talk with our autonomous assistant matrix.")

# 4. PAGE 2: Services Matrix
if page == "⚙️ Services Portfolio":
    st.header("⚡ Provided Engineering Services Matrix")
    
    st.markdown("### ⚙️ DevOps Infrastructure")
    st.write("CI/CD Automation Pipelines, Container Scaling, Cloud Infrastructure Configuration Nodes.")
    if st.button("🛒 Add to Cart (DevOps)"):
        st.toast("DevOps added to service cart queue.")
    if st.button("📞 Get Service Now (DevOps)"):
        st.success("Contact Founder via Call/WhatsApp: 03221837390")
        
    st.markdown("---")
    st.markdown("### 🛡️ Cyber Security & Hardening")
    st.write("Penetration Testing (VAPT), Vulnerability Auditing, Secure Server Nodes Configuration.")
    if st.button("🛒 Add to Cart (Cyber Security)"):
        st.toast("Cyber Security added to service cart queue.")
    if st.button("📞 Get Service Now (Cyber Security)"):
        st.success("Contact Founder via Call/WhatsApp: 03221837390")

    st.markdown("---")
    st.markdown("### 🧠 Machine Learning & Deep Learning architectures")
    st.write("Data Forecasting pipelines, Computer Vision Systems, Custom Neural Data Classifiers.")
    if st.button("🛒 Add to Cart (AI/ML)"):
        st.toast("AI/ML added to service cart queue.")
    if st.button("📞 Get Service Now (AI/ML)"):
        st.success("Contact Founder via Call/WhatsApp: 03221837390")

    st.markdown("---")
    st.markdown("### 🌐 Web & Mobile Applications")
    st.write("Full-stack modern Cloud platforms, Asynchronous Backends, Specialized Web Scrapers.")
    if st.button("🛒 Add to Cart (Apps)"):
        st.toast("Applications added to service cart queue.")
    if st.button("📞 Get Service Now (Apps)"):
        st.success("Contact Founder via Call/WhatsApp: 03221837390")

# 5. PAGE 3: AI Agent Interface
if page == "🤖 AI Agent Chat":
    st.header("🤖 Zain Tech Intelligent Support Assistant")
    st.write("Ask our specialized assistant model regarding system operations specs directly.")
    
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        if isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)
                
    user_query = st.chat_input("Ask Zain Tech Assistant Anything...")
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        if not groq_key:
            st.warning("⚠️ Enter your Groq API Key inside the sidebar control dashboard.")
        else:
            with st.chat_message("assistant"):
                system_instruction = "Aap Zain Tech Automation Solutions ke official ai assistant hain. DevOps, Security, AI, Full Stack platforms ke baray mein baat karein. Agar koi price poochaey toh kahen custom design ke liye founder Zain Ul Abadeen se is number par direct contact karein Call/WhatsApp: 03221837390."
                messages_to_send = [SystemMessage(content=system_instruction)] + st.session_state.chat_history
                llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_key)
                ai_response = llm.invoke(messages_to_send)
                st.write(ai_response.content)
                st.session_state.chat_history.append(AIMessage(content=ai_response.content))
