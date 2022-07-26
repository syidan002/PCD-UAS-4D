from PIL import Image
from matplotlib import pyplot as plt

# ambil image asli
original = Image.open(".\logounmer.jpg")

flipvertical = original.transpose(method=Image.FLIP_TOP_BOTTOM)
# simpan
flipvertical.save('flipvertical.png')

fliphorizontal =  original.transpose(method=Image.FLIP_LEFT_RIGHT)
fliphorizontal.save('fliphorizontal.png')


#membuat tampilan plot beberapa image
fig, axes = plt.subplots(1,3, figsize=(8,4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(flipvertical)
ax[1].set_title("flipvertical")
ax[2].imshow(fliphorizontal)
ax[2].set_title("fliphorizontal")

fig.tight_layout()
plt.show()
