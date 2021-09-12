import numpy as np
import cv2
import matplotlib.pyplot as plt

import sys
print(sys.version)

im = cv2.imread("2017-06-10-20-45-25.jpg")

luminance_vals = im.mean(axis=2).flatten()
l_count, l_bins = np.histogram(luminance_vals, range(0,255))

b_vals = im[:,:, 0].flatten() 
b_count, b_bins = np.histogram(b_vals, range(0,255))
g_vals = im[:,:, 1].flatten() 
g_count, g_bins = np.histogram(g_vals, range(0,255))
r_vals = im[:,:, 2].flatten() 
r_count, r_bins = np.histogram(r_vals, range(0,255))

fig, (axs1, axs2) = plt.subplots(2)
fig.suptitle("Histogram")
axs1.set_title("Luma")
axs1.bar(l_bins[:-1],l_count,width=1, edgecolor='#264d00')

axs2.set_title("RGB")
axs2.bar(b_bins[:-1],b_count,width=1, edgecolor='#0000ff')
axs2.bar(g_bins[:-1],g_count,width=1, edgecolor='#00ff00')
axs2.bar(r_bins[:-1],r_count,width=1, edgecolor='#ff0000')

plt.xlim([0,255])
plt.show()