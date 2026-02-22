import time
import os
import socket
import subprocess
default_commands = ["ls", "help", "add", "remove", "tick", "untick", "exit"]
termonal_command = []
list_Rutin = []
default_command_theme = """Rutin~>$"""
default_addr_theme = """Add~>$"""
index_y = "do you want remove things with index [yes/no]"
save_need = []
many_number = []
def termonal():
    command = input(default_command_theme)
    termonal_command.append(command)

while True:
    termonal()
    command = termonal_command.pop(0)
    if command == default_commands[6]:
        exit()
    elif command == default_commands[0]:
        for i in range(0, len(list_Rutin), 1):
            print(str(i)+".", list_Rutin[i])
    elif command == default_commands[1]:
        for i in range(0, len(default_commands), 1):
            print(str(i)+".", default_commands[i])
    elif command == default_commands[2]:
        print("pls try number you want place this and this ")
        print("example: 1 ; coock a dinner")
        comm = input(default_addr_theme).split(";")
        comm_int = int(comm[0])
        list_Rutin.insert(comm_int, comm[1])
    elif command == default_commands[3]:
        yes_no = input("do you want remove things with index [yes/no]")
        if yes_no == "yes":
            s = int(input("TYPE_INDEX~:$"))
            s2 = list_Rutin.pop(s)
            s2 = None
        elif yes_no == "no":
            s = input("name:")
            list_Rutin.remove(s)
        else:
            print("pls type corect")
    elif command == default_commands[4]:
        ask = input(index_y)
        if ask == "yes":
            number = int(input("Number:"))
            item = list_Rutin.pop(number)
            item = item+" ✅"
            list_Rutin.insert(number, item)
        elif ask == "no":
            item_name = input("name:")
            for i in range(0, len(list_Rutin), 1):
                lo = list_Rutin[i]
                if lo == item_name:
                    many_number.append(lo)
            finded = False
            for i in list_Rutin:
                if i == item_name:
                    finded = True
                    save_need.append(i)
                else:
                    print("ERROR not find")
            if finded == True:
                print("finded")
                list_Rutin.remove(item_name)
                op1 = save_need[0]+" ✅"
                list_Rutin.insert(many_number[0], op1)
                save_need.remove(save_need[0])
            else:
                print("NOT TRUE NOT FIND ")
    elif command == default_commands[5]:
        ask = input(index_y)
        if ask == "yes":
            inter = int(input("Number:"))
            item = list_Rutin.pop(inter)

            item = item.split(" ✅")
            item_orginal = item[0]
            print(item_orginal)
            list_Rutin.insert(inter, item_orginal)
