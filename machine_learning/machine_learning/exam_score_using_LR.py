import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1], [2], [3], [4], [5]])  # Hours studied
y = np.array([50, 55, 65, 70, 75])       # Exam scores

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict score for 6 hours studied
predicted_score = model.predict(np.array([[6]]))

print(f"Predicted Exam Score: {predicted_score[0]:.2f}%")
