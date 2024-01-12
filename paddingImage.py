import cv2

# Load the image
image = cv2.imread(r'D:\PythonProjects\objDetectionYOLOv5\runs\detect\exp6\Screenshot-2024-01-11-105444_png.rf.edef7dd6be3ac2a0bd54bfa4524e497f.jpg')

# Resize the image
resized_image = cv2.resize(image, (1920, 1080))

# Save the resized image
cv2.imwrite(r'D:\PythonProjects\objDetectionYOLOv5\final_image.jpg', resized_image)

