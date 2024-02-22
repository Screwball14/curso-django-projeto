from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_pagination_makes_right_range(self):
        pagination = make_pagination_range(pg_range=20, qty_pages_shown=list(range(0,6)), current_page=1)
        self.assertEqual(pagination, [1,2,3,4])

    def test_page_range_advences_paginationnumber(self):
        pagination = make_pagination_range(pg_range=20, qty_pages_shown=list(range(0,6)), current_page=3)
        self.assertEqual(pagination, [3,4,5,6])