import constants
import random


def file(name):
    """ Считывает файл со строками и генерирует список"""
    phrases = []
    with open(name) as f_in:
        for string in f_in:
            phrases.append(string)
        return phrases


def sale(phrases):
    """ Сколько продать? """
    price = 20
    print('{} {} {}'.format(random.choice(phrases), str(price), constants.GOLD))
    how_much = int(input(constants.HOW_SALE))
    return how_much


def buy(phrases):
    """ Сколько купить? """
    price = 20
    print('{} {} {}'.format(random.choice(phrases), str(price), constants.GOLD))
    how_much = int(input(constants.HOW_BUY))
    return how_much


def sow():
    """ Сколько посеять? """
    # TODO


def give_people():
    """ Сколько выдать народу? """
    # TODO


def event(phrases):
    """ Событие. """
    # TODO


def war(phrases):
    """ Война. """
    # TODO


def probability():
    """ Вероятность события, войны, покупки-продажи и тд"""
    # TODO


def main():
    """ Main """
    sale(file('sale.txt'))
    buy(file('buy.txt'))
    sow()
    give_people()
    event(file('events.txt'))
    war(file('war.txt'))


if __name__ == '__main__':
    main()
