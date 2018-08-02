import time
import datetime
import pyodbc
import urllib
from selenium import webdriver
import json
import requests
import PIL.ImageGrab

#GETS THE 50 MOST POPULAR VIDEOS

channel_id = "channel id"
key = "account key"
number_of_popular_videos = "50"
get_50_most_popular_videos = "https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId=" +channel_id +"&key=" + key + "&maxResults=" + number_of_popular_videos


print (get_50_most_popular_videos)

# opener_get_50_most_popular_videos = urllib2.urlopen(get_50_most_popular_videos)
# parsed_popular_videos = json.load(opener_get_50_most_popular_videos)
# parsed_popular_videos_two =  parsed_popular_videos["items"]
