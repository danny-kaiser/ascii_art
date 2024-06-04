# ascii_art

Notes:

I'll want to use a monospaced font like Courier
I'm going to want to write a module that enters the output text into an image format that's suitable for generating a gif.

Considering the ImageDraw module of PIL for text to image. It looks like I'll need to start with an image to write to, I'll need to generate a blank white canvas to print the text to. I might consider adding optional arguments for customizing the image dimensions/size.

Image dimensions:
- Perhaps I need to record the dimensions of the original file and then pass those along to text2img. then they can be passed directly to Image.new()
- Considering a class to contain reference to each frame, but maybe this is wasteful because each instance will contain repeated information about dimensions

Considering the imageio library for gif generation.

Downloaded yt-dlp for acquiring videos, it downloaded a low-res version of a video so I'm looking into ffmpeg to see if that was a missing dependency



~~Schematic~~
The current code I appropriated loads an image file, converts it to greyscale, assigns a character, and plugs the text into a txt file.

Before that:

OpenCV extracts frames into a folder called frames. The frames are named sequentially and an error is thrown if the number of frames exceeds 999.

The frames are individually sent to the script that converts them to Ascii. After conversion they are compiled into a gif or a video.
