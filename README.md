# ascii_art

Notes for development:

I'll want to use a monospaced font like Courier
I'm going to want to write a module that enters the output text into an image format that's suitable for generating a gif.

Considering the ImageDraw module of PIL for text to image. It looks like I'll need to start with an image to write to, I'll need to generate a blank white canvas to print the text to. I might consider adding optional arguments for customizing the image dimensions/size.

Image dimensions:
- Perhaps I need to record the dimensions of the original file and then pass those along to text2img. then they can be passed directly to Image.new()
- Considering a class to contain reference to each frame, but maybe this is wasteful because each instance will contain repeated information about dimensions

Considering the imageio library for gif generation.
