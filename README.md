# Music When
A simple python script to figure out which hours of the day you listen to music the most.

# Usage

```
python musicwhen.py -u USERNAME
```

where `USERNAME` is your last.fm username.

# Output
Running musicwhen.py will create 2 files:

1. `data/USERNAME.txt` with all tracks scrobbled by this user, including time of scrobble
2. `img/USERNAME.png` that shows the listening pattern as number of scrobbles per hour of the day

# Why is it so slow?
last.fm deliver a maximum of 200 tracks per request and has a policy of less than 5 requests per second. We respect this policy and the script therefore takes some time if you have listened to more than a few songs. But don't worry&mdash;the progress bar will let you know how far a long you are.
