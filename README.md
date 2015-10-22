# Music When
A simple python script to figure out which hours of the day you listen to music the most.

# Usage
```
python musicwhen.py -u USERNAME
```
where USERNAME is your last.fm username.

# Output
Running musicwhen.py will create 2 files:

1. A text file data/USERNAME.txt with all tracks scrobbled by this user, including time of scrobble
2. An image file img/USERNAME.png that shows the listening pattern as number of scrobbles per hour of the day

# Why is it so slow?
last.fm has a policy of less than 5 requests per second and deliver a maximum of 200 tracks per request. We respect this policy and therefore the script takes some time if you have listened to a lot of music. But don't worry -- the progress bar will let you know how far a long you are.
