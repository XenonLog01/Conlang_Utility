from src.repl import Repl
import sys

# TODO - Loading files
#        - This can literally just be copying the text over.
# TODO - An std lib
# TODO - Better error handling
#        - Currently it only spits out an error for a few things.
# TODO - Documentation
#        - Both for the code and the language.
# TODO - A way to make syllables generate with random syllable shapes.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        repl = Repl('clng', sys.argv[1])
    else:
        repl = Repl('clng')

