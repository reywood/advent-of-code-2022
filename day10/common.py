from abc import ABC, abstractmethod
from os.path import dirname, join


class CPU:
    def __init__(self):
        self.register_x = 1
        self.cycles = 0
        self._current_instruction = None
        self._observers = []

    def tick(self):
        self.cycles += 1

        self.notify_observers()

        if self._current_instruction:
            self._current_instruction.tick(self)
            if self._current_instruction.is_complete:
                self._current_instruction = None

    def execute_instruction(self, instruction: "Instruction"):
        if self._current_instruction:
            raise Exception("An instruction is already in progress")

        self._current_instruction = instruction
        while self._current_instruction:
            self.tick()

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.notify(self)


class Instruction(ABC):
    def __init__(self, ticks_needed: int):
        self.ticks_needed = ticks_needed
        self.ticks_counted = 0

    @property
    def is_complete(self):
        return self.ticks_needed == self.ticks_counted

    def tick(self, cpu: CPU):
        self.ticks_counted += 1

        if self.is_complete:
            self.execute(cpu)

    @abstractmethod
    def execute(self, cpu: CPU):
        pass


class NoopInstruction(Instruction):
    def __init__(self):
        super().__init__(1)

    def execute(self, cpu: CPU):
        pass


class AddXInstruction(Instruction):
    def __init__(self, v):
        super().__init__(2)
        self.v = v

    def execute(self, cpu: CPU):
        cpu.register_x += self.v


def generate_instructions():
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            if line.strip() == "noop":
                yield NoopInstruction()

            elif line.startswith("addx "):
                v = int(line.strip().split()[1])
                yield AddXInstruction(v)
