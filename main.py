from record import GenAudio
from recognize import recognizer
from turing import turing
from compose import composer
from player import player

ask_path = 'ask.wav'
ask_audio = GenAudio()
ask_audio.read_audio()
ask_audio.save_wav("ask.wav")

reco = recognizer()
ask_txt = reco.recognize(ask_path)
print('Me: '+ ask_txt)

tur = turing()
ans_txt = tur.ask(ask_txt)
print('Robot: '+ ans_txt)

com = composer()
ans_path = com.compose(ans_txt)

play = player()
play.play(ans_path)







