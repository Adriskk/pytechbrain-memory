# -*- coding: utf-8 -*-

import PyTechBrain as ptb
import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()
    
    # - Zmiana jasnosci RGB
    # while True:
        # x = board.potencjometr_raw()

        # board.RGB_kolor(
        #     x if x <= 255 else 255, 
        #     x if x <= 255 else 255, 
        #     x if x <= 255 else 255
        # )

        # if board.przycisk_lewy(): board.buzzer_sygnal('demo')
        # if board.przycisk_prawy(): board.buzzer_sygnal('off')


    # - Swiatla
    # board.sygnalizator_czerwony('on')
    # time.sleep(.5)
    # board.sygnalizator_zolty('on')
    # time.sleep(1.5)

    # board.sygnalizator_czerwony('off')
    # board.sygnalizator_zolty('off')

    # board.sygnalizator_zielony('on')
    
    # time.sleep(3)

    # board.sygnalizator_zielony('off')
    # board.sygnalizator_zolty('on')

    # time.sleep(1)
    # board.sygnalizator_zolty('off')
    # board.sygnalizator_czerwony('on')

    # time.sleep(4)
    # board.sygnalizator_czerwony('off')

    # - Wyczucie glosnosci
    # while True:
    #     print(board.glosnosc_raw())

    # - Zmiana kolorów w zależności od światła
    # MAX = 1023
    # while True: 
    #     # brightness = board.fotorezystor_raw() if board.fotorezystor_raw() < 255 else 255
    #     # board.RGB_kolor(
    #     #     brightness,
    #     #     50, 70
    #     # )

    #     brightness = board.fotorezystor_raw()
    #     if brightness > 0 and brightness < MAX / 5: 
    #         board.sygnalizator_czerwony('on')
    #         board.sygnalizator_zolty('off')
    #         board.sygnalizator_zielony('off')

    #     if brightness > MAX / 5 and brightness < MAX / 1.5:
    #         board.sygnalizator_czerwony('off')
    #         board.sygnalizator_zolty('on')
    #         board.sygnalizator_zielony('off')

    #     if brightness > MAX / 1.5 and brightness <= MAX:
    #         board.sygnalizator_czerwony('off')
    #         board.sygnalizator_zolty('off')
    #         board.sygnalizator_zielony('on')


    # - Sprawdza czy masz gorączke
    # while True:
    #     print(board.temperatura_C())
    #     if board.przycisk_lewy():
    #         print('Pobieranie temperatury')
    #         time.sleep(3)

    #         temp = board.temperatura_C()
    #         print(f'Twoja temperatura: {temp}')

    #         if temp >= 38: print('Masz goraczke! ')
    #         else:
    #             print('Nie masz goraczki!')
    #             board.buzzer_sygnal('demo')


    # - Nuta wlazł kotek na płotek
    # notes = [
    #     ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1, 
    #     ptb.C1, ptb.E1, ptb.G5, 
    #     ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1, 
    #     ptb.C3, ptb.E1, ptb.C3, 
    #     ptb.C3, ptb.E1, ptb.E1, ptb.D5, ptb.F1, ptb.F1, 
    #     ptb.C1, ptb.E1, ptb.G3, 
    #     ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1
    # ]

    # stops = [6, 9, 15, 18, 24, 27, 33]s

    # i = 0
    # while True:
    #     if board.przycisk_lewy():
    #         if i <= len(notes):
    #             board.nuta(notes[i], 1 / 4)
    #             i += 1
    #             if i in stops: time.sleep(.3)
    #         time.sleep(.2)

    # - Gra pamięciowa komputera
    class Memory:
        def __init__(self):
            self.buttons = []
            self.amount = 6
            self.clicked = 0

    memory = Memory()

    def static(button):
        time.sleep(1)
        memory.clicked += 1
        print(f'[?] Pressed {button} key')
        
    while True: 
        print('[+] Press key')
        left = board.przycisk_lewy()
        middle = board.przycisk_srodkowy()
        right = board.przycisk_prawy()

        if left: 
            memory.buttons.append(board.sygnalizator_czerwony)
            left = None
            static('left')
            
        if middle: 
            memory.buttons.append(board.sygnalizator_zolty)
            middle = None
            static('middle')

        if right: 
            memory.buttons.append(board.sygnalizator_zielony)
            right = None
            static('right')

        if memory.clicked == memory.amount: break

    print('Visualizing pressed keys: ')
    time.sleep(2)

    last = None
    for button in memory.buttons:
        button('on')
        if last: last('off')
        last = button
        board.nuta(ptb.C5, 1 / 4)
        time.sleep(1)

