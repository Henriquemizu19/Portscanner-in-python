import socket
import time



# getting the host informations
host = input('Enter the ip adress: ')

try:
    hostIP = socket.gethostbyname(host)

except:
    print("\n\nInvalid adress :|")
    exit(1)


start_time = time.time()

print("\n\nif you want to close the program without scan, just press ctrl + c ;]")


# just a massege :-]

print("-" * 60)

print("Making a nice scan 4 u ;-)")

print("-" * 60)

# the cool part B)

try:
    for port in range(1, 1025):

        # create a connection with the target
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # checling errors in ports
        result = s.connect_ex((hostIP, port))

        if result == 0:

            print("{} port are open in {} host".format(port, host))

except KeyboardInterrupt:
    print("You ended the program ")
    exit(1)


print("\nThe scan are complete, thanks for use this device <3")


print("The time of execution is: {}".format(start_time))