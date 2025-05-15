import cv2
import numpy as np
import pandas as pd

def preprocess_image(image_path):
    """ Convert image to grayscale and apply adaptive thresholding """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    return image, binary

def detect_lines(binary):
    """ Detect horizontal and vertical lines in the table """
    kernel_h = np.ones((1, 50), np.uint8)  # Horizontal kernel
    kernel_v = np.ones((50, 1), np.uint8)  # Vertical kernel
    
    horizontal_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_h)
    vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_v)
    
    table_structure = cv2.add(horizontal_lines, vertical_lines)  # Combine lines
    return table_structure

def detect_cells(binary, table_structure):
    """ Find table cells using contours """
    contours, _ = cv2.findContours(table_structure, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cell_boxes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 20 and h > 20:  # Filter small boxes
            cell_boxes.append((x, y, w, h))
    
    cell_boxes = sorted(cell_boxes, key=lambda x: (x[1], x[0]))  # Sort by row
    return cell_boxes

def extract_table_structure(image_path):
    """ Full pipeline to extract table structure from image """
    image, binary = preprocess_image(image_path)
    table_structure = detect_lines(binary)
    cell_boxes = detect_cells(binary, table_structure)
    print(cell_boxes)    
    # Create empty table structure
    table_data = []
    row = []
    last_y = None

    for x, y, w, h in cell_boxes:
        if last_y is None or abs(y - last_y) < 20:
            row.append(f"[{x},{y}]")  # Storing coordinates instead of text
        else:
            table_data.append(row)
            row = [f"[{x},{y}]"]
        last_y = y
    
    if row:
        table_data.append(row)
    
    return pd.DataFrame(table_data)

# Run the pipeline
image_path = r"C:\Users\hanna\Downloads\sales-invoice3.png"  # Change this to your image file
df = extract_table_structure(image_path)
print(df)
df.to_csv("table_extracted.csv", index=False)
