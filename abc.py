"""
    this is  the Elder Scroll online light attack helper
    when you use the assigned skill key , also have light attack enabled
    you can run on any python ide , or windows cmd after you install python 3.10
    you need pip install pynput
    this program is Ver 0.01  and tested on python 3.10
    
"""

import pynput
from pynput.keyboard import Key, Listener,Controller as key_cl
from pynput.mouse import Button, Controller
import time


d_time =0.08 # delay time for light attack and skill
keyboard = key_cl()
mouse = Controller()
print("press home key to exit program")


def on_press(key):
    #print('{0} pressed'.format(key))
    if (key.char if hasattr(key, 'char') else key.name) == '6': 
        # '6' is the key you press, you can assign what you want
        print('use skill 1') #skill 1  
        mouse.press(Button.left)
        time.sleep (d_time)
        mouse.release(Button.left)
        keyboard.press('1') # key 1 is you assign on game console, you can assign in game settings
        keyboard.release('1')  
         
    
    if (key.char if hasattr(key, 'char') else key.name) == '7':
        print('use skill 2')
        mouse.press(Button.left)
        time.sleep (d_time)
        mouse.release(Button.left)
        keyboard.press('2')
        keyboard.release('2')  
         
        
        
    if (key.char if hasattr(key, 'char') else key.name) == '8':
        print('use skill 3')
        mouse.press(Button.left)
        time.sleep (d_time)
        mouse.release(Button.left)
        keyboard.press('3')
        keyboard.release('3')  
         
    
    if (key.char if hasattr(key, 'char') else key.name) == '9':
        print('use skill 4')
        mouse.press(Button.left)
        time.sleep (d_time)
        mouse.release(Button.left)
        keyboard.press('4')
        keyboard.release('4')  
         
    
    if (key.char if hasattr(key, 'char') else key.name) == '0':
        print('use skill 5')
        mouse.press(Button.left)
        time.sleep (d_time)
        mouse.release(Button.left)
        keyboard.press('5')
        keyboard.release('5')  
         
    
    
    
    if key == Key.home:
        # Stop listener
        return False
"""def on_release(key):
    #print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
"""

with Listener(on_press=on_press) as listener:
    listener.join()