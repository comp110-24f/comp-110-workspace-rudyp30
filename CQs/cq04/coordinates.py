__author__ = "730767675"


def get_coords(xs: str, ys: str) -> None:
    """sends back letters of string in pairs"""
    idx_x: int = 0

    while idx_x < len(xs):  # first loop allows for control of inside
        idx_y: int = 0  # so that it goes back to 0 after running the nested loop
        while idx_y < len(ys):
            print("(" + xs[idx_x] + "," + ys[idx_y] + ")")
            idx_y += 1  # produces [0] and [1]
        idx_x += 1  # added outside of nested loop so it can go back through with [1]


get_coords("12", "34")
