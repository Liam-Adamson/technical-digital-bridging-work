#Liam Adamson
#numbers to words
#05/06/2020

from inflect import engine
e = engine()
num = int(input('Enter a number: '))
word = e.number_to_words(num)
print(word)
