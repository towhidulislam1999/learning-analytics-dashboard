# Learning Analytics Dashboard

## 📊 Project Introduction

The **Learning Analytics Dashboard** is a comprehensive web-based application designed to provide educators and administrators with powerful insights into student performance and learning patterns. This project combines interactive data visualization with Natural Language Processing (NLP) capabilities to analyze student data, generate detailed reports, and identify trends that can help improve educational outcomes.

The dashboard offers both a standalone HTML interface and a Python backend integration, making it flexible for various deployment scenarios. Whether you're an educator looking to understand your students' performance or a data analyst exploring educational data, this tool provides an intuitive and powerful solution.

---

## ✨ Features Overview

### 1. **Interactive Dashboard**
- **Performance Metrics**: Visual representation of student grades, attendance, and participation rates
- **Trend Analysis**: Track performance changes over time with dynamic charts
- **Comparative Analytics**: Compare individual student performance against class averages
- **Responsive Design**: Works seamlessly across desktop, tablet, and mobile devices
- **Real-time Updates**: Data refreshes automatically when new information is uploaded

### 2. **NLP Analysis Module**
- **Sentiment Analysis**: Analyze student feedback and comments to gauge sentiment
- **Text Classification**: Automatically categorize student responses and feedback
- **Keyword Extraction**: Identify common themes and topics in student submissions
- **Performance Prediction**: Use machine learning to predict at-risk students
- **Automated Report Generation**: Generate comprehensive analysis reports from student data

### 3. **File Upload & Data Processing**
- **CSV/Excel Support**: Upload student data in common spreadsheet formats
- **Batch Processing**: Handle multiple files simultaneously
- **Data Validation**: Automatic checks for data integrity and format compliance
- **Error Handling**: Clear error messages and suggestions for data corrections
- **Sample Data Included**: Pre-loaded datasets for testing and demonstration

### 4. **Student Analysis Tools**
- **Individual Student Profiles**: Detailed views of each student's academic journey
- **Grade Distribution**: Visualize grade patterns across courses and semesters
- **Attendance Tracking**: Monitor attendance patterns and correlations with performance
- **Risk Assessment**: Identify students who may need additional support
- **Engagement Metrics**: Track student participation and involvement

---

## 🚀 Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/towhidulislam1999/learning-analytics-dashboard.git
cd learning-analytics-dashboard
```

2. **Create a Virtual Environment** (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install the core dependencies manually:

```bash
pip install streamlit pandas numpy plotly scikit-learn nltk textblob
```

---

## 💻 Running the Application

### Option A: Using Streamlit (Recommended)

The Streamlit version provides an interactive web interface with real-time updates.

1. **Run the Streamlit App**

```bash
streamlit run streamlit_app.py
```

2. **Access the Dashboard**

Open your web browser and navigate to:
- Local: `http://localhost:8501`
- Network: The terminal will display a network URL for access from other devices

3. **Upload Your Data**
- Use the sidebar file uploader to select your CSV file
- The dashboard will automatically process and visualize your data

### Option B: Deploy to Streamlit Community Cloud ☁️

**Deploy your Learning Analytics Dashboard online for FREE with Streamlit Community Cloud!**

Streamlit Community Cloud allows you to deploy, manage, and share your Streamlit apps directly from GitHub. Your dashboard will be accessible from anywhere with a custom URL.

