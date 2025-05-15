from sklearn.linear_model import LinearRegression

# Step 1: Prepare data
X = [
    [1500, 3],
    [1800, 4],
    [2400, 4],
    [3000, 5],
    [3500, 5]
]  # [Size, Bedrooms]

y = [300000, 350000, 450000, 500000, 600000]  # Prices

# Step 2: Create the model
model = LinearRegression()

# Step 3: Train the model
model.fit(X, y)

# Step 4: Predict
predicted_price = model.predict([[2800, 4]])  # Size: 2800 sqft, Bedrooms: 4
print(f"Predicted Price: ${predicted_price[0]:.2f}")
