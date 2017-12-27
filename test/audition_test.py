import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.audition import it_runs  # noqa
import src  # noqa


class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        self.reversi_t1 = '''
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . B W . . .
        . . . W B . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        B'''
        self.reversi_a1 = '''
        . . . . . . . .
        . . . . . . . .
        . . . . 0 . . .
        . . . B W 0 . .
        . . 0 W B . . .
        . . . 0 . . . .
        . . . . . . . .
        . . . . . . . .
        B'''
        self.reversi_t2 = '''
        . . . . . . . .
        B . . . . . . .
        B W W W W W . .
        B W W B W W . .
        B W W W B W . .
        B W W W W W . .
        B W W W W W . .
        . B B B B B . .
        B'''
        self.reversi_a2 = '''
        . . . . . . . .
        B 0 0 0 0 0 . .
        B W W W W W 0 .
        B W W B W W 0 .
        B W W W B W 0 .
        B W W W W W 0 .
        B W W W W W 0 .
        . B B B B B 0 .
        B'''
        self.reversi_t3 = '''
        . . . . . . . .
        . . . . . . . .
        . . . B . . . .
        . . W B W . . .
        . . . B B . . .
        . B B B . . . .
        . . . . . . . .
        . . . . . . . .
        W'''
        self.reversi_a3 = '''
        . . . . . . . .
        . . 0 . 0 . . .
        . . . B . . . .
        . . W B W . . .
        . . . B B . . .
        . B B B 0 . . .
        . 0 . . . . . .
        . . . . . . . .
        W'''

    def test_it_runs(self):
        self.assertTrue(it_runs())

    def test_bowling(self):
        self.assertEqual(src.bowling.frame_score('X X X X X X X X X X X X'), 300)
        self.assertEqual(src.bowling.frame_score('X X X X X X X X X XXX'), 300)
        self.assertEqual(src.bowling.frame_score('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-'), 90)
        self.assertEqual(src.bowling.frame_score('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'), 150)
        self.assertEqual(src.bowling.frame_score('81 -9 2/ X 63 7- 52 X -6 2/X'), 122)

    def test_reversi(self):
        self.assertEqual(src.reversi.rstrip(src.reversi.legal_moves(self.reversi_t1)),
                         src.reversi.rstrip(self.reversi_a1))
        self.assertEqual(src.reversi.rstrip(src.reversi.legal_moves(self.reversi_t2)),
                         src.reversi.rstrip(self.reversi_a2))
        self.assertEqual(src.reversi.rstrip(src.reversi.legal_moves(self.reversi_t3)),
                         src.reversi.rstrip(self.reversi_a3))


if __name__ == '__main__':
    unittest.main()
