import time
import pygame
import os

print("\n")
print("Happy Valentine's Day, My Love!\n")
print("With all my love,\n")

lyrics = [
    ("00:00:00", ""),
    ("00:12.90", "0.748 I've 0.616 never 0.784 known 0.952 someone 0.504 like 1.4 you, 0.504 ooh"),
    ("00:19.17", "0.752 Tangled 0.292 in 0.904 love, 0.348 stuck 0.348 by 1.404 you, 0.404 from 0.348 the 0.404 glue"),
    ("00:25.52", "0.752 Don't 0.348 forget 0.292 to 0.348 kiss 0.404 me"),
    ("00:28.20", "0.752 Or 0.404 else 0.348 you'll 0.404 have 0.292 to 0.348 miss 0.404 me"),
    ("00:31.26", "0.404 I 0.404 guess 0.348 I'm 0.904 stuck 0.904 forever"),
    ("00:34.55", "0.348 by 0.292 the 0.46 glue, 0.348 oh, 0.348 and 1.168 you"),
    ("00:37.00", "0.952 Mm-mm"),
    ("00:39.00", "0.952 Mm-mm-mm"),
    ("00:41.00", "0.952 Mm-mm"),
    ("00:50.77", "1.252 Finding 0.392 the 0.684 right 0.66 words 0.448 to 0.504 use 0.448 for 0.448 this 0.56 song"),
    ("00:56.84", "0.448 I 0.504 have 0.504 you 0.392 in 0.56 mind"),
    ("00:59.05", "0.752 So 0.392 it 0.56 won't 0.504 take 0.348 so 1.512 long"),
    ("01:03.38", "0.788 Never 0.56 thought 0.448 I'd 0.504 find 0.504 you"),
    ("01:06.01", "0.448 But 0.504 you're 0.56 here"),
    ("01:07.83", "0.448 And 0.448 so 0.448 I 0.204 love 0.504 you"),
    ("01:09.25", "0.552 I'm not wrong"),
    ("01:10.88", "0.552 when 0.448 I 0.504 say"),
    ("01:13.00", "0.504 I've 0.92 been 0.56 stuck 0.448 by 0.34 glue 0.74 onto 2.24 you"),
    ("01:20.25", "0.504 I've 0.504 been 0.504 stuck 0.448 by 2.8 glue"),
    ("01:27.12", "0.448 Right 0.948 onto 3.92 you"),
    ("01:32.00", "0.504 I've 0.504 been 0.504 stuck 0.948 by 3.36 glue"),
    ("01:41.25", "0.504 I've 1.0 never 1.4 known"),
    ("01:47.66", "0.504 I've 1.0 never 0.56 known 0.66 someone 0.504 like 1.96 you, 0.504 ooh"),
    ("01:53.90", "0.504 I've 1.0 never 1.4 known"),
    ("02:00.30", "0.504 I've 1.0 never 0.56 known 0.66 someone 0.504 like 1.96 you, 0.504 ooh")
]

def timestamp_to_seconds(timestamp):
    """Convert HH:MM:SS.ms or MM:SS.ms format to seconds"""
    parts = timestamp.split(":")
    if len(parts) == 2:  # MM:SS.ms format
        minutes, seconds = map(float, parts)
        return minutes * 60 + seconds
    elif len(parts) == 3:  # HH:MM:SS.ms format (if applicable)
        hours, minutes, seconds = map(float, parts)
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError(f"Invalid timestamp format: {timestamp}")

def play_music(music_file, start_pos=0.0):
    """Plays the specified music file in the background from a given start position."""
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(start=start_pos)

music_file = "song/beabadoobee - Glue Song (Official Music Video).mp3"  # Replace with your music file path

# Set the start time to 01:25.25
start_minutes = 0
start_seconds = 0.0
start_seconds_total = start_minutes * 60 + start_seconds

play_music(music_file, start_seconds_total)

start_time = time.time() - start_seconds_total  # Adjust start_time

for timestamp, line in lyrics:
    target_time = timestamp_to_seconds(timestamp)
    current_time = time.time() - start_time

    # Skip lyrics until we reach the start time
    if target_time < start_seconds_total:
        continue

    # Wait until the correct timestamp is reached
    if target_time > current_time:
        time.sleep(target_time - current_time)

    words = line.split()

    i = 0
    while i < len(words):
        try:
            delay = float(words[i])
            word = words[i + 1]
            print(word, end=" ", flush=True)
            time.sleep(delay)
            i += 2
        except (ValueError, IndexError):
            i += 1

    print()  # Move to the next line for the next lyrics

while pygame.mixer.music.get_busy():
    time.sleep(1)
