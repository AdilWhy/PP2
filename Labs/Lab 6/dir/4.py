line_count = 0

with open("textfile.txt", 'r') as file:
    for line in file:
        line_count += 1

print(f"Number of lines: {line_count}")