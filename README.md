                          ┌────────────────────────────┐
                          │        User (Client)        │
                          │  - Enters 13 medical values │
                          │  - Uploads CSV/Excel file   │
                          └──────────────┬──────────────┘
                                         │
                           HTTP Request  │  (/predict or /upload)
                                         ▼
                     ┌──────────────────────────────────────────┐
                     │                Flask App                  │
                     │                (app.py)                   │
                     └───────────────┬───────────────┬──────────┘
                                     │               │
                                     │               │
                                     ▼               ▼
                   ┌─────────────────────┐   ┌──────────────────────┐
                   │ Input Processor     │   │  File Upload Handler │
                   │ - Reads form data   │   │ - Reads CSV/Excel    │
                   │ - Converts to list  │   │ - Extracts features  │
                   │ - Converts to array │   │ - Handles errors     │
                   └──────────┬──────────┘   └───────────┬─────────┘
                              │                          │
                              └──────────────┬───────────┘
                                             ▼
                           ┌──────────────────────────────────┐
                           │      ML Model Prediction Engine  │
                           │  (Loads PKL files from /models)  │
                           │                                  │
                           │  Models Used:                    |
                           │   ✔ KNN                          │
                           │   ✔ Logistic Regression          │
                           │   ✔ Naive Bayes                  │
                           │   ✔ Decision Tree                │
                           │   ✔ Random Forest                │
                           │   ✔ AdaBoost                     │
                           │   ✔ Gradient Boosting            │
                           │   ✔ XGBoost                      │
                           │   ✔ SVM                          │
                           │                                   │
                           └───────────────────┬──────────────┘
                                               │
                                   Predictions │ (heart disease / no disease)
                                               ▼
                    ┌────────────────────────────────────────────────┐
                    │               Result Processor                 │
                    │ - Converts labels to text                      │
                    │ - Formats results for HTML                     │
                    └──────────────────────┬─────────────────────── ─┘
                                            │
                                   Sends data to template
                                            ▼
                         ┌────────────────────────────────────┐
                         │           Frontend (HTML)          │
                         │           result.html              │
                         │                                    │
                         │ - Displays predictions per model   │
                         │ - Color coding (red/green)         │
                         └────────────────────────────────────┘



***1. Project Overview***

This project aims to assist in early detection of heart disease using machine learning.
I trained multiple classification models and compared their performance.
Then I integrated them into a Flask web application, where the user enters 13 health-related values, and the app displays predictions from all models.

The website shows results as:

Heart Disease (red color)

No Heart Disease (green color)

Each model predicts independently.



 ***2. Dataset Description***

The dataset used is the UCI Heart Disease Dataset, containing 13 key medical features:

Feature	Description
age	Age of the patient
sex	1 = Male, 0 = Female
cp	Chest pain type (0–3)
trestbps	Resting blood pressure
chol	Cholesterol level
fbs	Fasting blood sugar
restecg	Resting ECG results
thalach	Maximum heart rate achieved
exang	Exercise-induced angina
oldpeak	ST depression
slope	Slope of ST segment
ca	Number of major vessels
thal	Thalassemia



 ***3. Machine Learning Models Used***

I trained 8 different ML models:

K-Nearest Neighbors (KNN)

Logistic Regression

Naive Bayes

Decision Tree Classifier

Random Forest Classifier

AdaBoost Classifier

Gradient Boosting Classifier

XGBoost Classifier

Support Vector Machine (SVM)

Each model was trained separately and saved using:

joblib.dump(model, 'models/model_name.pkl')


 ***4. Training Process Summary***

Loaded and cleaned the dataset

Separated dataset into features (X) and target (y)

Used train_test_split

Trained all models one by one

Evaluated accuracy

Saved all models into the models/ folder

Example code:

model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
joblib.dump(model, 'models/RandomForest.pkl')


***5. Flask Backend Explanation***

The Flask backend does 3 main tasks:

✔ Loads all models at startup
models = {
    "KNN": joblib.load("models/KNN.pkl"),
    "LogisticRegression": joblib.load("models/Logistic.pkl"),
    ...
}

✔ Receives user input

Form input → converted into a list → converted to NumPy array

✔ Generates predictions from all models
pred = model.predict([input_data])[0]

✔ Sends results to result.html template

Using:

return render_template('result.html', predictions=final_predictions)



***6. Frontend Explanation***
index.html

Contains form with 13 input fields

User enters values

Form submits values to /predict

result.html

Displays output in a table

Red = Heart Disease

Green = No Heart Disease


***7. Folder Structure***
HeartDisease/
│── app.py
│── requirements.txt
│── models/
│      ├── KNN.pkl
│      ├── Logistic.pkl
│      ├── RandomForest.pkl
│      ├── ...
│── templates/
│      ├── index.html
│      ├── result.html
│

***8. How to Run the Project***
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Flask app
python app.py

3️⃣ **Open in browser**
http://127.0.0.1:5000


 ***9. Features***

✔ Uses multiple ML models
✔ Clean HTML interface
✔ Displays all model results at once
✔ Easy to deploy
✔ Lightweight and fast


