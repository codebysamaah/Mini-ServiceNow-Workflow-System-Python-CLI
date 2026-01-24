from models import Request
import json

class Workflow:
    """
    Manages all requests in the workflow system.
    """
    def load_db(self):
        """
        Load database.
        """
        with open("database.json", "r") as f:
            return json.load(f)

    def save_db(self, db):
        """
        Save database.
        """
        with open("database.json", "w") as f:
            json.dump(db, f, indent=4)
    
    # Employee methods
    def create_request(self, user):
        """
        Create a new request.
        """
        title = input("\nTitle: ")
        description = input("Description: ")

        db = self.load_db()
        req_id = len(db["requests"]) + 1

        req = Request(req_id, user.username, title, description)
        db["requests"].append(req.to_dict())
        
        self.save_db(db)
        print(f"\nRequest {req_id} created successfully!\n")

    def view_my_requests(self, user):
        """
        View all requests made by user.
        """
        db = self.load_db()
        print("\n======My Requests======")
        for r in db["requests"]:
            if r["created_by"] == user.username:
                req = Request.from_dict(r)
                print(req)

    def view_my_request_status(self, user):
        """
        Check status of a request given a request_id.
        """
        db = self.load_db()
        req_id = int(input("Enter request ID: "))
        for r in db["requests"]:
            if r["id"] == req_id and r["created_by"] == user.username:
                status = r["status"]
                print("---------")
                print(f"\nStatus: {status}\n")
                print("---------")
                return
                    
        print(f"\nNo Request with id {req_id} found.\n")

    def update_request(self, user):
        """
        Update an existing request of a user.
        """
        db = self.load_db()
        req_id = int(input("Enter request ID to update: "))

        for i, r in enumerate(db["requests"]):
            if r["id"] == req_id and r["created_by"] == user.username:
                if r["status"] != "Pending":
                    print("\nOnly pending requests can be updated.\n")
                    return
            
                req = Request.from_dict(r)
                print("\nSelect from 1-3 to update the request.")
                print("1. Update title")
                print("2. Update description")
                print("3. Update both")

                choice = input("Choose an option: ")
                if choice == "1":
                    req.title = input("New title: ")
                elif choice == "2":
                    req.description = input("New description: ")
                elif choice == "3":
                    req.title = input("New title: ")
                    req.description = input("New description: ")
                else:
                    print("Invalid choice. Please select 1-3.")
                    return

                db["requests"][i] = req.to_dict()
                self.save_db(db)
                print("\nRequest updated.\n")
                return

        print("\nRequest not found or access denied.\n")

    # Manager methods
    def view_all_requests(self):
        """
        View all requests.
        """
        db = self.load_db()
        print("\n======All Requests======")
        for r in db["requests"]:
            req = Request.from_dict(r)
            print(req)

    def process_request(self):
        """
        Process a request.
        """
        db = self.load_db()
        req_id = int(input("Enter request ID: "))

        for i, r in enumerate(db["requests"]):
            if r["id"] == req_id:
                req = Request.from_dict(r)
                print(req)

                choice = input("Approve (a) / Reject (r): ").lower()
                comment = input("Manager comment: ")

                if choice == "a":
                    req.approve(comment)
                elif choice == "r":
                    req.reject(comment)
                else:
                    print("Invalid option.")
                    return

                db["requests"][i] = req.to_dict()
                self.save_db(db)
                print("\nRequest updated.\n")
                return

        print("\nRequest not found.")
    
    def generate_summary(self):
        """
        Generate a summary of all requests.
        """
        with open("database.json", "r") as f:
            db = json.load(f)

        total = len(db["requests"])
        pending = sum(r["status"] == "Pending" for r in db["requests"])
        approved = sum(r["status"] == "Approved" for r in db["requests"])
        rejected = sum(r["status"] == "Rejected" for r in db["requests"])

        print("\n======Request Summary=======")
        print(f"Total: {total}") 
        print(f"Pending: {pending}")
        print(f"Approved: {approved}")
        print(f"Rejected: {rejected}")
        print("=============================")
        