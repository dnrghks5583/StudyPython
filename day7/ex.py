from PIL import Image
import numpy as np
import os

path = 'C:\\Sources\\StudyPython\\day7\\pic'
dir_list = os.listdir(path)
sz = (100, 200)
arr = np.array([])
y = np.array([0, 1])

for img in dir_list :

    img = Image.open(path+ '\\' + img).resize(sz)
    arr.append(np.array(img))

np.savez(path + '2\\exz', x = arr, y = y)
print('done')