#### Prerequisites:
- A GitHub account (you're already here! ✓)
- A Streamlit Community Cloud account (free to create)

#### Deployment Steps:

1. **Fork or Push This Repository to Your GitHub**
   - Ensure your repository contains `streamlit_app.py` in the root directory ✓
   - Commit and push all changes to your GitHub repository

2. **Create a Streamlit Community Cloud Account**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Authorize Streamlit to access your repositories

3. **Deploy Your App**
   - Click "New app" on your Streamlit Community Cloud dashboard
   - Select your repository: `towhidulislam1999/learning-analytics-dashboard`
   - Set the branch: `main`
   - Set the main file path: `streamlit_app.py`
   - Click "Deploy"!

4. **Access Your Live Dashboard**
   - Your app will be deployed at: `https://[your-app-name].streamlit.app`
   - Share this URL with colleagues, students, or stakeholders
   - The app will automatically update when you push changes to GitHub

#### Optional: Create requirements.txt for Cloud Deployment

If you don't have a `requirements.txt` file, create one with these dependencies:

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
scikit-learn>=1.3.0
nltk>=3.8
textblob>=0.17.0
```

#### Benefits of Streamlit Community Cloud:
- ✅ **Free Hosting**: No cost for public repositories
- ✅ **Auto-Deploy**: Automatic updates from GitHub commits
- ✅ **Easy Sharing**: Simple URL to share with anyone
- ✅ **No Server Management**: Streamlit handles all infrastructure
- ✅ **Built-in Analytics**: Track app usage and performance

### Option C: Using HTML Interface

For a simpler, static version without Python dependencies:

1. **Open the HTML File**

Simply open `index.html` in your web browser:
- Double-click the file, or
- Right-click and select "Open with" → Your preferred browser

2. **Limitations**
- No real file upload functionality
- Uses sample data for demonstration
- Best for quick previews and presentations

---

## 📁 Project Structure

```
learning-analytics-dashboard/
│
├── streamlit_app.py          # Main Streamlit application ⭐ NEW!
├── nlp_analysis.py            # NLP processing module (optional)
├── index.html                 # Standalone HTML dashboard
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── data/                      # Sample datasets (optional)
│   ├── sample_students.csv
│   └── sample_feedback.csv
│
└── assets/                    # Static resources (optional)
    ├── css/
    ├── js/
    └── images/
```

---

## 📊 Data Format

### Expected CSV Structure

Your CSV file should include columns such as:

```csv
student_id,name,grade,attendance,assignments_completed,engagement_score,feedback
1001,John Doe,85,92,15,78,"Great participation in class"
1002,Jane Smith,92,98,18,95,"Excellent work ethic"
1003,Bob Johnson,78,85,14,72,"Needs improvement in assignments"
```

### Supported Data Types

- **Numeric**: Grades, scores, percentages, counts
- **Text**: Names, feedback, comments, responses
- **Dates**: Enrollment dates, submission timestamps
- **Categories**: Course names, departments, student groups

---

## 🛠️ Technologies Used

### **Frontend & Visualization**
- **Streamlit**: Interactive web application framework
- **Plotly**: Dynamic, interactive charts and graphs
- **HTML/CSS/JavaScript**: Standalone web interface

### **Backend & Processing**
- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### **NLP & Machine Learning**
- **NLTK**: Natural Language Toolkit
- **TextBlob**: Sentiment analysis
- **scikit-learn**: Machine learning models

### **Visualization**
- Matplotlib, Seaborn, Plotly

---

## 📖 Usage Examples

### Example 1: Analyzing Class Performance

1. Upload a CSV file with student grades and attendance
2. View the dashboard's automatically generated visualizations:
   - Grade distribution histogram
   - Attendance vs. performance correlation
   - At-risk student identification

### Example 2: Sentiment Analysis of Student Feedback

1. Upload a CSV file containing student feedback comments
2. Navigate to the Analytics tab
3. View sentiment analysis results:
   - Positive, negative, and neutral sentiment distribution
   - Key themes and topics extracted from feedback
   - Word clouds of common terms

### Example 3: Tracking Student Progress Over Time

1. Upload historical grade data with timestamps
2. Use the time-series visualizations to:
   - Track individual student progress
   - Identify trends and patterns
   - Compare performance across different periods

---

## 🔧 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` when running the app
**Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue**: CSV file upload fails
**Solution**: Check that your CSV file:
- Is properly formatted with headers
- Uses UTF-8 encoding
- Contains no special characters in column names

**Issue**: Visualizations not displaying
**Solution**:
- Clear browser cache and reload
- Check browser console for JavaScript errors
- Ensure Plotly is properly installed: `pip install plotly --upgrade`

**Issue**: Streamlit app not loading
**Solution**:
- Check if port 8501 is already in use
- Try a different port: `streamlit run streamlit_app.py --server.port 8502`
- Verify Python version is 3.8 or higher

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - feel free to use it for educational and commercial purposes.

---

## 📞 Support and Contact

If you have questions, suggestions, or need help:

- **Open an Issue**: Use the GitHub Issues tab for bug reports and feature requests
- **Discussions**: Join GitHub Discussions for community support
- **Email**: [Add your email here]
- **LinkedIn**: [Add your LinkedIn profile here]

---

## 🙏 Acknowledgments

- Thanks to all contributors and users who have helped improve this project
- Special thanks to the open-source community for the amazing tools and libraries
- Inspired by the need for better educational analytics tools
- Built with ❤️ using Streamlit and Plotly

---

## ⭐ Star This Repository

If you find this project helpful, please consider giving it a star on GitHub. It helps others discover the project and motivates continued development!

---

## 📝 Changelog

### **Version 1.0.0** (Current)
- Initial release with core dashboard functionality
- NLP analysis module for sentiment analysis
- File upload and data processing features
- Streamlit integration for interactive web interface
- ✨ **NEW**: Streamlit Community Cloud deployment support
- ✨ **NEW**: Comprehensive starter template in streamlit_app.py

### **Planned Features**
- [ ] Multi-language support
- [ ] Advanced machine learning models for prediction
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Mobile app version
- [ ] Real-time collaboration features
- [ ] API for third-party integrations
- [ ] Export reports to PDF/Excel
- [ ] Custom dashboard themes

---

**Made with ❤️ for educators and students worldwide**

---

## 🌐 Live Demo

🚀 **Deploy this dashboard to Streamlit Community Cloud and add your live demo link here!**

Example: `https://your-learning-analytics.streamlit.app`
