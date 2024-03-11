from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_pagination_makes_right_range(self):
        pagination = make_pagination_range(pg_range=list(range(1,21)), qty_pages_shown=4, current_page=1)
        self.assertEqual([1,2,3,4], pagination) 

        pagination = make_pagination_range(pg_range=list(range(1,21)), qty_pages_shown=4, current_page=2)
        self.assertEqual([1,2,3,4], pagination)


    def test_page_range_advences_paginationnumber(self):
        pagination = make_pagination_range(pg_range=list(range(1,21)), qty_pages_shown=4, current_page=3)
        self.assertEqual([2,3,4,5], pagination)

        pagination = make_pagination_range(pg_range=list(range(1,21)), qty_pages_shown=4, current_page=4)
        self.assertEqual([3,4,5,6], pagination )

    def test_page_does_not_passes_range(self):
        pagination = make_pagination_range(pg_range=list(range(1,21)), qty_pages_shown=4, current_page=20)
        self.assertEqual([17,18,19,20], pagination)

    def test_page_throws_error_if_exceeded(self):
        with self.assertRaises(ValueError):
            make_pagination_range(qty_pages_shown=4, current_page=21, pg_range=list(range(1,21)))