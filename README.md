🐞 AI Bug Triage System
An intelligent, AI-powered QA tool designed to automatically categorize bugs in the iGaming and slot gaming domain. This system predicts the Priority and Component of reported issues, helping QA teams streamline their bug tracking and triage process.

🚀 Features
AI Engine: Uses RandomForest and TfidfVectorizer to learn patterns from historical bug data.

Smart Dashboard: Visualize bug trends and component hotspots in real-time.

Data Persistence: Automatically logs every report into a local SQLite database.

Exporting: Easily download your bug reports as CSV for Jira/Bugzilla integration.

Responsive UI: Clean, sidebar-based navigation for a professional workflow.

🛠 Tech Stack
Language: Python 3.10+

Framework: Streamlit (UI)

ML/AI: Scikit-Learn, Pandas, Joblib

Database: SQLite

📋 Getting Started
1. Prerequisites
Ensure you have Python installed. Clone the repository and navigate to the project folder:

Bash
cd AI_Bug_Tracker
2. Setup Virtual Environment
Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run the Application
Start the Streamlit dashboard:

Bash
./venv/bin/python -m streamlit run app.py
Open the provided URL (usually http://localhost:8501) in your browser.

📂 Project Structure
app.py: Main dashboard interface.

src/engine.py: AI model training and prediction logic.

src/database.py: Database connection and logging utilities.

data/metadata.csv: The training dataset for the AI.

data/bug_logs.db: The persistent storage for logged bugs.

💡 How to use
Enter a bug description (e.g., "The bonus round freezes after the 5th spin").

Click Analyze & Log Bug.

View the AI prediction and check the Bug History table for trends.

Use the sidebar to clear logs or export your report.
