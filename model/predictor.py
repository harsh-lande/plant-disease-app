import time
import random
import os

class PlantPredictor:
    def __init__(self, model_path="plant_model.h5"):
        self.model_path = model_path
        self._load_model()
        self.classes = ['Healthy', 'Early Blight', 'Late Blight']

    def _load_model(self):
        # Stub: normally you would do `from tensorflow.keras.models import load_model` here
        # and `self.model = load_model(self.model_path)`
        print(f"Mock Loading model from {self.model_path}")
        pass

    def predict(self, image_array):
        # Stub: normally you would do `self.model.predict(image_array)`
        # We simulate inference time and return a random mock prediction
        time.sleep(1.5)
        
        disease = random.choice(self.classes)
        confidence = round(random.uniform(70.0, 99.9), 2)
        
        return disease, confidence
