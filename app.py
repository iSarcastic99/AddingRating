import numpy as np
from flask import Flask, request, jsonify, render_template
from ratingUpd import addRate

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def addRating():
    jobId = request.form['jobID']
    userId = request.form['userId']
    rating = request.form['rating']
    print(userId," ", jobId," ", rating)
    status = addRate(userId, jobId, rating)

    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)