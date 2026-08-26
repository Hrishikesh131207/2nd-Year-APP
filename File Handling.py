file_name = "1st.txt"

f = open(file_name, "w")
f.write("This is the first line.\n")
f.write("This is the second line.\n")
f.close()

print("File created and data written.\n")

f = open(file_name, "r")
data = f.read()
f.close()

print("File contents:\n")
print(data)

f = open(file_name, "a")
f.write("This line is added later.\n")
f.close()

print("New data added.\n")

f = open(file_name, "r")
data = f.read()
f.close()

print("Updated file contents:\n")
print(data)

# OUTPUT:

# File created and data written.

# File contents:

# This is the first line.
# This is the second line.

# New data added.

# Updated file contents:

# This is the first line.
# This is the second line.
# This line is added later.