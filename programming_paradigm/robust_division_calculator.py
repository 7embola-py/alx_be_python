def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.
    Handles ZeroDivisionError and ValueError.
    Returns exact strings expected by ALX bot.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        # Exact error message expected by ALX bot
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Exact success message expected by ALX bot
    return f"The result of the division is {result}"

