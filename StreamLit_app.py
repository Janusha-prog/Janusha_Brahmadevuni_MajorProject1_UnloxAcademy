import streamlit as st
import pandas as pd
import joblib

# Page title
st.title("🚗 Indian Pre-Owned Car Price Prediction")

st.write("Enter the car details to predict its resale price.")

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("final_model.joblib")

model = load_model()


# Numerical input fields

st.sidebar.header("Car Details")

distance = st.sidebar.number_input("Distance (km)", min_value=0.0)
age = st.sidebar.number_input("Age of car", min_value=0.0)
engine_displacement = st.sidebar.number_input(
    "Engine Displacement", min_value=0.0
)
engine_power = st.sidebar.number_input(
    "Engine Power", min_value=0.0
)
door_count = st.sidebar.number_input(
    "Door Count", min_value=1.0
)
seat_count = st.sidebar.number_input(
    "Seat Count", min_value=1.0
)
vroom_rating = st.sidebar.number_input(
    "Vroom Audit Rating", min_value=0.0
)

# Categorical input fields

maker_models = {
    "audi": ["coupe", "q3", "q5", "q7", "tt"],
    "bmw": ["x1", "x3", "x5"],
    "fiat": ["coupe", "panda"],
    "hyundai": ["coupe", "i30"],
    "maserati": ["coupe"],
    "nissan": ["juke", "micra", "qashqai"],
    "skoda": ["citigo", "octavia", "rapid", "roomster", "superb", "yeti"],
    "toyota": ["auris", "avensis", "aygo", "yaris"]
}

maker = st.sidebar.selectbox(
    "Maker",
    list(maker_models.keys())
)

model_name = st.sidebar.selectbox(
    "Model",
    maker_models[maker]
)

location = st.sidebar.selectbox(
    "Location",
    [
        "Ahmedabad", "Bangalore", "Chennai", "Coimbatore",
        "Delhi", "Hyderabad", "Jaipur", "Kochi",
        "Kolkata", "Mumbai", "Pune"
    ]
)

owner_type = st.sidebar.selectbox(
    "Owner Type",
    ["First", "Second", "Third", "Fourth & Above"]
)

body_type = st.sidebar.selectbox(
    "Body Type",
    ["compact", "van"]
)

transmission = st.sidebar.selectbox(
    "Transmission",
    ["auto", "man"]
)

fuel_type = st.sidebar.selectbox(
    "Fuel Type",
    ["diesel", "petrol"]
)

# Prediction 

if st.button("🔮 Predict Price"):

    data = pd.DataFrame({
        "Distance": [distance],
        "Age of car": [age],
        "engine_displacement": [engine_displacement],
        "engine_power": [engine_power],
        "door_count": [door_count],
        "seat_count": [seat_count],
        "Vroom Audit Rating": [vroom_rating],
        "Maker": [maker],
        "model": [model_name],
        "Location": [location],
        "Owner Type": [owner_type],
        "body_type": [body_type],
        "transmission": [transmission],
        "fuel_type": [fuel_type]
    })

    price = model.predict(data)[0]

    lower_price = price * 0.95
    upper_price = price * 1.05

    st.success(f"Estimated Car Price: ₹{price:,.0f}")

    st.write(
        f"Fair Price Range: ₹{lower_price:,.0f} - ₹{upper_price:,.0f}"
    )

 
# BATCH PREDICTION


st.header("📁 Batch Prediction")

file = st.file_uploader(
    "Upload Test CSV file",
    type=["csv"]
)

if file is not None:

    test_data = pd.read_csv(file)
    test_data.columns = test_data.columns.str.strip()


    st.write("Uploaded Data:")
    st.dataframe(test_data.head())

    if st.button("Predict All Prices"):

        ids = test_data["ID"]

        test_data = test_data.drop(
            columns=["ID", "manufacture_year"]
        )

        test_data["body_type"] = test_data["body_type"].fillna("Unknown")

        predictions = model.predict(test_data)

        result = pd.DataFrame({
            "ID": ids,
            "Price": predictions
        })

        st.write("Predicted Prices:")
        st.dataframe(result.head())

        result.to_csv("predictions.csv", index=False)

        st.download_button(
            "⬇️ Download Predictions",
            result.to_csv(index=False),
            "predictions.csv",
            "text/csv"
        )


# VISUAL INSIGHTS

st.header("📊 Visual Insights")

if file is not None and "predictions" in locals():

    chart_data = test_data.copy()
    chart_data["Predicted Price"] = predictions

    st.subheader("Age vs Predicted Price")

    st.scatter_chart(
        chart_data,
        x="Age of car",
        y="Predicted Price"
    )

    st.subheader("Distance vs Predicted Price")

    st.scatter_chart(
        chart_data,
        x="Distance",
        y="Predicted Price"
    )
