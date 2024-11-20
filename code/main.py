import cv2
import numpy as np

# Load the final puzzle image
final_image = cv2.imread('image/Puzzle.png')
height, width, _ = final_image.shape

rows, cols = 25, 40
block_height = height // rows
block_width = width // cols


blocks = {}
for i in range(rows):
    for j in range(cols):
        block_id = i * cols + j + 1
        x_start, y_start = j * block_width, i * block_height
        x_end, y_end = x_start + block_width, y_start + block_height
        blocks[block_id] = final_image[y_start:y_end, x_start:x_end]
        
        cv2.imwrite(f'block_{block_id}.jpg', blocks[block_id])

for i in range(rows):
    for j in range(cols):
        x_center = j * block_width + block_width // 2
        y_center = i * block_height + block_height // 2
        cv2.putText(final_image, str(i * cols + j + 1), (x_center - 10, y_center), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Save the labeled image
cv2.imwrite('labeled_final_puzzle.jpg', final_image)


