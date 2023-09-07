#bir görüntüyü 2 boyutlu evrişim matrisiyle bulanıklaştırma
import cv2
import numpy as np

image= cv2.imread('/Users/bilal/Desktop/blender.jpg')

kernel1 = np.ones((5,5), np.float32)/30

img = cv2.filter2d(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original',image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.destroyAllWindows()


##Yumuşatma Filtresi
import cv2
import numpy as np

path = r'/Users/bilal/Desktop/blender.jpg'

img = cv2.imread(path)

im1 = cv2.blur(img(5,5))
im2 = cv2.boxFilter(img,-1,(2,2),normalize=True)

cv2.imshow('image', np.hstack((im1,im2)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)

#Sıra İstatistiği (Doğrusal Olmayan) Filtreler
import cv2
import numpy as np

img= cv2.imread('/Users/bilal/Desktop/blender.jpg')
median = cv2.medianBlur(img, 5)
compare = np.concatente((img,median),axis=1)
cv2.imshow('img',compare)
cv2.waitKey(0)
cv2.destroyAllWindows

#Uzamsal Keskinleştirme Filtreleri: Laplas İşleci
import sys
import cv2 as cv

def main(argv):
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace Demo"
    
    
    imageName = argv[0] if len(argv) > 0 else '/Users/bilal/Desktop/blender.jpg'
    
    src = cv.imread(cv.samples.findFile(imageName),cv.IMREAD_COLOR)
    
    if src is None:
        print('Eror opening image')
        print('Program Arguments : [image name -- default /Users/bilal/Desktop/blender.jpg]')
        return -1
    
    
    src = cv.GaussianBlur(src, (3,3), 0)
    
    src_gray = cv.cvtColor(src,cv.COLOR_BG2GRAY)
    cv.namedWindow(window_name,cv.WINDOW_AUTOSIZE)
    dst = cv.Lağlacian(src_gray,ddepth,ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)
    cv.imshow(window_name,abs_dst)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
    