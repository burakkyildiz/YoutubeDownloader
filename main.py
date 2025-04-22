from pytubefix import YouTube
from pytubefix.cli import on_progress

video_url = input("please enter video URL: ")
path = '/Users/burakyildiz/Downloads/'
yt = YouTube(video_url, on_progress_callback=on_progress)
print(yt.title)
ys = yt.streams.get_highest_resolution()
ys.download(path)