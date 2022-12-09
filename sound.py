import pygame, random
import parameters
import thorpy
#Sounds errors are a f*cking pain in the a*s.
class FakeSound(object):

    def play(self):
        pass


class SoundCollection:

    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

    def add(self,filename,name):
        pygame.mixer.init()
        try:
            sound = pygame.mixer.Sound(filename)
            sound.play()
            pygame.mixer.stop()
            print("loaded", filename, name)
        except:
            sound = FakeSound()
            print("couldnt load", filename, name)
        setattr(self, name, sound)


def get_sounds():
    c = SoundCollection()
    c.add("sounds/cannot.wav", "cannot")
    c.add("sounds/ok.wav", "ok")
    c.add("sounds/OpenSurge.ogg", "perigeo")
    c.add("sounds/Screaming-SoundBible.com-1597978996.ogg", "scream")
    c.add("sounds/gong.ogg", "gong")
    return c


m = {}
m["storm"] = "sounds/storm.wav"
m["music1"] = "sounds/music1.ogg"
m["music2"] = "sounds/music2.ogg"
m["music3"] = "sounds/music3.ogg"
m["music4"] = "sounds/music4.ogg"
m["before winter"] = "sounds/music5.ogg"
current = None

def play_random_music():
    play_music("music"+random.choice(["1","2","3","4"]))

def play_music(name, n=0):
    if parameters.MUSIC:
        try:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load(m[name])
            pygame.mixer.music.play(n)
        except:
            pass
