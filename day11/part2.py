from common import read_monkeys


def main():
    monkeys = read_monkeys(worry_divisor=1)

    moduli = set([m.test_modulus for m in monkeys])
    divisor = 1
    for modulus in moduli:
        divisor *= modulus

    for monkey in monkeys:
        monkey.worry_modulus = divisor

    for _ in range(10000):
        for monkey in monkeys:
            monkey.take_turn(monkeys)

    inspections = sorted([m.inspections for m in monkeys])

    print(inspections[-2] * inspections[-1])


if __name__ == "__main__":
    main()
