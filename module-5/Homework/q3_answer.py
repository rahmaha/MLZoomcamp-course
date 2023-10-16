
import pickle

dv_path = 'D:\MLZoomcamp\module-5\Homework\dv.bin'
model_path = 'D:\MLZoomcamp\module-5\Homework\model1.bin'

#load and read file

def load_file(file):
    with open(file, 'rb') as f_in: 
        return pickle.load(f_in)
    
dv = load_file(dv_path)
model = load_file(model_path)

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

def predict(customer):
    
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
 
    return y_pred

print(predict(customer))