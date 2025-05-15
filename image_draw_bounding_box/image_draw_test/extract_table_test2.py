import cv2
import pytesseract
import pandas as pd
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load image
image_path = r"C:\Users\hanna\Downloads\sales-invoice3.png"
image = cv2.imread(image_path)

# Preprocess image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Detect text
custom_config = r'--oem 3 --psm 6'
text_data = pytesseract.image_to_data(binary, config=custom_config, output_type=pytesseract.Output.DICT)
print(text_data)

# Extract table structure
n_boxes = len(text_data['level'])
table_data = []
for i in range(n_boxes):
    (x, y, w, h) = (text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i])
    text = text_data['text'][i]
    if text.strip():
        table_data.append({'x': x, 'y': y, 'text': text})


# Organize data into a table
table_data.sort(key=lambda x: (x['y'], x['x']))
df = pd.DataFrame(table_data)

# Save or display the table
df.to_csv('output_table.csv', index=False)
print(df)