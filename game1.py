import multi_pill_sort
import pyhop
from copy import deepcopy


def get_goal():
    goal = pyhop.Goal('goal')
    goal.days = {}      # Outer array: Day of week, Inner array: Time of day, Value: # of pills present
    goal.days['green'] = [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
    goal.days['blue'] = [[0,2,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [0,0,0,0]]
    #goal.light = 'on'
    return goal


# ph = planners.pyhop.pyhop.Pyhop('hoppity')
# methods.load_methods(ph)
# operators.load_operators(ph)

def get_start_state():
    state = pyhop.State('init')
    state.days = {}
    state.days['green'] = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    state.days['blue'] = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    state.pills = list(state.days.keys())
    return state


def modify_state(state, pill, day, time, action):
    if action == 'add_pill':
        return multi_pill_sort.add_pill(state, pill, day, time)
    elif action == 'remove_pill':
        return multi_pill_sort.remove_pill(state, pill, day, time)
    else:
        raise Exception('Not a valid action, check for typo in events!')


def result_length(state, event):
    modify_state(state, event[0], event[1], event[2], event[3])
    temp_state = deepcopy(state)
    pyhop.pyhop(temp_state, [('sort_meds', get_goal())], verbose=1)


def main():
    events = [['green', 1, 0, 'add_pill'], ['green', 2, 0, 'add_pill']]
    start_state = get_start_state()
    for event in events:
        result_length(start_state, event)


if __name__ == '__main__':
    main()