# Learning Analytics Dashboard

An interactive web-based dashboard built with Streamlit to visualize and analyze student performance data. This tool helps educators gain insights into student learning patterns, engagement trends, and overall class performance through intuitive visualizations.

## Features

- **Student Performance Overview**: Visual representation of overall student scores and performance metrics
- **Interactive Data Analysis**: Filter and explore data by various dimensions (subjects, time periods, student cohorts)
- **Engagement Metrics**: Track student participation, assignment completion rates, and time spent on activities
- **Text Analysis Tools**: Analyze student feedback and open-ended responses using NLP techniques
- **Customizable Visualizations**: Create custom charts and graphs using Plotly for interactive data exploration
- **Export Capabilities**: Download filtered data and visualizations for further analysis or reporting
- **User-Friendly Interface**: Clean, intuitive design that requires no technical expertise to use

## Project Structure

```
learning-analytics-dashboard/
├── my_dashboard/
│   ├── streamlit_app.py      # Main application file
│   ├── text_analyzer.py      # Text analysis utilities
│   └── requirements.txt      # Python dependencies
└── README.md                 # This file
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/towhidulislam1999/learning-analytics-dashboard.git
cd learning-analytics-dashboard
```

2. Install the required dependencies:
```bash
cd my_dashboard
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

4. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Example CSV Format

The dashboard expects CSV files with the following structure:

```csv
student_id,student_name,subject,score,date,engagement_level,assignment_completed
1001,John Doe,Mathematics,85,2024-01-15,High,Yes
1002,Jane Smith,Mathematics,92,2024-01-15,High,Yes
1003,Bob Johnson,Mathematics,78,2024-01-15,Medium,Yes
1001,John Doe,Science,88,2024-01-16,High,Yes
1002,Jane Smith,Science,95,2024-01-16,High,Yes
```

### CSV Field Descriptions:

- **student_id**: Unique identifier for each student
- **student_name**: Full name of the student
- **subject**: Course or subject name
- **score**: Numerical score (0-100)
- **date**: Date of the assessment (YYYY-MM-DD format)
- **engagement_level**: Student engagement (High/Medium/Low)
- **assignment_completed**: Whether the assignment was completed (Yes/No)

## Demo Account Information

This dashboard is designed to work with your own data files. Simply upload your CSV file through the application interface to begin analysis. No login is required.

If you need sample data for testing:
- Use the example CSV format provided above
- Create a test file with at least 10-15 rows of sample data
- Upload the file through the dashboard's file upload interface

## Customization

### Adding New Visualizations

To add custom visualizations, edit `streamlit_app.py` and use Plotly for creating interactive charts:

```python
import plotly.express as px
import streamlit as st

# Example: Create a custom scatter plot
fig = px.scatter(df, x='score', y='engagement_level', color='subject')
st.plotly_chart(fig)
```

### Modifying Text Analysis

The `text_analyzer.py` module contains functions for analyzing text data. You can customize these functions to:
- Add sentiment analysis
- Perform keyword extraction
- Generate word clouds
- Implement custom NLP pipelines

### Styling and Theming

Streamlit allows customization through configuration files. Create a `.streamlit/config.toml` file in the project root:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Python**: Core programming language

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the dashboard.

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 Towhidul Islam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support

For questions or support, please open an issue in the GitHub repository.

---

**Happy Analyzing! 📊📈**
