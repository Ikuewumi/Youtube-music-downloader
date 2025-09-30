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
- Everything runs locally on your system, **no restrictions**

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

## Installation (macOS)

1. **Install Homebrew** (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Install dependencies**:

```bash
brew install ffmpeg yt-dlp
```

3. **Add yt-dlp to PATH (if installed via pip)**

If `yt-dlp` is not found after installation:

```bash
nano ~/.zshrc
```

Add this line at the end:

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

Save and exit (`CTRL + O`, `ENTER`, `CTRL + X`) and reload shell:

```bash
source ~/.zshrc
```

Test:

```bash
yt-dlp --version
```

4. **Install ytmusicapi**:

```bash
brew install pipx
pipx install ytmusicapi
```

---

## Usage

1. Create project folder and Python script:

```bash
mkdir ytmusic_downloader
cd ytmusic_downloader
nano ytmusic_downloader.py
```

- Paste your final Python code into the file.  
- Save (`CTRL + O`) and exit (`CTRL + X`).  

2. Run the script with a playlist URL:

```bash
python3 ytmusic_downloader.py "<YouTube Music Playlist URL>"
```

Example:

```bash
python3 ytmusic_downloader.py "https://music.youtube.com/playlist?list=PLQNp-BCxMEnIeSoWfDbZXzJURVnItRyBz"
```

3. Songs will be saved in `DownloadedMusic` folder, organized by playlist.  

---

## Troubleshooting & Setup Notes

- Use Python 3.10+ to avoid deprecation warnings.  
- Only **playlist URLs** are supported; profile/channel URLs are not.  
- Special characters in video titles are sanitized automatically.  
- Already downloaded songs are skipped; deleted songs can be re-downloaded.  
- Script shows progress `[current / total]` for downloading, skipped, or missing songs.  
- High-resolution album art is embedded automatically.  
- At the end, a summary is displayed with: total songs, downloaded this run, already in folder, skipped (no video found).  

---
If you have any issue or comments, please leave a comment, i will try to resolve it as soon as possible.
---

## License

MIT License © Sumit Kumar
