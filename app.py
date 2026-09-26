#Prompt the user for input and validate that it is a float within the specified sensible range [min_val, max_val].
def get_positive_float(prompt, min_val, max_val, unit_name):
    
    user_input = input(prompt).strip()
    
    # Checks for non-numeric or empty input
    try:
        value = float(user_input)
    except ValueError:
        print(f"Invalid input: '{user_input}' is not a valid number.")
        return None
        
    # Checks for out-of-range values
    if value < min_val or value > max_val:
        print(f"Value out of range: {value} {unit_name}. The sensible range is {min_val} to {max_val} {unit_name}.")
        return None
        
    return value

def main():
    print("--- Body Mass Index (BMI) Calculator ---\n")
    
    # Setting up sensible ranges: Height in meters (0.5m to 2.5m), Weight in kg (10kg to 300kg)
    height_meters = get_positive_float(
        prompt="Enter your height in meters (e.g., 1.75): ",
        min_val=0.5,
        max_val=2.5,
        unit_name="meters"
    )
    if height_meters is None:
        return  # Exit safely without crashing

    weight_kilograms = get_positive_float(
        prompt="Enter your weight in kilograms (e.g., 70): ",
        min_val=10.0,
        max_val=300.0,
        unit_name="kg"
    )
    if weight_kilograms is None:
        return  # Exit safely without crashing

    # Calculate Body Mass Index: weight (kg) / height (m)^2
    body_mass_index = weight_kilograms / (height_meters ** 2)

    # Determine BMI category
    if body_mass_index < 18.5:
        bmi_category = "Underweight"
    elif body_mass_index < 25.0:
        bmi_category = "Normal weight"
    elif body_mass_index < 30.0:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obesity"

    # Prints a formatted result
    print(f"\nResult: Your BMI is {body_mass_index:.1f}, which falls into the '{bmi_category}' category.")

if __name__ == "__main__":
    main()