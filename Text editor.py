class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * max_size
        self.top = -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, data):
        if self.is_full():
            print("Stack is full")
        else:
            self.top += 1
            self.elements[self.top] = data

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.elements[self.top]
            self.top -= 1
            return data


# Input student names
student_names = input("Enter Text : ")

clipboard = Stack(len(student_names))  # To store copied/cut data


def cut(start, end):
    global clipboard, student_names

    if start >= 0 and end < len(student_names):
        cut_data = student_names[start : end + 1]
        clipboard = Stack(len(cut_data))
        for name in cut_data:
            clipboard.push(name)
        student_names = student_names[:start] + student_names[end + 1 :]
        print("Cut successful.")


def copy(start, end):
    global clipboard
    if start >= 0 and end < len(student_names):
        copied_data = student_names[start : end + 1]
        clipboard = Stack(len(copied_data))
        for name in copied_data:
            clipboard.push(name)
        print("Copy successful.")


def paste(index):
    global clipboard, student_names
    if not clipboard.is_empty() and index >= 0 and index <= len(student_names):
        paste_data = []
        while not clipboard.is_empty():
            paste_data.insert(0, clipboard.pop())
        student_names = (
            student_names[:index] + "".join(paste_data) + student_names[index:]
        )
        print("Paste successful.")


# Main program loop
while True:
    print("Student Names:", student_names)
    print("Clipboard Contents:", clipboard.elements)

    print("\nMenu:")
    print("1. Cut")
    print("2. Copy")
    print("3. Paste")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        start = int(input("Enter start index to cut: "))
        end = int(input("Enter end index to cut: "))
        cut(start, end)
    elif choice == 2:
        start = int(input("Enter start index to copy: "))
        end = int(input("Enter end index to copy: "))
        copy(start, end)
    elif choice == 3:
        index = int(input("Enter index to paste: "))
        paste(index)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose again.\n")
