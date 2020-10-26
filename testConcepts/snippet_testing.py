invalid_char = '<>:"/\\|?*'  # \\ is escaped to allow \ in string, using ' to allow " in string
testing_filename = True

while testing_filename:
    file_name = ((input("Enter a filename to save product data: ").lower()) + ".dat").replace(" ", "_")

    # Scrub filename to properly format final output
    file_name = file_name.replace(".dat.dat", ".dat")
    file_name = file_name.replace("..", ".")

    # Test to make sure filename doesn't contain characters prohibited by OS for Windows & Linux
    for fn in file_name:
        if fn in invalid_char:
            print(f'Invalid Character: {fn} is not allowed in filenames.  Please try again.')
            testing_filename = True
            break
        else:
            testing_filename = False

print(file_name)