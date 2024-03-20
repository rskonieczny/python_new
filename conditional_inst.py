port_status = "up"
if port_status == "up" :
    print("The port is operational.")


if port_status == "up" :
    print("The port is operational.")
else :
    print("The port is down")


port_speed = 1000
if port_speed == 100 :
    print("FastEth port")
elif port_speed == 1000 :
    print("Giga port")
else :
    print("Speed unrecognized")

########################
    
interface_configs = {
    "Giga0/1" : {"status" : "up" , "vlan" : "10"},
    "Giga0/2" : {"status" : "down" , "vlan" : "20"},
    "Giga0/3" : {"status" : "up" , "vlan" : "10"}
}


