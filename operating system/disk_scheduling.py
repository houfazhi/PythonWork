# 开发时间：2023/12/19 14:14


global diskNow


def FCFS():
    global diskNow
    print("please input the head access request sequence(delimited by space)\n")
    sq = input()
    orders = sq.split(" ")
    sequence = []
    sequence.append(diskNow)
    sequence += orders
    numberOfTracks = 0
    for order in orders:
        numberOfTracks += abs(int(order) - int(diskNow))
        diskNow = int(order)

    print("SCAN:\n"
          "sequence:", sequence)
    print("numberOfTraks", numberOfTracks)


def SSTF():
    global diskNow
    print("please input the head access request sequence(delimited by space)\n")
    sq = input()
    orders = sq.split(" ")
    numberOfTracks = 0
    sequence = []
    sequence.append(diskNow)
    while orders:
        sorted_orders = sorted(orders, key=lambda x: abs(int(x) - int(diskNow)))
        next_track = sorted_orders[0]
        diskNow = next_track
        sequence.append(next_track)
        numberOfTracks += abs(int(next_track) - int(diskNow))
        orders.remove(next_track)
    diskNow = int(sequence[-1])
    print("SCAN:\n"
          "sequence:", sequence)
    print("numberOfTraks", numberOfTracks)


def SCAN():
    global diskNow
    print("please input the head access request sequence(delimited by space)\n")
    sq = input()
    orders = sq.split(" ")
    orders = [int(order) for order in orders]  # 将字符串列表转换为整数列表
    print("please input the direction in which the magnetic head moves(0:DESC,1:ASC)\n")
    dr = input()
    numberOfTracks = 0
    list = []
    sequence = []
    sequence.append(diskNow)
    if dr == '0':
        lower_orders = [order for order in orders if int(order) < int(diskNow)]
        lower_orders.sort(reverse=True)
        upper_orders = [order for order in orders if int(order) >= int(diskNow)]
        upper_orders.sort()
        sequence += lower_orders
        sequence += upper_orders
        numberOfTracks = abs(int(diskNow) - int(lower_orders[-1])) + abs(int(upper_orders[-1]) - int(lower_orders[-1]))
    else:
        lower_orders = [order for order in orders if int(order) < int(diskNow)]
        lower_orders.sort(reverse=True)
        upper_orders = [order for order in orders if int(order) >= int(diskNow)]
        upper_orders.sort()
        sequence += upper_orders
        sequence += lower_orders
        numberOfTracks = abs(int(diskNow) - int(upper_orders[-1])) + abs(int(upper_orders[-1]) - int(lower_orders[-1]))
    diskNow = int(sequence[-1])

    print("SCAN:\n"
          "sequence:",sequence)
    print("numberOfTraks",numberOfTracks)
    print(lower_orders)
    print(upper_orders)

if __name__ == '__main__':
    global diskNow
    print("please input the location of the current head\n")
    diskNow = input()
    while (True):
        print("menu\n"
              "1.FCFS\n"
              "2.SSTF\n"
              "3.SCAN\n"
              "please choose the algorithm\n")
        choice = int(input())
        if choice == 1:
            FCFS()
            while(True):
                print("Continue to schedul?(yes/no)\n")
                if(input() == 'yes'):
                    FCFS()
                else:
                    break
        elif choice == 2:
            SSTF()
            while (True):
                print("Continue to schedul?(yes/no)\n")
                if (input() == 'yes'):
                    SSTF()
                else:
                    break
        elif choice == 3:
            SCAN()
            while (True):
                print("Continue to schedul?(yes/no)\n")
                if (input() == 'yes'):
                    SCAN()
                else:
                    break
        else:
            break
