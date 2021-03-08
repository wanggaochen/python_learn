# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from datatype.datatype import*

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("python base learn ")
    data = 10
    print(type(data))
    result = int_data(data, True)
    print("%d,%d" % (result, data))
    data = 5
    result = int_data(data, False)
    print("%d,%d" % (result, data))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
