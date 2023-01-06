import pyautogui, webbrowser
from time import sleep

def WppBot(numero, mensaje):
    webbrowser.open('https://web.whatsapp.com/send?phone=+57{numero}'.format(numero=numero))
    sleep(10)
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')


if __name__ == '__main__':
    mensaje = input('Que mensaje quieres enviar?: ')
    numero = input('A que numero quieres enviar este mensjae?: ')

    WppBot(mensaje, numero)
