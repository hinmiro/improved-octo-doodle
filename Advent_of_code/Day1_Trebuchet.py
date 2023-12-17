# Day 1: Trebuchet?!

def file_reader():
    PATH = 'C:\\Users\\miroh\\Documents\\koulu\\Vs_code\\improved-octo-doodle\\Advent_of_code\\calibration.txt'
    sum = 0
    try:
        with open(PATH , 'r') as f:
            number = ''
            data = f.readlines()
            f.seek(0)
            for line in data:
                digits = [char for char in line if char.isdigit()]
                if digits:
                    first_digit = digits[0]
                    last_digit = digits[-1]
                    number = str(first_digit)
                    number += str(last_digit)
                    sum += int(number)
    except FileNotFoundError:
        print(f"File not found from {PATH}")
    except Exception as e:
        print(f"An error occured: {e}")
    return sum

ammount = file_reader()
print(ammount)