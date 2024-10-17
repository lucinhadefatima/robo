#importar biblioteca de automacao.
#ha a nescessidade de instalacao 'pip instal pyautogui'
import pyautogui as auto

auto.PAUSE = 0.5

auto.press("win")
auto.write("edge")
auto.press("enter")
auto.hotkey("alt","space")
auto.press("x")
auto.write("python.org")
auto.press("enter")
auto.hotkey("ctrl","t")
auto.write("google.com.br")
auto.press("enter")
auto.write("logo python")
auto.press("enter")

for i in range(13):
    auto.press("tab")

    auto.press("enter")
