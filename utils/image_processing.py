from PIL import Image

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Load an image and preprocess it into a format expected by the model.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        # Convert to RGB (in case of PNG with alpha etc)
        img = img.convert('RGB')
        # Resize
        img = img.resize(target_size)
        
        # Here we would convert to numpy array and normalize
        # import numpy as np
        # img_array = np.array(img) / 255.0
        # return np.expand_dims(img_array, axis=0) # Add batch dimension
        
        # for our mock, we just return True
        return img
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None
