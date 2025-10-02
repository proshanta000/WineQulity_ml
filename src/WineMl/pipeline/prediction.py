import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        # Load the model only once when the class is initialized for efficiency
        # Ensure this path is correct for your project structure
        self.model = joblib.load(Path("artifacts\model_trainer\model.jonlib"))
        
        # Define the class names. IMPORTANT: These must match the order 
        # that Keras/TensorFlow determined during training (alphabetical by folder name).
        self.class_names = ['Coccidiosis', 'Healthy']






    def predict(self, data):
        predict = self.model.predict(data)

        return predict