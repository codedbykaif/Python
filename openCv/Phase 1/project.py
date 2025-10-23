import cv2

image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Could not load the image. Please check the path.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output_name = input("Enter the output filename (with extension, e.g., output.png): ")
    cv2.imwrite(output_name, gray_image)
    print(f"Image saved successfully as {output_name}")
