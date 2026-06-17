def validate_age(age):
    if 0 <= age <= 150:
        if age < 18:
            return "minor"

        if age < 65:
            return "adult"

        return "senior"

    return "invalid"


x = 10
y = 20
z = 30

if x < y < z:
    print("Increasing sequence")