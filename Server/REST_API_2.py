from flask import Flask, request, json, jsonify
import numpy as np
import tensorflow as tf
import os
import sys

app = Flask(__name__)
 
#---I get this from Mariya Sha so you won't have to use --add-data in pyinstaller---#
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#---The double "\\" is important for pyinstaller---#
# Note: This will still work. Tried it. 
model_path = resource_path('my_model_011323.h5')

#---load the saved model---
loaded_model = tf.keras.models.load_model(model_path)
 
@app.route('/predict', methods=['POST'])
def predict():
    #---get the features to predict---
    # request.json is a dictionary-like object that allows you to access the JSON data sent in the request's body.
    # The json attribute of the request object is used to access the JSON data sent in the request's body.
    features = request.json
 
    #---store the value from the key-value pair--- 
    features_list = features["image"] # extract the "value" of the "key" = image from the client

    #---Assuming that features_list is a list--- 
    input_img = np.array(features_list) # convert the list to numpy array
    input_img = np.expand_dims(input_img, axis=0) #add another bracket -> [input_img]
    input_img = np.vstack([input_img])

    #---get the prediction class---
    prediction = loaded_model.predict(input_img)

    #---json does not handle numpy array---
    output_result = prediction[0].tolist() # convert numpy array to list
 
    #---formulate the response to return to client---
    response = {} # create an empty dictionary
    response['prediction'] = output_result #Create a key-value pair for the dict: "key" = prediction (a string) and "value" = prediction[0]
    
    # returns a key-value pair (a dictionary)
    # response = {"predicton": output_result}
    # output_result is a list of prediction probabilities
    # Serialize it with jsonify is a function in the Flask web framework for Python that is used to convert a Python object
    # into a JSON-formatted response. 
    # Alternative: json.dumps(response)
    return  jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
