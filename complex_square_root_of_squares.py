"""
In algebra, the expression y = sqrt(z) can mean the same as y**2 = z which
usually has two solutions in the complex numbers. Computationally, however,
there is a only a single root calculated, so a computational expression of the
form sqrt(z**2) isn't necessarily equal to z like it is often times evaluated
when solving equations; it may also be the case that
sqrt(z**2) = sqrt((-z)**2) = -z.

For real z, the computational rule is:

    If z >= 0, then sqrt(z**2) = z.
    If z < 0, then sqrt(z**2) = -z.

For complex z, what are the rules? This program evaluates sqrt(z**2) and looks
for cases where sqrt(z**2) != z.

This program will generate a graph that plots a dot for each sample z in the
complex plane where sqrt(z**2) != z. Most dots will be blue, indicating the
inequality. Dots along the imaginary axis will be red indicating that the value
has Re(z) = -0 which produces a different sqrt(z**2) than when Rx(z) = 0.

The rules appear to be:

    If Re(z) >= 0 and Re(z) != -0, then sqrt(z**2) = z.
    If Re(z) < 0 and Re(z) == -0, then sqrt(z**2) = -z.

NEXT STEPS:

* Note that the behavior is dependant on the implementation of both complex
  multiplication and complex square root. Find the definitions of them that
  is used by Python and confirm these results.
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools

XMIN, XMAX = YMIN, YMAX = -4, 4
N = (XMAX - XMIN) * 5 + 1

plt.figure(figsize=(11.5,8))
plt.axhline(xmin = XMIN, xmax = XMAX)
plt.axvline(ymin = YMIN, ymax = YMAX)

points = []
pointsNeg = []
pointsNeg2 = []

for x in np.linspace(XMIN, XMAX, N):
    for y in np.linspace(YMIN, YMAX, N):
        z = x + y * 1.0j
        z2 = z * z
        z0 = np.sqrt(z2)
        if abs(z - z0) < 0.0001:
            points.append(z)
        elif abs(z + z0) < 0.0001:
            pointsNeg.append(z)
        else:
            raise Exception('Sqrt gave strange result.')

def toDeltaFloat(f):
    result = repr(f)
    if result[0] != '-':
        result = '+' + result
    return result

for y in np.linspace(YMIN, YMAX, N):
    z1 = complex('0.0'+toDeltaFloat(y)+'j')
    z1square = z1 * z1
    z1again = np.sqrt(z1square)
    z2 = complex('-0.0'+toDeltaFloat(y)+'j')
    z2square = z2 * z2
    z2again = np.sqrt(z2square)
    if abs(z1again - z2again) < 0.0001:
        pass
    elif abs(z1 - z1again) < 0.0001 and abs(z2 + z2again) < 0.0001:
        pointsNeg2.append(z1)
    else:
        raise Exception('Sqrt gave strange result.')

def plotPoints(pointsBlue, pointsRed):
    xs = [np.real(x) for x in pointsBlue]
    ys = [np.imag(x) for x in pointsBlue]
    plt.scatter(xs, ys, color = '#000088')

    xs = [np.real(x) for x in pointsRed]
    ys = [np.imag(x) for x in pointsRed]
    plt.scatter(xs, ys, color = '#880000')

plotPoints(pointsNeg, pointsNeg2)
plt.show()

def categorize(z, z2):
    if z == z2:
        return 'Equal'
    elif (z - z2) == 0:
        return 'Basically Equal'
    else:
        return 'Different ' + repr(z - z2)

# The following checks show the various ways that negative zero can change
# sqrt(x*x).
for x in [
    # Inputs are equal, outputs are equal, but both are technically different.
    complex('0.0+0.0j'),
    complex('0.0-0.0j'),
    None,

    complex('-0.0-0.0j'),
    complex('-0.0+0.0j'),
    None,

    complex('1.0-0.0j'),
    complex('1.0+0.0j'),
    None,

    complex('1.0-0.0j'),
    complex('1.0+0.0j'),
    complex('3.0-0.0j'),
    complex('3.0+0.0j'),
    None,

    complex('-1.0-0.0j'),
    complex('-1.0+0.0j'),
    complex('-3.0-0.0j'),
    complex('-3.0+0.0j'),
    None,

    # Input is nearly equal, but output is different for these cases.
    complex('0.0+1.0j'),
    complex('-0.0+1.0j'),
    complex('0.0+3.0j'),
    complex('-0.0+3.0j'),
    None,

    # Input is nearly equal, but output is different for these cases.
    complex('-0.0-1.0j'),
    complex('0.0-1.0j'),
    complex('-0.0-3.0j'),
    complex('0.0-3.0j'),
    None,
]:
    if x is None:
        print()
    else:
        print('sqrt(' + repr(x) + '*' + repr(x) + ') = sqrt(' + repr(x*x) + ') = ' + repr(np.sqrt(x*x)) + ' (' + categorize(x, np.sqrt(x*x)) + ')')
