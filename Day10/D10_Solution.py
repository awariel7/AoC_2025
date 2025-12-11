from itertools import combinations
from collections import deque
from ortools.sat.python import cp_model
def light_diagram_to_mask(s: str) -> int:
    mapping = {".": "0", "#": "1"}
    bin_str = "".join(mapping[ch] for ch in s)
    return int(bin_str, 2)

def start_the_machine(LEN_L_DIAG, button_wiring) -> int:
    got_combination = False
    # direct solutions with combinations check
    for k in range(1, LEN_L_DIAG):
        for ss in combinations(button_wiring, k):
            cur = start_diagram
            for s in ss:
                cur = cur ^ s
            if cur == light_diagram:
                got_combination = True
                break
        if got_combination:
            return k

def set_joltage_requirements_bfs(target_joltage, button_wiring_codes) -> int:
    # too much combinations here, switch to another approach
    target = tuple(target_joltage)
    k = len(target_joltage)
    start = (0,) * k

    # BFS
    q = deque([start])
    dist = {start: 0}
    while q:
        # get the state
        state = q.popleft()
        # get current steps
        steps = dist[state]
        # if we've found solution - stop
        if state == target:
            return steps
        # else - push every button for current state
        for b in button_wiring_codes:
            new_state = list(state)
            ok = True
            for idx in b:
                # add up num for position
                new_state[idx] += 1
                # check whether current adding overflowed target
                if new_state[idx] > target_joltage[idx]:
                    ok = False
                    break
            if not ok:
                # if too much already - try next button
                continue

            new_state = tuple(new_state)
            # remember the state if it wasn't
            if new_state not in dist:
                dist[new_state] = steps + 1
                # add state in deque for the next check (try to push all buttons for the state)
                q.append(new_state)


# TODO: is it necessary to use cp sat?
def set_joltage_requirements_cp_sat(target, button_wiring_codes, verbose=True):
    R = len(target)
    M = len(button_wiring_codes)

    model = cp_model.CpModel()

    # Set Top pushes
    ub = max(target) if target else 0
    x = [model.NewIntVar(0, ub, f"x_{j}") for j in range(M)]

    # Ограничения по разрядам
    for i in range(R):
        contributing = [x[j] for j, btn in enumerate(button_wiring_codes) if i in btn]
        if not contributing:
            if target[i] != 0:
                return None
        else:
            model.Add(sum(contributing) == target[i])

    # Minimize pushes
    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10.0

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        if verbose:
            print("No solution")
        return None

    presses = [solver.Value(x[j]) for j in range(M)]
    min_presses = sum(presses)

    if verbose:
        print("Min presses:", min_presses)
        for j, p in enumerate(presses):
            if p:
                print(f"Button {j} {button_wiring_codes[j]} -> {p}")

    return min_presses

# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

button_wiring = []
joltage_requirements = []
total_sum = 0
total_sum_2 = 0
c = 0
for l in lines:
    LEN_L = len(l)
    sbi = l.index(']')
    LEN_L_DIAG = len(l[1:sbi])
    cbi = l.index('{')
    # Part 1
    light_diagram = light_diagram_to_mask(l[1:sbi])
    start_diagram = light_diagram_to_mask('.' * LEN_L_DIAG)
    buttons = [r for r in l[sbi + 2:cbi-1].split()]
    button_wiring_codes = [{int(n) for n in b[1:len(b)-1].split(',')} for b in buttons]
    button_wiring = []
    for bwc in button_wiring_codes:
        diagram = ['.'] * LEN_L_DIAG
        for n in bwc:
            diagram[n] = '#'
        button_wiring.append(light_diagram_to_mask(''.join(diagram)))
    total_sum += start_the_machine(LEN_L_DIAG, button_wiring)
    print(f'Line {c}: Part 1 finished')
    # Part 2
    joltage_requirements = [int(t) for t in l[cbi+1:LEN_L-1].split(',')]
    #total_sum_2 += set_joltage_requirements_bfs(joltage_requirements, button_wiring_codes)
    total_sum_2 += set_joltage_requirements_cp_sat(joltage_requirements, button_wiring_codes)
    print(f'Line {c}: Part 2 finished')
    c += 1
print(f'Part 1: {total_sum}')
print(f'Part 2: {total_sum_2}')

