import re
from tqdm import tqdm


class Button:
    def __init__(self, xmod: int, ymod: int):
        self.xmod = xmod
        self.ymod = ymod


class Machine:
    def __init__(self, a_btn: Button, b_btn: Button):
        self.clawx = 0
        self.clawy = 0
        self.a_btn = a_btn
        self.b_btn = b_btn
        self.a_presses = 0
        self.b_presses = 0
        self.paid = 0

    def from_string(s: str):
        lines = s.split("\n")
        # print(lines)
        ax, ay = [int(si) for si in re.findall(r"\d+", lines[0])]
        bx, by = [int(si) for si in re.findall(r"\d+", lines[1])]
        a_btn = Button(xmod=ax, ymod=ay)
        b_btn = Button(xmod=bx, ymod=by)
        return Machine(a_btn=a_btn, b_btn=b_btn)

    def press_a(self):
        self.clawx += self.a_btn.xmod
        self.clawy += self.a_btn.ymod
        self.a_presses += 1
        self.paid += 3

    def press_b(self):
        self.clawx += self.b_btn.xmod
        self.clawy += self.b_btn.ymod
        self.b_presses += 1
        self.paid += 1


def get_solution_costs(
    m: Machine, ploc: tuple[int], most_paid: int = 999999, visited: set = None
) -> int:
    # initialize set of states
    if visited is None:
        visited = set()

    # represent the current state (claw position and amount paid)
    state = (m.clawx, m.clawy, m.paid)
    # stop checking if the state has been visited
    # this is the part I was missing!
    if state in visited:
        return None

    # mark the current state as visited
    visited.add(state)

    # return the amount paid if the claw is at the prize location
    if m.clawx == ploc[0] and m.clawy == ploc[1]:
        # print(f"found solution {m.paid}")
        return m.paid

    # stop recursion if the claw is past the prize or paid exceeds the most paid
    if m.clawx > ploc[0] or m.clawy > ploc[1] or m.paid >= most_paid:
        return None

    # try pressing the A and B buttons
    bm = Machine(a_btn=m.a_btn, b_btn=m.b_btn)
    bm.clawx, bm.clawy, bm.paid = m.clawx, m.clawy, m.paid
    bm.press_b()
    am = Machine(a_btn=m.a_btn, b_btn=m.b_btn)
    am.clawx, am.clawy, am.paid = m.clawx, m.clawy, m.paid
    am.press_a()

    # recursively find solutions
    a_sol = get_solution_costs(m=am, ploc=ploc, most_paid=most_paid, visited=visited)
    b_sol = get_solution_costs(m=bm, ploc=ploc, most_paid=most_paid, visited=visited)

    # filter out invalid and return minimum solution cost
    valid = [cost for cost in (a_sol, b_sol) if cost is not None]
    return min(valid, default=None)


def solve_day13():
    with open("input13.txt") as f:
        smachines = f.read().split("\n\n")

    prizes: list[tuple[int]] = []
    machines: list[Machine] = []
    prize_lines = [sm.splitlines()[2] for sm in smachines]

    # process each prize line and extract numbers
    prizes = [tuple(map(int, re.findall(r"\d+", pl))) for pl in prize_lines]

    # instantiate machines
    for sm in smachines:
        machines.append(Machine.from_string(sm))

    # solve for each machine
    c = 0
    for i in tqdm(range(len(machines))):
        sol = get_solution_costs(m=machines[i], ploc=prizes[i])

        # add to total cost if a valid solution exists
        if sol:
            c += sol
    print(c)


# solve_day13()
