def light_control(sensor_input):
    if sensor_input == "dark":
        return "turn on light"
    else:
        return "do nothing"

input = input("Enter the action:")
print(light_control(input))  # Output: turn on light
