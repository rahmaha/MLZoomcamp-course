import pickle
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify

dv_path = 'dv.bin'
model_path = 'model.bin'

# load and read file

def load_file(file):
    with open(file, 'rb') as f_in:
        return pickle.load(f_in)


dv = load_file(dv_path)
model = load_file(model_path)

app = Flask('predict')


@app.route('/predict', methods=['POST'])
def predict():
    diamond = request.get_json()

    X = dv.transform([diamond])

    result = {
        "price_prediction": np.expm1(model.predict(X)).round(0)[0]
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
