import pandas as pd

# Load the Excel file
file_path = "/Users/snowyan/PycharmProjects/cccc/Task 5 Equality Table.xlsx"  # Update this path if needed
df = pd.read_excel(file_path)

# Correct classification function
def classify(score):
    if -10 <= score <= 10:
        return "Fair"
    elif -20 <= score <= -11 or 11 <= score <= 20:
        return "Unfair"
    elif score <= -21 or score >= 21:
        return "Highly Discriminative"
    else:
        return "Unknown"

# Apply classification
df["Equality class"] = df["Equality Score"].apply(classify)

# Save updated file
output_file = "Equality Table_Updated.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Updated file saved as {output_file}")
