from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
from controller import *

server = "localhost"
# server = "192.168.0.103"
# server = "172.17.9.28"
server = "172.17.1.52"

#do all the init functions here
init_controller()

def simpleAdd():
    return 4+4

#setup the server
server = SimpleXMLRPCServer((server, 8000))

print "Listening on port 8000..."
# register the functoins here
server.register_function(add_admin, "add_admin")
server.register_function(delete_admin, "delete_admin")
server.register_function(register_vehicle, "register_vehicle")
server.register_function(deregister_vehicle, "deregister_vehicle")
server.register_function(emergency_bypass, "emergency_bypass")
server.register_function(gate_pass, "gate_pass")
server.register_function(gate_pass_via_pin, "gate_pass_via_pin")
server.register_function(login, "login")
server.register_function(logout, "logout")
server.register_function(disp_all_rows, "disp_all_rows") 
server.register_function(get_log_data, "get_log_data")
server.register_function(recognize_plate, "recognize_plate")
server.register_function(make_reg_true, "make_reg_true") 
server.register_function(make_reg_false, "make_reg_false") 
server.register_function(set_progress, "set_progress") 
server.register_function(get_progress, "get_progress") 
server.register_function(get_current_admin, "get_current_admin") 
server.register_function(simpleAdd, "simpleAdd") 



#run server forever 
server.serve_forever()
# print 'kkkkkkkkkkkkkkkkk'
