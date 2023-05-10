from project.bookstore import Bookstore

from unittest import TestCase



class TestBookstore(TestCase):

    def test_init_when_data_is_valid(self):
        bs = Bookstore(10)
        self.assertEqual(10, bs.books_limit)
        self.assertEqual({}, bs.availability_in_store_by_book_titles)
        self.assertEqual(0, bs.total_sold_books)
        self.assertEqual(0,len(bs))

    def test_book_limit_when_value_not_positive(self):
        with self.assertRaises(ValueError) as va:
            bs = Bookstore(0)
        self.assertEqual(f"Books limit of 0 is not valid", str(va.exception))

    def test_len_when_book_added_and_not_in_available_books(self):
        bs = Bookstore(10)
        result = bs.receive_book('Book', 5)
        expected = f"5 copies of Book are available in the bookstore."
        self.assertEqual(5, len(bs))
        self.assertEqual(5, bs.availability_in_store_by_book_titles["Book"])
        self.assertEqual(expected, result)



    def test_len_when_book_added_and_book_in_available_books(self):
        bs = Bookstore(10)
        bs.receive_book('Book', 5)
        result = bs.receive_book('Book', 3)
        expected = f"8 copies of Book are available in the bookstore."
        self.assertEqual(8, len(bs))
        self.assertEqual(8, bs.availability_in_store_by_book_titles["Book"])
        self.assertEqual(expected, result)
        bs.receive_book("test", 2)
        self.assertEqual(10, len(bs))
        self.assertEqual(8, bs.availability_in_store_by_book_titles["Book"])
        self.assertEqual(2, bs.availability_in_store_by_book_titles["test"])
        self.assertEqual(10, len(bs))
        with self.assertRaises(Exception) as ex:
            bs.receive_book("title", 5)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))


    def test_receive_when_no_space_available(self):
        bs = Bookstore(10)
        bs.receive_book('Book', 10)
        with self.assertRaises(Exception) as ex:
            bs.receive_book("Another book", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_sell_book_successful(self):
        bs = Bookstore(10)
        bs.receive_book('Book', 10)
        result = bs.sell_book("Book", 5)
        self.assertEqual(f"Sold 5 copies of Book", result)
        self.assertEqual(5, bs.availability_in_store_by_book_titles["Book"])
        self.assertEqual(5, bs.total_sold_books)
        self.assertEqual(5, len(bs))
        bs.receive_book("test", 5)
        result1 = bs.sell_book("test", 4)
        self.assertEqual(f"Sold 4 copies of test", result1)
        self.assertEqual(1, bs.availability_in_store_by_book_titles["test"])
        self.assertEqual(9, bs.total_sold_books)
        self.assertEqual(6, len(bs))
        self.assertEqual({"Book": 5, "test": 1}, bs.availability_in_store_by_book_titles)
        bs.sell_book('test', 1)
        self.assertEqual("Total sold books: 10\n" +
                         "Current availability: 5\n" + " - Book: 5 copies\n" + " - test: 0 copies", str(bs))
        self.assertEqual(5, len(bs))
        self.assertEqual(10, bs.total_sold_books)


    def test_sell_when_book_not_in_available_books(self):
        bs = Bookstore(10)
        bs.receive_book('Book', 10)
        with self.assertRaises(Exception) as ex:
            bs.sell_book("Another book", 5)
        self.assertEqual(f"Book Another book doesn't exist!", str(ex.exception))

    def test_sell_when_not_enough_copies(self):
        bs = Bookstore(10)
        bs.receive_book('Book', 10)
        with self.assertRaises(Exception) as ex:
            bs.sell_book("Book", 11)
        self.assertEqual(f"Book has not enough copies to sell. Left: 10", str(ex.exception))

    def test_str(self):
        bs = Bookstore(50)
        bs.receive_book('Book', 10)
        bs.receive_book('Test_book', 10)
        bs.receive_book('T_book', 10)
        bs.sell_book("Book", 5)
        expected = "Total sold books: 5" + '\n' + "Current availability: 25" + "\n" + " - Book: 5 copies" + "\n" + \
                   " - Test_book: 10 copies" + "\n" + " - T_book: 10 copies"
        result = str(bs)
        self.assertEqual(expected, result)



