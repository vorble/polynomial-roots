"""
See first: root_cloud.py

If you follow a process similar to creating the root cloud for a degree 2
polynomial, but that doesn't permute the roots when creating the next
polynomial, then the sequence of roots tends toward a cycle of 12 points in the
complex plane (i.e. most of the time, there are initial polynomial choices that
yield shorter cycles, e.g. cycle of length 1 where your start with a double
root at 0).

This program finds the roots of the polynomial with the quadratic formula that
is taught in algebra class:

roots = (-b -/+ sqrt(b*b - 4*c)) / 2

The roots are ordered with the - root first (- as in the - of the -/+) and that
root is used as the degree 1 term coefficient of the next polynomial. The second
root is used as the constant term.

This program plots the progression of the first root in blue and the progression
of the second root in red. The starting points for each are indicated with a
large dot.

I call this progression of roots for quadratic polynomials the "quadratic root
cycle".
"""

from itertools import permutations

import numpy as np
import matplotlib.pyplot as plt

def find_roots(poly):
    assert len(poly) == 3
    b, c = poly[1:]
    d = np.sqrt(b*b - 4*c)
    return (-b - d) / 2, (-b + d) / 2

def rootIterate(initial_poly, MAX_POINTS = 10000):
    queue = [(initial_poly, 0)]
    pointsB = []
    pointsC = []
    done = 0
    while len(pointsB) < MAX_POINTS:
        poly, generation = queue[0]
        queue[:] = queue[1:]
        b, c = roots = find_roots(poly)
        pointsB.append((b, generation))
        pointsC.append((c, generation))
        next_poly = [1.0 + 0.0j, b, c]
        queue.append((next_poly, generation + 1))
    return pointsB, pointsC

plt.figure(figsize=(11.5,8))

def plotPoints(pointsB, pointsC):
    xs = [np.real(x) for (x, g) in pointsB]
    ys = [np.imag(x) for (x, g) in pointsB]
    plt.plot(xs, ys, color = '#4444AA', linewidth = 1)
    plt.scatter([xs[0]], [ys[0]], marker = 'o', color = '#4444AA')

    xs = [np.real(x) for (x, g) in pointsC]
    ys = [np.imag(x) for (x, g) in pointsC]
    plt.plot(xs, ys, color = '#AA4444', linewidth = 1)
    plt.scatter([xs[0]], [ys[0]], marker = 'o', color = '#AA4444')

pointsB, pointsC = rootIterate([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])

plotPoints(pointsB, pointsC)

plt.show()
