# speech-robot
A robot can chat through  voice.(version 1.0) made by apis.

It simplely make a sentence-to-sentence conversion so far.

It will updated in real-time speech-robot.

语音聊天机器人，通过调用api组合而成。

目前只能实现通过单句问答。

后续将会改成实时对话。

### Requirement.
Python 3.0+, Pygame, Pyaudio, wave

### Usage(使用方法)
apply for api_key,secret_key,app_id in baidu voice.

apply for api_key in turing robot.

Write these into config.py, and run main.py.

申请百度语音的api_key,secrek_key,app_id

申请图灵机器人的api_key

将其填写在config文件当中，运行main.py即可。

### instruction（说明）

The chat robot is designed by five components.

这个聊天机器人通过五个组件构成。

####  record.py
This file record the human voice and transfer it into ask.wav to recognize.

记录人声，并且将其保存为ask.wav以便后续的识别。

### recognize.py
This file used baidu speech recognizer to recognize voice.

调用百度语音识别，来识别人声内容。

### chat.py
This file used turing chat-robot to get answer text.

通过图灵机器人获得回答内容文本。


### compose.py
This file make the text into speech and save as ans.mp3 in local.

通过百度语音合成将文本内容合成语音并保存在 ans.mp3.

### play.py
This filere play the ans.mp3, but it has some bugs. 

Python has few modules to play .mp3 on Mac. So I use pygame/mixer.

If you use windows, you can edit this file to get a fluent voice.

播放ans.mp3文件，但是这个有一点问题，python在mac上能够播放MP3的库很少。

这里使用了Pygame的组件来播放，稍微有点失真。

如果你使用windows系统，可以更改这个文件以便获得更流利的发音。
