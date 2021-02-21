from unittest import TestCase
from practice1 import naive_mul


class Test(TestCase):
    def test_naive_mul(self):
        for i in range(100):
            for j in range(100):
                assert naive_mul(i, j) == i * j
