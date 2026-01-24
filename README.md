# Mini ServiceNow Workflow System - Python CLI
A simple command-line interface (CLI) workflow system simulating ServiceNow functionality. Built in Python, this project implements role-based request management with separate user and manager workflows, supporting login, CRUD operations, approvals, and request tracking.

## **Features**

### Employees
- Login with username and password
- Submit new requests
- View and update their own requests
- Track request status (pending, approved, rejected)

### Managers
- Login with username and password
- View all employee requests
- Approve or reject requests
- Update request status and add comments
- Generate summary reports

## **CLI Navigation**
- Interactive menus for users and managers
- Input prompts guide users through workflow actions
- Clear separation between user and manager operations
  
## **Classes**
- **User**: Represents a user (employee or manager) with a username and role. 
- **Request**: Represents a service request with fields for id, title, description, created_by, status, and manager comments. Includes methods for employees and managers.
- **Workflow**: Contains the main business logic and methods for request creation, approval, updating, viewing, and generating summary reports. Interfaces between users and the persistent JSON database.

## **Skills and Concepts Demonstrated**
- Object-Oriented Programming (OOP)
- Role-based access control (RBAC)
- CRUD operations
- CLI interface development
- Persistent storage management
- Modular Python design and software architecture

## **Next Steps**
- Migrate CLI to Web Interface
- Add real time updates (created / updated / approved)
- Implement hashed passwords and session management

## **How to Run**
python3 main.py

## **Folder Structure**
```
mini-servicenow-cli/
│
├── main.py          # Entry point and CLI navigation
├── models.py        # Classes: User, Request
├── workflow.py      # Workflow logic (CRUD, approvals, status updates)
├── database.json    # Simple persistent storage for users/requests
├── auth.py          # Authentication logic for all users 
└── README.md        # This file
```

