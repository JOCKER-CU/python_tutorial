from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]  # hours studied
y = [1, 2, 3, 3.5, 5]          # test scores

# Train
model = LinearRegression()
model.fit(X, y)

# Predict
score = model.predict([[6]])  # Predict score after 6 hours studying
print("Predicted Score:", score)
