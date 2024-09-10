# ascii_art

Next up:

I want to sketch out the flow for the html requests

I want to make sure that my script checks for the necessary directories and makes them if missing. I think that was throwing errors when writing a new file in frame2text.

text2image is now set up to neatly format text for a particular font at a particular size, it might be nice to make it universal by using the tool that I checked the size with. but I fudged the amount of space between rows, I think I arbitrarily found 2 to be the correct amount to add in for each(?) line.

I'm ready to set up the frontend and reach the point where I can upload videos through it. 

Notes:

I'll want to use a monospaced font

I'm going to want to write a module that enters the output text into an image format that's suitable for generating a gif.

Considering the ImageDraw module of PIL for text to image. It looks like I'll need to start with an image to write to, I'll need to generate a blank white canvas to print the text to. I might consider adding optional arguments for customizing the image dimensions/size.

Image dimensions:
- Perhaps I need to record the dimensions of the original file and then pass those along to text2img. then they can be passed directly to Image.new()
- Considering a class to contain reference to each frame, but maybe this is wasteful because each instance will contain repeated information about dimensions

Considering the imageio library for gif generation.

Downloaded yt-dlp for acquiring videos, it downloaded a low-res version of a video so I'm looking into ffmpeg to see if that was a missing dependency

The conversion script needs to be updated to output image files. It seems like gif should be perfect for greyscale. 

_Schematic_

Flask will be used to create an API for these functions, then JS for the front-end. app.py is the hub for html requests. The next step is deciding which requests will come from the frontend and how they will trigger the cascade of conversion scripts.

vid2frame - OpenCV extracts frames into a folder called frames. The frames are named sequentially and an error is thrown if the number of frames exceeds 999.

frame2text - An image is loaded and it is converted to greyscale. Its dimensions are stored and it is divided into tiles based on the number of columns specified. A list is initialized and each row of tiles is represented as a subsequent string of characters in that list. The function returns the list. Might need to tweak the parameters or offer them as options in the UI.

text2image - Using PIL to initiate an image. The MODE for black and white will be "1" and the SIZE will be a tuple of integers inherited from the size of the video input. Or perhaps SIZE will be inherited from the amount of space that the characters will take up. Let's try 6px per row/column.

image2vid - compiles images into a video

frontend - I might initiate text at (0, 0) on my images, so I might want to add padding to the file in JS

NOTE - tile height is determined by applying the image scale to the tile height. perhaps I'll add a scale option to the UI so I can play with it and decide if there's a setting that optimized for monospaced fonts like courier. 
