katz_deli = ["Ada", "Malik"]

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for index, name in enumerate(line):
            line_str += f" {index +1}. {name}"
        print(line_str)

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(queue):
    if len(queue) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue[0]}.")
        queue.remove(queue[0])

