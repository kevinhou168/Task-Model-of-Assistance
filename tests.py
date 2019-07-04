import unittest
import game1
import pyhop
import multi_pill_sort


class TestEventFunctions(unittest.TestCase):
    def testModifyAdd(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill', 1)
        self.assertEqual(state.days['green'][0][0], 1)

    def testModifyRemove(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill', 1)
        game1.modify_state(state, 'green', 0, 0, 'remove_pill', 1)
        self.assertEqual(state.days['green'][0][0], 0)

    def testRemoveFromEmptySpot(self):
        state = game1.get_start_state()
        self.assertFalse(multi_pill_sort.remove_pill(state, 'green', 0, 0))


class TestStateLength(unittest.TestCase):
    def testStart(self):
        state = game1.get_start_state()
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 13)

    def testOne(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill', 1)
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 12)

    def testEnd(self):
        state = game1.get_start_state()
        state.days['green'] = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
                               [1, 0, 0, 0]]
        state.days['blue'] = [[0, 2, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0],
                              [0, 0, 0, 0]]
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 0)

    def testOneMoreThanGoal(self):
        state = game1.get_start_state()
        state.days['green'] = [[2, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
                               [1, 0, 0, 0]]
        state.days['blue'] = [[0, 2, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0],
                              [0, 0, 0, 0]]
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 1)


if __name__ == '__main__':
    unittest.main()