import os
import glob
import gtts
from gtts import gTTS
import pandas as pd
from pydub import AudioSegment, audio_segment


def generateSkeleton():
  audio = AudioSegment.from_mp3('Indian-Railways_Announcement.mp3')

  # Part-1 start music
  start = 0000
  finish = 1550
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-1.mp3'), format="mp3")

  # Part-2 kripya dhyan...gadi sankhiya
  start = 1800
  finish = 4150
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-2.mp3'), format="mp3")

  # Part-3 train no and name

  # Part-4 from city

  # Part-5 se chalkar
  start = 8950
  finish = 9750
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-5.mp3'), format="mp3")

  # Part-6 via city

  # Part-7 ke raaste
  start = 11100
  finish = 11850
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-7.mp3'), format="mp3")

  # Part-8 to city

  # Part-9 ko jane wali...platform sankhiya
  start = 12650
  finish = 15850
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-9.mp3'), format="mp3")

  # Part-10 platform no

  # Part-11 par aa rahi hai...end music
  start = 16400
  finish = 19500
  audioProcessed = audio[start:finish]
  audioProcessed.export(os.path.join('temp/', 'Part-11.mp3'), format="mp3")


def textToSpeechHindi(text, filename):
  mytext = str(text)
  language = 'hi'
  myobj = gTTS(text=mytext, lang=language, slow=False)

  myobj.save("temp/" + filename)


def mergeAudios(audios):
  combined = AudioSegment.empty()
  for audio in audios:
    combined += AudioSegment.from_mp3(audio)
  return combined


def generateAnnouncement():
  trainDetails = {
      'Train_Name': "तनव सुपर फास्ट",
      'Train_No': "1 3 0 0 3",
      'From': "Chandigarh",
      'Via': "Ambala Alwar Jaipur",
      'To': "Ajmer",
      'Platform_No': "2"
  }
  print(trainDetails)

  # Part-3 train no and name

  textToSpeechHindi(
      trainDetails['Train_No'] + "  " + trainDetails['Train_Name'],
      'Part-3.mp3')

  # Part-4 from city
  textToSpeechHindi(trainDetails['From'], 'Part-4.mp3')

  # Part-6 via city
  textToSpeechHindi(trainDetails['Via'], 'Part-6.mp3')

  # Part-8 to city
  textToSpeechHindi(trainDetails['To'], 'Part-8.mp3')

  # Part-10 platform no
  textToSpeechHindi(trainDetails['Platform_No'], 'Part-10.mp3')

  audios = []

  for i in range(1, 12):
    audios.append(f"{os.path.join('temp/', 'Part-'+str(i)+'.mp3')}")

  announcement = mergeAudios(audios)
  announcement.export(f"Announcement_{trainDetails['Train_No']}.mp3",
                      format="mp3")


if __name__ == "__main__":
  print("Generating Skeleton...Wait for a while...")
  generateSkeleton()
  print("Skeleton Generated Successfully.")
  print("Generating Announcement...Wait for a while...")
  # make changes is this function
  generateAnnouncement()
  for i in range(1, 12):
    os.remove(os.path.join('temp/', 'Part-' + str(i) + '.mp3'))
  os.makedirs('temp', exist_ok=True)
  print("Announcement Generated Successfully.")
