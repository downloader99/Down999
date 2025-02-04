from flask import Flask, request, render_template
import downloader
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    if url:
        downloader.download(url)
        return "Download started!"
    return "Please provide a valid URL."

if __name__ == '__main__':
    app.run(debug=True)
