# Music. When?
A simple Python script that figures out which hours of the day you listen to music the most.

![Listening Pattern Example Image](https://raw.githubusercontent.com/hanshenrik/music-when/master/img/shenrik.png)

# Usage

```
./musicwhen.py -u <username>
```

where `<username>` is your, your friend's or some stranger's last.fm username.

# Output
Running musicwhen.py will create 2 files:

1. `data/<username>.txt` with all tracks scrobbled by this user, including time of scrobble
2. `img/<username>.png` that shows the listening pattern as number of scrobbles per hour of the day

# Why is it so slow?
last.fm deliver a maximum of 200 tracks per request and has a policy of less than 5 requests per second. We respect this policy and the script therefore takes some time if you have listened to more than a few songs. But don't worry&mdash;the progress bar will let you know how far a long you are.

# lastexport.py
The script for retrieving and parsing songs from last.fm is a slightly modified version of a script by [bitmorse](https://github.com/bitmorse) available at https://gist.github.com/bitmorse/5201491.
