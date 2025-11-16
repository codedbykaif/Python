import cv2
image_path = input("Enter the path of image: ")
image = cv2.imread(image_path)
if image is None:
    print("could not load the image")
else:    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    output_name = input("Enter the output filename: ")
    cv2.imwrit(output_name, gray_image)
    print(f"image successfully saved as {output_name}")