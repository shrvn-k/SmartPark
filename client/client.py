import xmlrpclib
import dialogs

host = "http://localhost:8000/"
# host = 'http://192.168.0.103:8000'
host = 'http://192.168.43.253:8000'
# host = "http://172.17.9.28:8000/"
# host = "http://172.168.1.52:8000/"

#create a proxy server 
proxy = xmlrpclib.ServerProxy(host)

#define interface methods from view to controller
def add_admin(values):
	# global proxy
	data = proxy.add_admin(values)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	print 'name-',name
	met()
	# met = view.methods[name]
	# met()

def delete_admin(username,suadmin):
	data = proxy.delete_admin(username,suadmin)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	met()

def register_vehicle(owner,vehicle):
	data = proxy.register_vehicle(owner,vehicle)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	if param:
		met(param[0])
	else:
		met()
		# pass

def make_reg_true():
	data = proxy.make_reg_true()
	# print data['regFalg'] 

def make_reg_false(): 
	data = proxy.make_reg_false()

def deregister_vehicle(vehicle):
	data = proxy.deregister_vehicle(vehicle)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	met()

def emergency_bypass(lplate):
	data = proxy.emergency_bypass(lplate)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	met()

def set_progress(values):
	proxy.set_progress(values)

def get_progress():
	data = proxy.get_progress()
	return data

# def gate_pass(lplate):
# 	data = proxy.gate_pass(lplate)
# 	# print data
# 	name = data['name']
# 	param = data['param']
# 	met = view.methods[name]
# 	met()

# def gate_pass_via_pin(pin):
# 	data = proxy.gate_pass_via_pin(pin)
# 	# name = data['name']
# 	param = data['param']
# 	met = view.methods[name]
# 	met()

def login(username,password):
	data = proxy.login(username,password)
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	met()

def logout():
	data = proxy.logout()
	name = data['name']
	param = data['param']
	met = dialogs.methods[name]
	met()

def disp_all_rows():
	data = proxy.disp_all_rows()
	owners = data['Owner']
	head = owners['head']
	values = owners['values']
	for i in head:
		print i,'\t'
	for i in values:
		print i,'\t'
	
def get_log_data(choice):
	# print 'hello'
	parkHead = ["Lplate","Username","time"]
	bypassHead = ["Lplate","Username","time"]
	regHead = ["Lplate","Name","Username","Date"]
	data = proxy.get_log_data(choice)
	# print type(data)
	data = data['Records']
	# if choice == 1:
	# 	print regHead[0],'\t',regHead[1],'\t',regHead[2],'\t'
	# if choice == 2:
	# 	for i in bypassHead:
	# 		print i,'\t'
	# if choice == 3:
	# 	for i in parkHead:
	# 		print i,'\t'
	# for i in data:
	# 	print i,'\t'
	return data
	
def recognize_plate():
	data = proxy.recognize_plate()
	return data


def get_current_admin():
	data = proxy.get_current_admin()
	return data

if __name__ == '__main__':
	# values = ['sdg',123565623,'sdfdsff','sdfsdf','226656','sms123']
	# values = ['sdsdg',1235565623,'sdfdsdsff','sdsfdfsdf','22656656','sms1d23']
	# add_admin(values)

	# suadmin = {'super_password': 'sms123', 'super_admin': 'supersms'}
	# add_admin(values)
	# username = 'dsfsdf'
	
	# delete_admin("sdsfdfsdf","sms123")
	# name = 'bhdfddadsfv'
	# mob = 1234854
	# email = "EMAILdf11.COM"
	# lpalte = "ka 2563 abcd"
	# str(lpalte)
	# owner = [name,mob,email]
	# vehicle = [lpalte]
	# register_vehicle(owner,vehicle)
	# deregister_vehicle(lpalte)
	# emergency_bypass(lpalte)
	# gate_pass(lpalte)
	# pin = 569103
	# gate_pass_via_pin(pin)
	# username = "ak123"
	# password = "ak123"
	# login(username,password)
	# logout()

	disp_all_rows()


	





