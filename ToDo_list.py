action = raw_input("What would you like to do?")
day = raw_input("What day?").capitalize()



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
    Todo_list[day].append(action)
def get():
    for x in Todo_list[day]:
        print x
for x in range(0,7):
    #trying to get it to repeat the correct amount of times.
