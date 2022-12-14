from common import CPU, generate_instructions


def main():
    cpu = CPU()
    crt = CRT()
    cpu.add_observer(crt)

    for instruction in generate_instructions():
        cpu.execute_instruction(instruction)

    crt.render()


class CRT:
    PIXELS_PER_ROW = 40
    ROWS = 6

    def __init__(self):
        self.pixels = [
            ["." for _ in range(self.PIXELS_PER_ROW)] for _ in range(self.ROWS)
        ]
        self.pixel_position = 0

    def notify(self, cpu: CPU):
        sprite_center_position = cpu.register_x
        sprite_positions = (
            sprite_center_position - 1,
            sprite_center_position,
            sprite_center_position + 1,
        )

        pixel_row = self.pixel_position // self.PIXELS_PER_ROW
        pixel_column = self.pixel_position % self.PIXELS_PER_ROW

        if pixel_column in sprite_positions:
            self.pixels[pixel_row][pixel_column] = "#"

        self.pixel_position += 1

    def render(self):
        for row in self.pixels:
            print("".join(row))


if __name__ == "__main__":
    main()
