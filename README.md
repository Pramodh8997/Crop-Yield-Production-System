# 🌾 Crop Production Prediction App

A Machine Learning-based crop production prediction system developed using Python and Streamlit. The application predicts agricultural production outcomes using regression models and provides interactive visualizations for data-driven farming insights and planning.

## 🚀 Features

- 📂 Upload and process agricultural datasets in CSV format  
- 🧠 Train ML regression models including Random Forest and XGBoost  
- 📊 Interactive charts and visual analytics for production trends  
- 🌍 Support for multiple crops, regions, and yearly forecasting  
- 🔮 Predict crop production using user-provided inputs  
- 📥 Export predictions and processed results in CSV format  

## 📂 Project Structure

```bash
Crop-Production-Prediction-App/
│── data/                 # Dataset files
│── models/               # Trained ML models
│── app.py                # Main Streamlit application
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
```

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Crop-Production-Prediction-App.git
cd Crop-Production-Prediction-App
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

Activate environment:

```bash
# Windows
env\Scripts\activate

# Linux / Mac
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

## 📊 Technologies Used

- Python
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Matplotlib
- Plotly

## 🧪 Machine Learning Models

- Random Forest Regressor
- XGBoost Regressor
- Multi-output Regression

### Evaluation Metrics

- R² Score
- RMSE
- MAE

## 📈 Visualizations

- Crop production trend analysis
- Region-wise production comparison
- Correlation heatmaps
- Predicted vs Actual analysis

## 🛠️ Future Improvements

- Real-time weather API integration
- Soil analysis support
- Cloud deployment
- Advanced analytics dashboard

## 📜 License

This project is licensed under the MIT License.
