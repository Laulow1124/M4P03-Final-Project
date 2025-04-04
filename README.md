# M4P03 Final Project
## Supervised Classification Model to predict Injury Severity from Vehicle Crashes
-------------------------------------------------------------------

**Summary/Objective: <br>** 
This project involves building a classification model to predict the severity of injuries from vehicle crashes. The dataset contains information such as the type of weather, extent of vehicle damage, speed limit, driver fault, etc. Various machine learning models will be evaluated to determine the best model for predicting injury severity. The goal is to determine the most accurate model and deploy it for future predictions of traffic accident severity. After choosing a final model, the final model will be deployed in a Streamlit app to make a prediction.

**Reference link for dataset: <br>** 
https://catalog.data.gov/dataset/crash-reporting-drivers-data

**Dataset (.csv) file name: <br>**
- Crash_Reporting_-_Drivers_Data.csv

**Interactive Python Notebook file (Data cleaning, Model Training, Model Evaluation, Saving Final Model, etc.):**
- M4P03 Final Project.ipynb <br>

**App Python file used to run code for Streamlit app: <br>**
- M4P03_app.py <br> 

**Required/Imported files used for Streamlit app: <br>**
<br>
*Requirements text file:* 
- M4P03_requirements.txt <br>

*Binary Encoder (Pickle File):* 
- binary_encoder.pkl <br>

*Final Model (JOBLIB File):*
- M4P03_final_model.joblib <br>

**M4P03 Powerpoint Presentation Slides (.pptx File): <br>**
- M4P03 Final Project Powerpoint.pptx

**URLs for Streamlit app:** <br>
Local URL: http://localhost:8501 <br>
Network URL: http://10.0.0.201:8501 <br>


**The three classification models used are:**
1. Logistic Regression
2. Support Vector Classification (SVC)
3. Random Forest Classification
    
**The main methodologies and techniques applied in this project:**
1. Feature Engineering and Data Preprocessing
2. Classification Models (Logistic Regression, Support Vector Classification (SVC), and Random Forest Classification)
3. Hyperparameter Tuning (with GridsearchCV)
4. Model Evaluation and Comparison (Confusion Matrix and Classification Reports)    
   
**The project is split into five parts:**
1. Part 1: Data Exploration, Data Cleaning, and Data Preparation (e.g., splitting data into features and target).
2. Part 2: Model #1, Logistic Regression.
3. Part 3: Model #2, Support Vector Classification (SVC).
4. Part 4: Model #3, Random Forest Classification.
5. Part 5: Model Evaluation and Comparison, with the final model chosen based on accuracy. The selected model will be deployed and used for predictions. 
    
**Vehicle Crash Injury Severity Prediction Project criteria:** <br>
1. **Exploratory Data Analysis (EDA) includes:** <br>
- Checking for missing data and verifying value types.
- Visualizations to understand data distributions and feature relationships. (ex: Count Plot, Box Plot, Violin Plot, etc.)

    Observations from EDA:
    - The dataset contains information such as weather, vehicle damage, speed limits, etc.
    - A significant class imbalance exists in injury severity. 

2. **Modeling Process:**
- Logistic Regression: A linear model that is interpretable and simple.
- Support Vector Classification (SVC): Focuses on finding the optimal hyperplane in high-dimensional spaces.
- Random Forest Classification: Uses an ensemble of decision trees to predict injury severity.

3. **Feature Engineering and Preprocessing:**
- Categorical features are encoded to numerical values (e.g., Binary Encoding for weather and vehicle damage extent).
- Data is split into training, validation, and test sets for model evaluation.
- Custom class weights are applied to address class imbalance in the dataset.
- Pre-processing: Make all objects/strings upper case to avoid duplicates.  
- Pre-processing and Feature Engineering on 'Crash Date/Time':
  - Pre-processing: Converting 'Crash Date/Time' into a datetime format.
  - Feature Engineering: Creating new features like 'Year', 'Month', 'Day', 'DayOfWeek', 'Hour', and 'TimeOfDay' from the datetime data.
<br> 
- Feature Engineering: Mapped 'Injury Severity' (target variable, y) categorical values to the following:
   - 'FATAL INJURY': 4
   - 'SUSPECTED SERIOUS INJURY': 3
   - 'SUSPECTED MINOR INJURY': 2
   - 'POSSIBLE INJURY': 1
   - 'NO APPARENT INJURY': 0

4. **Model Evaluation:**
- GridSearchCV is used for hyperparameter tuning. <br>
- Evaluation metrics such as accuracy, precision, recall, F1-score from classification reports and the confusion matrix are used to compare model performances. <br>

   **Validation Scheme:**
- Cross-validation with hyperparameter tuning ensures robustness and avoids overfitting. <br>

   **Validation and Evaluation include:**
- Confusion Matrix: To visualize model performance. <br>
- Classification Report: To evaluate precision, recall, F1-score, and accuracy for each injury severity class. <br>
- Comparison of Results: Final comparison of Logistic Regression, SVC, and Random Forest models. <br>

5. **Final Model:**
- Random Forest Classification was chosen as the final model due to its superior accuracy and performance metrics.
- The model was trained on the dataset and deployed for future predictions.

6. **Model Deployment:**
- The trained Random Forest model is saved using the joblib library for deployment.
- The final model is saved as M4P03_final_model.joblib and will be loaded and used for predictions on new traffic accident data.
- The final model ('M4P03_final_model.joblib') will be used for deployment as a Streamlit app and will be used to make a prediction.

## Conclusion 
In conclusion, three models were tested: Logistic Regression, Support Vector Classification (SVC) and Random Forest Classification. <br>
**Of the three models, the Random Forest Classification model had the best performance as it had the highest accuracy. The Random Forest Classification model was chosen as the final model.** <br>

- For chosen features (applied to final model, Random Forest Classification): features related to Crash Circumstances (ex: Weather, etc.), Driver Behavior & Risk Factors (ex: Driver At Fault, etc.), Vehicle Information (ex: Vehicle Damage Extent), Location Data (ex: Latitude, etc.) and High Correlation (ex: ACRS Report Type) were chosen as they could influence the Injury Severity. <br>
- The features underwent various preprocessing and feature engineering techniques to enhance their suitability for model prediction. (ex: Made all objects/strings upper case to avoid duplicates, etc.)
- Cross-validation (with GridSearchCV) was used as a validation scheme. Cross-validation was used to evaluate the holdout data for the final model, and has almost similar results/metrics with the test data. <br>
- All three classification models required the data to be converted into numerical format hence the use of encoding. Binary Encoder was used was used on all applicable features (which were originally objects/strings) to convert their values to be numerical. <br>
- Mapping was used for 'Injury Severity' to convert their values to be numerical. <br> 
- With what was stated above, the final model (Random Forest Classification) had the encoding feature BinaryEncoder to convert the feature values to be numerical. This encoder was applied as part of feature engineering for the final model. <br>  
- Continuing with feature engineering, scaling was not applied on the data for the final model (Random Forest Classification), as it was not necessary for the Random Forest model. <br>
- As per prediction experimentation, with "new_data_input" (data frame)" as input, the Random Forest Classification Model was able to provide a prediction of the Injury Severity. <br>
- The final model was saved as a joblib file (as 'M4P03_final_model.joblib'). After loading the final model, the final model ('M4P03_final_model.joblib') was able to make a prediction. <br>
- The final model ('M4P03_final_model.joblib') was used for deployment as a Streamlit app and was able to make a prediction. <br>
