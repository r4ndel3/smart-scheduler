exams = []

def add_exam():
    """Add a new exam to the scheduler"""
    name = input("Enter exam name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    room = input("Enter room number: ")
    
    exams.append({
        'name': name,
        'date': date,
        'time': time,
        'room': room
    })
    print("Exam added successfully!")

def view_exams():
    """Display all scheduled exams"""
    if not exams:
        print("No exams scheduled.")
        return
    
    for idx, exam in enumerate(exams, 1):
        print(f"{idx}. {exam['name']} - Date: {exam['date']}, Time: {exam['time']}, Room: {exam['room']}")

def edit_exam():
    """Modify an existing exam"""
    view_exams()
    if not exams:
        return
        
    try:
        exam_num = int(input("Enter exam number to edit: ")) - 1
        if 0 <= exam_num < len(exams):
            exam = exams[exam_num]
            print(f"Editing: {exam['name']}")
            exam['name'] = input(f"Name ({exam['name']}): ") or exam['name']
            exam['date'] = input(f"Date ({exam['date']}): ") or exam['date']
            exam['time'] = input(f"Time ({exam['time']}): ") or exam['time']
            exam['room'] = input(f"Room ({exam['room']}): ") or exam['room']
            print("Exam updated successfully!")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_exam():
    """Remove an exam from the scheduler"""
    view_exams()
    if not exams:
        return
        
    try:
        exam_num = int(input("Enter exam number to delete: ")) - 1
        if 0 <= exam_num < len(exams):
            deleted = exams.pop(exam_num)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Display main menu and handle user input"""
    while True:
        print("\n==Smart Scheduler Menu==")
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting Smart Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main_menu()