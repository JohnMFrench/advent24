import time
import traceback
import os


class Loc:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_gps(self) -> int:
        return 100 * self.y + self.x

    def __eq__(self, other) -> bool:
        if isinstance(other, Loc):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


LEFT = Loc(x=-1, y=0)
RIGHT = Loc(x=1, y=0)
UP = Loc(x=0, y=-1)
DOWN = Loc(x=0, y=1)
DIRS = (
    LEFT,
    RIGHT,
    UP,
    DOWN,
)
dm = {"<": LEFT, "^": UP, ">": RIGHT, "v": DOWN}


class Robot:
    def __init__(self, loc: Loc, last_dir: str = "@"):
        self.loc = loc
        self.last_dir = last_dir  # direction after last move


class Map:
    def __init__(self, w: int, h: int, boxes: set[Loc], robot: Robot):
        self.w = w
        self.h = h
        self.boxes = boxes
        self.robot = robot
        self.walls: set[Loc] = set()
        # fill in the default wall locations
        for y in range(self.h):
            for x in range(self.w):
                if x == 0 or y == 0 or x == self.w - 1 or y == self.h - 1:
                    self.walls.add(Loc(x=x, y=y))

    def get_cell_str(self, loc: Loc) -> str:
        if self.robot.loc == loc:
            return f"\033[36m{self.robot.last_dir}\033[0m"  # cyan
        elif loc in self.boxes:
            return "\U0001F4E6"
        elif loc in self.walls:
            return "\U0001F9F1"
        else:
            return " "

    def parse_string(s: str):
        grid = s.splitlines()
        boxes: set[Loc] = set()
        walls: set[Loc] = set()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "O":
                    boxes.add(Loc(x=x, y=y))
                elif grid[y][x] == "@":
                    robot = Robot(loc=Loc(x=x, y=y))
                elif grid[y][x] == "#":
                    walls.add(Loc(x=x, y=y))
        m = Map(w=len(grid[0]), h=len(grid), boxes=boxes, robot=robot)
        m.walls = walls
        return m

    def get_focused_view(self, vw: int, vh: int) -> str:
        vx, vy = self.robot.loc.x - (vw // 2), self.robot.loc.y - (vh // 2)
        view = ""
        for y in range(vh):
            for x in range(vw):
                view += self.get_cell_str(Loc(x=vx + x, y=vy + y))
            view += "\n"
        return view

    def is_pushable_in_dir(self, xmod: int, ymod: int, loc: Loc) -> bool:
        # loc.x = loc.x + xmod
        # loc.y = loc.y + ymod
        # print(
        # f"checking ({loc.x}, {loc.y}) {self.get_cell_str(loc)} moving ({xmod}, {ymod})"
        # )
        if loc not in self.boxes:
            return False
        loc.x += xmod
        loc.y += ymod

        while loc not in self.walls:
            if loc not in self.boxes:
                return True
            else:
                loc.x += xmod
                loc.y += ymod
        return False

    def is_robot_movable_in_dir(self, xmod: int, ymod: int, loc: Loc) -> bool:
        curx = loc.x + xmod
        cury = loc.y + ymod
        while Loc(x=curx, y=cury) not in self.walls:
            if Loc(x=curx, y=cury) not in self.boxes:
                return True
            else:
                curx += xmod
                cury += ymod
        return False

    def proc_move(self, s: str):
        """
        mutative function that...
            - updates the robot's direction
            - keeps robot in same position if movement not possible
            - pushes any boxes in that direction including adjacent boxes

        Args:
            s (str): representing next command, <, >, ^, or v
        """
        if len(s) != 1:
            print(f"input error ({s})")
        self.robot.last_dir = s

        xmod, ymod = dm[s].x, dm[s].y
        curx, cury = self.robot.loc.x, self.robot.loc.y
        if not self.is_robot_movable_in_dir(
            xmod=xmod, ymod=ymod, loc=Loc(x=curx, y=cury)
        ):
            # print(f"robot can't move {self.robot.last_dir} from {self.robot.loc}")
            return
        else:
            self.robot.loc = Loc(x=self.robot.loc.x + xmod, y=self.robot.loc.y + ymod)
            curx = self.robot.loc.x
            cury = self.robot.loc.y

            # find pushable boxes
            pushable: list[Loc] = []
            # s = self.to_str()
            while self.is_pushable_in_dir(
                xmod=xmod, ymod=ymod, loc=Loc(x=curx, y=cury)
            ):
                pushable.append(Loc(x=curx, y=cury))
                curx += xmod
                cury += ymod

            new_boxes = set()

            # update the location of the pushed boxes
            for pi in pushable:
                self.boxes.remove(Loc(x=pi.x, y=pi.y))
                new_boxes.add(Loc(x=pi.x + xmod, y=pi.y + ymod))
            self.boxes ^= new_boxes

    def to_str(self) -> str:
        numline = "".join([str(i) for i in range(self.w)]) + "\n"
        wall = "#"
        output = ""
        for y in range(self.h):
            for x in range(self.w):
                if Loc(x=x, y=y) in self.walls:
                    output += wall
                elif Loc(x=x, y=y) in self.boxes:
                    output += "0"
                elif Loc(x=x, y=y) == self.robot.loc:
                    output += self.robot.last_dir
                else:
                    output += "."
            output += f"{y}\n"
        return numline + output + numline


def solvept1():
    with open("input15.txt") as f:
        smap, smoves = f.read().split("\n\n")
    map: Map = Map.parse_string(smap)
    print(map.to_str())
    smoves = smoves.replace("\n", "")
    # moves = "<<<^^^>>>vvv"

    print(map.is_pushable_in_dir(0, -1, Loc(x=3, y=1)))
    print(map.is_pushable_in_dir(1, 0, Loc(x=8, y=1)))
    print(map.is_pushable_in_dir(0, 1, Loc(x=5, y=8)))
    print(map.is_pushable_in_dir(0, 1, Loc(x=5, y=7)))
    print(map.is_pushable_in_dir(-1, 0, Loc(x=4, y=7)))

    try:
        for ix, m in enumerate(smoves):
            map.proc_move(s=m)
            os.system("cls")
            per = "{:.2f}".format((ix / len(smoves)) * 100)
            print(f"move {ix} ({per}%)")
            print(map.get_focused_view(25, 12))
            time.sleep(0.05)
    except Exception:
        print(map.to_str())
        print(traceback.print_exc())

    # calculate gps total
    gps_coords = 0
    for b in map.boxes:
        gps_coords += b.get_gps()
    print(gps_coords)


solvept1()
