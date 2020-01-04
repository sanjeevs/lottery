#!usr/bin/env python
import random


def is_jackpot(winner, my_card):
    for digit in winner:
        if(digit not in my_card):
            return False
    return True

def is_deuce(winner, my_card):
    win_lst = [char for char in winner]
    num_matches = 0
    for i in win_lst:
        if i in my_card:
            num_matches += 1
    return True if (num_matches == 2) else False

def get_ticket():
    seq_digits = ["1", "2", "3", "4", "5", "6", "7"]
    random.shuffle(seq_digits)
    d = ""
    for i in range(3):
        d += seq_digits[i]
    assert(is_ticket_valid(d))
    return d

def is_ticket_valid(ticket):
    """ A ticket is valid is the digits are unique"""
    checker = 0
    for i in range(len(ticket)):
        val = ord(ticket[i]) - ord('0')
        if(checker & (1 << val)):
            return False
        else:
            checker |= (1 << val)
    return True

def get_book_of_tickets():
    book = []
    for _ in range(7):
        book.append(get_ticket())
    return book

def is_jackpot_in_book(book, winning_ticket):
    lst = [x for x in book if is_jackpot(winning_ticket, x) == True]
    return True if(len(lst) > 0) else False

def is_min_double_deuce_in_book(book, winning_ticket):
    lst = [x for x in book if is_deuce(winning_ticket, x) == True]
    return True if len(lst) >= 2 else False

def is_book_winner(book, winning_ticket):
    return True if(is_jackpot_in_book(book, winning_ticket) or 
                   is_min_double_deuce_in_book(book, winning_ticket)) else False

def magic_book():
    return ["123", "145", "167", "247", "256", "346", "357"]
