import pandas as pd

# Sample data for vegetation correlation
data = {
    "Vegetation": ["Salal", "Sphagnum Moss", "Labrador Tea", "Bog Laurel", "Hemlock"],
    "pH Correlation": [-0.55, -0.40, -0.06, 0.06, -0.15],
    "Soil Moisture Correlation": [0.45, 0.68, 0.67, 0.61, 0.62],
    "Light Intensity Correlation": [-0.47, 0.15, 0.44, 0.45, 0.12]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to calculate correlation strength
def get_strength(correlation):
    if 0 <= abs(correlation) <= 0.19:
        return "Very weak"
    elif 0.20 <= abs(correlation) <= 0.39:
        return "Weak"
    elif 0.40 <= abs(correlation) <= 0.69:
        return "Moderate"
    elif 0.70 <= abs(correlation) <= 0.89:
        return "Strong"
    elif 0.90 <= abs(correlation) <= 1.00:
        return "Very strong"

# Function to calculate significance level based on corrected boundaries
def get_significance(correlation):
    if abs(correlation) < 0.39:
        return ">5%"
    elif 0.39 <= abs(correlation) < 0.46:
        return ">1%"
    elif 0.46 <= abs(correlation) < 0.58:
        return ">0.1%"
    else:
        return "<0.1%"

# Applying strength and significance calculations
df['pH Strength'] = df['pH Correlation'].apply(get_strength)
df['pH Significance'] = df['pH Correlation'].apply(get_significance)
df['Soil Moisture Strength'] = df['Soil Moisture Correlation'].apply(get_strength)
df['Soil Moisture Significance'] = df['Soil Moisture Correlation'].apply(get_significance)
df['Light Intensity Strength'] = df['Light Intensity Correlation'].apply(get_strength)
df['Light Intensity Significance'] = df['Light Intensity Correlation'].apply(get_significance)

# Display the updated DataFrame
print(df)