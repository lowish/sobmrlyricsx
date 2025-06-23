import time, sys
from threading import Thread

lyrics = [
    (0.52, "How can we go back to being friends"),
    (4.10, "When we just shared a bed?"),
    (10.10, "How can you look at me and pretend"),

]

def typewriter(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_lyrics_synced():
    start = time.time()
    for ts, line in lyrics:
        while time.time() - start < ts:
            time.sleep(0.04)
        typewriter(line)



print_lyrics_synced()
