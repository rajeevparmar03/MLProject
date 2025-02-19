from flask import Flask,request,render_template
import numpy as np
import pandas as pd 
from src.pipelines.predict_pipeline import CustomData,PredictPipeline
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

app= application
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predictdata',methods= ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
          data = CustomData(
               gender=request.form.get('gender'),
               race_ethnicity=request.form.get('race/ethnicity'),
               parental_level_of_education=request.form.get('parental level of education'),

               lunch=request.form.get('lunch'),
               test_preparation_course=request.form.get( 'test preparation course'),
               reading_score= float(request.form.get('reading score')),
               writing_score= float(request.form.get('writing score')),
          )
          pred_df = data.get_data_as_data_frame()
          print(pred_df)

          predict_Pipeline = PredictPipeline()
          results= predict_Pipeline.predict(pred_df)
          return render_template('home.html',results= results[0] )


if __name__ =="__main__":
     app.run(host="127.4.0.0",debug= True )