import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.7

cont = 79

while cont > 0:
    #ABRIR COREL
    pyautogui.hotkey("win", "e")
    pyautogui.click(x=540, y=101)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyperclip.copy(r"A:\videos\PACK 500 ESTAMPAS INFANTIS")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    
    #ABRINDO PRIMEIRO ARQUIVO
    pyautogui.click(x=258, y=234, clicks=2)
    pyautogui.click(x=2524, y=14)
    time.sleep(6)

    #EXCLUINDO BARRA DE BAIXO
    pyautogui.press("f4")
    pyautogui.click(x=1125, y=910, button='right')
    pyautogui.click(x=1188, y=950)
    pyautogui.press("2")
    pyautogui.hotkey("ctrl", "s")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=2547, y=11)
    time.sleep(2)
    pyautogui.click(x=2547, y=11)

    #EXCLUINDO COPIA DE SEGURANÇA
    
    pyautogui.hotkey("win", "e")
    pyautogui.click(x=540, y=101)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyperclip.copy(r"A:\videos\PACK 500 ESTAMPAS INFANTIS")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    pyautogui.click(x=342, y=240)
    pyautogui.press("del")
    pyautogui.click(x=342, y=240)
    pyautogui.hotkey("ctrl", "x")
    pyautogui.click(x=230, y=212, clicks=2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("alt", "f4")
    cont = cont -1
    print(cont)
