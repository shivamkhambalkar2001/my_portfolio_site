from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

# -------------------------------
# Image lists for galleries
# -------------------------------
films_songs_images = [
    "logos/logo1.jpg", "logos/logo2.jpg", "logos/logo3.jpg",
    "logos/logo4.jpg"
]

posters_images = [
    "posters/motion1.jpg", "posters/motion2.jpg"
]

motions_images = [
    "motions/graphic1.jpg", "motions/graphic2.jpg"
]

work_skills_images = [
    "work_skills_images/film1.jpg", "work_skills_images/film2.jpg"
]

# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posters")
def posters():
    return render_template("posters.html", images=posters_images)

@app.route("/films_songs")
def films_songs():
    return render_template("films_songs.html", images=films_songs_images)

@app.route("/motions")
def motions():
    return render_template("motions.html", images=motions_images)

@app.route("/work_skills")
def work_skills():
    return render_template("work_skills.html", images=work_skills_images)

# -------------------------------
# Debugging paths
# -------------------------------
print("Current folder:", os.getcwd())
print("Templates folder exists?", os.path.isdir("templates"))
print("Index exists?", os.path.isfile("templates/index.html"))

# -------------------------------
# Run app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
