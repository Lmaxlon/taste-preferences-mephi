from collections import deque
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def kmeans_draw(clusters):
    """Drawing kmeans clustering result"""
    colors = deque(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
    fig = plt.figure()
    # Prior to version 1.0.0, the method of creating a 3D axes was different. For those using older versions of matplotlib,
    # change ax = fig.add_subplot(111, projection='3d') to ax = Axes3D(fig).
    ax = Axes3D(fig)
    for cluster in clusters:
        color = colors.popleft()
        for name, coord in cluster:
            x, y, z = coord
            ax.plot3D([x], [y], [z], marker='o', c=color)
    ax.set_xlabel(u'Белки')
    ax.set_ylabel(u'Жиры')
    ax.set_zlabel(u'Углеводы')
    plt.show()
kmeans_draw(K_res)