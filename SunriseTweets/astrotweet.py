#### Name:   Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 8

import ephem
import sqlite3
import sys
import time
from twitter import *
from datetime import datetime, timedelta

# Put Twitter keys here
OAUTH_KEY = '<your oauth key>'
OAUTH_SECRET = '< your oauth secret>'
CONSUMER_KEY = '< your consumer key>'
CONSUMER_SECRET = '<your consumer secret>'

# Dictionary of the difference between GMT and the unique timezones from database
TIME_ZONES = {'US/Pacific': -7,  'US/Mountain': -6, 'US/Central': -5, 
              'US/Eastern': -4, 'US/Arizona': -7, 'America/New_York': -4, 
              'America/Indianapolis': -4, 'Pacific/Samoa': -11, 
              'America/Denver': -6, 'America/Puerto_Rico': -4, 
              'America/Los_Angeles': -7, 'Pacific/Guam': +10 , 
              'America/Adak': -9, 'America/Virgin': -4, 'Pacific/Saipan': +10,
              'US/Alaska': -8, 'US/Hawaii': -10}

# Argument checking and getting
def getArgs(l):
    if len(l) < 3:
        print('Error: please enter additional arguments - City and State(abbrev) in the USA.')
        sys.exit()
    city = sys.argv[1].upper()
    state = 'US/' + sys.argv[2].upper()
    return city, state

# Get the user's timezone and location(latitude/longitude) information
def getLocationInfo(city, state):
    conn = sqlite3.connect('us_only.sq3')
    c = conn.cursor()
    query = 'select time_zone, latitude, longitude from sol_places where' +\
            ' uc_name="{}" and region="{}"'.format(city, state)
    c.execute(query)
    info = c.fetchone()
    c.close()
    return info[0], info[1], info[2]

# Parse through date string
def getDate(day):   
    date = day.split('/')
    return int(date[0]), int(date[1]), int(date[2])

# Parse through time string
def getTime(clock):
    time = clock.split(':')
    return int(time[0]), int(time[1]), int(time[2])

# Converts time from a string containing date and time in GMT to timezone tz
def convertFromGmt(s, tz):
    gmt = s.split()
    year, month, day = getDate(gmt[0])
    hour, minute, second = getTime(gmt[1])
    gmt_datetime = datetime(year, month, day, hour, minute, second)
    time_difference = timedelta(hours=TIME_ZONES.get(tz))
    local_datetime = gmt_datetime + time_difference
    fmt = '%Y/%m/%d %H:%M:%S'
    return local_datetime.strftime(fmt)

# Get the current time in user's time zone
def getCurrentDate(time_zone):
    now = str(ephem.now())
    users_now = convertFromGmt(now, time_zone)
    return users_now

# Uses current time in timezone to calculate amount of seconds needed to sleep
def getSleepTime(tz):
    time_now = getCurrentDate(tz).split()
    year, month, day = getDate(time_now[0])
    hour, minute, second = getTime(time_now[1])
    current_time = datetime(year, month, day, hour, minute, second)
    next_day = timedelta(days=1)
    wake_day = next_day + current_time
    wake_day = wake_day.replace(hour=3, minute=0, second=0)
    sleep_time = wake_day - current_time
    return sleep_time.seconds
    
# Get the moon phases according to the current date
def getMoonPhases():
    date = ephem.now()
    new_moon = str(ephem.next_new_moon(date))
    first_quarter_moon = str(ephem.next_first_quarter_moon(date))
    full_moon = str(ephem.next_full_moon(date))
    last_quarter_moon = str(ephem.next_last_quarter_moon(date))
    return new_moon, first_quarter_moon, full_moon, last_quarter_moon

# Check to see if we are approaching new moon or full moon depending on which
# moon phase is closer to our current date.
def checkMoonPhaseDirection(date):
    new_moon = ephem.next_new_moon(date)
    full_moon = ephem.next_full_moon(date)
    if new_moon < full_moon:
        return 'Waning '
    else:
        return 'Waxing '

# Check which quarter moon the phase is currently on.
def checkWhichQuarterMoon(s):
    if s == 'Waxing Quarter':
        return 'First Quarter'
    else:
        return 'Last Quarter'

# Get the current moon phase depending on illumination of the moon.
def getMoonPhase(moon):
    return { moon.phase <= 1.0: 'New Moon', 
             moon.phase > 1.0 and moon.phase <= 49.0: 'Crescent',
             moon.phase > 49.0 and moon.phase <= 51.0: 'Quarter',
             moon.phase > 51.0 and moon.phase <= 99.0: 'Gibbous',
             moon.phase > 99.0 and moon.phase <= 100: 'Full Moon' }[1]

def tweet(Twitter, s):
    Twitter.statuses.update(status=s)

def main():
    t = Twitter(auth=OAuth(OAUTH_KEY, OAUTH_SECRET, 
                           CONSUMER_KEY, CONSUMER_SECRET))
    
    city, state = getArgs(sys.argv)    
    time_zone, latitude, longitude = getLocationInfo(city, state)
    location = '{}, {}\n'.format(city, state[3:])

    while True:
        # Create observer and body for calculation
        user = ephem.Observer()
        user.lat = str(latitude)
        user.lon = str(longitude)
        user.horizon = '-6'
        sun = ephem.Sun()
        sun.compute(user)
        moon = ephem.Moon()
        moon.compute(user)
        
        # Calculate next sunrise/sunset
        next_sunrise = str(user.next_rising(sun))
        next_sunrise = convertFromGmt(next_sunrise, time_zone)
        next_sunset = str(user.next_setting(sun))
        next_sunset = convertFromGmt(next_sunset, time_zone)

        sun_status = 'Next sunrise: {}\nNext sunset: {}\n'.format(next_sunrise, next_sunset)

        # Get the current moon phase
        now = getCurrentDate(time_zone)
        moon_status = getMoonPhase(moon)
        if moon_status == 'Quarter':
            moon_status = checkWhichQuarter(moon_status)
        elif moon_status == 'Crescent':
            moon_status = checkMoonPhaseDirection(now) + moon_status
        elif moon_status == 'Gibbous':
            moon_status = checkMoonPhaseDirection(now) + moon_status
        
        moon_phase = 'Current moon phase: ' + moon_status

        # Create the new status for tweeting a status update
        new_status = location + sun_status + moon_phase
        print(new_status)
        tweet(t, new_status)

        # Calculate time needed to sleep until the next 3a.m.
        sleep_time = getSleepTime(time_zone)
        print('Seconds to sleep: {}'.format(sleep_time))
        time.sleep(sleep_time)

if __name__ == '__main__':
    main()
