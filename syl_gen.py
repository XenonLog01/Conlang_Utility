import random

class Shape_Symbol:
    def __init__(self, symbol, cat_name, category):
        self.sym = symbol
        self.cat = category
        self.name = cat_name

    def __repr__(self):
        return f" => symbol {self.sym} :: {self.name}"

class Shape:
    def __init__(self, shape, symbols):
        self.shape = []
        for sym in shape.upper():
            for symbol in symbols:
                if sym == symbol.sym:
                    self.shape.append(symbol)
                    break

    def __repr__(self):
        shap = ''
        for shp in self.shape:
            shap += shp.sym

        return f' => shape {shap}'

class Syllable:
    def __init__(self, shape):
        self.shape = shape
        self.syl = ''

        for sym in shape:
            self.syl += random.choice(sym.cat)

    def __repr__(self):
        return f' => syllable :: {self.syl}'

if __name__ == "__main__":
    consonants = ['p', 'b', 't', 'k', 's', 'x', 'l', 'm', 'n']
    obstruents = consonants[:4]
    nasals = ['m', 'n']
    vowels = ['i', 'u', 'e', 'o', 'a']

    cons_shape = Shape_Symbol('C', 'consonant', consonants)
    obst_shape = Shape_Symbol('S', 'obstruent', obstruents)
    nasl_shape = Shape_Symbol('N', 'nasal', nasals)
    vowel_shape = Shape_Symbol('V', 'vowel', vowels)

    shapes = [cons_shape, obst_shape, nasl_shape, vowel_shape]

    shape_cvc = Shape('CVN', shapes)

