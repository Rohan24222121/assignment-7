def add_student_info(roll_number, name, student_class, file="student_data.txt"):
    try:
        with open(file, "a") as f:
            f.writelines([roll_number + '\n', name + '\n', student_class + '\n'])
    except IOError as e:
        print("An error occurred while accessing the file:", e)

def print_student_info(file="student_data.txt"):
    try:
        with open(file, "r") as f:
            print(f.readlines())
    except IOError as e:
        print("An error occurred while accessing the file:", e)
