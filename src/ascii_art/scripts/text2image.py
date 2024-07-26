from PIL import Image, ImageDraw, ImageFont
import textwrap

# def draw_multi_line_text(image, text_file, font, text_color, columns):
# with open(text_file) as file:
#     raw_text = file.read()


def create_image(text_file, columns, rows):
    margin = offset = 10
    spacebetween = 2
    spacesbetween = rows - 1
    image_width = columns * 5 + margin * 2
    image_height = rows * 9 + spacebetween * spacesbetween + margin * 2

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
        width, height = fnt.getsize(line)
        draw.text((margin, offset), line, fill="black", font=fnt)
        offset += height
    img.show()
    pass
