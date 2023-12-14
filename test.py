import pandas as pd

def f_fa():
    pass
def w_fa():
    pass
def b_fa():
    pass
if __name__ == '__main__':
    while (True):
        print("---menu---\n"
              "1.First fit algorithm\n"
              "2.worst fit algorithm\n"
              "3.best fit algorithm\n"
              "please choose the option\n")
        choice = int(input())
        if choice == 1:
            f_fa()
        elif choice == 2:
            w_fa()
        elif choice == 3:
            b_fa()
        else:
            break
