#STUDENT MARKS MANAGER
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("\n--- Student Marks Manager Menu ---")
    print("1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        name = input("Enter student name: ").strip()
        if name in students:
            print("Student already exists")
            continue
            
        temp_marks = []
        i = 1
        while i <= 3:
            try:
                m = float(input(f"Enter mark {i}: "))
                if 0 <= m <= 100:
                    temp_marks.append(m)
                    i += 1
                else:
                    print("Invalid mark, try again.")
            except ValueError:
                print("Invalid mark, try again.")
        students[name] = temp_marks
        print(f"Student {name} added successfully!")
        
    elif choice == "2":
        for name, marks in students.items():
            avg = sum(marks) / len(marks)
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
            print(f"{name} {avg:.2f} {grade}")
            
    elif choice == "3":
        if not students:
            print("No students recorded.")
        else:
            highest_avg = -1
            topper_name = ""
            for name, marks in students.items():
                avg = sum(marks) / len(marks)
                if avg > highest_avg:
                    highest_avg = avg
                    topper_name = name
            print(f"Topper: {topper_name}")
            
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
