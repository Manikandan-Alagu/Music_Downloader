# Music_Downloader


# YouTube Playlist Audio Downloader

This Python script downloads audio-only streams from a YouTube playlist and saves them as MP3 files in a folder called **Music**. It ensures valid filenames are used, skips downloading files that already exist, and counts how many new songs were downloaded.

---

## Features

- Downloads audio-only streams from a YouTube playlist.
- Saves audio files in MP3 format.
- Skips already downloaded files to avoid duplicates.
- Creates a "Music" folder if it doesn't exist.
- Sanitizes file names to remove invalid characters.
- Displays the total number of songs downloaded at the end of the process.

---

## Requirements

To run this script, you need:

- Python 3.x
- Required libraries:
  - `pytubefix`


You can install the necessary Python packages using the `requirements.txt` file provided.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/playlist-audio-downloader.git
   cd playlist-audio-downloader
   ```

2. **Install required dependencies**:
   Run the following command to install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Script**:
   After installing the dependencies, run the script by typing:

   ```bash
   python downloader.py
   ```

2. **Provide the Playlist URL**:
   When prompted, enter the URL of the YouTube playlist you want to download audio from:

   ```
   url > <paste_your_playlist_url_here>
   ```

3. **Download Process**:
   - The script will check if each file already exists in the **Music** folder.
   - If the file exists, it will skip the download.
   - If the file doesn't exist, it will download the audio as an MP3.

4. **See Download Summary**:
   After all files are processed, the script will print the total number of new songs downloaded.

---

## Example Output

```
url > https://www.youtube.com/playlist?list=EXAMPLE1234
Skipping 'song1.mp3', already downloaded.
Downloading 'song2.mp3'...
Total songs downloaded: 1
```

---

## Folder Structure

Once the script runs successfully, the folder structure will look like this:

```
/path/to/your/project/
│
├── downloader.py
├── requirements.txt
├── README.md
└── Music/
    ├── song1.mp3
    ├── song2.mp3
    └── ... (more downloaded songs)
```

---

## Notes

- The script ensures valid file names by removing invalid characters such as `<>:"/\|?*`.
- MP3 files that are already downloaded will not be downloaded again to avoid duplicates.
- The downloaded audio files will be saved in a folder called **Music**.

---


---

## Contributions

Feel free to submit a pull request if you'd like to contribute!
