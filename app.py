from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hamidbinameziane'
app.config['UPLOAD_FOLDER'] = 'static/images'




@app.route("/", methods=["GET", "POST"])
def index():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        if os.path.isfile("./static/images/canv.jpg"):
            os.remove("./static/images/canv.jpg")
        filename = secure_filename("canv.jpg")
        file.save(os.path.join(os.path.join(app.config['UPLOAD_FOLDER'], filename)))

    return render_template("index.html")

@app.route("/canv", methods=["GET", "POST"])
def canv():
    return render_template("canv.html")







if __name__ == '__main__':
    app.run(debug=True)
