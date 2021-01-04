
'''
This Python script copies number appended with string to ClipBoard to be pasted for 
renaming of file or other use.
Script waits for 'Enter' (key-press). And after that number is incremented and loop is repeated.
'''


import pyperclip #use 'pip install pyperclip' to install module
import keyboard  #use 'pip install keyboard' to install module

def copyToClipBoard(noWithStr):
    pyperclip.copy(noWithStr)
    
    keyboard.wait('enter')
    return 1

    

if __name__=='__main__':
    no = int(input('From Which No Do you want to start?'))
    strIf = int(input('Do you want to append any string with it. If yes then type 1 and if no then type 0:'))

    apStr = ''

    if strIf == 1:
        stringToAppend = input('Enter String:')
        apStr = stringToAppend
    
    '''
    Range taken is 'no' to 100 . You can change as per your comfort.
    '''
    for i in range(no, 100):
        tmp = str(i) + apStr
        tmp1 = copyToClipBoard(tmp)
        print('Copied String --> ', tmp)
        

    print('Suceessfully Completed...')
    print('Made With Love in India.')
