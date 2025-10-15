import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Try to import nlp_analysis if it exists
try:
    import nlp_analysis
    NLP_AVAILABLE = True
except ImportError:
    NLP_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Learning Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for file upload and configuration
st.sidebar.title("📁 Data Upload & Configuration")
st.sidebar.markdown("---")

# CSV File Upload
st.sidebar.subheader("Upload Your Data")
uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    help="Upload your learning analytics data in CSV format"
)

st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.info(
    "This Learning Analytics Dashboard helps educators analyze student "
    "performance, engagement, and learning patterns through interactive "
    "visualizations and insights."
)

if NLP_AVAILABLE:
    st.sidebar.success("✅ NLP Analysis Module Loaded")
else:
    st.sidebar.warning("⚠️ NLP Analysis Module Not Found")

# Main content area
st.markdown('<h1 class="main-header">📊 Learning Analytics Dashboard</h1>', unsafe_allow_html=True)

st.markdown("""
### Welcome to the Learning Analytics Dashboard!

This interactive dashboard is designed to help educators and administrators gain valuable 
insights from educational data. Upload your CSV file using the sidebar to get started.

#### Features:
- 📈 **Performance Metrics**: Track student grades, completion rates, and progress
- 👥 **Engagement Analysis**: Analyze student participation and activity patterns
- 🎯 **Predictive Insights**: Identify at-risk students early
- 📊 **Interactive Visualizations**: Explore data through dynamic charts and graphs
- 🔍 **Detailed Analytics**: Dive deep into individual and group performance
""")

if NLP_AVAILABLE:
    st.markdown("- 🤖 **NLP Analysis**: Advanced text analysis of student responses and feedback")

st.markdown("---")

# Process uploaded data
if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        st.success(f"✅ Successfully loaded {len(df)} records!")
        
        # Display basic information
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Records", len(df))
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            st.metric("Numeric Columns", len(df.select_dtypes(include=[np.number]).columns))
        with col4:
            st.metric("Text Columns", len(df.select_dtypes(include=['object']).columns))
        
        st.markdown("---")
        
        # Tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Data Overview", "📊 Visualizations", "📈 Analytics", "🔍 Data Explorer"])
        
        with tab1:
            st.subheader("Data Overview")
            
            # Display first few rows
            st.write("**First 10 rows of your data:**")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Display data summary
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Column Names and Data Types:**")
                col_info = pd.DataFrame({
                    'Column': df.columns,
                    'Data Type': df.dtypes.values,
                    'Non-Null Count': df.count().values,
                    'Null Count': df.isnull().sum().values
                })
                st.dataframe(col_info, use_container_width=True)
            
            with col2:
                st.write("**Basic Statistics:**")
                st.dataframe(df.describe(), use_container_width=True)
        
        with tab2:
            st.subheader("Data Visualizations")
            
            # Let users select columns for visualization
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                st.write("**Select a numeric column to visualize:**")
                selected_col = st.selectbox("Column", numeric_cols)
                
                viz_col1, viz_col2 = st.columns(2)
                
                with viz_col1:
                    # Histogram
                    fig_hist = px.histogram(
                        df, 
                        x=selected_col, 
                        title=f"Distribution of {selected_col}",
                        marginal="box"
                    )
                    st.plotly_chart(fig_hist, use_container_width=True)
                
                with viz_col2:
                    # Box plot
                    fig_box = px.box(
                        df, 
                        y=selected_col, 
                        title=f"Box Plot of {selected_col}"
                    )
                    st.plotly_chart(fig_box, use_container_width=True)
                
                # Correlation heatmap if multiple numeric columns
                if len(numeric_cols) > 1:
                    st.write("**Correlation Heatmap:**")
                    corr_matrix = df[numeric_cols].corr()
                    fig_corr = px.imshow(
                        corr_matrix,
                        labels=dict(color="Correlation"),
                        x=corr_matrix.columns,
                        y=corr_matrix.columns,
                        color_continuous_scale="RdBu_r",
                        aspect="auto"
                    )
                    st.plotly_chart(fig_corr, use_container_width=True)
            else:
                st.warning("No numeric columns found in the dataset for visualization.")
        
        with tab3:
            st.subheader("Analytics & Insights")
            
            # Provide basic analytics
            st.write("**Key Insights:**")
            
            # Missing data analysis
            missing_data = df.isnull().sum()
            if missing_data.sum() > 0:
                st.write("**Missing Data Analysis:**")
                missing_df = pd.DataFrame({
                    'Column': missing_data.index,
                    'Missing Count': missing_data.values,
                    'Percentage': (missing_data.values / len(df) * 100).round(2)
                })
                missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
                st.dataframe(missing_df, use_container_width=True)
            else:
                st.success("✅ No missing data found!")
            
            # Display value counts for categorical columns
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            if len(categorical_cols) > 0:
                st.write("**Categorical Data Distribution:**")
                selected_cat = st.selectbox("Select a categorical column", categorical_cols)
                
                value_counts = df[selected_cat].value_counts().head(10)
                fig_cat = px.bar(
                    x=value_counts.index,
                    y=value_counts.values,
                    title=f"Top 10 Values in {selected_cat}",
                    labels={'x': selected_cat, 'y': 'Count'}
                )
                st.plotly_chart(fig_cat, use_container_width=True)
            
            # NLP Analysis if available
            if NLP_AVAILABLE:
                st.write("**NLP Analysis:**")
                st.info("NLP analysis module is available. Implement nlp_analysis.py for advanced text analysis.")
        
        with tab4:
            st.subheader("Data Explorer")
            st.write("**Filter and explore your data:**")
            
            # Column selection
            selected_columns = st.multiselect(
                "Select columns to display",
                df.columns.tolist(),
                default=df.columns.tolist()[:5] if len(df.columns) >= 5 else df.columns.tolist()
            )
            
            if selected_columns:
                # Row filtering
                num_rows = st.slider("Number of rows to display", 1, len(df), min(100, len(df)))
                
                # Display filtered data
                st.dataframe(df[selected_columns].head(num_rows), use_container_width=True)
                
                # Download option
                csv = df[selected_columns].head(num_rows).to_csv(index=False)
                st.download_button(
                    label="📥 Download filtered data as CSV",
                    data=csv,
                    file_name=f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            else:
                st.warning("Please select at least one column to display.")
        
    except Exception as e:
        st.error(f"❌ Error loading file: {str(e)}")
        st.info("Please make sure your file is a valid CSV format.")

else:
    # Show example/demo section when no file is uploaded
    st.info("👆 Please upload a CSV file using the sidebar to begin analysis.")
    
    st.markdown("### Sample CSV Format")
    st.markdown("""
    Your CSV file should contain learning analytics data. Here's an example structure:
    
    ```
    student_id,name,grade,attendance,assignments_completed,engagement_score
    1001,John Doe,85,92,15,78
    1002,Jane Smith,92,98,18,95
    1003,Bob Johnson,78,85,14,72
    ```
    """)
    
    # Show demo data
    st.markdown("### Demo Data Example")
    demo_data = pd.DataFrame({
        'Student ID': [1001, 1002, 1003, 1004, 1005],
        'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams', 'Charlie Brown'],
        'Grade': [85, 92, 78, 88, 95],
        'Attendance (%)': [92, 98, 85, 90, 96],
        'Assignments Completed': [15, 18, 14, 16, 19],
        'Engagement Score': [78, 95, 72, 84, 92]
    })
    st.dataframe(demo_data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Made with ❤️ for educators and students worldwide</p>
    <p>Powered by Streamlit | Version 1.0.0</p>
</div>
""", unsafe_allow_html=True)
