from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Rating',methods=['POST'])

def addRating():
    isThere = False

    df1 = pd.read_csv('rating.csv')
    dfjson = df1.to_json(r'./endgameRating.json')
    jobId = request.form['jobId']
    userId = request.form['userId']
    rating = request.form['rating']
    print(userId, " ", jobId, " ", rating)


    try:
        userFloat = float(userId)
        jobFloat = float(jobId)
        ratingFloat = float(rating)
        print(userFloat, jobFloat, ratingFloat)

        if (0 > ratingFloat or ratingFloat > 10):
            invalid = "invalid"
            return invalid

    except ValueError:
        error = "error"
        return error

    for index, row in df1.iterrows():
        print(row['userID'], row['jobID'])
        if str(row['jobID']) == str(jobId) and str(row['userID']) == str(userId):
            row['rating'] = rating
            isThere = True

        # Creating the Second Dataframe using dictionary

    if isThere != True:
        df2 = pd.DataFrame({"userID": [userId],
                            "jobID": [jobId],
                            "rating": [rating]})

        dff = df1.append(df2, ignore_index=True)
        dff.to_csv(r'./rating.csv', index=False)
        added = "added"
        return render_template('index.html', DataStored="The rating has been stored")

    else:

        df1.to_csv(r'./rating.csv', index=False)
        updated = "updated"
        return updated


    return render_template('index.html', DataStored="The rating has been stored")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)