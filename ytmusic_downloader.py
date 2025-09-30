import os
import re
import sys
from ytmusicapi import YTMusic
import subprocess

def sanitize_name(name: str) -> str:
    """Make safe folder/filename."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def download_playlist(playlist_url: str, base_dir="DownloadedMusic"):
    """Download all songs from a YouTube Music playlist with proper titles, metadata, and high-res album art."""
    print(f"\n=== Downloading playlist: {playlist_url} ===")

    ytmusic = YTMusic()
    playlist_id = playlist_url.split("list=")[-1].split("&")[0]
    playlist = ytmusic.get_playlist(playlist_id, limit=None)

    playlist_name = sanitize_name(playlist['title'])
    playlist_folder = os.path.join(base_dir, playlist_name)
    os.makedirs(playlist_folder, exist_ok=True)

    tracks = playlist['tracks']
    total_songs = len(tracks)

    downloaded_count = 0
    already_present_count = 0
    no_video_count = 0

    for idx, track in enumerate(tracks, start=1):
        song_title = sanitize_name(track['title'])
        file_path = os.path.join(playlist_folder, f"{song_title}.mp3")

        if os.path.exists(file_path):
            print(f"[{idx:3d} / {total_songs}] Already exists, skipping: {song_title}")
            already_present_count += 1
            continue

        video_id = track.get('videoId')
        if not video_id:
            print(f"[{idx:3d} / {total_songs}] ⚠️ No video found, skipping: {song_title}")
            no_video_count += 1
            continue

        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"[{idx:3d} / {total_songs}] Downloading: {song_title}")

        command_download = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--add-metadata",
            "--embed-metadata",
            "--embed-thumbnail",
            "-o", os.path.join(playlist_folder, "%(title)s.%(ext)s"),
            video_url
        ]
        subprocess.run(command_download)
        downloaded_count += 1

    skipped_total = already_present_count + no_video_count

    # Final summary
    print("\n✅ Playlist download completed!")
    print(f"Playlist: {playlist_name}")
    print(f"Total songs in playlist: {total_songs}")
    print(f"Downloaded this run: {downloaded_count}")
    print(f"Already in folder: {already_present_count}")
    print(f"Skipped (no video found): {no_video_count}")
    print(f"Total skipped: {skipped_total}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ytmusic_downloader.py <playlist-url>")
        sys.exit(1)

    link = sys.argv[1]

    if "playlist?list=" in link:
        download_playlist(link)
    else:
        print("❌ Unsupported link type. Provide a YouTube Music playlist URL.")

if __name__ == "__main__":
    main()
