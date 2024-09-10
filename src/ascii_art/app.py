from flask import Flask, render_template
from pathlib import Path
from scripts import vid2frame, frame2text, text2image

app = Flask(__name__)


@app.route("/", methods=[])
def home():
    return render_template("index.html")


@app.route("/api/submit/", methods=["POST", "GET"])
def submit():
    inputname = "baratiddies"  # will be received from frontend
    inputextension = ".mp4"  # will be received from frontend
    outputextension = ".gif"
    column_number_choice = 120  # will be received from frontend, implement error
    # line 51 of frame2text has a print statement for column amount error

    vid2frame.framecapture("../../videos/" + inputname + inputextension)

    framedirectory = "../../frames/"
    framepathlist = Path(framedirectory).relative_to(".").rglob("*")
    for path in sorted(framepathlist):
        newpath = Path("../../strings/" + str(path)[13:-3] + "txt")
        columns, rows = frame2text.convert2ascii(path, newpath, column_number_choice)
        path.unlink(missing_ok=False)
    pass

    text2image.animate_gif(
        "../../gifs/" + inputname + outputextension, columns=columns, rows=rows
    )
