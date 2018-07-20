from netaddr import *
import sys
"""
Script with <3
Took reference of: http://jodies.de/ipcalc
Module help: http://netaddr.readthedocs.io/en/latest/tutorial_01.html
"""
list_1 = []
#Default IP ranges and netmask
#Class A
class_ip_a_1 = IPAddress('10.0.0.0')
class_ip_a_2 = IPAddress('10.255.255.255')
class_netmask_a = '255.0.0.0'
class_ip_a_int_1 = int(class_ip_a_1)
class_ip_a_int_2 = int(class_ip_a_2)
class_ip_a_range = list(range(class_ip_a_int_1, class_ip_a_int_2))

#Class b
class_ip_b_1 = IPAddress('172.16.0.0')
class_ip_b_2 = IPAddress('172.31.255.255')
class_netmask_b = '255.255.240.0'
class_ip_b_int_1 = int(class_ip_b_1)
class_ip_b_int_2 = int(class_ip_b_2)
class_ip_b_range = list(range(class_ip_b_int_1, class_ip_b_int_2))


#Class C
class_ip_c_1 = IPAddress('192.168.0.0')
class_ip_c_2 = IPAddress('192.168.255.255')
class_netmask_c = '255.255.255.0'
class_ip_c_int_1 = int(class_ip_c_1)
class_ip_c_int_2 = int(class_ip_c_2)
class_ip_c_range = list(range(class_ip_c_int_1, class_ip_c_int_2))


def network_address(ip_net):
    global ip_net_3
    """ This function calculates the network address for a determinated IP with a netmask """
    ip_2 = IPAddress(ip_net) #Getting IPAddress out of the network
    netmask = ip_net.netmask #Getting the netmask out of the ip_2 ip address
    print("Your netmask is: {}\nYour IP is {}".format(netmask, ip_2))
    ip_3 = int(ip_2) #Convering to an INTEGER the IPAddress
    netmask_int = int(netmask) #Converting to an INTEGER the netmask
    ip_net_2 = ip_3 & netmask_int #IMPORTAND --> This makes the operation of AND with the IP and the netmask
    ip_net_3 = IPAddress(ip_net_2) #Converting to IP the integer value obtain from the operation
    print("Your network address is: {}".format(ip_net_3)) # For iterations to find which IP is in which PRIVATE CLASS
    #Here the scripts iterate on the different ranges to guess if the IP is between any of the ranges
    for x in class_ip_a_range:
        if ip_3 == x:
            print("You are using a private Class A IP, which means your netmask is: {}".format(class_netmask_a))
        else:
            print("This IP is not private Class A")
    for x in class_ip_b_range:
        if ip_3 == x:
            print("You are using a private Class B IP, which means your netmask is: {}".format(class_netmask_b))
        else:
            print("This IP is not private Class B")
    for x in class_ip_c_range:
        if ip_3 == x:
            print("You are using a private Class C IP, which means your netmask is: {}".format(class_netmask_c))
        else:
            print("This IP is not private Class C")
    return ip_net_3 #return the network address for further use


def all_ranges(main_network_ip, main_subnet, main_netmask_move):
    """ This functions prints all ranges avaiable for an especified network """
    print("You have the network --> {}".format(main_network_ip))
    print("Subnetting to {}".format(main_netmask_move))
    main_ip = IPNetwork(main_network_ip)
    main_netmask = main_ip.netmask
    print("Netmask --> {}".format(main_netmask))
    #Explanation of how this works
    print("""Ranges are divided like this:
    *Range IP: (Network address) <-- In this order. Every 1 of this indicates a range, as well as the network address
    *Broadcast IP: <-- This indicates the broadcast IP of the range
    *Min host: <-- Min host avaiable for that range
    *Max host: <-- Max host avaiable for that range
    Ranges will be now saved on subnet_range.txt """)
    num = int() #Var for range ID calculation
    orig_stdout = sys.stdout
    file_1 = open('subnet_range.txt', 'w')
    sys.stdout = file_1
    #This for do the magic
    for x in main_subnet: #Iterate from the main_subnet IP addresses, which indicate the range
        print("----------------------------")
        num += 1
        print("Range {}".format(num))
        print("Range IP: (Network address)", x) #Print the IP
        print("Broadcast IP: ", x.broadcast) #Print the broadcast of that range
        #This for iterates through the hosts of every IP range and save it into a list as an int
        for i in x.iter_hosts():
            b = int(i)
            c = list_1.append(b)
        #This part process the first and the last item of that list and print it. The list overwrite itself with the next iteration
        list_min_host_1 = str(list_1[1])
        list_max_host_1 = str(list_1[-1])
        list_min_host_2 = IPAddress(list_min_host_1)
        list_max_host_2 = IPAddress(list_max_host_1)
        print("Min hosts: ", list_min_host_2)
        print("Max hosts: ", list_max_host_2)
    sys.stdout = orig_stdout
    file_1.close()
    print("File saved!")
    return None

    #In case you want the ranges displayed on the screen
    #Delete lines 73, 74, 75, 91 and 92




#start
def __main__():
    print("Subnetting script by AdSanz ~ @AdSanz_IT // Twitter")
    option = input("What do you want to do:\n   1. Calculate the network address of an IP, and guess if its a class A, B, or C IP\n   2. Calculate ranges of a subnet \nChoose: ")
    if option == "1":
        print(
        """
        A litle reminder of classes:
        ---------------------------------------------------------------------------------
        Class	  Private Networks	        Subnet Mask	   Address Range                |
        A	      10.0.0.0	                255.0.0.0	   10.0.0.0 - 10.255.255.255    |
        B	      172.16.0.0 - 172.31.0.0	255.240.0.0	   172.16.0.0 - 172.31.255.255  |
        C	      192.168.0.0               255.255.0.0	   192.168.0.0 - 192.168.255.255|
        ---------------------------------------------------------------------------------
        """
        )
        main_net_ip = input("We need an IP with the netmask (Ej, 192.168.1.4/24): ")

        ip_net = IPNetwork(main_net_ip)
        network_address(ip_net)
        print("Thanks for using the script")
    elif option == "2":
        main_range_ip = input("We need the network IP, something like: 192.168.1.0/24\nRemember, we need the Class netmask, if you don't know which one it is, you can use the first option to guess it\nInput: ")
        main_network_ip = IPNetwork(main_range_ip)
        #main_subnet = list(main_network_ip.subnet())
        main_netmask_move = input("Netmask to move: (in bits --> 24) ")
        main_netmask_move_2 = int(main_netmask_move)
        main_subnet = list(main_network_ip.subnet(main_netmask_move_2))
        all_ranges(main_range_ip, main_subnet, main_netmask_move)
        print("Thanks for using the script")
    else:
        pass

__main__()
