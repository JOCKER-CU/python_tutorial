from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([
     [3, 50000, 1.8],
    [1, 30000, 2.0],
    [5, 100000, 1.6],
    [2, 40000, 2.2]
])

# Target prices
y = np.array([20000, 25000, 15000, 23000])

# Create the model
model = LinearRegression()
model.fit(x, y)

# Predict the price of a car with 4 doors, 60000 miles, and 1.5L engine
predicted_price = model.predict([[2, 45000, 2.0]])

print(f"Predicted Price: ${predicted_price[0]:.2f}")