from itertools import permutations

import numpy as np
import matplotlib.pyplot as plt

def generateRootCloud(initial_poly, MAX_POINTS = 100000):
    queue = [initial_poly]
    points = []
    while len(points) < MAX_POINTS:
        poly = queue[0]
        queue[:] = queue[1:]
        roots = np.roots(poly)
        points.extend(roots)
        for perm in permutations(roots):
            next_poly = np.concatenate(([1.0 + 0.0j], perm))
            queue.append(next_poly)
    return points

plt.figure(figsize=(16,16))

def plotPoints(points):
    xs = [np.real(x) for x in points]
    ys = [np.imag(x) for x in points]
    plt.scatter(xs, ys, marker='.', s=1)

points2 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])
#points3 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])
#points4 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.j])

plotPoints(points2)
#plotPoints(points3)
#plotPoints(points4)

plt.show()
