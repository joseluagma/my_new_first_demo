x = 12
y = 'hours'


def days_to_hours(num_of_days):
    return f"{num_of_days} days are {num_of_days * x} {y}"


user_input = int(input())
calculate = days_to_hours(user_input)
print(calculate)