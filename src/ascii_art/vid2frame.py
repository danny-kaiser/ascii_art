import os
import cv2


def framecapture(path, dest="../../frames/"):
    cap = cv2.VideoCapture(path)
    path_to_save = os.path.relpath(dest)

    current_frame = 1
    current_frame_mag = len(str(current_frame))
    current_zeroes = "0" * (4 - current_frame_mag)
    if current_frame_mag > 3:
        print("Error -- video is too long")
        return

    elif cap.isOpened() == False:
        print("Cap is not open")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            name = "frame" + current_zeroes + str(current_frame) + ".jpg"
            print(f"Creating: {name}")
            cv2.imwrite(os.path.join(path_to_save, name), frame)
            current_frame += 1
            current_frame_mag = len(str(current_frame))
            current_zeroes = "0" * (4 - current_frame_mag)
        else:
            break
    cap.release()
    print("done")


# import cv2
#
#
# def framecapture(path):
#     vidobj = cv2.VideoCapture(path)
#     count = 0
#     success = 1
#
#     while success:
#         success, image = vidobj.read()
#         cv2.imwrite("frame%d.jpg" % count, image)
#         count += 1
