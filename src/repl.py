from src.evaluate import *
from src.util import *

# TODO - syllables again.

class Repl:
    categories = []
    symbols    = []
    shapes     = []

    commands = [
        SymbolCmd(),
        CategoryCmd(),
        ShapeCmd(),
        ListCmd()
    ]

    def __init__(self, name, in_file=''):
        self.name = name
        self.running = True
        self.file = ''

        if in_file != '':
            self.file = in_file

            txt = self.read_file()

            for ln in txt:
                self.eval_line(ln)
        else:
            while self.running:
                ln = self.read_line()
                self.eval_line(ln)

    def eval_line(self, ln):
        text = clean_line(ln).split(' ')
        
        if text[0] == 'done':
            self.running = False
            return

        for cmd in self.commands:
            if cmd.name == text[0]:
                cmd.execute(text[1:], self.categories, self.symbols, self.shapes)

    def read_line(self):
        text = input(f'{self.name}> ')

        return text

    def read_file(self):
        text = []
        with open(self.file, 'r') as file:
            text = file.read().split('\n')

        out = []
        for ln in text:
            line = ''
            for i in range(len(ln)):
                if ln[i] == '#':
                    break
                else:
                    line += ln[i]

            if ln == '':
                continue
            else:
                out.append(ln)

        return out

