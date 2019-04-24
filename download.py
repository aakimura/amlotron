import youtube_dl
import os
import glob
from datetime import datetime

youtube_url = 'https://www.youtube.com/watch?v=WBc7gNgPw4k'

options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([youtube_url])

cwd = os.getcwd()
files = glob.glob(cwd + '/*.mp3')
latest = max(files, key=os.path.getctime)

# rename file
year = str(datetime.today().year)
month = str(datetime.today().month)
day = str(datetime.today().day)

yy = year[-2:]
mm = month if len(month) > 1 else str(0) + month
dd = year if len(day) > 1 else str(0) + day

today = yy + mm + dd
filename = 'amlo_cm_' + today + '.mp3'
os.rename(latest, 'archive/' + filename)
