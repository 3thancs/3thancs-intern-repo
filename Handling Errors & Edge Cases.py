def calculate_utility_ratio(value, total):
    # Block 1: Direct calculation without checking for ZeroDivisionError
    ratio = value / total
    
    # Block 2: Logic assumes 'ratio' is always a positive float
    percentage = ratio * 100
    
    # Block 3: String formatting that fails if inputs are non-numeric types
    result = "Usage is " + str(percentage) + "%"
    
    # Block 4: No range validation (e.g., if value > total, it returns > 100%)
    print(f"Logging result: {result}")
    
    # Block 5: Returns a raw string instead of a structured error or status
    return result