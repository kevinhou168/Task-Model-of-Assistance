import multi_pill_sort
import pyhop

def get_goal():
  goal = pyhop.Goal('goal')
  goal.days = {}      # Outer array: Day of week, Inner array: Time of day, Value: # of pills present
  goal.days['Green'] = [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
  goal.days['Blue'] = [[0,2,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [2,0,0,0], [0,0,0,0], [0,0,0,0]]
  #goal.light = 'on'
  return goal

# ph = planners.pyhop.pyhop.Pyhop('hoppity')
# methods.load_methods(ph)
# operators.load_operators(ph)

def get_start_state():
  state = pyhop.State('init')
  state.days = {}
  state.days['Green'] = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
  state.days['Blue'] = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
  state.pills = list(state.days.keys())
  return state

print(get_goal())
pyhop.pyhop(get_start_state(), [('sort_meds', get_goal())], verbose = 2)