import lottery

num_of_players = 10

books = []
for _ in range(num_of_players):
    books.append(lottery.get_book_of_tickets())

cnt = 0
len_h = []
while(len(books) > 1):
    winning_ticket = lottery.get_ticket()
    next_books = [x for x in books if lottery.is_book_winner(x, winning_ticket)]
    books = next_books
    cnt += 1
    len_h.append(len(books))
    # FIXME: Not clear what the intent is?
    if((len(len_h) > 3) and ((len_h[-1] == len_h[-2]) and (len_h[-2] == len_h[-3]))):
        break

if(len(books) == 1):
    print("Finished:Number of Loops=", str(cnt))
else:
    print("Terminated:Number of Loops=", str(cnt), ":Number of players=", str(len(books)))

