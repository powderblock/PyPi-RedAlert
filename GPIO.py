import RPi.GPIO as gpio
import time
import feedparser

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

def updateRSS():
    global redditRSS, date, title
    redditRSS = feedparser.parse('http://www.reddit.com/r/pics/new/.rss')
    title = redditRSS['entries'][0]['title']
    date = redditRSS.entries[0].published

updateRSS()
post = title+' Time and Date posted: '+date


#Main loop.
while(1):
    updateRSS()

    #Make a string out of some of the items in the RSS feed.
    newPost = title+' Time and Date posted: '+date

    #Check if the post has changed since last loop.
    if post != newPost:
        print("New post!\n")
        print newPost
        post = newPost
        for i in range(1, 15):
                gpio.output(14, gpio.LOW)
                time.sleep(1)
                gpio.output(14, gpio.HIGH)

    else:
        print("No new post.")
