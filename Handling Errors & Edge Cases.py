def calculate_utility_ratio(value, total):
    try:
        # Block 1: Type Validation
        # Ensures inputs are numbers; avoids TypeError during math operations
        if not all(isinstance(i, (int, float)) for i in [value, total]):
            raise ValueError("Both 'value' and 'total' must be numeric.")

        # Block 2: Zero Division Guard
        # Prevents the most common crash in ratio calculations
        if total == 0:
            return "Usage is 0.0% (Total is zero)"

        # Block 3: Logic & Range Validation
        # Handles edge cases where value might be negative or exceed the total
        value = max(0, value)  # Clamp to 0 if negative
        if value > total:
            # We can log a warning here if exceeding 100% is unexpected
            pass 

        # Block 4: Calculation and Precision
        # Calculate ratio and round for a cleaner user experience
        percentage = round((value / total) * 100, 2)
        
        # Block 5: Structured Return
        # Using f-strings for efficiency and clarity
        return f"Usage is {percentage}%"

    except Exception as e:
        # Catch-all for unexpected issues to prevent the entire app from crashing
        return f"Error calculating ratio: {str(e)}"