""" Account in coding game !  https://www.codingame.com/profile/26a6c9ea9318d0aae4416bb2c86d513c6337854 """
class CGXFormatter:
    def __init__(self):
        self.input_indent = 4
        self.inside_string = False
        self.not_printed = True
        self.total_indent_for_count = 0
        self.number_of_line = 0

    def read_char(self, character: str):
        if self.inside_string:
            if character == '\'':
                self.inside_string = False
            self.print_char(character)
        else:
            self.read_char_outside_string(character)

    def read_char_outside_string(self, character: str):
        if character == ' ' or character == '\t':
            return
        if character == '\'':
            self.inside_string = True
            self.print_char(character)
        elif character == '(':
            if not self.not_printed:
                self.print_not_printed()
            self.print_char(character)
            self.print_not_printed()
            self.total_indent_for_count += self.input_indent
        elif character == ')':
            self.total_indent_for_count -= self.input_indent
            if not self.not_printed:
                self.print_not_printed()
            self.print_char(character)
        elif character == ';':
            self.print_char(character)
            self.print_not_printed()
        else:
            self.print_char(character)

    def read_lines(self):
        self.number_of_line = int(input())
        for _ in range(self.number_of_line):
            line = input()
            for character in line:
                self.read_char(character)

    def print_not_printed(self):
        print()
        self.not_printed = True
   
    def print_char(self, character: str):
        if self.not_printed:
            for _ in range(self.total_indent_for_count):
                print(' ', end='')
            self.not_printed = False
        print(character, end='')


if __name__ == "__main__":
    formatter = CGXFormatter()
    formatter.read_lines()