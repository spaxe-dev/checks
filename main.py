import random
def bday_messages():
  bday = [
  'Hope you have a very Happy Birthday! :balloon:',
  'It\'s your special day – get out there and celebrate! :tada:',
  'You were born and the world got better – everybody wins! :partying_face:',
  'Have lots of fun on your special day! :birthday:',
  'Another year of you going around the sun! :sun_with_face:']
  random_message = random.choice(bday)
  return random_message



#main.py
import datetime
today = datetime.date.today()
next_birthday = datetime.date(2025, 7, 26)
days_away = next_birthday - today
if today == next_birthday:
  bday_messages() #<--Moved it here so you dont call it eachtime the code runs, only when its actually the bday
  print(bday_messages)
else: 
  print(f'My next birthday is {days_away.days} days away!')