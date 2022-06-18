from src.syl_gen import *
from src.cat import *

class Command:
    def __init__(self, name):
        self.name = name 

    def execute(self, inputs, categories, symbols, shapes):
        pass

class SymbolCmd(Command):
    def __init__(self):
        super().__init__('symbol')
        
        self.symbol = None

    def execute(self, inputs, categories, symbols, shapes):
        symbol = ''
        cat_name = ''
        category = None

        if inputs[1] != '=':
            print("Error: Symbol definition needs `=`")
            return

        symbol = inputs[2]
        for cat in categories:
            if cat.name == inputs[3]:
                category = cat
                cat_name = cat.name
                break

        if category is None:
            print(f" => Error: category {inputs[3]} does not exit!")
            return

        self.symbol = Shape_Symbol(symbol, cat_name, category.sounds)
        symbols.append(self.symbol)

class CategoryCmd(Command):
    def __init__(self):
        super().__init__('category')

    def execute(self, inputs, categories, symbols, shapes):
        name = ''
        sounds = []

        if inputs[1] != '=':
            print("Error: Category definition needs `=`")
            return

        name = inputs[0]
        sounds = inputs[2:]

        self.category = Category(name, sounds)
        categories.append(self.category)

class ShapeCmd(Command):
    def __init__(self):
        super().__init__('shape')

    def execute(self, inputs, categories, symbols, shapes):
        shape_str = inputs[0]

        self.shape = Shape(shape_str, symbols)
        shapes.append(self.shape)

class SyllableCmd(Command):
    def __init__(self):
        super().__init__('syllable')

    def execute(self, inputs, categories, symbols, shapes):
        shape = []
        qty = 1
        
        if len(inputs) > 1:
            qty = int(inputs[1])
        
        for char in inputs[0]:
            for sym in symbols:
                if sym.sym == char:
                    shape.append(sym)
                    break

        for i in range(qty):
            syllable = Syllable(shape)
            print(repr(syllable))

class ListCmd(Command):
    def __init__(self):
        super().__init__('list')

    def execute(self, inputs, categories, symbols, shapes):
        if inputs[0] == 'symbols':
            for sym in symbols:
                print(repr(sym))
        elif inputs[0] == 'categories':
            for cat in categories:
                print(repr(cat))
        elif inputs[0] == 'shapes':
            for shape in shapes:
                print(repr(shape))
        else:
            print("Could not find specified category!")
            return

