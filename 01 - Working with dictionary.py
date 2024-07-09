python_dictionary = {
    "Bug": "An error in the program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(python_dictionary["Function"])
# Adding new items to dictionary
python_dictionary["Loop"] = "The action of doing something over and over again."
# Create the empty dictionary like the given below:
new_dictionary = {}
#Better to work out with empty dictionary for better.
new_dictionary["Mobile"] = "An electroric device."
# Edit an item in a dictionary like the given below:
python_dictionary["Bug"] = "A moth in your computer."
# Loop through a dictionary like the given below:
for things in python_dictionary:
    print(things)
    print(python_dictionary[things])
