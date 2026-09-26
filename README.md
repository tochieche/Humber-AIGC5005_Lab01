# BMI Category Reporter
This is a Python script that collects a user's height and weight, validates the input for safety, and computes their Body Mass Index (BMI) along with their official health category. It helps prevent runtime crashes by catching invalid text or out of range measurements before processing.

## Data source
User input is collected through the interface. One record represents a single person's physical measurements (height in meters and weight in kilograms). Since it runs interactively, it processes 1 record per session execution.

## Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run
python app.py

## Example output

--- Body Mass Index (BMI) Calculator ---

Enter your height in meters (e.g., 1.75): 1.75
Enter your weight in kilograms (e.g., 70): 68.5

Result: Your BMI is 22.4, which falls into the 'Normal weight' category.

This output tells the user their calculated BMI value rounded to one decimal place and maps it directly to the corresponding classification which in this scenario is Normal weight.

## Data quirks
Entering letters, symbols, or empty spaces causes float() to throw a ValueError. The program catches this using a try except block and prints a clear message asking for numbers instead of crashing with a traceback.

Inputs like negative numbers, 0, or extreme values are mathematically valid for BMI formulas but not realistic and impossible. The code checks boundary ranges 0.5m - 2.5m for height,10kg - 300kg for weightand informs the user of allowed ranges if they enter something wild.

## Design choices
Instead of duplicating input validation twice for height and weight, I wrapped the checks in a reusable function to keep the code not to repeat.

Standard primitive types were used instead of complex collections like lists or dicts because the application processes a single stateful record for each execution.

## Known limitations

The program only accepts metric inputs which is meters and kilograms. If someone enters 5'11 or 150lbs for example, the program will flag them as out-of-range rather than automatically converting them.

It stops immediately if bad input is entered. If I had more time, I would put the input prompts inside a while loop so it reprompts the user until they give a valid entry instead of quitting the program.