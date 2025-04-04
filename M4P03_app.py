import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
import category_encoders as ce

# Load the previously saved BinaryEncoder
with open('binary_encoder.pkl', 'rb') as f:
    binary_encoder = pickle.load(f)

# Load the model
def load_model():
    model = joblib.load('M4P03_final_model.joblib')  
    return model

loaded_model = load_model()

# Function to get user input
def get_user_input():
    # Title and description for the app inside the function
    st.title("Vehicle Crash Injury Severity Prediction")
    st.write("""### Please provide the crash details to predict the injury severity""")
    
    # ACRS Report Type (Categorical) 
    acrs_report_type = st.selectbox("ACRS Report Type", 
                                    ["FATAL CRASH", "INJURY CRASH", "PROPERTY DAMAGE CRASH"])
    
    # Vehicle Damage Extent (Categorical) 
    vehicle_damage_extent = st.selectbox("Vehicle Damage Extent", 
                                        ["DESTROYED", "DISABLING", "FUNCTIONAL", "NO DAMAGE", "SUPERFICIAL"])
    
    # Speed Limit (Numeric - Slider)
    speed_limit = st.slider("Speed Limit", 0, 75, 35)  # Default to 35 mph

    # Driver At Fault (Categorical) 
    driver_at_fault = st.selectbox("Driver At Fault", ["NO", "UNKNOWN", "YES"])

    # Vehicle Movement (Categorical) 
    vehicle_movement = st.selectbox("Vehicle Movement", 
                                    ["ACCELERATING", "BACKING", "CHANGING LANES", "DRIVERLESS MOVING VEH.",
                                     "ENTERING TRAFFIC LANE", "LEAVING TRAFFIC LANE", "MAKING LEFT TURN", 
                                     "MAKING RIGHT TURN", "MAKING U TURN", "MOVING CONSTANT SPEED", 
                                     "PARKED", "PARKING", "RIGHT TURN ON RED", "SKIDDING", 
                                     "SLOWING OR STOPPING", "STOPPED IN TRAFFIC LANE"])
    
    # Create dictionary with the user input
    user_input = {
        'ACRS Report Type': [acrs_report_type],
        'Vehicle Damage Extent': [vehicle_damage_extent],
        'Speed Limit': [speed_limit],
        'Driver At Fault': [driver_at_fault],
        'Vehicle Movement': [vehicle_movement]
    }
    
    return user_input

# Main function to run the app
def show_predict_page():
    # Get user inputs
    user_input = get_user_input()

    # Display user inputs for confirmation
    st.write("### Your Inputs:")
    st.write(f"ACRS Report Type: {user_input['ACRS Report Type'][0]}")
    st.write(f"Vehicle Damage Extent: {user_input['Vehicle Damage Extent'][0]}")
    st.write(f"Speed Limit: {user_input['Speed Limit'][0]} mph")
    st.write(f"Driver At Fault: {user_input['Driver At Fault'][0]}")
    st.write(f"Vehicle Movement: {user_input['Vehicle Movement'][0]}")

    # Data input dictionary
    data_input_dict = {
        'ACRS Report Type': 'FATAL CRASH',
        'Route Type': 'RAMP',
        'Road Name': 'RAMP 8 FR US 29 SB TO DUSTIN RD',
        'Cross-Street Name': 'DUSTIN RD',
        'Collision Type': 'SINGLE VEHICLE',
        'Weather': 'CLEAR',
        'Surface Condition': 'DRY',
        'Light': 'DAYLIGHT',
        'Traffic Control': 'YIELD SIGN',
        'Driver Substance Abuse': 'NONE DETECTED',
        'Driver At Fault': 'YES',
        'Injury Severity': 'FATAL INJURY',
        'Driver Distracted By': 'UNKNOWN',
        'Drivers License State': 'MD',
        'Vehicle Damage Extent': 'DESTROYED',
        'Vehicle Body Type': 'PASSENGER CAR',
        'Vehicle Movement': 'MOVING CONSTANT SPEED',
        'Vehicle Going Dir': 'NORTH',
        'Speed Limit': 30,
        'Vehicle Year': 2009,
        'Vehicle Make': 'HYUNDAI',
        'Vehicle Model': 'ELANTRA',
        'Latitude': 39.12246766,
        'Longitude': -76.92633791,
        'Year': 2023,
        'Month': 10,
        'Day': 28,
        'DayOfWeek': 5,
        'Hour': 12,
        'TimeOfDay': 'AFTERNOON'
    }

    # Update the data dictionary with user input
    updated_data_dict = data_input_dict.copy()
    for key, value in user_input.items():
        if key in updated_data_dict:
            updated_data_dict[key] = value[0]  # Replace with the user's selected value

    # Convert the updated dictionary into a DataFrame
    df_updated = pd.DataFrame([updated_data_dict])

    # Apply the BinaryEncoder
    encoded_df_updated = binary_encoder.transform(df_updated)

    # Drop the 'Injury Severity' column as it's not needed for prediction
    encoded_df_updated = encoded_df_updated.drop(columns=['Injury Severity'])

    # Prediction button
    if st.button("Predict Accident Severity"):
        # Make prediction with the loaded model
        prediction = loaded_model.predict(encoded_df_updated)
        
        # Show the prediction result
        st.subheader(f"The predicted accident severity is: {prediction[0]}")

# Explanation of output labels
        st.write("""
        ### Output numbers represent the following:
        0 : NO APPARENT INJURY  
        1 : POSSIBLE INJURY  
        2 : SUSPECTED MINOR INJURY  
        3 : SUSPECTED SERIOUS INJURY  
        4 : FATAL INJURY  
        """)

# Run the app
if __name__ == "__main__":
    show_predict_page()



