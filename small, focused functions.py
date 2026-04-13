import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def process_everything_and_train(csv_path, target_col, epochs=100, lr=0.01):
    # --- 1. Data Loading and Cleaning ---
    df = pd.read_csv(csv_path)
    df = df.dropna()
    
    # --- 2. Feature Engineering & Preprocessing ---
    # Mixed responsibility: splitting data and scaling in one block
    X = df.drop(target_col, axis=1).values
    y = df[target_col].values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    # Converting to tensors
    X_train_t = torch.FloatTensor(X_train)
    y_train_t = torch.FloatTensor(y_train).view(-1, 1)
    X_test_t = torch.FloatTensor(X_test)
    y_test_t = torch.FloatTensor(y_test).view(-1, 1)
    
    # --- 3. Model Definition ---
    # Hidden inside the function, making it impossible to reuse the architecture
    input_dim = X_train.shape
    model = nn.Sequential(
        nn.Linear(input_dim, 64),
        nn.ReLU(),
        nn.Linear(64, 32),
        nn.ReLU(),
        nn.Linear(32, 1)
    )
    
    # --- 4. Training Loop ---
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    losses = []
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train_t)
        loss = criterion(outputs, y_train_t)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch} loss: {loss.item()}")
            
    # --- 5. Evaluation & Visualization ---
    model.eval()
    with torch.no_grad():
        predictions = model(X_test_t)
        test_loss = criterion(predictions, y_test_t)
        print(f"Final Test Loss: {test_loss.item()}")
    
    plt.plot(losses)
    plt.title("Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("MSE")
    plt.show()
    
    return model, scaler