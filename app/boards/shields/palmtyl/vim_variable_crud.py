import keyboard
from keyboard import send

scan_code_is_keypad_tuple_to_letter = {
    (93, False):     {'let':'0', 'name': 'menu'}, 
    (69, False):     {'let':'a', 'name': 'pause'},
    (70, False):     {'let':'b', 'name': 'scroll lock'},
    (-173, False):   {'let':'c', 'name': 'volume mute'},
    (-179, False):   {'let':'d', 'name': 'play/pause media'},
    (-177, False):   {'let':'e', 'name': 'previous track'},
    (-176, False):   {'let':'f', 'name': 'next track'},
    (79, True):      {'let':'g', 'name': '1'},
    (80, True):      {'let':'h', 'name': '2'},
    (81, True):      {'let':'i', 'name': '3'},
    (75, True):      {'let':'j', 'name': '4'},
    (76, True):      {'let':'k', 'name': '5'},
    (77, True):      {'let':'l', 'name': '6'},
    (71, True):      {'let':'m', 'name': '7'},
    (72, True):      {'let':'n', 'name': '8'},
    (73, True):      {'let':'o', 'name': '9'},
    (82, True):      {'let':'p', 'name': '0'},
    (78, True):      {'let':'q', 'name': '+'},
    (74, True):      {'let':'r', 'name': '-'},
    (55, True):      {'let':'s', 'name': '*'},
    (53, True):      {'let':'t', 'name': '/'},
    (83, True):      {'let':'u', 'name': 'decimal'},
    (82, False):     {'let':'v', 'name': 'insert'},
    (54, False):     {'let':'w', 'name': 'right shift'},
    (29, False):     {'let':'x', 'name': 'right ctrl'},
    (56, False):     {'let':'y', 'name': 'right alt'},
    (92, False):     {'let':'z', 'name': 'right windows'}
} 


while True:
    event = keyboard.read_event()
    sc, kp = event.scan_code, event.is_keypad 
    if (sc,kp) in scan_code_is_keypad_tuple_to_letter and event.event_type == 'down':
        print(f'{scan_code_is_keypad_tuple_to_letter[(sc,kp)]=}')