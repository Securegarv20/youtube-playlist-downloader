from flask import Flask, request, render_template
from pytube import Playlist
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/playlistdownload', methods=['POST'])
def download_playlist_route():
    try:
        playlist_url = request.form.get('playlist_url')
        if playlist_url:
            videos = download_playlist(playlist_url)
            if videos:
                return f"Playlist downloaded successfully: {videos}"
            else:
                return "Failed to download the playlist."
        else:
            return "Playlist URL is required."
    except Exception as e:
        print(e)
        return "Some Error Happened, Contact Developer!"

def download_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist_name = playlist.title
        playlist_videos = []
        # Create a folder for the playlist
        folder_name = playlist_name.replace(' ', '_')  # Replace spaces with underscores
        folder_path = os.path.join('videos', folder_name)
        os.makedirs(folder_path, exist_ok=True)
        # Download each video in the playlist
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=folder_path)
            playlist_videos.append(video.title)
        return playlist_videos
    except Exception as e:
        print(f"Error downloading playlist: {e}")
        return None

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
