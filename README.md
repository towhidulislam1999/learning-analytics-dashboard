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
- **Export Capabilities**: Download reports in PDF and Excel formats

---

## 🚀 How to Run Locally (HTML Dashboard)

The simplest way to get started is using the standalone HTML dashboard:

### **Step 1: Download the Project**
```bash
git clone https://github.com/towhidulislam1999/learning-analytics-dashboard.git
cd learning-analytics-dashboard
```

### **Step 2: Open the Dashboard**
- Navigate to the project folder
- Locate the `index.html` file
- Double-click `index.html` to open it in your default web browser
- Alternatively, right-click and select "Open with" to choose a specific browser

### **Step 3: Upload Your Data**
- Click on the "Upload Data" button in the dashboard
- Select your CSV or Excel file containing student data
- The dashboard will automatically process and display the analytics

**Note**: The HTML dashboard works entirely in your browser without requiring any server setup. However, some advanced features require the Python backend.

---

## 🐍 How to Use with Python Backend

For advanced features including NLP analysis, use the Python backend:

### **Prerequisites**
- Python 3.7 or higher
- pip (Python package installer)

### **Option A: Using Streamlit**

#### **Step 1: Install Dependencies**
```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn nltk
```

#### **Step 2: Download Required NLTK Data**
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

#### **Step 3: Run the Streamlit App**
```bash
streamlit run streamlit_app.py
```

#### **Step 4: Access the Dashboard**
- The app will automatically open in your browser at `http://localhost:8501`
- If it doesn't open automatically, navigate to the URL manually

#### **Step 5: Upload Sample Data**
- Use the file uploader in the sidebar
- Sample file path: `./data/student_data.csv`
- Or create your own CSV with columns: `student_id`, `name`, `grade`, `attendance`, `participation`

### **Option B: Using Flask**

#### **Step 1: Install Dependencies**
```bash
pip install flask pandas numpy matplotlib seaborn scikit-learn nltk
```

#### **Step 2: Run the Flask Server**
```bash
python flask_app.py
```

#### **Step 3: Access the Application**
- Open your browser and go to `http://localhost:5000`
- The dashboard interface will load with all features enabled

---

## 📁 File Structure

Here's a detailed explanation of the key files in this project:

### **1. index.html**
**Purpose**: Main dashboard interface

**Description**: This is the front-end of the Learning Analytics Dashboard. It contains:
- HTML structure for the dashboard layout
- Embedded CSS for styling and responsive design
- JavaScript code for data visualization using Chart.js or D3.js
- Interactive elements for file upload and data filtering
- Client-side data processing for quick analytics

**Key Features**:
- No server required - runs entirely in the browser
- Responsive grid layout for different screen sizes
- Interactive charts that respond to user input
- Local storage support to save user preferences

**Usage**: Open directly in any modern web browser (Chrome, Firefox, Safari, Edge)

---

### **2. nlp_analysis.py**
**Purpose**: Natural Language Processing and data analysis module

**Description**: This Python script contains the core analytical functions:
- **Text Processing**: Tokenization, stemming, and lemmatization of student feedback
- **Sentiment Analysis**: Uses VADER or TextBlob to analyze sentiment in comments
- **Topic Modeling**: Implements LDA (Latent Dirichlet Allocation) for discovering themes
- **Predictive Analytics**: Machine learning models (Random Forest, SVM) to predict student outcomes
- **Statistical Analysis**: Calculates means, medians, standard deviations, and correlations

**Key Functions**:
```python
- analyze_sentiment(text): Returns sentiment scores (positive/negative/neutral)
- extract_keywords(text): Identifies key terms and phrases
- predict_performance(student_data): Predicts future performance
- generate_report(data): Creates comprehensive analytics reports
```

**Dependencies**: pandas, numpy, scikit-learn, nltk, matplotlib, seaborn

**Usage**: Can be imported into other Python scripts or run standalone for batch processing

---

### **3. streamlit_app.py**
**Purpose**: Interactive web application using Streamlit framework

