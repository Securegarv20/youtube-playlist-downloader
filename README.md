# YouTube Playlist Downloader

This is a simple web application built with Python and Flask for downloading YouTube playlists.

## Features
- Allows users to enter the URL of a YouTube playlist and download all the videos in the playlist.
- Automatically creates a separate directory for each downloaded playlist.
- Downloads the highest available resolution for each video in the playlist.

## How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Access the application in your web browser by visiting `http://localhost:5000`.
5. Enter the URL of the YouTube playlist you want to download and click "Submit".
6. Wait for the download process to complete. Once done, the videos will be available in the `videos` directory.

## Technologies Used
- Python
- Flask
- Pytube (for YouTube video downloading)

## Directory Structure
- `app.py`: The main Flask application file.
- `templates/`: Directory containing the HTML template for the web interface.
- `videos/`: Directory where downloaded videos are stored.

