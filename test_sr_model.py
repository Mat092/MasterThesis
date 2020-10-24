from Pyron.utils.image import Image
import numpy as np

import matplotlib.pyplot as plt

from PIL import Image as pilmage

import cv2

dompon = Image(filename='../images/dog50_DOMPON.png')
dompof = Image(filename='../images/dog50_DOMPOFF.png')

don = np.asarray(pilmage.open('../images/dog50_DOMPON.png')) / 255
dof = np.asarray(pilmage.open('../images/dog50_DOMPOFF.png')) / 255

old = Image('../images/dog50_sr_old_wdsrx4.png')

plt.imshow(np.abs((np.asarray(old.data) - dompon.data)))


np.allclose(dompon.data, dompof.data)
np.allclose(don, dompon.data)

don = pilmage.open('../images/dog50_DOMPON.png')
dof = pilmage.open('../images/dog50_DOMPOFF.png')

don_cv = cv2.rotate(dompon.data, cv2.ROTATE_90_CLOCKWISE)

dompon = dompon.rotate(-90)
dompof = dompof.rotate(-28)

don = np.asarray(don.rotate(-90)) / 255.
dof = np.asarray(dof.rotate(-28)) / 255.

np.allclose(dompon.data, dompof.data)
np.allclose(don, dompon.data)

np.allclose(don_cv, don)

plt.imshow(don_cv)

plt.imshow(dompon.data)

plt.imshow(don)

plt.imshow(np.abs(don - dompon.data))
plt.imshow(np.abs(dof - dompof.data))
