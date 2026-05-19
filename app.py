

# import streamlit as st
# import pandas as pd
# import joblib
# import plotly.express as px

# # --- Load the trained model ---
# model = joblib.load("multioutput_crop_model.pkl")

# # --- Load the dataset to extract dropdown options ---
# df_pivot = pd.read_csv("df_pivot.csv")
 

# # --- Clean and get unique values ---
# unique_areas = sorted(df_pivot['Area'].dropna().unique())
# unique_items = sorted(df_pivot['Item'].dropna().unique())

# # --- Units for display ---
# units = {
#     'Area harvested': 'ha',
#     'Production': 't',
#     'Yield': 'kg/ha'
# }

# # --- UI ---
# st.title("🌾 Crop Production Predictor")

# st.sidebar.header("🔧 Enter Input Details")
# year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2025)
# area = st.sidebar.selectbox("Area (Region)", unique_areas)
# item = st.sidebar.selectbox("Item (Crop)", unique_items)

# # --- Predict ---
# if st.sidebar.button("Predict"):
#     input_df = pd.DataFrame({'Year': [year], 'Area': [area], 'Item': [item]})

#     prediction = model.predict(input_df)[0]
#     targets = ['Area harvested', 'Production', 'Yield']

#     # --- Format results with units ---
#     result_df = pd.DataFrame({
#         'Metric': targets,
#         'Value': prediction,
#         'Unit': [units[t] for t in targets]
#     })

#     # --- Display Results ---
#     st.subheader("📈 Predicted Crop Metrics")
#     for _, row in result_df.iterrows():
#         st.markdown(f"- **{row['Metric']}**: {row['Value']:.2f} {row['Unit']}")

#     # --- Bar Chart ---
#     st.subheader("📊 Prediction Breakdown")
#     fig = px.bar(result_df, x='Metric', y='Value', color='Metric',
#                  text=result_df['Value'].round(2),
#                  labels={'Value': 'Predicted Value'})
#     fig.update_traces(textposition='outside')
#     st.plotly_chart(fig)
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ---------------- Page Config ----------------
st.set_page_config(page_title="Crop Production Predictor", layout="wide")

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    return pd.read_csv("df_pivot.csv")

df = load_data()

# ---------------- Features & Targets ----------------
FEATURES = ["Year", "Area", "Item"]
TARGETS = ["Area harvested", "Production", "Yield"]

X = df[FEATURES]
y = df[TARGETS]

# ---------------- Build Pipeline ----------------
@st.cache_resource
def train_model():
    categorical_cols = ["Area", "Item"]
    numeric_cols = ["Year"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    )

    pipeline = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X, y)
    return pipeline

model = train_model()

# ---------------- UI ----------------
st.title("🌾 Crop Production Predictor")

st.sidebar.header("🔧 Enter Input Details")
year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2025)
area = st.sidebar.selectbox("Area (Region)", sorted(df["Area"].dropna().unique()))
item = st.sidebar.selectbox("Item (Crop)", sorted(df["Item"].dropna().unique()))

# ---------------- Prediction ----------------
if st.sidebar.button("Predict"):
    input_df = pd.DataFrame({
        "Year": [year],
        "Area": [area],
        "Item": [item]
    })

    prediction = model.predict(input_df)[0]

    result_df = pd.DataFrame({
        "Metric": TARGETS,
        "Value": prediction,
        "Unit": ["ha", "t", "kg/ha"]
    })

    st.subheader("📈 Predicted Crop Metrics")
    for _, row in result_df.iterrows():
        st.markdown(f"- **{row['Metric']}**: {row['Value']:.2f} {row['Unit']}")

    st.subheader("📊 Prediction Breakdown")
    fig = px.bar(
        result_df,
        x="Metric",
        y="Value",
        color="Metric",
        text=result_df["Value"].round(2),
        labels={"Value": "Predicted Value"}
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)
