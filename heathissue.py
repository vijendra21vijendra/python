from pygame import mixer
file = 'some.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()