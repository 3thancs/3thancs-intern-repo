import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data from csv
df = pd.read_csv('dataset.csv')

# Define x and y
X = df.drop('target', axis=1)
y = df['target']

# Split data into train and test
# Use 0.2 for test size
# Set random state to 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes
print(X_train.shape, X_test.shape)