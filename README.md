# YouTube Music Playlist Downloader

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Required-red)

A Python script to **download YouTube Music playlists** directly from a playlist link.  

- Downloads **high-quality MP3 audio**  
- Embeds **metadata** (artist, album, description)  
- Embeds **high-resolution album art**  
- **Skips already downloaded songs**  
- Shows **progress per song** and a **final summary**  
- Everything runs locally on your system, **no restrictions or accounts required**

---

## Features

- Clean filenames and folder structure  
- Supports **YouTube Music playlist URLs**  
- Handles songs with missing videos gracefully  
- Automatically organizes songs into playlist folders  

---

## Requirements

- Python 3.10+ (or compatible)  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org/)  
- [ytmusicapi](https://github.com/sigma67/ytmusicapi)  

---

## Installation / Setup

### MacOS Users 🍎

1. **Install Homebrew** (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install dependencies:

bash
Copy code
brew install ffmpeg yt-dlp
Add yt-dlp to PATH (if installed via pip):

bash
Copy code
nano ~/.zshrc
# Add the line at the end:
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
# Save and reload shell
source ~/.zshrc
Install ytmusicapi:

bash
Copy code
brew install pipx
pipx install ytmusicapi
Windows Users 💻
Install Python 3.10+ from python.org

Install dependencies via pip:

powershell
Copy code
pip install yt-dlp ytmusicapi
Install FFmpeg

Download from FFmpeg website

Add bin folder to System PATH

Tip: Open PowerShell and run ffmpeg -version to verify installation

Linux Users 🐧
Install dependencies via package manager:

Ubuntu/Debian:

bash
Copy code
sudo apt update
sudo apt install ffmpeg python3-pip
pip3 install --user yt-dlp ytmusicapi
Fedora/CentOS:

bash
Copy code
sudo dnf install ffmpeg python3-pip
pip3 install --user yt-dlp ytmusicapi
Verify installation:

bash
Copy code
ffmpeg -version
yt-dlp --version
python3 -m pip show ytmusicapi
Usage
Create project folder and Python script:

bash
Copy code
mkdir ytmusic_downloader
cd ytmusic_downloader
nano ytmusic_downloader.py
Paste your final Python code into the file.

Save (CTRL + O) and exit (CTRL + X).

Run the script with a playlist URL:

bash
Copy code
python3 ytmusic_downloader.py "<YouTube Music Playlist URL>"
Example:

bash
Copy code
python3 ytmusic_downloader.py "https://music.youtube.com/playlist?list=PLQNp-BCxMEnIeSoWfDbZXzJURVnItRyBz"
Songs will be saved in DownloadedMusic folder, organized by playlist.

Troubleshooting & Notes
Use Python 3.10+ to avoid deprecation warnings.

Only playlist URLs are supported; profile/channel URLs are not.

Special characters in video titles are sanitized automatically.

Already downloaded songs are skipped; deleted songs can be re-downloaded.

Script shows progress [current / total] for downloading, skipped, or missing songs.

High-resolution album art is embedded automatically.

At the end, a summary is displayed with: total songs, downloaded this run, already in folder, skipped (no video found).

License
MIT License © Sumit Kumar

If you have any issue or comments, please leave a comment, I will try to resolve it as soon as possible.

yaml
Copy code

---

I can also **package this into a zip with your placeholder Python script** ready for GitHub if you want, so you can upload it directly. Do you want me to do that?
