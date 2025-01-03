from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        stream.download(output_path)
        print("Download complete.")
        print(f"Video title: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("YouTube video URL enter : ")
    output_path = input("video save path : ") or '.'
    download_video(url, output_path)

if __name__ == "__main__":
    main()
