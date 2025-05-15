from db.liveDB import init_db,getMovies,getMoviesTop
from utils.csvUtils import createFile, loadRating
from flask import Flask, jsonify

#Simulate The description on the Home assingment
createFile() # Create the file mention in the example
init_db(loadRating()) #  this would be a postgress connection

#Start the app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message="server is running, Read the README file for description of the project")

@app.route('/csvratings', methods=['GET'])
def csvRating():
    return jsonify(loadRating())

@app.route('/dbratings', methods=['GET'])
def dbRatings():
    return jsonify(getMovies())

@app.route('/top', methods=['GET'])
def top():
    return jsonify(getMoviesTop())

if __name__ == "__main__":
    # Runs on http://127.0.0.1:5000/ by default
    app.run(debug=True)