**Description**: This file creates a modern, interactive web interface:
- **Sidebar Navigation**: Easy access to different sections (Upload, Dashboard, Analysis, Reports)
- **File Upload Widget**: Drag-and-drop interface for uploading student data
- **Real-time Visualization**: Updates charts and graphs as data changes
- **NLP Integration**: Calls functions from `nlp_analysis.py` for advanced features
- **Download Options**: Export results as CSV, PDF, or Excel files

**Key Sections**:
1. **Data Upload**: Accepts CSV/Excel files and validates the data structure
2. **Overview Dashboard**: Displays key metrics and summary statistics
3. **Student Details**: Individual student performance analysis
4. **NLP Analysis**: Sentiment analysis and text mining results
5. **Reports**: Generate and download comprehensive reports

**Configuration**:
- Port: Default 8501 (configurable in `.streamlit/config.toml`)
- Theme: Customizable light/dark mode
- Caching: Uses Streamlit's caching for improved performance

**Usage**: Run with `streamlit run streamlit_app.py` and access via web browser

---

### **Additional Files** (if present)

**requirements.txt**: List of Python dependencies for easy installation
```bash
pip install -r requirements.txt
```

**data/**: Folder containing sample datasets for testing
- `student_data.csv`: Sample student performance data
- `feedback.csv`: Sample student feedback and comments

**assets/**: Contains images, icons, and CSS files for styling

**tests/**: Unit tests for validating functionality

---

## 🎬 Demo and Credentials

### **Live Demo**
If you've deployed this project, you can access the live demo at:
- **URL**: [Add your deployment URL here]
- **Status**: [Active/Under Development]

### **Sample Credentials** (if authentication is implemented)
- **Username**: demo_user
- **Password**: demo123

**Note**: These are demo credentials for testing purposes only. Never use these in production.

### **Sample Data Files**
Included in the `data/` folder:
1. `student_data.csv` - Contains 100 sample student records
2. `feedback.csv` - Sample student feedback comments
3. `attendance.csv` - Attendance records for demonstration

### **CSV Format Example**
Your student data CSV should follow this structure:
```csv
student_id,name,grade,attendance,participation,feedback
001,John Doe,85,95,Good,"Really enjoyed the course"
002,Jane Smith,92,88,Excellent,"Great learning experience"
```

---

## 🏆 Credits and Contact Information

### **Project Developer**
**Name**: Towhidul Islam

**GitHub**: [@towhidulislam1999](https://github.com/towhidulislam1999)

**Project Repository**: [learning-analytics-dashboard](https://github.com/towhidulislam1999/learning-analytics-dashboard)

### **Technologies Used**
- **Frontend**: HTML5, CSS3, JavaScript, Chart.js
- **Backend**: Python 3.x, Flask/Streamlit
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **NLP**: NLTK, TextBlob, VADER
- **Visualization**: Matplotlib, Seaborn, Plotly

### **Contributing**
Contributions are welcome! If you'd like to improve this project:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

### **License**
This project is licensed under the MIT License - feel free to use it for educational and commercial purposes.

### **Support and Contact**
If you have questions, suggestions, or need help:
- **Open an Issue**: Use the GitHub Issues tab for bug reports and feature requests
- **Email**: [Add your email here]
- **LinkedIn**: [Add your LinkedIn profile here]

### **Acknowledgments**
- Thanks to all contributors and users who have helped improve this project
- Special thanks to the open-source community for the amazing tools and libraries
- Inspired by the need for better educational analytics tools

### **Star This Repository** ⭐
If you find this project helpful, please consider giving it a star on GitHub. It helps others discover the project and motivates continued development!

---

## 📝 Changelog

### **Version 1.0.0** (Current)
- Initial release with core dashboard functionality
- NLP analysis module for sentiment analysis
- File upload and data processing features
- Streamlit integration for interactive web interface

### **Planned Features**
- [ ] Multi-language support
- [ ] Advanced machine learning models for prediction
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Mobile app version
- [ ] Real-time collaboration features
- [ ] API for third-party integrations

---

**Made with ❤️ for educators and students worldwide**
