MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    print(f'{name} is{(" not","")[age >= MIN_DRIVING_AGE]} allowed to drive!')
