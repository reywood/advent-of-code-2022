import re
from os.path import dirname, join
from typing import List


class Monkey:
    def __init__(
        self,
        items: List[int],
        operation,
        test_modulus: int,
        true_monkey: int,
        false_monkey: int,
        worry_divisor: int,
        worry_modulus: int = None,
    ):
        self.items = items
        self.operation = operation
        self.test_modulus = test_modulus
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.worry_divisor = worry_divisor
        self.worry_modulus = worry_modulus

        self.inspections = 0

    def take_turn(self, all_monkeys):
        while len(self.items) > 0:
            item = self.items.pop(0)
            new_item = self.operation(item) // self.worry_divisor
            if self.worry_modulus:
                new_item %= self.worry_modulus
            self.inspections += 1

            if new_item % self.test_modulus == 0:
                self.throw_to(all_monkeys[self.true_monkey], new_item)
            else:
                self.throw_to(all_monkeys[self.false_monkey], new_item)

    def throw_to(self, monkey, item):
        monkey.items.append(item)


def read_monkeys(worry_divisor):
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        monkeys_text = f.read().strip().split("\n\n")

    return [parse_monkey_text(text, worry_divisor) for text in monkeys_text]


def parse_monkey_text(text: str, worry_divisor: int):
    pattern = (
        r"Monkey \d+:\n"
        r"\s+Starting items: (?P<items>[^\n]+)\n"
        r"\s+Operation: new = old (?P<operation>[^\n]+)\n"
        r"\s+Test: divisible by (?P<test_modulus>[^\n]+)\n"
        r"\s+If true: throw to monkey (?P<true_monkey>[^\n]+)\n"
        r"\s+If false: throw to monkey (?P<false_monkey>[^\n]+)"
    )
    match = re.search(
        pattern,
        text,
    )
    items = [int(item) for item in match.group("items").split(", ")]

    operation_text = match.group("operation")
    operator, operand = operation_text.split()

    return Monkey(
        items=items,
        operation=lambda old: operation(old, operator, operand),
        test_modulus=int(match.group("test_modulus")),
        true_monkey=int(match.group("true_monkey")),
        false_monkey=int(match.group("false_monkey")),
        worry_divisor=worry_divisor,
    )


def operation(old, operator, operand):
    if operand == "old":
        operand = old
    else:
        operand = int(operand)

    if operator == "+":
        return old + operand
    if operator == "*":
        return old * operand

    raise Exception(f"Unknown operator: {operator}")
