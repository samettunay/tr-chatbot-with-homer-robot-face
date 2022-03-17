import os
import time 
from gtts import gTTS
from nltk.chat.util import Chat

tr_pairs = [
    ['benim adım (.*)', ['merhaba %1']],
    ['(.*)adın (ne|nedir)?',['benim adım RobOtizm']],
    [('merhaba|meraba|hey|hay'),['merhaba','heeey','naaber']],
    ['(.*) eğlenceli bir yer',['%1 gerçekten de çok eğlenceli bir yer']],
    ['(.) (.) oldukça (.*)',['%1 %2 gerçekten de çok %3']],
    ['bitti',['']],
    ['(.*)nerede yaşıyorsun?',['Şuanlık bu bilgisayar\'da yaşıyorum.']],
    ['(.*)nerelisin?',['ben bir sohbet botuyum. doğum yerim yok.']],
    ['(.*)kaç yaşındasın ?',['ben bir sohbet botuyum. doğum yerim yok.']],
    ['(.*)hava nasıl ?',['her zamanki gibi. bir değişiklik yok!']],
    ['(.*)nasılsın ?',['ben çok iyiyim. sen nasılsın?']],
    ['(.*)yardım eder misin?',['elbette yardım ederim.']],
    ['boyun kaç?',['ben bir bot olduğum için boyum tanımsız.']],
    ['kimsin lan sen?',['senin abin benim lan']],
    ['(.*)merhaba de', ['Merhaba Egecim Nasılsın']]

]
 
tr_reflections = {
    'nasılsın':'iyiyim',
    'ben':'sen',
    'benim':'senin',
    'benimki':'seninki'
}

chat = Chat(tr_pairs, tr_reflections)

def save_audio(audio_string):
    try:
        tts = gTTS(audio_string, lang="tr")
        audioFile = "gtts.mp3"
        tts.save(audioFile)
        #os.remove(audioFile)
    except AssertionError:
        1


# orijinal İngilizce reflections içeriği
# print(reflections)
"""
os.system("gnome-terminal -- roscore")
time.sleep(3) 
os.system("gnome-terminal -- rosrun homer_robot_face RobotFace")
time.sleep(3)
"""

while True:
    metin = chat.converse(quit='tamam')
    save_audio(metin)
    if metin != None :
        komut1 = 'rostopic pub -1 /robot_face/text_out std_msgs/String "' + "." + " " + metin + '"'
        komut2 = 'rostopic pub -1 /robot_face/talking_finished std_msgs/String "' + "." + '"'
        komut3 = 'sleep 0.5s'
        komut4 = 'play gtts.mp3 -q'
        komut = komut1 + "&\n" + komut3 + "\n" + komut4 + " &\n" + komut2
        os.system(komut)
    elif metin == None:
        metin = "Kelimenin karşılığını henüz öğrenmedim"
        save_audio(metin)
        komut1 = 'rostopic pub -1 /robot_face/text_out std_msgs/String "' + "." + " " + metin + '"'
        komut2 = 'rostopic pub -1 /robot_face/talking_finished std_msgs/String "' + "." + '"'
        komut3 = 'sleep 0.5s'
        komut4 = 'play gtts.mp3 -q'
        komut = komut1 + "&\n" + komut3 + "\n" + komut4 + " &\n" + komut2
        os.system(komut)
