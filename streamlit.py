import streamlit as st
import pickle
import pandas as pd
# Load the CSV file with the car data
pred_df = pd.read_csv("./AB_US_2020.csv")

# Write the title of the application on the UI
st.write("""# Price Prediction App
""")

# Function to make the prediction using the pre-trained model
def model_pred(reviews_per_month, latitude, longitude, id):


 with open("USA_database.ipynb") as file:
        reg_model = pickle.load(file)


    # Prepare the input features
    input_features = [[reviews_per_month, latitude, longitude, id]]
    return reg_model.predict(input_features)

# Create two columns in the UI
col1, col2, col3 = st.columns(3)

row1, row2 = st.columns(2)

# Create a textbox to put for the id
id = row1.text_input("ID")

# Create a slider to set the latitude
latitude = row1.slider("Latitude",
                        0, 50, step=1)

# Create a slider to set the longitude
longitude = row1.slider("Longitude",
                        -200, 0, step=1)

# Create a slider to set the reviews per month
reviews_per_month = row1.slider("Reviews / Month",
                        0, 10, step=1)





# Create a button to trigger the prediction
if(st.button("Predict Price")):

    # Make the prediction
    price = model_pred(reviews_per_month, latitude, longitude, id)

     # Display the result on the UI
    st.text("Predicted price: "+ str(price))
