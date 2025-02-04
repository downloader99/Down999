from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

def download_video(url):
    ydl_opts = {
        'outtmpl': './downloads/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        download_video(url)
        return f"Video is being downloaded from {url}!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
