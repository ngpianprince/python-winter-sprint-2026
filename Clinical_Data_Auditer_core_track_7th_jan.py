# Clinical Data Audit using Functions and Recursion

# -------- Validation Functions --------
def validate_age(age):
    if 0 <= age <= 120:
        return True
    return False


def validate_heart_rate(hr):
    return isinstance(hr, int)


def decide_audit_status(flag, warning):
    if flag:
        return "FAIL"
    elif warning:
        return "REVIEW"
    else:
        return "PASS"


# -------- Recursive Function --------
def take_heart_rates(count, readings=None):
    if readings is None:
        readings = []

    if count == 0:
        return readings

    hr = input(f"Enter heart rate reading {len(readings)+1}: ")
    if hr.isdigit():
        readings.append(int(hr))
    else:
        readings.append(hr)  # invalid input kept for flagging

    return take_heart_rates(count - 1, readings)


# -------- Main Program --------
name = input("Enter Patient Name: ")
age_input = input("Enter Age: ")
num_readings = int(input("Enter number of heart rate readings: "))

flag = False
warning = False

# Age validation
if age_input.isdigit():
    age = int(age_input)
    if not validate_age(age):
        flag = True
else:
    flag = True

# Take heart rate readings using recursion
heart_rates = take_heart_rates(num_readings)

# Heart rate validation
for hr in heart_rates:
    if not validate_heart_rate(hr):
        flag = True
    else:
        if hr > 180:
            warning = True

# Final Audit Status
status = decide_audit_status(flag, warning)

# -------- Output --------
print("\n----- Clinical Audit Report -----")
print(f"Patient Name : {name.title()}")
print(f"Age          : {age_input}")
print(f"Heart Rates  : {heart_rates}")
print(f"Audit Status : {status}")
print("---------------------------------")