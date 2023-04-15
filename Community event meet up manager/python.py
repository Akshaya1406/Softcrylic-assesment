# Import necessary libraries
import datetime

# Define Event class
class Event:
    def __init__(self, name, date, location, description, online_event=False):
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.online_event = online_event
        
# Define User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.groups = []
        self.events = []
        
    def join_group(self, group):
        self.groups.append(group)
        
    def opt_in_event(self, event):
        self.events.append(event)
        
# Define Group class
class Group:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.members = []
        self.events = []
        
    def add_member(self, user):
        self.members.append(user)
        
    def create_event(self, name, date, location, description, online_event=False):
        event = Event(name, date, location, description, online_event)
        self.events.append(event)
        
# Define EventAdmin class
class EventAdmin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        
    def create_group(self, name, description):
        group = Group(name, description)
        return group
        
    def create_event(self, group, name, date, location, description, online_event=False):
        event = group.create_event(name, date, location, description, online_event)
        return event
        
# Define Coordinator class
class Coordinator(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        
# Example usage
admin = EventAdmin("John Doe", "admin@example.com")
group = admin.create_group("Python Developers", "A group for Python developers")
event = admin.create_event(group, "Python Meetup", datetime.datetime(2023, 5, 15, 14, 0), "123 Main St", "Monthly Python meetup")
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
coordinator = Coordinator("Charlie", "charlie@example.com")
group.add_member(user1)
group.add_member(user2)
coordinator.opt_in_event(event)
user1.join_group(group)
user1.opt_in_event(event)
user2.join_group(group)
