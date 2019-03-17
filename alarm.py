#!/usr/bin/python3

# inspired by http://code.activestate.com/recipes/579117-simple-command-line-alarm-clock-in-python

# Description: 
# Start it running with a command line argument specifying the
# duration in minutes or the time of day in 24h format.
# It will sleep for that time and beep for the alarm.
# Use a duration of 0 to test the alarm immediately.


import sys
import string
from time import sleep, localtime, strftime

sa = sys.argv
lsa = len(sys.argv)

if lsa != 2:
    print("Usage: alarm_clock.py [duration_in_minutes]\nor     alarm_clock.py [time_of_day in 24h format]")
    print("Example: alarm_clock.py 10\n         alarm_clock.py 04:20")
    print("Use a value of 0 minutes for testing the alarm immediately.")
    print("Beeps a few times after the duration is over.")
    print("Press Ctrl-C to terminate the alarm clock early.")
    sys.exit(1)

try:
	if ":" in sa[1]:
		local_time = (strftime("%H:%M", localtime()))
		split_local_time = local_time.partition(":")
		split_sa_time = sa[1].partition(":")
		# delta in minutes
		delta_h = int(split_sa_time[0]) * 60 - int(split_local_time[0]) * 60
		delta_m = int(split_sa_time[2]) - int(split_local_time[2])
		minutes = delta_h + delta_m
		if minutes < 0:
			delta_h = (23 - int(split_local_time[0])) * 60 + int(split_sa_time[0]) * 60
			delta_m = 60 - int(split_local_time[2]) + int(split_sa_time[2])
			minutes = int(delta_h) + int(delta_m)
			
	if ":" not in sa[1]:
		minutes = int(sa[1])
except ValueError:
    print("Invalid numeric value (%s) for minutes" % sa[1])
    print("Should be an integer >= 0")
    sys.exit(1)

if minutes < 0:
    print("Invalid value for minutes, should be >= 0")
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

try:
    if minutes > 0:
        print("Sleeping for " + str(minutes) + unit_word)
        sleep(seconds)
    print ("Wake up")
    for i in range(5):
        print("\a")
        sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(1)
