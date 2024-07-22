from flask import Flask
from pathlib import Path
from scripts import text2image, frame2text

app = Flask(__name__)


@app.route("/api/submit/", methods=["POST", "GET"])
def submit():
    # might need to create directories for writing files into
    # receives a video file, maybe also some paramaters like columns and scale
    # registers the file dimensions to a variable
    # calls vid2frame
    # sends each extracted frame to frame2text.main(...)
    # frame2text.main(...) returns tuple (cols, rows) for each string
    # outfile will be ../../strings/outfile_name.txt
    # each tuple is compared to a variable, if dims change an error is thrown
    # the columns and rows will be used to determine the size of the next image
    # I'll start with 6pt font, the image will be sized accordingly
    # sends each string to text2image
    # calls image2vid
    return "<p>Submission</p>"


text2image.create_image((600, 600), "../../strings/punterstring.txt")
