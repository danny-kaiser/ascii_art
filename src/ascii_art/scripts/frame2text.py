# Python code to convert an image to ASCII image
import sys, random, argparse
import numpy as np
import math
from pathlib import Path

from PIL import Image

# 69 levels of grey
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvuxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of grey
gscale2 = "@%#*+=-:. "


def get_average_grey(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w * h))


def get_ascii(imgfile, outfile, cols, scale=0.43, morelevels=True):
    global gscale1, gscale2

    image = Image.open(imgfile).convert("L")
    W, H = image.size[0], image.size[1]
    w = W / cols  # tile width
    h = w / scale  # tile height
    rows = int(H / h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    if cols > W or rows > H:
        print("Image too small for specified columns")
        exit(0)

    # aimg is a list of strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        # correct last tile
        if j == rows - 1:
            y2 = H

        aimg.append("")
        for i in range(cols):
            # crop image to tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            # correct last tile
            if i == cols - 1:
                x2 = W
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
            # get average luminance
            avg = int(get_average_grey(img))
            # look up ascii characters
            if morelevels:
                gsval = gscale1[int((avg * 68) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            # append ascii char to string
            aimg[j] += gsval
    return aimg, rows


def convert2ascii(imgfile, outfile, cols, scale=0.43, morelevels=True):
    outfile = str(outfile)
    scale = float(scale)
    cols = int(cols)

    file_path = Path(outfile)
    aimg, rows = get_ascii(
        imgfile, outfile, cols
    )  # add more parameters in here if desired
    with file_path.open("w") as f:
        for row in aimg:
            f.write(row + "/n")
    f.close()
    return (cols, rows)
