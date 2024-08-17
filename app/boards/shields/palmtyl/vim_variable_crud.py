import json
import os
import time
import pyperclip as pc
import keyboard
from keyboard import send, add_hotkey, play

VAR_FILE = '.\\vim_variables.json'

HOLD_LET = 'a' # 3rd letter after bigram is complete
TAP_LET = 'b'

scan_code_is_keypad_tuple_to_letter = {
    (69, False):     {'let':'a', 'name':'pause'},
    (70, False):     {'let':'b', 'name':'scroll lock'},
    (-173, False):   {'let':'c', 'name':'volume mute'},
    (-179, False):   {'let':'d', 'name':'play/pause media'},
    (-177, False):   {'let':'e', 'name':'previous track'},
    (-176, False):   {'let':'f', 'name':'next track'},
    (79, True):      {'let':'g', 'name':'1'},
    (80, True):      {'let':'h', 'name':'2'},
    (81, True):      {'let':'i', 'name':'3'},
    (75, True):      {'let':'j', 'name':'4'},
    (76, True):      {'let':'k', 'name':'5'},
    (77, True):      {'let':'l', 'name':'6'},
    (71, True):      {'let':'m', 'name':'7'},
    (72, True):      {'let':'n', 'name':'8'},
    (73, True):      {'let':'o', 'name':'9'},
    (82, True):      {'let':'p', 'name':'0'},
    (78, True):      {'let':'q', 'name':'+'},
    (74, True):      {'let':'r', 'name':'-'},
    (55, True):      {'let':'s', 'name':'*'},
    (53, True):      {'let':'t', 'name':'/'},
    (83, True):      {'let':'u', 'name':'decimal'},
    (28, True):     {'let':'v', 'name':'enter'},
    (82, False):     {'let':'w', 'name':'insert'},
    (58, False):     {'let':'x', 'name':'caps lock'},
    (-175, False):     {'let':'y', 'name':'volume up'},
    (-174, False):     {'let':'z', 'name':'volume down'}
} 

if not os.path.exists(VAR_FILE):
    bigram_to_variable = {}
    alphas = 'abcdefghijklmnopqrstuvwxyz'

    for a1 in alphas:
        for a2 in alphas:
            bigram_to_variable[a1+a2] = a1+a2 

    with open(VAR_FILE, "w") as outfile:
        json.dump(bigram_to_variable, outfile)

bigram = '' 
while True:
    event = keyboard.read_event(suppress=True)
    sc, kp = event.scan_code, event.is_keypad

    if (sc,kp) in scan_code_is_keypad_tuple_to_letter:
        if event.event_type == 'up':
            pass
        elif event.event_type == 'down':
            print(f'{scan_code_is_keypad_tuple_to_letter[(sc,kp)]=}')
            val = scan_code_is_keypad_tuple_to_letter[(sc,kp)]
            if len(bigram) < 2:
                bigram += val['let']
            else:
                print(f'{bigram=}')
                if val['let'] == HOLD_LET:
                # HOLD behaviour: store vim variable name
                    print('Holding:')                    
                    send('escape')
                    time.sleep(0.05)
                    send('v')
                    time.sleep(0.05)
                    send('b')
                    time.sleep(0.2)
                    send("shift+\"")
                    time.sleep(0.05)
                    send('shift+equal')
                    time.sleep(0.05)
                    send('y')
                    time.sleep(0.05) 
                    variable = pc.paste()
                    print(f'{variable=}')
                    time.sleep(0.05)
                    send('e')
                    time.sleep(0.05)
                    send('a')
                    with open(VAR_FILE) as json_file:
                        bigram_to_variable = json.load(json_file)
                        bigram_to_variable[bigram] = variable
                    time.sleep(0.05)
                    with open(VAR_FILE, "w") as outfile:
                        json.dump(bigram_to_variable, outfile)
                if val['let'] == TAP_LET:
                # TAP behaviour: retrieve vim variable name
                    print('Tapping:')
                    with open(VAR_FILE) as json_file:
                        bigram_to_variable = json.load(json_file)
                    variable = bigram_to_variable[bigram]
                    pc.copy(variable)
                    print(f'{variable=}') 
                    send('ctrl + r')
                    time.sleep(0.1)
                    send('shift+equal')
                bigram = ''  # reinitialize after successful variable crud
    else:
        play([event]) # type all non-suppressed keys
