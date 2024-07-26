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
    # textwrap will help format text to image
    # I found a stackoverflow post with a script to measure the image and text
    # sends each string to text2image
    # calls image2vid
    return "<p>Submission</p>"


# columns, rows = frame2text.convert2ascii(
#     "../../images/punter.jpg", "../../strings/punterstring.txt"
# )

text2image.create_image("../../strings/punterstring.txt", columns=80, rows=45)
