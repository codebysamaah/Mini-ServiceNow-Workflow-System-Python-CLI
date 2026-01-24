class User:
    """
    Represents a user (employee and manager).
    """
    def __init__(self, username, role):
        self.username = username
        self.role = role  

class Request:
    """
    Represents a single workflow request.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

    def __init__(self, request_id, user, title, description, status=PENDING, manager_comment=""):
        self.id = request_id
        self.title = title
        self.description = description
        self.created_by = user
        self.status = status
        self.manager_comment = manager_comment
    
    def __str__(self):
        return (f"""
        ID: {self.id}
        Title: {self.title}
        Description: {self.description}
        Created By: {self.created_by}
        Status: {self.status}
        Manager Comment: {self.manager_comment}
        ------------------------
        """)

    def approve(self, comment):
        """
        Approve a request.
        """
        self.status = self.APPROVED
        self.manager_comment = comment

    def reject(self, comment):
        """
        Reject a request.
        """
        self.status = self.REJECTED
        self.manager_comment = comment

    def to_dict(self):
        """
        Make Request into dict format.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by,
            "status": self.status,
            "manager_comment": self.manager_comment
        }
    
    @staticmethod
    def from_dict(data):
        """
        Return a Request object.
        """
        return Request(
            data["id"],
            data["created_by"],
            data["title"],
            data["description"],
            data["status"],
            data.get("manager_comment", "")
        )
    