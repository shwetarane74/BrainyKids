from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)


# BrainyKids home page
@app.route("/")
def home():
    return render_template("index.html")


# Animal Picture Matching game
@app.route("/animal-matching")
def animal_matching():
    return render_template("animal_matching.html")

# Shape Matching game
@app.route("/shape-matching")
def shape_matching():
    return render_template("shape_matching.html")

@app.route("/cow-farm")
def cow_farm():
    return render_template("cow_farm.html")

@app.route("/picture-puzzles")
def picture_puzzles():
    return render_template("picture_puzzles.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=False, port=5002)