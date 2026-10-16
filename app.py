def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive" if value >= 0.5 else "negative"

def prediction_message(value):
    """Returns a readable message for the prediction."""
    return f"Input {value} is predicted as {predict_label(value)}"

if __name__ == "__main__":
    print("Prediction:", predict_label(0.8))
    print(prediction_message(0.8))