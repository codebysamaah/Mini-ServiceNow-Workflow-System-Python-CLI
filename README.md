# Mini ServiceNow Workflow System - Python CLI
A simple command-line interface (CLI) workflow system simulating ServiceNow functionality. Built in Python, this project implements role-based request management with separate user and manager workflows, supporting login, CRUD operations, approvals, and request tracking.

## **Features**

### Users (Employees)
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
- **User**: Represents an employee; can create and manage their own requests
- **Manager**: Represents a manager; can approve, reject, and manage all requests
- **Request**: Represents a service request with fields for title, user, description, and status
- **Workflow**: Contains main business logic and methods for request creation, approval, updating, and viewing

## **Skills and Concepts Demonstrated**
- Object-Oriented Programming (OOP)
- Role-based access control (RBAC)
- CRUD operations
- CLI interface development
- Modular Python design and software architecture

## **Folder Structure**
```
mini-servicenow-cli/
│
├── main.py      # Entry point and CLI navigation
├── models.py    # Classes: User, Manager, Request
├── workflow.py  # Workflow logic (CRUD, approvals, status updates)
├── data.json    # simple persistence for users/requests
└── README.md    # This file
```

