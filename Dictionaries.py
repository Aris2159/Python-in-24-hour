
# Open the file in read mode
file_read = "C:/Users/Agamk/Downloads/AliceInWonderland.txt"

with open(file_read, 'r', encoding='utf-8') as file:
    
    Whole = file.read()
    first_200 = Whole[:200]
    print(first_200)

    name_count = first_200.count("Alice")
    read_count = Whole.count("Alice")
    print(f"There are {name_count} Alice in the count for first 200 characters.")
    print(f"There are {read_count} Alice in the whole book.")

    Do_5_lines_or_u_are_a_not_cool = Whole.splitlines()[:5]

    for print_the_line in Do_5_lines_or_u_are_a_not_cool:
        print(print_the_line)
