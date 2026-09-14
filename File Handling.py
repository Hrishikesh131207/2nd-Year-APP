# Open the input file and read all lines
with open("file.txt", "r") as f:
    data = f.readlines()

print("Number of lines:", len(data))

# Get the first two lines
selected_lines = data[:2]

# Save them into the output file
with open("output.txt", "w") as f:
    f.writelines(selected_lines)

print("First two lines saved successfully")