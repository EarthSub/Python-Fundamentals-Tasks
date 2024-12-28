# Write a program that reads the path to a file and subtracts the file name and its extension.


#                             Examples

# Input                                                           Output

# C:\Internal\training-internal\Template.pptx                     File name: Template
#                                                                 File extension: pptx

# C:\Projects\Data-Structures\LinkedList.cs                       File name: LinkedList



the_path = input().split("\\")
current_file = the_path[-1]
name, extension = current_file.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")