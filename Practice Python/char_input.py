'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
import datetime

name = input('What is your name?')
age = input('that is great %s, now how old are you?' % name)

old = 100 - int(age)
super_old = datetime.datetime.now().year + old
print('You will turn 100 in the year %d' % super_old)
