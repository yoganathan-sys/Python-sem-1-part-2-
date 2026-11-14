import yt_dlp

def download_video(url):
    # Options for the download
    ydl_opts = {
        'format': 'best',  # Download the best quality video+audio combined
        'outtmpl': '%(title)s.%(ext)s',  # Name the file using the video title
        'quiet': False,    # Print download progress to console
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace this string with your YouTube URL
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
