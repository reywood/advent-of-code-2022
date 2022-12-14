from common import CrateStacks, Move, read_stacks_and_moves


def main():
    crate_stacks, moves = read_stacks_and_moves()

    crate_mover = CrateMover9001()
    for move in moves:
        crate_mover.execute_move(crate_stacks, move)

    print(crate_stacks.stacks)

    print("".join([stack[-1] for stack in crate_stacks.stacks]))


class CrateMover9001:
    def execute_move(self, stacks: CrateStacks, move: Move):
        crates_to_move = stacks.remove_crates_from_stack(move.from_stack, move.count)
        stacks.add_crates_to_stack(move.to_stack, crates_to_move)


if __name__ == "__main__":
    main()
