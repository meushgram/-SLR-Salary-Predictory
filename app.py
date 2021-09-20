import pickle
import pandas as pd
from flask import Flask, render_template
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    newdata = pd.Series([200, 300])
    data_pred = pd.DataFrame(newdata, columns=['YearsExperience'])
    model = pickle.load(open('model-SLR','rb'))
    print(model.predict(data_pred))
    return render_template('hello.html')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()