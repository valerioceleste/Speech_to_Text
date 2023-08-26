import requests
from PIL import Image
from io import BytesIO
from pytube import YouTube


def YouTubeURL_converter(URL,filepath):

    yt = YouTube(URL)
    podcast_title = yt.title

    # Save the URL Thumbnail
    response = requests.get(yt.thumbnail_url)
    img = Image.open(BytesIO(response.content))
    img.save(filepath + '/' + podcast_title + '.png',format='png')
    print('...saved YouTube video thumbnail...')

    # Downlaod the audio stream
    stream = yt.streams.get_by_itag(140)
    stream.download(filepath, filename=podcast_title + '.mp3')
    print('saving mp3 file.')

def mp3_file_path(URL,filepath):

    yt = YouTube(URL)
    podcast_title = yt.title
    return f"{filepath}/{podcast_title}.mp3"