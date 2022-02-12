import subprocess
import os

done = False

try:
	from pytube import YouTube
	done = True
except:
	try:
		cmd = "pip install git+https://github.com/baxterisme/pytube"
		returned_output = subprocess.check_output(cmd)
		os.system('color 7')
		os.system('cls')
		done = True
	except:
		print("Не удалось установть необходимые модули :(")
		done = False

if done == True:
	if not os.path.isdir("videos"):
	     Fol = os.mkdir("videos")
	os.chdir("videos")
	Dir = os.getcwd()
	video_url = input('Вставьте ссылку видео: ')
	try:
		video_obj = YouTube(video_url)
		stream = video_obj.streams.get_highest_resolution()
		stream.download (Dir)
		print(f'Видео сохранено тут: {Dir}')
	except:
		print("Что-то пошло не так... Возможно вы указали неверную ссылку или на вашем пк отсутствует интернет")
input()