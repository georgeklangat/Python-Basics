# # Define who studies pure mathematics
# studies = {"x", "y", "z"}
#
# # Define friendships (mutual relationships)
# friendships = {
#     ("x", "y"), ("y", "x"),
#     ("x", "z"), ("z", "x"),
#     ("y", "z"), ("z", "y")
# }
#
# # Function to check if everyone studies pure mathematics
# def all_study(group):
#     return all(person in studies for person in group)
#
# # Function to check if everyone is friends with each other
# def all_friends(group):
#     return all((a, b) in friendships for i, a in enumerate(group) for b in group[i+1:])
#
# # Combined function to check both conditions
# def valid_group(group):
#     return all_study(group) and all_friends(group)
#
# # Test group
# group = ["x", "y", "z"]
#
# # Run checks
# if valid_group(group):
#     print("The group satisfies all conditions.")
# else:
#     print("The group does not satisfy all conditions.")

# Rainfall data for each month
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
rainfall = [5, 2, 12, 17, 18, 12, 10, 7, 3, 12, 18, 13]

# Loop to display average rainfall for each month
for i in range(12):
    print(f"The average rainfall in {months[i]} is {rainfall[i]} mm")

# Compute the mean of average rainfall for the year
average_rainfall_year = sum(rainfall) / len(rainfall)

# Display the computed average rainfall for the year
print(f"The average rainfall for the year is {average_rainfall_year:.2f} mm")
