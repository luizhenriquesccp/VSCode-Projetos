import pyautogui as auto
import time

auto.PAUSE = 1

auto.press('win')
auto.write('opera')
auto.press('enter')
auto.sleep(6)
auto.click(x=1270, y=382)
auto.sleep(7)
auto.click(x=816, y=165)
auto.write("canal peewee")
auto.hotkey('enter')

# Isso tudo basicamente para abri o opera, o navegador que uso, e ir para o canal Peewee, onde uso as quatro principais coisas...
# para usar o pyautogui, que são clicar, escrever, pressionar teclas e usar hotkeys.