"""
See first: quadratic_root_cycle.py

NEEDS WORK

This program searches for exact solutions for the numbers involved in the
quadratic root cycle. It uses the hypothesis that there are 12 pairs of exact
points in the cycle and that the inverse operation of root finding is
multiplying degree-1 binomials.

Assuming the cycle of length 12 exists, then an initial condition for the
iterative process that follows the cycle exactly can be found by studying either
the forward or inverse operation.

To use this program, run it with an argument which is the cycle length of
interest. For example:

    python3 quadratic_root_cycle_solver.py 2

This program is not well optimized and can practically only solve for cycles
of length 2 and 3.

    $ time python3 quadratic_root_cycle_solver.py 2
    [(-1, 0), (b, 0)]

    real    0m0.857s
    user    0m0.626s
    sys     0m0.046s

This output shows that starting with polynomial x**2 - x + 0 or for any b
with polynomial x**2 + b*x + 0 produces the original polynomial after 2 steps:

x**2 + b*x + 0 = (x + b) * x and has roots -b and 0.
x**2 - b*x + 0 = (x - b) * x and has roots b and 0, completing the cycle.

ISSUES:

    $ time python3 quadratic_root_cycle_solver.py 3
    [(b, 0), (-1/2 - sqrt(3)*I/2, 0), (-1/2 + sqrt(3)*I/2, 0)]

    real    0m0.897s
    user    0m0.810s
    sys     0m0.028s

Notice that (b, 0) is part of the solution set for the length 3 cycle, I
would contend that this is only the case when b = 0 by following the example
analysis of the length 2 cycle above.
"""

import sympy as sym
import sys

def fn(b, c):
    return b + c, b * c

cycle = int(sys.argv[1])

b, c = sym.symbols('b c')
ns = [(b, c)]
for i in range(cycle):
    ns.append(fn(*ns[-1]))

eq1 = sym.Eq(ns[cycle][0], ns[0][0])
eq2 = sym.Eq(ns[cycle][1], ns[0][1])
print(sym.solve([eq1,eq2],(b,c)))
