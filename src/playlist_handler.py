#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 13:55:59 2025

@author: mortivarus
"""
import json_handler as jh
import subprocess

playlists_folder = "../playlists/"
downloads_folder = "../downloads/"
playlist = "Electronic"

data = jh.read_json(playlists_folder + playlist + ".json")


videos = []

for i in data:
    video = {}
    video['link'] = f"https://youtu.be/{i['videoId']}"
    videos.append(video)
    
    
# jh.write_json(videos, playlist)    


for i in videos:
    subprocess.run(f"yt-dlp -x {i['link']} -P {downloads_folder}{playlist} --output '%(title)s.%(ext)s'", shell=True)

