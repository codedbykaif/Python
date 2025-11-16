import cv2
image = cv2.imread("hack.png")
if image is not None: 
    success = cv2.imwrite("output_python.png", image)
    if success:
        print("image saved successfully")
    else: 
        print("failed to save an image")
else:        
    print("could not load the image ")