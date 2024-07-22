from PIL import Image, ImageDraw, ImageFont


def create_image(dimensions, text_file):
    img = Image.new("1", (dimensions), (1))
    draw = ImageDraw.Draw(img)
    # I'll need to reconcile the file size and the font size
    # I need to extract the text from the txt file, line by line
    ascii_font = ImageFont.truetype("fonts/SFMono-Med.otf", 8)
    # not yet sure if black will be (0, 0, 0) or 0
    draw.text((5, 5), text_file, fill="black", font=ascii_font)
    img.show()
    pass
