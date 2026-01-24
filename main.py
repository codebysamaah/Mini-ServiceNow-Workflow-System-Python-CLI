from workflows import Workflow
from auth import login

def main():
    wf = Workflow()
    role = None

    print("Welcome to Mini ServiceNow CLI")
    print("Please login.")
    
    # Role selection
    while True:
        print("\nOptions: \n1. Manager\n2. Employee\n")
        choice = input("Choose an option: ")
        if choice == "1":
            role = "manager"
            break
        elif choice == "2":
            role = "employee"
            break
        else:
            print("Invalid Choice! Please enter 1 or 2.")

    # Login
    user = login(role)
    if not user:
        print("Login failed. Exiting...")
        return

    # Employee menu
    if role == "employee":
        while True:
            print("Employee Menu: \n1. Create a Request\n2. View My Requests\n3. Update My Request\n" \
            "4. Check status of Request\n5. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                wf.create_request(user)
            elif choice == "2":
                wf.view_my_requests(user)
            elif choice == "3":
                wf.update_request(user)
            elif choice == "4":
                wf.view_my_request_status(user)
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid Choice! Please enter 1-4.")
    
    # Manager Menu
    elif role == "manager":
        while True:
            print("\nManager Menu: \n1. View All Requests\n2. Process a Request\n3. Generate Summary Report\n4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                wf.view_all_requests()
            elif choice == "2":
                wf.process_request()
            elif choice == "3":
                wf.generate_summary()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid Choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
