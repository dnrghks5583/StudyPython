import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Sources\\StudyPython\\day7\\pic2'

imgs = np.load(path + '\\exz.npz')

img = imgs['x']
y = imgs['y']

for pic in img :
    plt.imshow(pic)
    plt.show()