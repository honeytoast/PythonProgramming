#### Name:   Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 8

Product: A python program that tweets a status regarding sunrise/set and the
         current moon phase to a specific twitter everyday at 3 A.M.

Description: "astrotweet.py", when given a city and state within the U.S., will
             calculate the next sunrise, sunset and current moon phase according
             to the local time of the city. The program will tweet a new status
             with the information to a specific twitter account. It will also 
             output the message and time(in seconds) it needs to sleep until 3A.M.
             to the terminal. Once it's 3A.M., the program will recalculate the 
             information for the day and do another tweet. This will keep 
             happening until the program is exited by the user.

             Modules used:
             PyEphem
             homepage url: http://rhodesmill.org/pyephem/
             PyPI url: https://pypi.python.org/pypi/ephem/3.7.5.1
             date retrieved: 4/14/2014
             license: LGPL

             Python Twitter Tools
             homepage url: http://mike.verdone.ca/twitter/
             PyPI url: https://pypi.python.org/pypi/twitter/1.14.3
             date retrieved: 4/14/2014
             license: MIT License

How to run: Set up your virtual environment in the SunriseTweets directory.
            Activate virtual environment.
            Install required modules using pip.
            Run the program with your city and state(the two letter abbreviation)
            both in quotations, and separated by a space.

Commands: virtualenv-3.3 env
          source env/bin/activate
          python astrotweet.py '{city}' '{state}'

	     # where {city} is the name of your city, and {state} is the 
	     # two letter abbreviation for your state.

[important] 
     The specific twitter account that will receive the status updates can be
     reached by this url: http://twitter.com/honeybricktoast
