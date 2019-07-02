import unittest
import game1
import pyhop
import multi_pill_sort


class TestEventFunctions(unittest.TestCase):
    def testAdd(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill')
        self.assertEqual(state.days['green'][0][0], 1)

    def testRemove(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill')
        game1.modify_state(state, 'green', 0, 0, 'remove_pill')
        self.assertEqual(state.days['green'][0][0], 0)


class TestStateLength(unittest.TestCase):
    def testStart(self):
        state = game1.get_start_state()
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 13)

    def testOne(self):
        state = game1.get_start_state()
        game1.modify_state(state, 'green', 0, 0, 'add_pill')
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 12)

    def testEnd(self):
        state = game1.get_start_state()
        state.days['green'] = [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
        state.days['blue'] = [[0,2,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.assertEqual(pyhop.pyhop(state, [('sort_meds', game1.get_goal())]), 0)



# standard python style




if __name__ == '__main__':
    unittest.main()