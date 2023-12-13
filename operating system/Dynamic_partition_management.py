# 开发时间：2023/12/13 8:10
import pandas as pd
pd.set_option('display.max_colwidth', 20)

in_memorys = []
processes = []

class In_memory:
    size = 0
    address = 0

    def __init__(self,size,address):
        self.size = int(size)
        self.address = int(address)

    def __str__(self):
        return f"In_memory(size={self.size}, address={self.address})"

class Process:
    name = ''
    address = 0
    size = 0
    state = 0

    def __init__(self,name,m_address,desired_size):
        self.name = name
        self.address = int(m_address)
        self.size = int(desired_size)

    def __str__(self):
        return f"Process(name={self.name}, priority={self.address}, size={self.size})"

def init():     #初始化内存和进程
    global  in_memorys
    global processes
    print("init the storage and process")
    print("请以“大小 首址”的格式依次初始化内存空闲区")
    while(True):
        line = input()
        if line != "":
            values = line.split(" ")
            in_memory = In_memory(values[0],values[1])
            in_memorys.append(in_memory)
        else:
            break
    print("请以“进程名 进程所需内存大小”的格式依次初始化进程")
    while (True):
        line = input()
        if line != "":
            values = line.split(" ")
            process = Process(values[0],0,values[1])
            processes.append(process)
        else:
            break
    return in_memorys,processes

def show():     #输出内存和进程处理状态表
    global in_memorys
    global processes
    print("当前内存情况：")
    data = [{"size": in_memory.size,"address": in_memory.address}for in_memory in in_memorys]
    df = pd.DataFrame(data)
    print(df)
    print("当前进程处理情况：")
    data = [{"name": process.name, "address": process.address,"size":process.size,"state":process.state} for process in processes]
    df = pd.DataFrame(data)
    print(df)

def allocation(i,j):
    global in_memorys
    global processes
    processes[i].state = 1      #状态设置为被分配存储空间
    processes[i].address = in_memorys[j].address
    if processes[i].size == in_memorys[j].size:     #size相等的情况下删除此空闲块
        del in_memorys[j]
    else:
        in_memorys[j].address += processes[i].size
        in_memorys[j].size -= processes[i].size

def merge_memory_blocks(memory_blocks):
    # 按地址排序内存块
    sorted_blocks = sorted(memory_blocks, key=lambda x: x.address)

    merged_blocks = []
    current_block = sorted_blocks[0]

    for block in sorted_blocks[1:]:
        # 检查当前块的结束地址是否与下一个块的起始地址相同
        if current_block.address + current_block.size == block.address:
            # 合并内存块
            current_block.size += block.size
        else:
            # 添加当前块到结果列表，并更新当前块
            merged_blocks.append(current_block)
            current_block = block

    # 添加最后一个块
    merged_blocks.append(current_block)

    return merged_blocks

def recycle():
    global in_memorys
    global processes
    print("请输入要释放的进程名")
    p = input()
    for process in processes:
        if p == process.name and process.state == 1:
            in_memory = In_memory(process.size,process.address)
            in_memorys.append(in_memory)
            in_memorys = merge_memory_blocks(in_memorys)
            processes.remove(process)
            break
    else:
        print("Err : The process does not exit or is not executing")

def f_fa():
    print("正在使用最先适应算法...")
    global in_memorys
    global processes
    in_memorys.sort(key=lambda x:x.address)
    while (True):
        print("---menu---\n"
              "1.storage allocation\n"
              "2.storage recycle\n"
              "3.show\n")
        choice = int(input())
        if choice == 1:
            for i in range(0, len(processes)):
                for j in range(0, len(in_memorys)):
                    if processes[i].size <= in_memorys[j].size:
                        allocation(i, j)
                        in_memorys.sort(key=lambda x: x.address)
                        break
                    else:
                        break

        elif choice == 2:
            recycle()
            in_memorys.sort(key=lambda x: x.address)
        elif choice == 3:
            show()
        else:
            break
def w_fa():
    print("正在使用最坏适应算法...")
    global in_memorys
    global processes
    in_memorys.sort(key=lambda x: x.size,reverse=True)
    while (True):
        print("---menu---\n"
              "1.storage allocation\n"
              "2.storage recycle\n"
              "3.show\n")
        choice = int(input())
        if choice == 1:
            for i in range(0, len(processes)):
                if processes[i].size <= in_memorys[0].size:
                    allocation(i,0)
                    in_memorys.sort(key=lambda x: x.size, reverse=True)
                else:
                    continue
        elif choice == 2:
            recycle()
            in_memorys.sort(key=lambda x: x.size, reverse=True)
        elif choice == 3:
            show()
        else:
            break
def b_fa():
    print("正在使用最佳适应算法...")
    global in_memorys
    global processes
    in_memorys.sort(key=lambda x: x.size)
    while (True):
        print("---menu---\n"
              "1.storage allocation\n"
              "2.storage recycle\n"
              "3.show\n")
        choice = int(input())
        if choice == 1:
            for i in range(0, len(processes)):
                for j in range(0, len(in_memorys)):
                    if processes[i].size <= in_memorys[j].size:
                        allocation(i, j)
                        in_memorys.sort(key=lambda x: x.size)
                        break
                    else:
                        continue

        elif choice == 2:
            recycle()
            in_memorys.sort(key=lambda x: x.size)
        elif choice ==3:
            show()
        else:
            break

if __name__ == '__main__':
    init()
    show()
    while(True):
        print("---menu---\n"
              "1.First fit algorithm\n"
              "2.worst fit algorithm\n"
              "3.best fit algorithm\n"
              "4.show\n"
              "please choose the option\n")
        choice = int(input())
        if choice == 1:
            f_fa()
        elif choice == 2:
            w_fa()
        elif choice == 3:
            b_fa()
        elif choice == 4:
            show()
        else:
            break