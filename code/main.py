import cv2
import numpy as np

# Load the final puzzle image
final_image = cv2.imread('final_puzzle.jpg')
height, width, _ = final_image.shape
