from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Models
try:
    models = pickle.load(open("Project_Heart.pkl", "rb"))
    print("✔ Models loaded successfully!")
except Exception as e:
    print("❌ Error loading models:", e)
    models = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"]),
        ]

        votes = []

        for model_name, model in models.items():
            pred = model.predict([features])[0]
            votes.append(pred)

        final = 1 if votes.count(1) > votes.count(0) else 0
        final_label = "Heart Disease" if final == 1 else "No Heart Disease"

        return render_template("result.html", final_result=final_label)

    except Exception as e:
        return f"❌ Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
