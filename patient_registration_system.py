# --------------------------------------------------------
# patient_registration_system.py
# Basic EMR Intake & Health Age Analytics System
# --------------------------------------------------------
import datetime
import re 

# === Patient Name Registration ===
first_name = input("Enter Patient First Name: ").strip().capitalize()
middle_name = input("Enter Patient Middle Name: ").strip().capitalize()
last_name = input("Enter Patient Last Name: ").strip().capitalize()

print(f"\nPatient Registered: {first_name} {middle_name} {last_name}")

# === Contact Information ===
email = input("Enter Patient Email Address: ").strip()

email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]")
if "@" not in email:
    print("Invalid email format.")
    exit()

username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Patient Portal Username: {username}")
print(f"Email Domain (Provider): {domain}")

# === Age & Health Analytics ===
try:
    age = int(input("\nEnter Patient Age: "))
except ValueError:
    print("Age must be a number.")
    exit()

# Time-based life statistics
date_time= datetime.datetime.now()

months_lived = age * 12
days_lived = age * 365
hours_lived = days_lived * 24

print("\n--- Patient Life Statistics ---")
print(f"Age: {age} years")
print(f"Months Lived: {months_lived:,}")
print(f"Days Lived: {days_lived:,}")
print(f"Hours Lived: {hours_lived:,}")

# Basic Preventive Care Recommendation
if age < 18:
    category = "Pediatric"
    recommendation = "Routine vaccination schedule monitoring recommended."
elif 18 <= age < 40:
    category = "Young Adult"
    recommendation = "Annual physical exam and lifestyle assessment recommended."
elif 40 <= age < 60:
    category = "Middle Age"
    recommendation = "Cardiovascular screening and blood pressure monitoring recommended."
else:
    category = "Senior"
    recommendation = "Comprehensive geriatric assessment recommended."

print("\n--- Clinical Category ---")
print(f"Patient Category: {category}")
print(f"Preventive Recommendation: {recommendation}")
