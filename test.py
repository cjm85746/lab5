import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
    def test_other_player(self):
        player = 'O'
        self.assertEqual(logic.other_player(player), 'X')
    
    def test_make_empty_board(self):
        player = 'O'
        self.assertEqual(logic.other_make_empty_board(), 'X')

    

if __name__ == '__main__':
    unittest.main()