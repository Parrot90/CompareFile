with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('output.txt', 'w') as output_file:
    # Read the contents of both files
    file1_contents = file1.readlines()
    file2_contents = file2.readlines()

    # Get the lines that are in file1 but not in file2
    lines_only_in_file1 = set(file1_contents) - set(file2_contents)
    output_file.write('Lines only in file1:\n')
    for line in lines_only_in_file1:
        output_file.write(line)

    # Get the lines that are in file2 but not in file1
    lines_only_in_file2 = set(file2_contents) - set(file1_contents)
    output_file.write('\nLines only in file2:\n')
    for line in lines_only_in_file2:
        output_file.write(line)

    # Get the lines that are in both files
    common_lines = set(file1_contents).intersection(set(file2_contents))
    output_file.write('\nCommon lines:\n')
    for line in common_lines:
        output_file.write(line)
