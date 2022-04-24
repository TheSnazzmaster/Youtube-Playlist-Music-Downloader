import pytube  # library for downloading youtube videos
import os

#these are the two variables that will change with playlist and destination
url = "https://youtube.com/playlist?list=PLbasGLcW7rPMksTxyJ8eKd--8jx6YKqOD"
destination = '\\bungus\\'



links = []
def exact_link(link):
	vid_id = link.split('=')
	str = ""
	for i in vid_id[0:2]:
		str += i + "="

	str_new = str[0:len(str) - 1]
	index = str_new.find("&")

	new_link = "https://www.youtube.com" + str_new[0:index]
	return new_link
links = pytube.Playlist(url)
count = 1
for link in links:
	yt = pytube.YouTube(
		str(link))
	videoTitleButEpic = yt.title#.encode("ascii","ignore").decode()#.replace(":","").replace("'","").replace("/","")\
		# .replace(".","").replace("?","").replace("#","").replace("'","").replace("")
	keepcharacters = (' ', '-', '_',"【","】",")","(","[","]")
	videoTitleButEpic = "".join(c for c in videoTitleButEpic if c.isalnum() or c in keepcharacters).rstrip()
	file_exists = os.path.isfile(destination+videoTitleButEpic+".mp3")
	if not file_exists:
		video = yt.streams.get_audio_only()
		out_file = video.download(output_path=destination
								  ,filename=videoTitleButEpic
								  )
		try:
			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)
		except:
			print("there is an imposter among us")
		print(yt.title + " has been successfully downloaded.")
	else:
		print("already downloaded " + yt.title)
	count+=1
