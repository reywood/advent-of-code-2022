from common import CPU, generate_instructions


def main():
    cpu = CPU()

    signal_strength_observer = SignalStrengthObserver()
    cpu.add_observer(signal_strength_observer)

    for instruction in generate_instructions():
        cpu.execute_instruction(instruction)

    print(signal_strength_observer.signal_strength_sum)


class SignalStrengthObserver:
    def __init__(self):
        self.signal_strength_sum = 0

    def notify(self, cpu: CPU):
        interesting_clock_cycles = [20, 60, 100, 140, 180, 220]

        if cpu.cycles in interesting_clock_cycles:
            self.signal_strength_sum += cpu.cycles * cpu.register_x


if __name__ == "__main__":
    main()
