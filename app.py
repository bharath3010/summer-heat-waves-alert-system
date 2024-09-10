from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('models/heatwave_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        features = [np.array(data)]
        prediction = model.predict(features)

        if prediction == 1:
            result = 'Heatwave Alert: Stay Safe!'
        else:
            result = 'No Heatwave: Enjoy your day!'

        return render_template('index.html', prediction_text=result)
    except:
        return render_template('index.html', prediction_text="Error in processing input")

if __name__ == "__main__":
    app.run(debug=True)


