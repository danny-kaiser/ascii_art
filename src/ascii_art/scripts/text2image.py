from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# def draw_multi_line_text(image, text_file, font, text_color, columns):
# with open(text_file) as file:
#     raw_text = file.read()

animation_list = []


def create_image(text_file, columns, rows):
    margin = offset = 10
    spacebetween = 2
    spacebetweennumber = rows - 1
    image_width = columns * 5 + margin * 2
    image_height = rows * 9 + spacebetween * spacebetweennumber + margin * 2

    # loading text file and splitting the string on newlines
    with open(text_file) as file:
        raw_text = file.read()
    lines = raw_text.split("/n")

    # initiating the background image and font
    img = Image.new("1", ((image_width, image_height)), (1))
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("fonts/inconsolata.regular.ttf", 10, encoding="unic")

    # iteratively writing lines to background image
    for line in lines:
        left, right, top, bottom = fnt.getbbox(line)
        draw.text((margin, offset), line, fill="black", font=fnt)
        offset += bottom
    # img.save(outfile)
    return img


def animate_gif(gifpath, columns, rows):
    stringdirectory = "../../strings/"
    stringpathlist = Path(stringdirectory).relative_to(".").rglob("*")
    for path in sorted(stringpathlist):
        animation_list.append(create_image(path, columns, rows))
        path.unlink(missing_ok=False)
    # need to check if the file exists before saving
    animation_list[0].save(
        gifpath,
        save_all=True,
        append_images=animation_list[1:],
        optimize=False,
        duration=40,  # 40 for normal videos, 100 for slowmo
        loop=0,
    )
