import streamlit as st


def render():
    
    # Landing page CSS
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 3.5rem 2rem;
            background: linear-gradient(135deg, #132A47 0%, #0B1C33 100%);
            color: #E8EEF5;
            border-radius: 20px;
            margin-bottom: 2rem;
            border: 1px solid #24405F;
            box-shadow: 0 10px 40px rgba(45, 212, 191, 0.15);
        }
        .main-header h1 {
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #FFFFFF;
            letter-spacing: -0.5px;
        }
        .main-header h3 {
            color: #2DD4BF;
            font-weight: 500;
        }
        .main-header p {
            color: #A9B8C9;
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="main-header">
        <h1>📊 Resume Analyzer Pro</h1>
        <h3>Get Past the Filters. Land the Interview.</h3>
        <p>Precision resume analysis powered by AI — built to match how real recruiting systems actually screen candidates.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Call-to-Action Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Analyze My Resume", use_container_width=True, type="primary"):
            st.session_state.current_view = 'scorer'
            st.rerun()
    
    st.markdown("---")
    
    # Features Overview
    st.markdown("## ✨ Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Multi-Dimensional Analysis
        A precise breakdown across 5 key dimensions:
        - Formatting (20%)
        - Keywords & Skills (25%)
        - Content Quality (25%)
        - Skill Validation (15%)
        - ATS Compatibility (15%)
        """)
    
    with col2:
        st.markdown("""
        ### 🔍 Skill Validation
        Verify that your claimed skills are demonstrated in your projects and experience using AI-powered semantic analysis.
        
        **No more empty claims!**
        """)
    
    with col3:
        st.markdown("""
        ### 🔒 Privacy First
        All analysis runs locally with no external API calls. Your resume data never leaves your system.
        
        **100% Private & Secure**
        """)
    
    st.markdown("---")
    
    # How It Works
    st.markdown("## 🚀 How It Works")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 1️⃣ Upload Your Resume
        Support for PDF, DOC, and DOCX formats
        """)
    
    with col2:
        st.markdown("""
        #### 2️⃣ AI Analysis
        Our local AI models analyze your resume across multiple dimensions
        """)
    
    with col3:
        st.markdown("""
        #### 3️⃣ Get Actionable Feedback
        Receive detailed recommendations to improve your resume
        """)