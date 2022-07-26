import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)

fig, axes = plt.subplots(1,2,figsize=(8,4))
ax = axes.ravel()
ax[0].imshow(gambarasli)
ax[0].set_title("Gambar Asli")
ax[1].imshow(gambarabu, cmap=plt.cm.gray)
ax[1].set_title("Gambar Abu")
fig.tight_layout()
plt.show()