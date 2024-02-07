import os
import joblib
import numpy as np
from ..processing import preprocessors


# Define the default path to the model.bin file
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MODEL_PATH = os.path.join(MODEL_DIR, 'CCCV_model.bin')

class JobFunClassifier:
    def __init__(self, model_path = None):
        if model_path is None:
            model_path = DEFAULT_MODEL_PATH
        self.model_path = model_path
        self.model = self.load_model()
    
    def load_model(self):
        model = joblib.load(self.model_path)
        return model
    
    def predict(self, text, top = 3):
        text = preprocessors.basic_clean(text)
        y_pred = self.model.predict_proba([text])
        # Round the values in y_pred to 3 decimal places
        y_pred_rounded = np.round(y_pred, 2)
        
        zero_indices = np.where(y_pred_rounded == 0)[1]
        top_indices = np.argsort(y_pred_rounded[0])[::-1][:top]
        # Extract the top 3 categories
        # Filter out the corresponding top categories where all elements in the row are zeros
        top_indices_m = [top_indices[i] for i in range(len(top_indices)) if top_indices[i] not in zero_indices]
        top_categories = self.model.classes_[top_indices_m]
            
        return top_categories.tolist()
