🌾 Crop Production Prediction App

This project is a Streamlit-based web application that predicts crop production (in tons) using machine learning models.
It allows users to upload CSV files, train models, visualize trends, and make predictions to support agricultural planning and decision-making.

🚀 Features

📂 Upload CSV Files – Import datasets with crop production data.

🧠 Train Machine Learning Models – Supports XGBoost and other regression models.

📊 Interactive Visualizations – Analyze trends in crop yield, production, and area harvested.

🌍 Multi-Region & Multi-Crop Support – Predictions across different regions and crop types.

🔮 Future Predictions – Estimate production based on selected features like crop type, region, and year.

📥 Downloadable Reports – Export insights in PDF/CSV format for easy sharing.

📂 Project Structure
Crop-Production-Prediction-App/
│── data/                 # Sample datasets (CSV files)
│── models/               # Saved trained models
│── app.py                # Main Streamlit app
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

⚙️ Installation
1. Clone the repository
git clone https://github.com/Vamsi216522/Crop-Production-Prediction-App.git
cd Crop-Production-Prediction-App

2. Create and activate a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate     # On Linux/Mac
env\Scripts\activate        # On Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Usage
1. Run the Streamlit App
streamlit run app.py

2. Open in Browser

Go to http://localhost:8501
 to access the app.

3. Steps in the App

Upload your dataset (.csv)

Explore EDA (Exploratory Data Analysis) visualizations

Train a regression model (default: XGBoost Regressor)

Upload new CSVs to predict production values

Download predictions and reports

📊 Example Dataset
Crop	Region	Year	Area (ha)	Yield (kg/ha)	Production (tons)
Wheat	Punjab	2018	5000	3200	16000
Rice	AP	2019	4500	2800	12600
Maize	Bihar	2020	3000	2500	7500
🧪 Models Used

XGBoost Regressor – Handles large datasets with high accuracy

Multi-output Regression – For predicting multiple targets (e.g., yield & production)

Evaluation Metrics:

R² Score

RMSE (Root Mean Square Error)

📈 Visualizations

Yearly production trends

Region-wise crop yield distribution

Correlation heatmap between environmental & production factors

Predicted vs. Actual production

📌 Requirements

Python 3.8+

Streamlit

Pandas

NumPy

Scikit-learn

XGBoost

Plotly / Matplotlib

Install all using:

pip install -r requirements.txt

🛠️ Future Enhancements

🌱 Integration with real-time weather & soil APIs

🛰️ Satellite data for yield forecasting

📡 Cloud deployment (Heroku / AWS / GCP)

📊 Advanced visualization dashboards with Power BI / Tableau

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo, open issues, and submit pull requests.

📜 License

This project is licensed under the MIT License.
You’re free to use, modify, and distribute it with attribution.
