import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': './downloads/%(title)s.%(ext)s',  # Saves videos to a folder called 'downloads'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the xHamster video URL: ")
    download_video(video_url)
