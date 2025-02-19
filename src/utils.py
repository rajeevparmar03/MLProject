import os
import sys
import dill  
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(x_train,y_train, X_test , y_test,models , params):                                               
    try:
        report = {}        
        for model_name, model in models.items():
            para = params[model_name]

            # Perform Grid Search
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(x_train, y_train)  # Fit the GridSearchCV model

            best_params = gs.best_params_  # Get best parameters after fitting
            model.set_params(**best_params)

            model.fit(x_train, y_train)  # Train model with best parameters

            # Predictions
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(X_test)

            # Evaluate Model
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

        return report
    except Exception as e:
        raise CustomException(e,sys) 

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e :
        CustomException(e ,sys)