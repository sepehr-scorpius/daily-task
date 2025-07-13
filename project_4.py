file_text = "text_for_project_4.txt"
try:
    with open(file_text, "x") as f:
        f.write("Tasks:")
except Exception:
    pass
def print_t():
    return print('''*********************
[1] View tasks
[2] Add task
[3] Remove task
[4] Save and Exit''')
print_t()       
option = input("select an option: ")
while option != "4":
    if option != "4":
        print_t()
    with open(file_text, "r") as file:
        content = file.read()
    count = content.count(
        "\n") + (1 if not content.endswith("\n") and content else 0)
    if option == "1":
        try:
            with open(file_text, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("file didn't found")
        except PermissionError:
            print("permission to that file is denied")
        except Exception:
            print("something's wrong with reading file")
    elif option == "2":
        try:
            with open(file_text, "a") as file:
                new = input("input your task: ")
                if new not in content:
                    append = "\n" + "task(" + str(count) + "): " + new
                    file.write(append)
                else:
                    print("the task exist!")
        except FileNotFoundError:
            print("file didn't found")
        except PermissionError:
            print("permission to that file is denied")
        except Exception:
            print("something's wrong with reading file")
    elif option == "3":
        try:
            remove_line = int(input("input the task number: "))
        except Exception:
            print("your input has somthing wrong with it. try again from the beginning")
        try:
            with open(file_text, "r") as f:
                data = f.readlines()
                header = [data[0]]
                raw = data[1:remove_line]
                new_data = data[(remove_line+1):]
                updated_data = []
                for task in new_data:
                    start = task.find('(') + 1
                    end = task.find(')')
                    number = int(task[start:end])
                    new_number = number - 1
                    description = task.split(":", 1)[1]
                    updated_line = f"task({new_number}): {description}"
                    updated_data.append(updated_line)
                final =''.join(header + raw + updated_data)
                with open(file_text, "w") as y:
                    y.write(final)
            print("selected taked removed")
            print("*********************")
        except Exception:
            print("somthing went wrong try again")
    else:
        print("invalid input try (1_4)")
    option = input("select an option: ")
print("*********************")
print("you saved the file. have a nice day!")