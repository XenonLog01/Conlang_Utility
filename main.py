from syl_gen import Shape_Symbol, Shape, Syllable
from cat import Category
import sys

# TODO - Loading files
#        - This can literally just be copying the text over.
# TODO - An std lib
# TODO - Better error handling
#        - Currently it only spits out an error for a few things.
# TODO - Documentation
#        - Both for the code and the language.
# TODO - A way to make syllables generate with random syllable shapes.

shapes = []
symbols = []
categories = []

def rm_extra_whitespace(text):
    last_was_ws = False
    in_comment = False
    out = ''
    for t in text:
        if t in ' \t':
            if last_was_ws:
                continue
            else:
                last_was_ws = True
        else:
            last_was_ws = False

        if in_comment:
            continue
        else:
            if t == '#':
                in_comment = True
            else:
                out += t

    return out

def parse_text(txt):
    text = rm_extra_whitespace(txt).split(' ')

    if text[0] == 'symbol':
        gen_symbol(text[1:])
    elif text[0] == 'category':
        gen_cat(text[1:])
    elif text[0] == 'shape':
        gen_shape(text[1:])
    elif text[0] == 'list':
        list_out(text[1])
    elif text[0] == 'syllable':
        gen_syllable(text[1:])
    elif text[0] == 'load':
        load_file(text[1:])
    elif text[0] == '':
        pass
    else:
        print(f"Invalid Command {text[0]}!")

def load_file(inputs):
    f = inputs[0]
    text = []

    with open(f, 'r') as fl:
        text = fl.read().split('\n')

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
            parse_text(ln)

def gen_syllable(inputs):
    # syllable <shape> <qty>
    shape = []
    qty = 0
    try:
        qty = int(inputs[1])
    except Exception:
        qty = 1

    for char in inputs[0]:
        for sym in symbols:
            if sym.sym == char:
                shape.append(sym)
                break

    for i in range(qty):
        syllable = Syllable(shape)
        print(repr(syllable))

def gen_symbol(inputs):
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

    symbols.append(Shape_Symbol(symbol, cat_name, category.sounds))

def gen_shape(inputs):
    shape_str = inputs[0]

    shapes.append(Shape(shape_str, symbols))

def gen_cat(inputs):
    name = ''
    sounds = []

    if inputs[1] != '=':
        print("Error: Category definition needs `=`")
        return
    name = inputs[0]
    sounds = inputs[2:]

    categories.append(Category(name, sounds))

def list_out(thing):
    if thing == 'symbols':
        for sym in symbols:
            print(repr(sym))
    elif thing == 'categories':
        for cat in categories:
            print(repr(cat))
    elif thing == 'shapes':
        for shape in shapes:
            print(repr(shape))
    else:
        print("Could not find specified category!")
        return

def main():
    while True:
        txt = input('clng> ')
        if txt.lower() == 'done' or txt.lower() == 'quit': break
        parse_text(txt)

def run_file():
    text = []
    with open(sys.argv[1], 'r') as file:
        text = file.read().split('\n')

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
            parse_text(ln)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_file()
    else:
        main()

