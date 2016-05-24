Todo_list = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': []
}
def add():
    action = raw_input("What would you like to do today?")
    day = raw_input("What day?").capitalize()
    Todo_list[day].append(action)
def get():
    day = raw_input("What day?").capitalize()
    for x in Todo_list[day]:
        print x
user_input = "something"
while user_input != "exit":
    user_input = raw_input("What would you like to do?")
    if user_input == "add":
        add()
    if user_input == "get":
        get()
