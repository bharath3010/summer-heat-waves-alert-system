import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv('heatwave_data.csv')

# Define features and target
X = data[['temperature', 'humidity', 'wind_speed']]
y = data['heatwave']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model to a file
with open('models/heatwave_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete. Saved to models/heatwave_model.pkl")

