from __future__ import unicode_literals
import youtube_dl

def download_file(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url, download=False)
    filename = f'{video_info["title"]}.mp3'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_info["webpage_url"]])
    print('Download complete... {}'.format(filename))


def main():
    df1 = download_file('https://youtu.be/NB0RRdXSqeQ?t=4')

if __name__ == '__main__':
    main()

