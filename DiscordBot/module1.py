import random

greekLetters = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']

def oof():
    letter = ['','','']
    for x in range(len(letter)):
        letter[x] = greekLetters[random.randint(0, len(greekLetters)-1)]
    return "That's a " + letter[0] + ' ' + letter[1] + ' ' + letter[2] + ' level oof'