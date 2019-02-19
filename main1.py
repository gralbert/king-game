import constants
from loc import *
import random

resources = {'Земля': 150, 'Казна': 10000, 'Крестьяне': 100, 'Зерно': 10500, 'Смута': 5, 'Армия': 50, 'Год': 0}


def file(name):
    """ The function reads a file with strings and generates a list"""
    phrases = []
    with open(name) as f_in:
        for string in f_in:
            phrases.append(string)
        return phrases


def prob(n1,n2):
    """ Count probability """
    return random.randint(n1, n2)


def sale(phrases, resources):
    """ The function is responsible for the amount of grain sold """
    price = prob(20, 32)
    print('{} {} {}'.format(random.choice(phrases)[:-1], str(price), GOLD))
    how_much = int(input(HOW_SALE))
    resources['Зерно'] -= how_much
    resources['Казна'] += how_much * price
    return resources


def buy(phrases, resources):
    """ The function is responsible for the amount of purchased grain """
    price = prob(20, 30)
    print('{} {} {}'.format(random.choice(phrases)[:-1], str(price), GOLD))
    how_much = int(input(HOW_BUY))
    resources['Зерно'] += how_much
    resources['Казна'] -= how_much * price
    return resources


def sow(resources):
    """ The function is responsible for the amount of grain sown """
    how_sow = int(input(HOW_SOW))
    resources['Зерно'] -= how_sow
    return resources


def krasota(resources):
    """ The function is responsible for the formatting of the game """



def give_zerno(resources):
    """ The function is responsible for the amount of grain issued to the people"""
    how_give = int(input(HOW_GIVE))
    resources['Зерно'] -= how_give
    if how_give < 200:
        resources['Смута'] += 10
    elif 200 < how_give < 300:
        resources['Смута'] += 5
    return resources


def man_event(phrases):
    """ The function is responsible for control events """


def not_man_event(phrases):
    """ The function is responsible for unmanaged events """
    inher_gold = prob(4000, 30000)
    inher_grain = prob(2000, 15000)
    event = random.choice(phrases)
    if event == phrases[0]:
        resources['Зерно'] += inher_grain
    if event == phrases[1]:
        resources['Казна'] //= 1.2
    if event == phrases[2]:
        resources['Зерно'] //= 1.2
    if event == phrases[3]:
        resources['Казна'] //= 1.5
    if event == phrases[4]:
        resources['Казна'] //= 1.3
        resources['Зерно'] //= 1.2
    if event == phrases[5]:
        resources['Казна'] += inher_gold
    print(event)


def war(phrases):
    """ The function is responsible for the management of the war """



def record(your_name, rec_str):
    """ The function is responsible for making a nickname in the list of records """
    f = open('records.txt', 'w')
    f.write(your_name + '-----' + str(rec_str) + '\n')


def main():
    your_name = str(input('Пожалуйста, введите имя игрока: '))

    while resources['Крестьяне'] > 15 and resources['Смута'] < 100 and resources['Земля'] > 45:
        if resources['Год'] > 0:
            print('\n\nС новым годом!\n\n')
        krasota(resources)
        sale(file('sale.txt'), resources)
        krasota(resources)
        buy(file('buy.txt'), resources)
        krasota(resources)
        sow(resources)
        krasota(resources)
        give_zerno(resources)
        war(file('war.txt'))
        krasota(resources)
        not_man_event(file('indep.txt'))
        question = input('Идем дальше? [enter]')
        resources['Год'] += 1
    else:
        print(your_name + ', игра окончена! Нужно больше заботиться о своём народе.')
        rec_str = resources['Земля'] + resources['Зерно'] + resources['Казна'] + resources['Народ'] + resources['Армия']
        record(your_name, str(rec_str))

if __name__ == '__main__':
    main()

