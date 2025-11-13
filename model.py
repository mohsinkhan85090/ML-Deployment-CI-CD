import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Create sample data
data = {
    'sqft': [1000, 1500, 2000, 2500, 3000],
    'rooms': [2, 3, 3, 4, 5],
    'price': [200000, 250000, 300000, 350000, 400000]
}
df = pd.DataFrame(data)

# Train model
X = df[['sqft', 'rooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model trained and saved as model.pkl")
