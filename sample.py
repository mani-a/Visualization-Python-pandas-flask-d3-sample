from flask import Flask, jsonify
from flask import render_template
import pandas as pd
import json
app = Flask(__name__)

@app.route('/')
def hello(name=None):
	df = pd.read_csv('bar-data.csv')
	data = df.to_json(orient='records')
	return render_template('index.html',data=data)


 
if __name__ == '__main__':
    app.run(threaded=True,
    host='localhost'
)