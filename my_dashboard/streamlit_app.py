import streamlit as st
# learning_analytics_dashboard.py
import streamlit as st
import pandas as pd
from docx import Document 
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
from text_analyzer import TextAnalyzer
import re
# ============================================
# STREAMLIT APP CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Learning Analytics Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stTabs [data-baseweb=\"tab-list\"] {
        gap: 10px;
    }
    .stTabs [data-baseweb=\"tab\"] {
        height: 50px;
        padding: 10px 20px;
        background-color: #22223b; 
        border-radius: 5px;
        color: #e0e1dd; 
        opacity: 1;
        transition: background 0.2s;
    }
    .stTabs [aria-selected=\"true\"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# ============================================
# SESSION STATE INITIALIZATION
# ============================================
if 'students' not in st.session_state:
    st.session_state.students = {}
if 'essays' not in st.session_state:
    st.session_state.essays = []
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = TextAnalyzer()
# ============================================
# SIDEBAR - LOGIN & SETTINGS
# ============================================
with st.sidebar:
    st.markdown("### 🔐 Login")
    
    # Demo accounts
    accounts = {
        'prof_yamada': 'analytics2025',
        'prof_suzuki': 'learning123',
        'prof_tanaka': 'corpus2025'
    }
    
    username = st.text_input("Teacher ID", key="username")
    password = st.text_input("Password", type="password", key="password")
    
    if st.button("Login", type="primary"):
        if username in accounts and accounts[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials")
    
    st.markdown("---")
    st.markdown("**Demo Accounts:**")
    st.code("prof_yamada / analytics2025")
    st.code("prof_suzuki / learning123")
    st.code("prof_tanaka / corpus2025")
    
    st.markdown("---")
    st.markdown("### 📖 Instructions")
    with st.expander("🚀 Getting Started"):
        st.markdown("""
        1. Select a demo account above
        2. Click Login button
        3. Start with Overview tab
        """)
    
    with st.expander("📁 File Upload"):
        st.markdown("""
        **Requirements:**
        - CSV format
        - Columns: `student_name`, `essay`
        - Max 200MB
        """)
# Check if logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.markdown('<p class="main-header">📚 Learning Analytics Dashboard</p>', unsafe_allow_html=True)
    st.info("👈 Please login using the sidebar")
    st.stop()
# ============================================
# MAIN DASHBOARD
# ============================================
st.markdown('<p class="main-header">📚 Learning Analytics Dashboard</p>', unsafe_allow_html=True)
st.markdown(f"**Current User:** {st.session_state.current_user}")
# ============================================
# TABS
# ============================================
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📁 File Management", "👥 Student Analysis", "🔬 NLP Analysis"])
# ============================================
# TAB 1: OVERVIEW
# ============================================
with tab1:
    st.subheader("Class Statistics")
    
    # Calculate statistics
    total_students = len(st.session_state.students)
    total_essays = len(st.session_state.essays)
    
    if total_essays > 0:
        all_analyses = []
        for student in st.session_state.students.values():
            for essay in student['essays']:
                all_analyses.append(essay['analysis'])
        
        avg_words = sum(a['word_count'] for a in all_analyses) / len(all_analyses)
        avg_sentiment = sum(a['sentiment'] for a in all_analyses) / len(all_analyses)
    else:
        avg_words = 0
        avg_sentiment = 0
    
    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", total_students)
    with col2:
        st.metric("Total Essays", total_essays)
    with col3:
        st.metric("Avg Word Count", f"{avg_words:.0f}")
    with col4:
        st.metric("Avg Sentiment", f"{avg_sentiment:.2f}")
    
    if total_essays > 0:
        st.markdown("---")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Word Count by Student")
            student_data = pd.DataFrame([
                {'student': name, 'avg_words': s['avg_words']}
                for name, s in st.session_state.students.items()
            ])
            fig1 = px.bar(student_data, x='student', y='avg_words', 
                          color_discrete_sequence=['#667eea'])
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.subheader("😊 Sentiment Distribution")
            positive = sum(1 for s in st.session_state.students.values() if s['avg_sentiment'] > 0.1)
            neutral = sum(1 for s in st.session_state.students.values() if -0.1 <= s['avg_sentiment'] <= 0.1)
            negative = sum(1 for s in st.session_state.students.values() if s['avg_sentiment'] < -0.1)
            
            fig2 = go.Figure(data=[go.Pie(
                labels=['Positive', 'Neutral', 'Negative'],
                values=[positive, neutral, negative],
                marker_colors=['#4ade80', '#94a3b8', '#f87171']
            )])
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("📤 Upload CSV files in the 'File Management' tab to see analytics")
# ============================================
# TAB 2: FILE MANAGEMENT
# ============================================
with tab2:
    st.subheader("📁 Upload Student Essays")
    uploaded_file = st.file_uploader(
        "Upload CSV, Excel, or Word file (columns: student_name, essay)",
        type=['csv', 'xlsx', 'xls', 'docx'],
        help="Supported: CSV (comma), Excel (.xlsx, .xls), Word (.docx)"
    )
    if uploaded_file is not None:
        try:
            file_name = uploaded_file.name.lower()
            if file_name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                df = pd.read_excel(uploaded_file)
            elif file_name.endswith('.docx'):
                doc = Document(uploaded_file)
                data = []
                for para in doc.paragraphs:
                    txt = para.text.strip()
                    if txt:
                        if ' ' in txt:
                            name, essay = txt.split(' ', 1)
                        else:
                            name, essay = 'Unknown', txt
                        data.append({'student_name': name, 'essay': essay})
                df = pd.DataFrame(data)
            else:
                st.error("Unsupported file format.")
                st.stop()
            # Normalize column headers
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
            if 'student_name' not in df.columns or 'essay' not in df.columns:
                st.error("❌ File must have 'student_name' and 'essay' columns!")
                st.stop()
            st.success(f"✅ Successfully loaded {len(df)} essays from {uploaded_file.name}")
            st.dataframe(df.head(), use_container_width=True)
            # Main loop: add/aggregate to session state, perform analysis
            for _, row in df.iterrows():
                name = str(row['student_name']).strip()
                text = str(row['essay']).strip()
                # Initialize student in session_state if new
                if name not in st.session_state.students:
                    st.session_state.students[name] = {
                        'name': name,
                        'essays': [],
                        'total_words': 0,
                        'avg_sentiment': 0,
                        'avg_words': 0,
                        'strengths': [],
                        'weaknesses': []
                    }
                # Analyze essay with your analyzer
                analysis = st.session_state.analyzer.analyze_text(text)
                st.session_state.students[name]['essays'].append({
                    'text': text,
                    'analysis': analysis
                })
                st.session_state.students[name]['total_words'] += analysis['word_count']
                st.session_state.essays.append({
                    'student_name': name,
                    'essay': text
                })
            # Update calculated statistics for each student
            for student in st.session_state.students.values():
                essay_count = len(student['essays'])
                sentiments = [e['analysis']['sentiment'] for e in student['essays']]
                student['avg_sentiment'] = sum(sentiments) / essay_count
                student['avg_words'] = student['total_words'] // essay_count
                student['strengths'], student['weaknesses'] = [], []
                if student['avg_words'] > 200:
                    student['strengths'].append('good_essay_length')
                else:
                    student['weaknesses'].append('short_essays')
                if student['avg_sentiment'] > 0.3:
                    student['strengths'].append('positive_tone')
                elif student['avg_sentiment'] < -0.1:
                    student['weaknesses'].append('negative_tone')
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")
    # Show uploaded files
    if st.session_state.essays:
        st.markdown("---")
        st.subheader(f"📚 Loaded Data: {len(st.session_state.essays)} essays")
        if st.button("🗑️ Clear All Data", type="secondary"):
            st.session_state.students = {}
            st.session_state.essays = []
            st.rerun()
# ============================================
# TAB 3: STUDENT ANALYSIS
# ============================================
with tab3:
    st.subheader("👥 Individual Student Analysis")
    
    if not st.session_state.students:
        st.info("No student data available. Upload files first.")
    else:
        # Student selector
        student_names = list(st.session_state.students.keys())
        selected_student = st.selectbox("Select a student:", student_names)
        
        if selected_student:
            student = st.session_state.students[selected_student]
            
            # Student metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📝 Total Essays", len(student['essays']))
            with col2:
                st.metric("📊 Avg Words", student['avg_words'])
            with col3:
                st.metric("😊 Avg Sentiment", f"{student['avg_sentiment']:.2f}")
            
            # Strengths and weaknesses
            col1, col2 = st.columns(2)
            with col1:
                st.success("**✅ Strengths:**")
                if student['strengths']:
                    for strength in student['strengths']:
                        st.write(f"• {strength}")
                else:
                    st.write("Analyzing...")
            
            with col2:
                st.warning("**⚠️ Areas for Improvement:**")
                if student['weaknesses']:
                    for weakness in student['weaknesses']:
                        st.write(f"• {weakness}")
                else:
                    st.write("Good overall performance")
            
            # Essay progression chart
            st.subheader("📈 Essay Progression")
            
            essay_data = pd.DataFrame([
                {
                    'essay': f"Essay {i+1}",
                    'word_count': essay['analysis']['word_count'],
                    'sentiment': essay['analysis']['sentiment'] * 100
                }
                for i, essay in enumerate(student['essays'])
            ])
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=essay_data['essay'], 
                y=essay_data['word_count'],
                mode='lines+markers',
                name='Word Count',
                line=dict(color='#667eea', width=3)
            ))
            fig.add_trace(go.Scatter(
                x=essay_data['essay'], 
                y=essay_data['sentiment'],
                mode='lines+markers',
                name='Sentiment (x100)',
                line=dict(color='#764ba2', width=3),
                yaxis='y2'
            ))
            
            fig.update_layout(
                yaxis=dict(title='Word Count'),
                yaxis2=dict(title='Sentiment Score', overlaying='y', side='right'),
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Show individual essays
            with st.expander("📄 View All Essays"):
                for i, essay in enumerate(student['essays']):
                    st.markdown(f"**Essay {i+1}:**")
                    st.text_area(f"essay_{i}", essay['text'], height=100, disabled=True, label_visibility="collapsed")
                    st.caption(f"Word Count: {essay['analysis']['word_count']} | Sentiment: {essay['analysis']['sentiment']:.2f}")
                    st.markdown("---")
# ============================================
# TAB 4: NLP ANALYSIS
# ============================================
with tab4:
    st.subheader("🔬 NLP Analysis Results")
    
    if not st.session_state.essays:
        st.info("No data available. Upload CSV files first.")
    else:
        # Class-wide NLP metrics
        all_analyses = []
        for student in st.session_state.students.values():
            for essay in student['essays']:
                all_analyses.append(essay['analysis'])
        
        avg_complexity = sum(a['complexity'] for a in all_analyses) / len(all_analyses)
        avg_sentences = sum(a['sentence_count'] for a in all_analyses) / len(all_analyses)
        avg_flesch = sum(a['flesch_score'] for a in all_analyses) / len(all_analyses)
        
        # Display NLP metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Avg Complexity", f"{avg_complexity:.2f}")
        with col2:
            st.metric("📝 Avg Sentences", f"{avg_sentences:.1f}")
        with col3:
            st.metric("
