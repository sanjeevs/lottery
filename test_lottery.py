import unittest
import lottery
class TestLottery(unittest.TestCase):

    def test_is_jackpot(self):
        self.assertTrue(lottery.is_jackpot("123", "123"))
        self.assertTrue(lottery.is_jackpot("231", "123"))
        self.assertTrue(lottery.is_jackpot("321", "123"))
        self.assertFalse(lottery.is_jackpot("324", "123"))

    def test_is_deuce(self):
        self.assertTrue(lottery.is_deuce("123", "134"))
        self.assertTrue(lottery.is_deuce("135", "134"))
        self.assertTrue(lottery.is_deuce("234", "134"))
        self.assertFalse(lottery.is_deuce("234", "234"))

    def test_is_ticket_valid(self):
        self.assertTrue(lottery.is_ticket_valid("123"))
        self.assertFalse(lottery.is_ticket_valid("113"))
        self.assertFalse(lottery.is_ticket_valid("122"))
        self.assertFalse(lottery.is_ticket_valid("313"))
        self.assertFalse(lottery.is_ticket_valid("333"))

    def test_pick_ticket(self):
        for _ in range(100):
            self.assertTrue(lottery.is_ticket_valid(lottery.get_ticket()))

    def test_book_of_ticket(self):
        self.assertEqual(len(lottery.get_book_of_tickets()), 7)
        print(lottery.get_book_of_tickets())

    def test_jackpot_in_book(self):
        book = ['634', '278', '921', '746', '385', '582', '347']
        self.assertTrue(lottery.is_jackpot_in_book(book, '921'))
        self.assertTrue(lottery.is_jackpot_in_book(book, '347'))
        self.assertFalse(lottery.is_jackpot_in_book(book, '348'))

    def test_min_double_deuce_in_book(self):
        book = ['634', '278', '921', '746', '385', '582', '347']
        self.assertTrue(lottery.is_min_double_deuce_in_book(book, '643'))
        self.assertTrue(lottery.is_min_double_deuce_in_book(book, '439'))
        self.assertFalse(lottery.is_min_double_deuce_in_book(book, '938'))

    def test_is_book_jackpot_winner(self):
        book = ['634', '279', '921', '746', '385', '582', '349']
        self.assertTrue(lottery.is_book_winner(book, '385'))
        self.assertFalse(lottery.is_book_winner(book, '387'))
        self.assertTrue(lottery.is_book_winner(lottery.magic_book(), '357'))

    def test_is_book_deuce_winner(self):
        book = ['634', '278', '921', '746', '385', '582', '347']
        self.assertTrue(lottery.is_book_winner(book, '643'))
        self.assertFalse(lottery.is_book_winner(book, '938'))

    def test_magic_book_video_example(self):
        self.assertTrue(lottery.is_min_double_deuce_in_book(lottery.magic_book(), "567")) 
        self.assertTrue(lottery.is_jackpot_in_book(lottery.magic_book(), "167")) 
        self.assertTrue(lottery.is_min_double_deuce_in_book(lottery.magic_book(), "245")) 
        self.assertTrue(lottery.is_min_double_deuce_in_book(lottery.magic_book(), "134")) 

    def test_magic_book(self):
        for _ in range(1000):
            winning_ticket = lottery.get_ticket()
            print(winning_ticket)
            print(lottery.magic_book())
            self.assertEqual(lottery.is_book_winner(lottery.magic_book(), winning_ticket), True)

    def test_deuce_1(self):
        self.assertFalse(lottery.is_deuce("123", '954'))
        self.assertTrue(lottery.is_deuce("145", '954'))
        self.assertFalse(lottery.is_deuce("167", '954'))
        self.assertFalse(lottery.is_deuce("247", '954'))
        self.assertFalse(lottery.is_deuce("256", '954'))
        self.assertFalse(lottery.is_deuce("346", '954'))
        self.assertFalse(lottery.is_deuce("357", '954'))
        
if __name__ == "__main__":
    unittest.main()
