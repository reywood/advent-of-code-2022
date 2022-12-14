from common import read_monkeys


def main():
    monkeys = read_monkeys(worry_divisor=3)

    for _ in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys)

    inspections = sorted([m.inspections for m in monkeys])

    print(inspections[-2] * inspections[-1])


if __name__ == "__main__":
    main()
