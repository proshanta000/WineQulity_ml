import os
from flask import Flask, request,render_template
# IMPORTANT: Added numpy import, which was missing for np.array(data)
import numpy as np 
from WineMl.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Renders the main input form page."""
    return render_template("index.html")

@app.route('/train',methods=['GET'])   # route to train the pipeline
def training():
    """Triggers the training pipeline."""
    # Ensure 'main.py' is runnable from the current environment
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    """Handles wine quality prediction based on POST data."""
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
        
            
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            # Uses the newly imported np (numpy)
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # --- CHANGE START ---
            # Extract the prediction value (a float)
            prediction_value = predict[0]
            
            # Format the prediction to a string with exactly 4 decimal places
            formatted_prediction = f"{prediction_value:.4f}"

            # Renders results.html using the formatted prediction value
            return render_template('results.html', prediction = formatted_prediction) 
            # --- CHANGE END ---

        except Exception as e:
            # Printing the exception to the console helps tremendously in debugging!
            print('The Exception message is: ',e)
            return f'Something went wrong. Check the console for the error details. Error: {e}'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
