from PIL import Image, ImageDraw, ImageFont


def create_image(dimensions):
    img = Image.new("1", (dimensions), (1))
    draw = ImageDraw.Draw(img)
    # not sure if my font filepath should be relative to app.py or this script
    # I'll need to reconcile the file size and the font size
    font = ImageFont.truetype("fonts/SFMono-Med.otf", 8)
    # not yet sure if black will be (0, 0, 0) or 0
    # draw.text((0, 0), text_file, (0, 0, 0), font=font)
    img.show()
    pass
