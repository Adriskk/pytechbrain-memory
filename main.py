# -*- coding: utf-8 -*-

import PyTechBrain as ptb
import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()

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

