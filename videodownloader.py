from pytube import YouTube

url = 'https://www.youtube.com/watch?v=2v0rWuNtOoE'

try:
	youtube = YouTube(url)
except KeyError:
	print("Fail to download video try again.")

print(youtube.title)
print(youtube.description)
print(youtube.age_restricted)
print(youtube.vid_info)
print(youtube.captions)
print(youtube.embed_url)
print(youtube.fmt_streams)
print(youtube.thumbnail_url)

input()