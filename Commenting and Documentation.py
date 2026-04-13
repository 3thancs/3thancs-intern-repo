# Import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# Dataset contains cleaned features; target is a continuous variable
df = pd.read_csv('dataset.csv')
X = df.drop('target', axis=1)
y = df['target']

# We use a 80/20 split to ensure that no underfitting or overfitting occurs
# A polynomial regression algorithm was used due to a non-linear relationship between data points
# Random state = 42 ensures consistent results across several experiments
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verify split dimensions to ensure feature count consistency
print(X_train.shape, X_test.shape)