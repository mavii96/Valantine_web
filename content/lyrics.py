# -*- coding: utf-8 -*-
import time
import sys


def type_lyric(line, speed=0.15):
    """Print each word slowly, like typing effect"""
    for word in line.split():
        for char in word:
            print(char, end='', flush=True)
            time.sleep(speed / 2)  # smaller delay between letters
        print(' ', end='', flush=True)
        time.sleep(speed)
    print()  

print("Music Credit to : Pamith Mandiv")
print("\nOba Kage Kawrundoo Lyrics 🎶:")

def print_lyrics():
    lyrics = [
        "Oba Kage Kawrundhooo ",
        "Mata Nadhdha Pembandhoo",
        "Hara Yanne Sithakindhooo", 
        "Man Soyanawaa Adareee Danuna Thanak.........!",
        
       
    ]

    delays = [1.4,1.2,1.1,5]  
    
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()