#Liam Adamson
#23/05/2020
#missing word game

def main():
    display_separator()
    display_intro()
    display_separator()
    score = 0
    rounds = 0
    missing_words = [('<iteration>', '_________'),('<idle>','____'),('<variable>','________'),('<decompose>','_________'),('<metadata>','________')]


    with open('sentences.txt', 'r') as f:
        while rounds < 5:
            for key, value in missing_words:
                f_contents = f.readline()
                f_contents = f_contents.replace(key,value)
                user_input = input(f_contents).lower()
                rounds = rounds + 1
                if user_input in key[1:-1]:
                    print('You are correct.')
                    score = score + 1
                else:
                    print('That is incorrect.')
                    print('The correct word was',key[1:-1])
    display_separator()
    print('You total score was', score, 'out of', rounds)
    display_separator()




def display_intro():
    title = "** Missing word game **"
    print('*'*len(title))
    print(title)
    print('*'*len(title))

def display_separator():
    print('-'*23)

main()
exit()
