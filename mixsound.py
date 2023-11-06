from pydub import AudioSegment
import tkinter as tk
from pydub.playback import play
import time
import threading
import os
# Load the audio files you want to merge
sound1 = AudioSegment.from_file("talking.mp3", format="mp3")
sound2 = AudioSegment.from_file("white.mp3", format="mp3")
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
def choose():
  print("1.GAP\n2.mix sound")
  ch=int(input("choose:"))
  if ch==2:
    merge_aud(sound1,sound2)
  elif ch==1:
    gap_test(sound2)

def merge_aud(s1,s2):
  merged_audio = s1[:8000] + s2[:9000]
  # Export the merged audio to a new file
  merged_audio.export("merged_audio.mp3", format="mp3")
  play(merged_audio)
def gap_test(s1):
  def play_audio_wrapper():
    global start_time
    start_time = time.time()
    play_audio()

  def play_audio():
      part1 = audio[:3000] + 10
      part2 = audio[5000:8000] + 10
      delay = AudioSegment.silent(duration=3000)
      modified_sound = part1 + delay + part2
      play(modified_sound)

  def record_click_time():
      global user_click_time
      user_click_time = time.time() - start_time  # Calculate the time relative to the start time

  # Load your sound file
  audio = s1

  # Create the main window
  root = tk.Tk()
  root.title("Audio Timing Test")

  # Create a button for the user to click
  click_button = tk.Button(root, text="Click when you hear the noise", command=record_click_time)
  click_button.pack()

  # Create a button to play audio
  play_audio_button = tk.Button(root, text="Play audio", command=lambda: threading.Thread(target=play_audio_wrapper).start())
  play_audio_button.pack()

  root.mainloop()
  user_time="{:.1f}".format(user_click_time)
  print("User clicked the button at {} seconds.".format(user_time))
  if (float(user_time)>3.1 and float(user_time)<=6.5):
     print("GOOD JOB PERFECT")
  else:
     print("YOU DIDN'T GET IT")

    
    

choose()