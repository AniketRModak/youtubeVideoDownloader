from pytube import YouTube

link = "https://youtu.be/gwm3M_ix6sY"
youtube_video = YouTube(link)
# print(youtube_video.title) # for title video

# print(youtube_video.thumbnail_url)  # for tambailurl

# for quality and video download
videos = youtube_video.streams.all()  # all video  format
# videos = youtube_video.streams.filter(only_audio=True)  # for only aduio
videos = youtube_video.streams.filter(file_extension='mp4')  # for mp4

vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("enter : "))  # enter a array number for quality
# for download
videos[strm].download()
print("successful")

# you can also download playlist