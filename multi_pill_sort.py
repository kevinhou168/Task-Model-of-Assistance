import pyhop


# operators

# helper function to be used in just about every operator
# the light is on iff the power is on, the light is plugged in, the switch is on, and the bulb is good

def add_pill(state, pill, day, time):
    state.days[str(pill)][int(day)][int(time)] += 1
    return state


def remove_pill(state, pill, day, time):
    if state.days[str(pill)][int(day)][int(time)] > 0:
        state.days[str(pill)][int(day)][int(time)] -= 1
        return state
    else:
        raise Exception('Removing from an empty spot!')


pyhop.declare_operators(add_pill, remove_pill)


# methods

def one_pill_at_a_time(state, goal):
    pill = state.pills[0]
    state.pills.pop(0)
    if len(state.pills) == 0:
        return [('sort_pill', pill, 0, goal)]
    else:
        return [('sort_pill', pill, 0, goal), ('sort_meds', goal)]


def one_day_at_a_time(state, pill, day, goal):
    if day == len(state.days[pill]) - 1:
        return [('fix_day', pill, day, goal)]
    else:
        return [('fix_day', pill, day, goal), ('sort_pill', pill, day + 1, goal)]


def wrong_time(state, pill, day, goal):
    numTimes = len(state.days[pill][day])  # Returns number of times in the day ex.(lunch, dinner) = 2
    for time in range(0, numTimes):  # Iterates through times of day
        if state.days[pill][day][time] < goal.days[pill][day][time]:  # If state time's # of pills less than goal time's # of pills
            for otherTime in range(0, numTimes):  # Iterate through times of say again
                if time != otherTime and state.days[pill][day][otherTime] > goal.days[pill][day][
                    otherTime]:  # If time is different and other time has more pills during state
                    return [('remove_pill', pill, day, otherTime), ('add_pill', pill, day, time),
                            ('fix_day', pill, day, goal)]  # Remove pill from other time, put at correct time
    return False


def missing_pill(state, pill, day, goal):
    numTimes = len(state.days[pill][day])
    for time in range(0, numTimes):
        if state.days[pill][day][time] < goal.days[pill][day][time]:
            for otherTime in range(0, numTimes):
                if time != otherTime and state.days[pill][day][otherTime] <= goal.days[pill][day][otherTime]:
                    return [('add_pill', pill, day, time), ('fix_day', pill, day, goal)]
    return False


def extra_pill(state, pill, day, goal):
    numTimes = len(state.days[pill][day])
    for time in range(0, numTimes):
        if state.days[pill][day][time] > goal.days[pill][day][time]:
            for otherTime in range(0, numTimes):
                if time != otherTime and state.days[pill][day][otherTime] >= goal.days[pill][day][otherTime]:
                    return [('remove_pill', pill, day, time), ('fix_day', pill, day, goal)]
    return False


def no_problem(state, pill, day, goal):
    numTimes = len(state.days[pill][day])
    for time in range(0, numTimes):
        if state.days[pill][day][time] != goal.days[pill][day][time]:
            return False
    return []


pyhop.declare_methods('sort_meds', one_pill_at_a_time)
pyhop.declare_methods('sort_pill', one_day_at_a_time)
pyhop.declare_methods('fix_day', wrong_time, missing_pill, extra_pill, no_problem)








