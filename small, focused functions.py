import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1. Separate the Data loading and cleaning from the rest of the pipeline
def load_and_clean_data(file_path, target_col):
    df = pd.read_csv(file_path)
    return df.dropna(), target_col
    
# 2. Define a pure preprocessing function that only handles scaling and splitting
def preprocess_data(df, target_col, test_size=0.2, random_state=42):
    X = df.drop(columns=[target_col]).values    
    y = df[target_col].values.reshape(-1, 1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test, scaler

# Convert to PyTorch tensors
def convert_to_tensors(X_train, X_test, y_train, y_test):
    X_train_t = torch.tensor(X_train, dtype=torch.float32)
    X_test_t = torch.tensor(X_test, dtype=torch.float32)
    y_train_t = torch.tensor(y_train, dtype=torch.float32)
    y_test_t = torch.tensor(y_test, dtype=torch.float32)
    return X_train_t, X_test_t, y_train_t, y_test_t

    
# 3. Model Definition
def buildmodel(input_dim):
    return nn.Sequential(
        nn.Linear(input_dim, 64),
        nn.ReLU(),
        nn.Linear(64, 32),
        nn.ReLU(),
        nn.Linear(32, 1)
    )
    
    
# 4. Define Training Loop
def train_model(model, X_train_t, y_train_t, epochs=100, lr=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    losses = []
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        predictions = model(X_train_t)
        loss = criterion(predictions, y_train_t)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
            
# 5. Visualization and Reporting Utility
def plot_losses(losses):
    plt.plot(losses)
    plt.title('Training Loss Over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()    