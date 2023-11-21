from playsound import playsound
import random
import pygame
import time
filename = 'kk.mp3'

#print(f"Playing {filename}..............................")
#playsound(filename)  #play audio
#playsound(filename)



filename = 'kk.mp3'
def play_sound():
    pygame.init()

    # Load the sound file and store it in a variable
    sound = pygame.mixer.Sound(filename)

    # Play the sound
    sound.play()

    # Add a gap of 2 seconds (you can adjust the duration as needed)
    time.sleep(10)
    sound.stop()
    return
    # Pause the sound for the gap duration

    # Add another gap of 2 seconds (you can adjust the duration as needed)

    # Resume the sound

    # Allow time for the sound to finish playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.stop()
    # Quit pygame
    pygame.quit()
def play_gap(n):

    # Initialize pygame
    pygame.init()

    # Load the sound file and store it in a variable
    sound = pygame.mixer.Sound(filename)

    # Play the sound
    sound.play()

    # Add a gap of 2 seconds (you can adjust the duration as needed)
    time.sleep(5)

    # Pause the sound for the gap duration
    pygame.mixer.pause()

    time.sleep(n)

    # Resume the sound
    pygame.mixer.unpause()

    time.sleep(5)

    sound.stop()
    return

#play_sound()
l=[]
g=0.1
while True:
    r = random.randint(0, 2)
    #print(r)
    for i in range(3):

        if i==r:
            play_gap(g)
        else:
            play_sound()
        time.sleep(5)
    k=int(input("Where was the gap"))-1

    if k==r:
        print("You detected correctly")
        g=g-0.02
    else:
        print("Wrong detection")
        g=g+0.02
        l.append(g)

    if len(l)>=5 or g<=0.02:
        break
print(l)