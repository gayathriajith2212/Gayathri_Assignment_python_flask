from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    with open('model (5).pkl','rb') as model_file:
        model = pickle.load(model_file)
    if request.method == 'POST':
        age = int(request.form['age'])
        estimated_salary = int(request.form['estimated_salary'])
        
     # Make prediction
    feature = np.array([[age, estimated_salary]])
    prediction = model.predict(feature)
    # Map numerical predictions to meaningful labels
    prediction_label = "Purchased" if prediction == 1 else "Not Purchased"
    print("Prediction Label:", prediction_label)


    # Return prediction result
    return render_template('prediction.html', pred_res=prediction_label)

if __name__=='__main__':
    app.run(debug=True)