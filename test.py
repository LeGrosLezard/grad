import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def sobel_function():
   # Read image
   im = cv2.imread('image.jpg')
   im = np.float32(im) / 255.0
   print(type(im))



   c = 0
   for i in im:
      print(i)
      if c == 10:
         break
      c+=1


   # Calculate gradient 
   gx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=1)
   gy = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=1)
   mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)


   #cv2.imshow("dza", mag)



def reconstruction():
   
   reconstruction = np.ones(shape=[300, 400, 3],
                            dtype=np.uint8)

   for i in range(im.shape[0]):
       for j in range(im.shape[1]):
          reconstruction[i][j][0] = int(numpy_tab[i, j][0] * 255)
          reconstruction[i][j][1] = int(numpy_tab[i, j][1] * 255)
          reconstruction[i][j][2] = int(numpy_tab[i, j][2] * 255)

   cv2.imshow("dzadezada", reconstruction)



def noob_fonction():
   print("")
   print("")
   im = cv2.imread('image.jpg')
   print(type(im))


   liste = []
   for i in im:
      liste.append(i/255)

   numpy_tab = np.asarray(liste)






   
sobel_function();noob_fonction();








