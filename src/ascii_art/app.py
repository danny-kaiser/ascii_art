from flask import Flask

app = Flask(__name__)


@app.route("/api/submit/", methods=["POST", "GET"])
def submit():
    # might need to create directories for writing files into
    # receives a video file, maybe also some paramaters like columns and scale
    # registers the file dimensions to a variable
    # calls vid2frame
    # sends each extracted frame to frame2text.main(...)
    # outfile will be ../../strings/outfile_name.txt
    # frame2text.main(...) returns tuple (cols, rows) for each string
    # each tuple is compared to a variable, if dims change an error is thrown
    # sends each string to text2image
    # calls image2vid
    return "<p>Submission</p>"
