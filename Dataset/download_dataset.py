import os
import shutil
import pandas as pd
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

df = pd.read_csv("Dataset.csv")
count = {}

for i in range(0,len(df)):
    folder_name = df['label'][i]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    link = "https://www.youtube.com/watch?v="+df['youtube_id'][i]
    try:
        yt = YouTube(link)
        yt.streams.first().download()
    
        current_title = yt.title + ".mp4"
        if folder_name not in count:
            count[folder_name] = 0
    
        count[folder_name]+=1
        new_title = folder_name + "_" + str(count[folder_name]) + ".mp4"
        ffmpeg_extract_subclip(current_title, df["time_start"][i], df["time_end"][i], targetname= new_title)
    
        path = folder_name+"/"
        shutil.move(new_title, path)
        os.remove(current_title)
    
    except:
        pass
            
