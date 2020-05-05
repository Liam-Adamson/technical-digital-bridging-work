# date : 05/05/2020
# creator : Liam Adamson

def character_freq(str1):
    dict = {}
    for x in str1:
        keys = dict.keys()
        if x in keys:
         dict[x] += 1
        else:
         dict[x] = 1
    return dict

string = input("Enter your word or scentance: ")
print(character_freq(string))
