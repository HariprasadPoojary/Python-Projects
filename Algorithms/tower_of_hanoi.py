# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
#   i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.
# Note: Transferring the top n-1 disks from source rod to Auxiliary rod can again be thought of as a fresh problem and can be solved in the same manner.


def tower_hanoi(n_disks, fromm, aux, to):
    """
    Moving disks from  A to C by using B as auxiliary/temp rod
    with rules mentioned above this func
    """
    # Base case
    if n_disks == 1:
        print(f"Move 1 from {fromm} to {to}")
    else:
        # Moving disks from  A to B by using C as auxiliary/temp rod
        tower_hanoi(n_disks - 1, fromm, to, aux)
        print(f"Move {n_disks} from {fromm} to {to}")
        # Moving disks from  B to C by using A as auxiliary/temp rod
        tower_hanoi(n_disks - 1, aux, fromm, to)

    # count to moves = 2ⁿ - 1
    return (2 ** n_disks) - 1


if __name__ == "__main__":
    print(tower_hanoi(3, "A", "B", "C"))
