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

3. **Install ytmusicapi**:

```bash
python3 -m pip install --break-system-packages ytmusicapi
```

---

## Usage

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Run the script with a playlist URL:

```bash
python3 ytmusic_downloader.py "<YouTube Music Playlist URL>"
```

Example:

```bash
python3 ytmusic_downloader.py "https://music.youtube.com/playlist?list=PLQNp-BCxMEnIeSoWfDbZXzJURVnItRyBz"
```

3. Your songs will be saved in the `DownloadedMusic` folder, organized by playlist.

---

## Output

During download, the script shows progress:

```
[  5 / 114] Downloading: Maruti
[  6 / 114] Already exists, skipping: Laado
[  7 / 114] ⚠️ No video found, skipping: Inspire
```

After completion, a summary is displayed:

```
✅ Playlist download completed!
Playlist: Haryanvi
Total songs in playlist: 114
Downloaded this run: 110
Already in folder: 3
Skipped (no video found): 1
Total skipped: 4
```

---

## Notes

- Only **playlist URLs** are supported. Channel/profile URLs are not supported.  
- Skipped songs either **already exist** or **have no downloadable video**.  
- Ensure `yt-dlp` and `FFmpeg` are installed and in your PATH.  

---

## License

MIT License © Sumit Kumar
