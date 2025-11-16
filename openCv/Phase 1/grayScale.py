import cv2
image = cv2.imread("hack.png")
if image is not None: 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else: 
    print("could not load the image")