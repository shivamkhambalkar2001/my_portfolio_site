from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

# -------------------------------
# Image lists for galleries
# -------------------------------
logo_images = [
    "logos/logo1.jpg", "logos/logo2.jpg", "logos/logo3.jpg",
    "logos/logo4.jpg"
]

motion_images = [
    "motion_graphic/motion1.jpg", "motion_graphic/motion2.jpg"
]

graphic_images = [
    "graphic_work/graphic1.jpg", "graphic_work/graphic2.jpg"
]

film_images = [
    "film/film1.jpg", "film/film2.jpg"
]

# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/motion-graphic")
def motion_graphic():
    return render_template("motion_graphic.html", images=motion_images)

@app.route("/logo-design")
def logo_design():
    return render_template("logo_design.html", images=logo_images)

@app.route("/graphic-work")
def graphic_work():
    return render_template("graphic_work.html", images=graphic_images)

@app.route("/film")
def film():
    return render_template("film.html", images=film_images)

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
