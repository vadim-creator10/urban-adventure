import requests
import os
from moviepy.editor import VideoFileClip


def download_video(url=input()):
    try:
        response = requests.get(url=url)
        with open("saved_video.mp4", "wb") as file:
            file.write(response.content)
            print("Success")
            return "Success"

    except Exception as _ex:
        print("Check the URL please")
        return "Check the URL please"


download_video()


def video_to_gif():
    try:
        video_clip = VideoFileClip("saved_video.mp4")
        video_clip.subclip(t_end=3).write_gif("converted_to_gif.gif", fps=6)
        print(os.path.abspath("converted_to_gif.gif"))
        return os.path.abspath("converted_to_gif.gif.gif")
        print ("Success")
        return "Success"

    except Exception as _ex:
        print("Check the video_file please")
        return "Check the video_file please"


video_to_gif()
