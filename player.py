
#coding=utf-8
 
import pyaudio
import wave
import time
from pygame import mixer # Load the required library
class player():

	def __init__(self):
		
		pass

	def play(self,path = 'ans.mp3'):

		

		mixer.init()
		mixer.music.load(path)
		
		mixer.music.play()
		time.sleep(10)
		mixer.music.stop()


		# #define stream chunk 
		# chunk = 1024

		# #open a wav format music
		# f = wave.open(path,"rb")
		# #instantiate PyAudio
		# p = pyaudio.PyAudio()
		# #open stream
		# stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
		# 				channels = f.getnchannels(),
		# 				rate = f.getframerate(),
		# 				output = True)
		# #read data
		# data = f.readframes(chunk)

		# #paly stream
		# while data != '':
		# 	stream.write(data)
		# 	data = f.readframes(chunk)

		# #stop stream
		# stream.stop_stream()
		# stream.close()

		# #close PyAudio
		# p.terminate()
if __name__== '__main__':
	a = player()
	a.play()