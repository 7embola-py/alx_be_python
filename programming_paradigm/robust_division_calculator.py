def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator with robust error handling.
    Returns exact strings expected by ALX bot.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Both inputs must be numeric."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

