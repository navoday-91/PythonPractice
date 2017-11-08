# --------------
# User Instructions
# 
# Modify the function compile_formula so that the function 
# it returns, f, does not allow numbers where the first digit
# is zero. So if the formula contained YOU, f would return 
# False anytime that Y was 0 

import re
import itertools
import string


def compile_formula(formula, verbose=True):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z0-9]', formula))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z0-9]+)', formula))
    body = ''.join(tokens)
    print(tokens)
    print(parms)
    print(body)
    if firstletters:
        tests = ' and '.join(L + '!=0' for L in firstletters)
        body = '%s and %s' % (tests, body)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters


def compile_word(word):
    print(word)
    if word.isupper():
        terms = [('%s*%s' % (10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            return "There was an Arithmetic Error! Please Retry."


def test():
    print(faster_solve('NORTH + EAST + SOUTH + WEST == EARTH'))

test()