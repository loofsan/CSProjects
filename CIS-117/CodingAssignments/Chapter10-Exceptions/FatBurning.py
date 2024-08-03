def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print(f"Fat burning heart rate for a {age} year-old: {fat_burning_heart_rate(age)} bpm")
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.")