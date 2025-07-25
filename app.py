from flask import Flask, jsonify
from truthbrush import Api
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
api = Api(username="newsalpha", password="98%IQSquad")

@app.route('/trump')
def get_statuses():

    created_after = datetime.now(timezone.utc) - timedelta(hours=5)
    posts = api.pull_statuses("realDonaldTrump", created_after=created_after, verbose=True)
    response_list = []
    for post in posts:
        print(post)
        response_list.append(post)


    return jsonify(response_list)

if __name__ == '__main__':
    app.run(port=5000)