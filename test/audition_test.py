import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.audition import it_runs  # noqa
from src.bowling import frame_score  # noqa


class TestMarkdownPy(unittest.TestCase):

    def test_it_runs(self):
        self.assertTrue(it_runs())

    def test_bowling(self):
        self.assertEqual(frame_score('X X X X X X X X X X X X'), 300)
        self.assertEqual(frame_score('X X X X X X X X X XXX'), 300)
        self.assertEqual(frame_score('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-'), 90)
        self.assertEqual(frame_score('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'), 150)
        self.assertEqual(frame_score('81 -9 2/ X 63 7- 52 X -6 2/X'), 122)


if __name__ == '__main__':
    unittest.main()
