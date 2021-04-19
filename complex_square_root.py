"""
This program generates a visual guide for how the complex square root function
behaves for values in the complex plane. The program maps points from the four
quadrants of the complex plane to their square root, correlated by color. The
regularly spaced points are the input values and the points in the resulting
"curved star" shape are the square roots. An extra circle is provided in the
negative real portion of the graph along with its points' image under sqrt()
on the right.

Notice that the complex square root always produces a value which has a non-
negative real part.

Notice that sqrt() is not continuous when crossing the negative portion of the
real axis.
"""

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

N = 91

# Generate a grid of points in the complex plane in the shape of a "box".
def box(corner, width, height, slices):
    xs = np.linspace(np.real(corner), np.real(corner) + width, slices)
    ys = np.linspace(np.imag(corner), np.imag(corner) + height, slices)
    result = reduce(lambda result, y: np.append(result, 1.0j * y + xs), ys)
    return result

def circle(radius, slices):
    return radius * np.exp(np.linspace(0.0, 2 * np.pi, slices) * 1.0j)

preimage = box(-2.0 - 2.0j, 4.0, 4.0, N)

# Abbreviation "pi": pre-image.
piA = [x for x in preimage if np.real(x) >= 0 and np.imag(x) >= 0]
piB = [x for x in preimage if np.real(x) >= 0 and np.imag(x) < 0]
piC = [x for x in preimage if np.real(x) < 0 and np.imag(x) >= 0]
piD = [x for x in preimage if np.real(x) < 0 and np.imag(x) < 0]
piCurve = (-1.0 + 0.0j) + circle(0.5, N)
# Abbreviation "i": image.
iA, iB, iC, iD = np.sqrt(piA), np.sqrt(piB), np.sqrt(piC), np.sqrt(piD)
iCurve = np.sqrt(piCurve)

plt.figure(figsize=(11, 8.5))
def show(points, color, s=1):
    plt.scatter(np.real(points), np.imag(points), marker='.', color=color, s=s)
show(piA, (0.9, 0.7, 0.7), s = 16)
show(piB, (0.7, 0.7, 0.9), s = 16)
show(piC, (0.9, 0.7, 0.9), s = 16)
show(piD, (0.7, 0.9, 0.7), s = 16)
show(piCurve, (0.2, 0.2, 0.2), s = 16)
show(iA, (0.5, 0.0, 0.0))
show(iB, (0.0, 0.0, 0.5))
show(iC, (0.5, 0.0, 0.5))
show(iD, (0.0, 0.5, 0.0))
show(iCurve, (0.0, 0.0, 0.0), s = 16)
plt.show()
