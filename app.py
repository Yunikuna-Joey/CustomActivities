# install pypresence library before continuing 
from pypresence import Presence 

# time library to display custom timer 
import time 

bot_token = 'Enter your token as a string here'

# Instantiate your bot connection with the Presence module 
bot = Presence(bot_token) 
bot.connect() 

# this is just used to calculate the passed time 
start_time = time.time()

# you can adjust this to your liking of which key to terminate the custom activity
user = input('Enter q to quit') 

# if you change the top line to a different key than 'q'
# make sure you change below here as well for the condition to work
while user != q: 
    current_time = time.time() 
    elasped = int(current_time - star_time)
    
    # time formatting logic here
    hours, remainder = divmod(elasped, 3600)
    minutes, seconds = divmod(remainder, 60)
    elasped_text = f'{hours:02d}:{minutes:02d}:{seconds:02d}' 
    
    # this is the portion of what will show up when you click your own profile in member list 
    bot.update(
        # this will display the text associated
        state=f'Enter custom text here', {elasped_text},
        large_image='Picture image name here'
    )
    
    time.sleep(1)

