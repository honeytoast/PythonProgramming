#### Grace Hadiyanto
#### e-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment 7

Product: 1 aphorism app (using Django)

Descriptions and How to Run:
  This is an app that displays a random aphorism and current date+time per page refresh.

  The app uses the database freebsd_fortunes_clean.sl3.
  I edited an open source TypingText javascript to get the text so that
  it appears to type itself and have sound playing as it types. Credits are 
  written within the script tag in templates/aphorisms/index.html.
  I also had to make a custom templatetag to format line breaks in django      
  context variables to be recognized strings by the html. Other important code
  that makes the app look pretty are in static/aphorisms/style.css and index.js
  

  Features:
    Click on the treasure chest to get a new fortune.
    The fortune will always type itself out.
    The sound will stop playing upon completion of the fortune.
    If you do not hear any sounds, your web browser does not support the html
    audio tag. The "Shhh.." button next to the date viewed will stop the sound.
    
  One issue with sound: # only worry if the fortune is longer than 1 minute.
    If you happen to get a really long fortune on the first time you load the
    page, the sound will not loop, it will stop playing before the fortune finishes
    typing out # caused by some cache issue with the loop attribute of
    the html tag... It will start looping and playing correctly on the next refresh
    or treasure chest click. Any hard refresh on the page will cause this issue.

  Change directory into aphorism_app. Set up the virtual environment in that
  directory. Activate virtual environment. Install requirements using pip.
  Change directory into mysite. 
  commands: cd aphorism_app.
            virtualenv-3.3 env
            source env/bin/activate
            pip install -r requirements.txt
            cd mysite/
            python manage.py runserver 0.0.0.0:8000
  To see the website, type localhost:8000 in the url address of your browser.

  sounds for aphorism_app: 
        http://www.freesound.org/people/jasonLON/sounds/125408/

  images for aphorism_app:
        chest: http://www.netanimations.net/Moving_Animated_piggy-bank-money-and-treasure-pictures.htm
        background: http://www.rgbstock.com/bigphoto/mvllHxi/Parchment+Scrolls+2

   
