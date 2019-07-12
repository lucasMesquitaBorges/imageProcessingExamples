import cv2
import numpy as np

def rgb2gray(rgb):
	r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	return gray

# img = cv2.imread('thermo-imaging.jpg')
img = cv2.imread('field.jpg')
# img = cv2.imread('panda.jpg')

size = img.shape
if len(size)==3:
	img = rgb2gray(img)

newImg = np.empty([len(img[:, 0]), len(img[0, :]), 3])

print(img.shape)
print(newImg.shape)

for i in range(len(img[0, :])):
	for j in range(len(img[:, 0])):
		newImg[j, i, 1] = img[j, i]
		if(img[j, i] > 150):
			newImg[j, i, 2] = img[j, i]
			newImg[j, i, 0] = round(img[j, i] / 3)
		else:
			newImg[j, i, 0] = img[j, i]
			newImg[j, i, 2] = round(img[j, i] / 3)

# print(newImage)
cv2.imwrite('pseudoColoring.jpg', newImg)
