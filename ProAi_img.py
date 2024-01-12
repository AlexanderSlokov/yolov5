import cv2


def resize_and_save(input_image_path,
                    output_image_path,
                    target_width,
                    target_height):
    # Load the image
    image = cv2.imread(input_image_path)

    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: Unable to load image at {input_image_path}")
        return

    # Resize the image to match the target dimensions
    resized_image = cv2.resize(image, (target_width, target_height))

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)
    print(f"Image saved to {output_image_path}")


def draw_bboxes_on_image(image_path, box_file_path, output):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Get image dimensions
    height, width = image.shape[:2]

    # Read bounding boxes from file and draw them on the image
    bboxes = read_boxes_from_file(box_file_path, width, height)
    for bbox in bboxes:
        x_center, y_center, _, _ = bbox
        cv2.circle(image, (x_center, y_center), 5, (0, 0, 255), -1)  # Draw a red dot at the center

    # Save the image with bounding boxes drawn
    cv2.imwrite(output_path, image)
    print(f"Image with bounding boxes saved to {output}")

    # Optionally print the coordinates of the centers
    for bbox in bboxes:
        print(f"Center coordinates: {bbox[:2]}")  # Print only x and y centers


def read_boxes_from_file(file_path, image_width, image_height):
    bboxes = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            class_id, x_center, y_center, width, height, *rest = map(float, line.split())
            # Convert from normalized to absolute coordinates
            x_center_abs = int(x_center * image_width)
            y_center_abs = int(y_center * image_height)
            width_abs = int(width * image_width)
            height_abs = int(height * image_height)
            bboxes.append((x_center_abs, y_center_abs, width_abs, height_abs))
    return bboxes


# Example usage:
original_image_path = r'D:\PythonProjects\objDetectionYOLOv5\final_resized_image.jpg'
box_file_path = r'D:\PythonProjects\objDetectionYOLOv5\runs\detect\exp8\labels\Screenshot-2024-01-11-105444_png.rf.edef7dd6be3ac2a0bd54bfa4524e497f.txt'
output_path = r'D:\PythonProjects\objDetectionYOLOv5\final_image_with_centers.jpg'

draw_bboxes_on_image(original_image_path, box_file_path, output_path)

# Function to read the bounding box information from a txt file
# def read_bboxes_from_file(file_path, image_width, image_height):
#     with open(file_path, 'r') as file:
#         bboxes = []
#         for line in file.readlines():
#             class_id, x_center, y_center, width, height, *rest = map(float, line.split())
#             # Convert from normalized to absolute coordinates
#             x_center_abs = int(x_center * image_width)
#             y_center_abs = int(y_center * image_height)
#             width_abs = int(width * image_width)
#             height_abs = int(height * image_height)
#             bboxes.append((x_center_abs, y_center_abs, width_abs, height_abs))
#         return bboxes
#
# # Load the original image to get its dimensions
# original_image_path = r'D:\PythonProjects\objDetectionYOLOv5\final_resized_image.jpg'
# original_image = cv2.imread(original_image_path)
# original_height, original_width = original_image.shape[:2]
#
# # Path to the YOLOv5 .txt file containing the bbox data
# bbox_file_path = r'D:\PythonProjects\objDetectionYOLOv5\runs\detect\exp8\labels\Screenshot-2024-01-11-105444_png.rf.edef7dd6be3ac2a0bd54bfa4524e497f.txt'
#
# # Read the bounding box data from the file
# bboxes = read_bboxes_from_file(bbox_file_path, original_width, original_height)
#
# # Draw the center points on the original image for visualization
# for bbox in bboxes:
#     x_center, y_center, width, height = bbox
#     cv2.circle(original_image, (x_center, y_center), 5, (0, 0, 255), -1)  # Draw a red dot at the center
#
# # Save the original image with the center points drawn
# output_path = r'D:\PythonProjects\objDetectionYOLOv5\final_image_with_centers.jpg'
# cv2.imwrite(output_path, original_image)
#
# # Optionally print the coordinates of the centers
# for bbox in bboxes:
#     print(f"Center coordinates: {bbox[:2]}")  # Print only x and y centers


# # Load the original image to get its dimensions
# original_image_path = r"C:\Users\Admin\Pictures\Screenshots\Screenshot 2024-01-11 105444.png"
# # Replace with the path to your original image
# original_image = cv2.imread(original_image_path)
# original_height, original_width = original_image.shape[:2]
#
# # Load the 640x640 image
# resized_image_path = r'D:\PythonProjects\objDetectionYOLOv5\runs\detect\exp6\Screenshot-2024-01-11-105444_png.rf.edef7dd6be3ac2a0bd54bfa4524e497f.jpg'
# image = cv2.imread(resized_image_path)
#
# # Resize the image to match the original dimensions
# resized_image = cv2.resize(image, (original_width, original_height))
#
# # Save the resized image
# output_path = r'D:\PythonProjects\objDetectionYOLOv5\final_resized_image.jpg'
# cv2.imwrite(output_path, resized_image)
