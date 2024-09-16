import os
from pytubefix import Playlist
import re

def sanitize_filename(name):
    # Remove invalid characters for filenames
    return re.sub(r'[<>:"/\\|?*]', '', name)

script_directory = os.getcwd()
music_directory = os.path.join(script_directory, "Music")
os.makedirs(music_directory, exist_ok=True)

url = input("url > ")
p = Playlist(url)

# Initialize a counter for the number of songs downloaded
downloaded_count = 0

for video in p.videos:
    # Get the title of the video and sanitize it
    file_name = sanitize_filename(video.title) + ".mp3"
    file_path = os.path.join(music_directory, file_name)

    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"Skipping '{file_name}', already downloaded.")
        continue

    # Get the audio-only stream
    ys = video.streams.get_audio_only()

    # Download the audio as an MP3, only if it's not already downloaded
    print(f"Downloading '{file_name}'...")
    ys.download(mp3=True, output_path=music_directory, filename=file_name)

    # Increment the counter
    downloaded_count += 1

# Print the total number of songs downloaded
print(f"Total songs downloaded: {downloaded_count}")
print("All videos processed.")
