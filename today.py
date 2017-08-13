#!/usr/bin/env bash
import time, datetime, yweather, yahoo_finance, subprocess, os, json, urllib.request
day_of_week = time.localtime().tm_wday
now = time.time()
#now = time.time() + 60*28 + 60*60*13
tmp = "/tmp/"

voice = False

### A fucton of helpers

def time_period():
    return "Morning" if time.localtime(now).tm_hour < 12 else "Afternoon"

# hours = 3
# str(hours) + " hours" + sp(hours) -> "3 hours"
# hours = 1
# str(hours) + " hours" + sp(hours) -> "1 hour"
def sp(a):
    if a == 1:
        return ""
    return "s"

# "90" -> "90"
# "90.00" -> "90"
# "90.1" -> "90 point 1"
def format_float(s):
    s = str(s)
    if not "." in s: return s
    while True:
        if s[-1] == "0":
            s = s[:-1]
        elif s[-1] == ".":
            s = s[:-1]
            break
        else:
            break
    if voice:
        return s.replace(".", " point ")
    return s

# "12" -> "12th"
# etc..
def ordinal(s):
    if s[-1] == "1": return s + "st"
    if s[-1] == "2": return s + "nd"
    if s[-1] == "3": return s + "rd"
    return s + "th"

# 1493353783.0026777 -> "Friday, April 28th"
# will replace leading zeroes in the day with a space, like April 01 becomes April 1st
def get_pretty_date(when = now):
    l = time.localtime(when)
    return ordinal(time.strftime("%A, %B %_d", l))

# 1493353783.0026777 -> "0:30"
# 1493352043.3361661 -> "0 hundred hours"
# 1493402438.1561348 -> "14 hundred
# Will replace leading zeroes in the hour with spaces, like 02:30 becomes 2 30
def get_pretty_time(when = now):
    l = time.localtime(when)
    start = time.strftime("%_H:%M", l)
    if l.tm_min == 0:
        if l.tm_hour < 10:
            start = start.replace(":00", " hundred hours")
        else:
            start = start.replace(":00", " hundred")
    return start

# *(0, 60*65) -> "1 hour 5 minutes"
# could use work, seems to floor any difference you give it instead of round,
#     leads to "the time is 7 15 and your first class is in 44 minutes"
def get_pretty_interval(start, end):
    diff = end - start
    l = time.gmtime(diff)
    hours = int(time.strftime("%H", l), 10)
    minutes = int(time.strftime("%M", l), 10)
    result = ""
    if hours > 0:
        result += str(hours) + " hour" + sp(hours) + " " # + ", "
    return result + str(minutes) + " minute" + sp(minutes)

# todo: document
def today(hour, minute):
    l = datetime.datetime.fromtimestamp(now)
    l = l.replace(hour = hour)
    l = l.replace(minute = minute)
    l = l.replace(second = 0)
    return l.timestamp()

def get_name(c): return c[0]
def get_time(c): return c[1]

### Actual commands

classes = [
      [["Multivar", today(10, 10)], ["Physics", today(11, 15)], ["Physics again", today(12, 20)]] # monday is zero
    , [["2505", today(14, 00)], ["Discrete", today(15, 30)], ["Seminar", today(17, 00)]]
    , [["Multivar", today(10, 10)], ["Physics", today(12, 20)], ["Lab", today(14, 30)]]
    , [["2505", today(14, 00)], ["Discrete", today(15, 30)]]
    , [["Multivar", today(10, 10)], ["Physics", today(12, 20)]] # friday
    , []
    , [] # sunday
]

# TODO Update
alarms = [
      [today(8, 15), today(15, 30)] # monday
    , [today(7, 15), today(12, 00)]
    , [today(8, 15), today(15, 30)]
    , [today(7, 15), today(12, 00)]
    , [today(15,30)] # friday
    , []
    , [] # sunday
]
for k in range(len(alarms)):
    alarms[k].append(today(22, 0))
    #alarms[k].append(today(23, 0))

# pass -1 for today
# 0 for tomorrow's forecast, 1 for the day after that, etc..
def weather(day = -1):
    filename = tmp + "weather_" + str(day)
    if os.path.exists(filename) and now - os.stat(filename).st_mtime < 60*60: # cache for a maximum of one hour
        return open(filename, "r").read()
    wid = "2365044" # BLACKSBURG
    wid = "12798962" # SEATTLE
    #url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%20%3D%20%22blacksburg%2C%20va%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%20"+wid+"&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    data = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    if day == -1:
        data = data["query"]["results"]["channel"]["item"]["condition"]
        retval = data["text"] + ", " + data["temp"] + " degrees"
    else:
        forecast = data["query"]["results"]["channel"]["item"]["forecast"][day]
        retval = forecast["text"] + ", " + format_float((float(forecast["low"])+float(forecast["high"]))/2) + " degrees"
    open(filename, "w").write(retval)
    return retval

def stock(stk):
    filename = tmp + "stock_" + stk
    if os.path.exists(filename) and now - os.stat(filename).st_mtime < 60*60: # cache for a maximum of one hour
        return open(filename, "r").read()
    yesterday = time.strftime("%Y-%m-%d", time.localtime(now - 24*60*60))
    s = yahoo_finance.Share(stk)
    #val = float(s.get_percent_change().replace("%", "")) # unstable as fuck

    val = round(100 * (float(s.get_price())/float(s.get_prev_close()) - 1), 1)

    #s_y = s.get_historical(yesterday, yesterday)
    #price_now = float(s.data_set["Ask"])
    #price_yesterday = float(s_y[0]["Close"])
    #val = round(100 * ((price_now/price_yesterday) - 1), 1)

    word = "up"
    if val < 0:
        word = "down"
    retval = word + " " + format_float(abs(val)) + " percent"
    open(filename, "w").write(retval)
    return retval

todays_classes = classes[day_of_week]
todays_classes = [k for k in todays_classes if get_time(k) > now]
todays_alarms = alarms[day_of_week]
todays_alarms = [k for k in todays_alarms if k > now]

### Actual printed stuff

messages = [
      ["say", "Good " + time_period() + " Niles"]
    , ["say", "Today is " + get_pretty_date()]
    , ["say", "The time is " + get_pretty_time()]
    , ["say", ("Your next class is " + get_name(todays_classes[0]) + " in " + get_pretty_interval(now, get_time(todays_classes[0])) if len(todays_classes) > 0 else "You have no classes today")]
    , ["say", ("You have an alarm set for " + get_pretty_time(todays_alarms[0])) if len(todays_alarms) > 0 else "You have no alarms set for today"]
    , ["say", "The SNP 500 is " + stock("^GSPC") + " and AMD is " + stock("AMD")]
    , ["say", "The weather for Seattle is " + weather()]
    , ["say", "Tommorow's weather is " + weather(0)]
    #, ["exec", "npr"] # todo, skip 20 secs
]

### Does the actual printing

m = "\n".join([k[1] for k in messages])

print(m)
if voice:
    import gtts
    tts = gtts.gTTS(m)
    tts.save("/tmp/temp.mp3")
    subprocess.call(["mpv", "/tmp/temp.mp3"])
