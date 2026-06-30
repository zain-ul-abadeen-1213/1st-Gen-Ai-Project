import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Page Global Setup
st.set_page_config(page_title="Zain Tech Automation", page_icon="💻", layout="wide")

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

# 3. Sidebar Configuration Setup (Strict 3 Pages Layout)
st.sidebar.markdown("## 💻 ZAIN TECH ENGINES")
page = st.sidebar.radio("Corporate Directory Matrix:", ["🏠 Headquarters Showcase", "⚙️ Technical Services Portfolio (Basic to Advance)", "🤖 AI Support Agent Chat"])

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
    st.info("👈 Use the 3-Page Corporate Directory Matrix Menu inside the left sidebar panel to switch sections directly.")
    st.link_button("📞 Schedule Enterprise Consultation Now", wa_link)

# ==================== PAGE 2: REAL-WORLD PORTFOLIO (BASIC TO ADVANCE) ====================
if page == "⚙️ Technical Services Portfolio (Basic to Advance)":
    st.title("⚡ Premium Engineering Services Matrix")
    st.write("Review our real-world tech stack catalog below. Every implementation node scales from basic local scripts up to deep advance global cloud structures.")
    
    # ------------------ VERTICAL A: DEVOPS & CLOUD ------------------
    st.markdown("---")
    st.markdown("### ⚙️ DevOps & Cloud Computing (Basic to Advance)")
    
    st.markdown("**🟢 LEVEL 1: BASIC SYSTEMS SETUP**")
    st.write("1. Local Server Environment Config (Dockerized)")
    st.write("2. Static Web App Cloud Static Hosting Setup")
    st.write("3. Basic Git & GitHub Project Workflow Integration")
    st.write("4. Linux Server Shell Command Script Automation")
    st.write("5. Automated Server Resource Metric Alerts Setup")
    
    st.markdown("**🟡 LEVEL 2: INTERMEDIATE AUTOMATION**")
    st.write("6. Core GitHub Actions CI/CD Pipeline Automation")
    st.write("7. Centralized Database Automated Replication Strategy")
    st.write("8. Cloudflare Security DNS Proxy Configuration")
    st.write("9. Basic Terraform Resource Architecture Scripting")
    st.write("10. Multi-Environment Staging/Production Configurations")
    
    st.markdown("**🔴 LEVEL 3: ADVANCE ENTERPRISE DEPLOYMENTS**")
    st.write("11. Production-Grade Kubernetes Elastic Auto-Scaling Clusters")
    st.write("12. High-Availability Multi-Region AWS / Google Cloud Global Pipeline")
    st.write("13. Full Infrastructure-as-Code (IaC) Architecture Management")
    st.write("14. Cloud Cost Optimization & Computational Scaling Audit")
    st.write("15. Advanced DevSecOps Automated Vulnerability CI Pipeline Patching")
    st.link_button("📞 Order Cloud Frameworks via WhatsApp Live", wa_link)

    # ------------------ VERTICAL B: CYBER SECURITY ------------------
    st.markdown("---")
    st.markdown("### 🛡️ Cyber Security Cloud Matrix (Basic to Advance)")
    
    st.markdown("**🟢 LEVEL 1: BASIC NETWORK SEC**")
    st.write("16. SSL/TLS Certificate System Configuration Execution")
    st.write("17. Basic WordPress/Shopify Site Security Hardening")
    st.write("18. Server Firewall Access Rules Matrix Tuning")
    st.write("19. Corporate Email Phishing Vulnerability Training Modules")
    st.write("20. Basic Linux Root Account Authentication Locks")
    
    st.markdown("**🟡 LEVEL 2: COMPLIANCE AUDITING**")
    st.write("21. Automated Source Code Dependency Vulnerability Audits")
    st.write("22. Local Server Database Injection Protection Configuration")
    st.write("23. Cross-Site Scripting (XSS) Exploit Interception Filters")
    st.write("24. Secure API Token Validation & Routing Protocols")
    st.write("25. Multi-Factor Authentication (MFA) Core Integration")
    
    st.markdown("**🔴 LEVEL 3: ADVANCE PENETRATION AUDITS**")
    st.write("26. Full-Scope Professional Black-Box Network Penetration Scanning")
    st.write("27. Automated Zero-Trust Enterprise Key Server Configurations")
    st.write("28. Kernel Architecture Access Injection Interception Hardening")
    st.write("29. Advanced System Backdoor Exploitation Mitigation Strategies")
    st.write("30. Corporate Cyber Security Clearance Compliance Auditing")
    st.link_button("📞 Order Cyber Security Packages via WhatsApp Live", wa_link)

    # ------------------ VERTICAL C: AI, ML & DEEP LEARNING ------------------
    st.markdown("---")
    st.markdown("### 🧠 Data Science & Generative AI Matrix (Basic to Advance)")
    
    st.markdown("**🟢 LEVEL 1: BASIC AUTOMATION LOGIC**")
    st.write("31. Automated Lead Generation Bot Web Processing Scripts")
    st.write("32. Basic Excel Sheet Formula Analytics Script Automation")
    st.write("33. Social Media Content Auto-Scheduler AI Interface")
    st.write("34. Simple Text Categorizer Linear Logic Engine")
    st.write("35. Customer Feedback Email Sentiment Parser")
    
    st.markdown("**🟡 LEVEL 2: BUSINESS MACHINE LEARNING**")
    st.write("36. Predictive Time-Series Revenue Forecasting Data Models")
    st.write("37. Automated Customer Behavior Segmentation Algorithms")
    st.write("38. Corporate Documents OCR Intelligent Data Retrieval Pipelines")
    st.write("39. Basic Custom Trained Neural Network Classifiers Setup")
    st.write("40. Automated Analytics Dashboard Core Data Pipelines Setup")
    
    st.markdown("**🔴 LEVEL 3: ADVANCE GENERATIVE AI**")
    st.write("41. Custom Autonomous LangChain Chat Agent Architecture Config")
    st.write("42. Corporate Vector Database Indexing Semantic Retrieval Solutions")
    st.write("43. Real-Time Spatial Object Tracking Neural Computer Vision Nodes")
    st.write("44. Multi-Modal Vision Processing Application Core Interfaces")
    st.write("45. Advanced Large Language Model LLM Custom Dataset Tuning Logic")
    st.link_button("📞 Order AI Engines via WhatsApp Live", wa_link)

    # ------------------ VERTICAL D: APPS & WEB SOLUTIONS ------------------
    st.markdown("---")
    st.markdown("### 🌐 Web Systems & Headless Crawlers (Basic to Advance)")
    
    st.markdown("**🟢 LEVEL 1: BASIC WEB MODULES**")
    st.write("46. Landing Page Web Interface UI Responsive Deployment")
    st.write("47. Local Python Automation Web-Scraping Scripts")
    st.write("48. Simple Contact Form API Endpoint Integrations")
    st.write("49. Local Database SQLite Data Backup Pipelines")
    st.write("50. E-commerce Product Inventory Loader Scripts Setup")
    
    st.markdown("**🟡 LEVEL 2: DYNAMIC WEB SYSTEMS**")
    st.write("51. Secure RESTful API Backend Architectures built with Python FastAPI")
    st.write("52. Interactive Dynamic Web Dashboards using Modern Streamlit Framework")
    st.write("53. High-Speed Multi-Threaded Headless Selenium Automation Scrapers")
    st.write("54. Corporate Payment Gateway Stripe Integration Routers Setup")
    st.write("55. Distributed Caching Database Operations Loops Built with Redis")
    
    st.markdown("**🔴 LEVEL 3: ADVANCE FULL-STACK PLATFORMS**")
    st.write("56. Next.js Enterprise Software Single-Page Application Interfaces")
    st.write("57. Scalable Distributed PostgreSQL Database Structuring Optimization")
    st.write("58. Complex Real-time Web Socket Interactive Dashboard Systems")
    st.write("59. Legacy Software Codebase Migration & Backend Microservices Overhaul")
    st.write("60. High-Performance Mobile Application Core API Sync Engines")
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
