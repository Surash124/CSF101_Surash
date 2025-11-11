import time
import sys

def music():
    lyrics = [
        "I don't really give a damn about the way you touch me when we're alone",
        "You can hold my hand if no one's home..",
        "Do you like it when I'm away?",
        "If I went and hurt my body, baby, would you love me the same?",
       " I can feel all my bones coming back, and I'm craving motion"
    ]
    delay = [1.0, 0.11, 1.12, 0.9,0.8, 0.8]

    print("hi")
    time.sleep(1.4)

    for i,line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delay[i])
music()