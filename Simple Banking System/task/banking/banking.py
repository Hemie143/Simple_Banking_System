from random import randint

class Card:

    def __init__(self):
        self.IIN = '400000'
        self.CAN = ''
        self.checksum = '0'
        self.pin = ''
        self.generate_can()
        self.generate_check()
        self.generate_pin()
        self.full_number = f'{self.IIN}{self.CAN}{self.checksum}'

    def generate_can(self):
        self.CAN = f'{randint(0, 999999999):09}'
        self.full_number = f'{self.IIN}{self.CAN}{self.checksum}'

    def generate_check(self):
        self.full_number = f'{self.IIN}{self.CAN}{self.checksum}'
        step = [int(x) for x in self.full_number[:-1]]
        step = [x * 2 if i % 2 == 0 else x for i, x in enumerate(step)]
        step = [x - 9 if x > 9 else x for x in step]
        step_sum = sum(step)
        self.checksum = str((step_sum // 10 + 1) * 10 - step_sum)
        if self.checksum == '10':
            self.checksum = '0'
        self.full_number = f'{self.IIN}{self.CAN}{self.checksum}'

    def generate_pin(self):
        self.pin = f'{randint(0, 9999):04}'

    def card_menu(self):
        print('You have successfully logged in!')
        while True:
            print('1. Balance')
            print('2. Log out')
            print('0. Exit')
            command = input()
            if command == '1':
                print(f'Balance: {self.balance}')
            elif command == '2':
                print('You have successfully logged out!')
                return
            elif command == '0':
                exit()

    def luhn_check(self):
        step = [int(x) for x in self.full_number[:-1]]
        step = [x * 2 if x % 2 == 0 else x for x in step]
        step = [x - 9 if x > 9 else x for x in step]
        control = sum(step) + int(self.full_number[-1])
        return control % 10 == 0

class Interface:

    def __init__(self):
        self.cards = []

    def generate_card(self):
        card = Card()
        self.cards.append(card)
        print('Your card has been created')
        print('Your card number:')
        print(card.full_number)
        print('Your card PIN:')
        print(card.pin)

    def login(self):
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        pin = input()
        for card in self.cards:
            if card.full_number == card_number and card.pin == pin:
                card.card_menu()
                break
        else:
            print('Wrong card number or PIN!')

    def run_menu(self):
        while True:
            print('1. Create an account')
            print('2. Log into  account')
            print('0. Exit')
            command = input()
            if command == '1':
                self.generate_card()
            elif command == '2':
                self.login()
            elif command == '0':
                print('Bye!')
                exit()

interface = Interface()
interface.run_menu()
