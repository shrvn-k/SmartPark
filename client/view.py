import client as cont
# import querystring as qs

def display_pin(pin):
	print "\n"
	print "\tplease note your PIN:"
	print "\t","-"*20
	print "\t\t",pin

def display_registerd_user():
	print "You Number plate is already registred!"

def display_already_admin():
	print "\n"
	print "\tEither You are already an admin "
	print "\tOr your entry details conflict with another admin!! "
	print "\tTry different username or password"

def display_sucessful_login():
	print "\n"
	print "\tSucessful login"

def display_unsucessful_login():
	print "\n"
	print "\tIncorrect Username or Password !!"

def display_not_logged():
	print "\n"
	print "\tNot Loged in!!"

def display_not_super_admin():
	print "\n"
	print "\tSuper Password miss match!!"

def display_sucessful_admin_created():
	print "\n"
	print "\tSucessfully created the admin!!"

def display_sucessful_delete_admin():
	print "\n"
	print "\tSucessfully deleted the admin!!"

def display_unsucessful_delete_admin():
	print "\n"
	print "\tNo such admin found!!"

def display_sucessful_bypass():
	print "\n"
	print "\tgatepassed Sucessfully!!"

def display_unsucessful_bypass():
	print "\n"
	print "\tcould not gatepass!!"

def display_sucessful_gatepass():
	print "\n"
	print "\tgatepassed Sucessfully!!"

def display_unsucessful_gatepass():
	print "\n"
	print "\tcould not gatepass!!"

def display_sucessful_deregister():
	print "\n"
	print "\tSucessfully De-registered!!"

def display_unsucessful_deregister():
	print "\n"
	print "\tno plate match!!"

def display_sucessful_logout():
	print "\n"
	print "\tSucessfull logout!!"

def display_improper_username():
	print "\n"
	print "\timproper username!!"


def add_admin():


	print "Name :"
	name = raw_input()

	print "Mob :"
	mob = raw_input()
	try:
		mob = int(mob)
	except:
		print "incorrect mob no."
		#print "Mob :"
		
	print "Email :"
	email = raw_input()

	print "Username :"
	username = raw_input()

	print "Password :"
	password = raw_input()

	print "Confirm Password :"
	cpassword = raw_input()

	
	if password != cpassword:
		print "password did'nt match!"
		add_admin()

	suadmin = raw_input("Enter the super password: ")

	print ("Enter 'Y' to add 'N' to exit")
	option = raw_input("Enter your option: ")
	
	if option == 'y' or option == 'Y':
		values = [name,mob,email,username,password,suadmin]
		cont.add_admin(values)
	else: load_GUI()

def register_vehicle():
	cont.make_reg_true()
	#######################
	from time import *
	#######################
	automated = raw_input('Do you want to recognize plate automatically? : ')
	if automated == 'Y' or automated == 'y':
		#################################
		start = time()
		lplate = cont.recognize_plate()
		end = time()
		print 'time taken is :', end - start
		#################################
		if lplate is False:
			print 'Couldn\'t recognize the plate.'
			lplate = raw_input('Enter the plate No. : ')
		else:
			print 'The recognized plate No : ',lplate
			confirm = raw_input('please confirm plate : ')
			confirm = confirm.upper()
			if confirm != 'Y':
				lplate = raw_input('Enter the plate No.: ')

	else:
		lplate = raw_input('Enter the plate No.: ')

	print "Name :"
	name = raw_input()

	print "Mob :"
	mob = raw_input()
	mob = int(mob)

	print "Email :"
	email = raw_input()

	# print 'lpate ===',lpate

	# print "Vehicle No :"
	# lplate = raw_input()

	###########################
	# name = 'bsdfdgdgsf'
	# mob = 42455562
	# email = "sasdfsdfsfs212"

	# lpalte = "ka 30 abcd"

    ################################

	print ("Enter 'Y' to register 'N' to exit")
	option = raw_input("Enter your option: ")
	if option == 'y' or option == 'Y':
		owner = [name,mob,email]
		vehicle = [lplate]
		#ownership = []
		cont.register_vehicle(owner,vehicle)
	else: load_GUI()

def deregister_vehicle():
	
	print "Vehicle No :"
	lplate = raw_input()

	print ("Enter 'Y' to De-register 'N' to exit")
	option = raw_input("Enter your option: ")
	if option == 'y' or option == 'Y':
		cont.deregister_vehicle(lplate)
	else: load_GUI()

def emergency_bypass():

	lplate = raw_input("Vehicle No :")

	print ("Enter 'Y' to Bypass 'N' to exit")
	option = raw_input("Enter your option: ")
	if option == 'y' or option == 'Y':
		cont.emergency_bypass(lplate)
	else: load_GUI()

# def gate_pass():
# 	plate = cont.recognize_plate()
# 	# print plate
# 	if not plate:
# 		sucess = False
# 	else: sucess = cont.gate_pass(plate)
# 	# print sucess

# 	if sucess is not None:
# 		pin = raw_input('Enter the PIN: ')
# 		pin = int(pin)
# 		pinSucess = cont.gate_pass_via_pin(pin)
# 	else:
# 		cont.gate_pass(plate)

def login():
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	cont.login(username,password)

def delete_admin():
	username = raw_input('Enter  the username: ')
	suadmin = raw_input('Enter the super password: ')
	cont.delete_admin(username,suadmin)

def disp_head(table,col):
	
	print ' ' * 35, table
	print '_' * 80
	sp = ' ' * 20
	st = sp.join(col)
	print st
	print '_' * 80

def disp_body(table,fields):
	from model import *
	fields = ','.join(fields)
	values = retrive_values(fields,table)
	for val in values:
		for i in val:
			print '{: ^10}'.format(i),'\t',
		print '\n'	


def display_rows():
	pass

def view_logs(option = 1):

	REGISTER = ['VEHICLE','OWNER','ADMIN','DATE']
	BYPASSED = ['VEHICLE','ADMIN','DATE']
	PARKED = ['VEHICLE','ADMIN','TIME']

	record = None

	if option == 1:
		record = cont.get_registered_vehicles()
		disp_head("REGISTER",REGISTER)
	elif option == 2:
		record = cont.get_bypassed_vehicles()
		disp_head("BYPASSED",BYPASSED)
	elif option == 3:
		record = cont.get_parked_vehicles()
		disp_head("PARKED",PARKED)
	else :
		print 'wrong option!' 
		return

	for rec in record:
			for r in rec:
				print '{: ^10}'.format(r),'\t',
			print '\n'	
			# print '\n'

	



def load_GUI():

	print("1. ADD ADDMIN")
	print("2. REGISTER VEHICLE")
	print("3. DE-REGISTER VEHICLE")
	print("4. EMERGENCY BYPASS")
	print("5. VIEW LOGS")
	print("6. Login")
	print("7. Logout")
	print("8. VIEW Tables")
	print("9. delete Admin")
	# print("10. Gate pass")

	option = input("Enter your option: ")

	while option >= 1 and option <= 9:
		
		if option == 1:
			add_admin()
		elif option == 2:

			register_vehicle()
		elif option == 3:
			deregister_vehicle()
		elif option == 4:
			emergency_bypass()
		elif option == 5:
			print """ 
			1. REGISTERED
			2. BYPASSED
			3. PARKED"""

			choice = input('Enter you choice: ')
			cont.get_log_data(choice)
		elif option == 6:
			login()
		elif option == 7:
			cont.logout()
		elif option == 8:
			# display_rows()
			disp_all_rows()
		elif option == 9:
			delete_admin()
		# elif option == 10:
		# 	gate_pass()
		else: 

			
			exit()
		option = input("Enter your option: ")
	cont.logout()

#global data dictonary for mapping methods
# methods = {
# 			'view.display_not_super_admin':display_not_super_admin,
# 			'view.display_already_admin' :display_already_admin,
# 			'view.display_sucessful_admin_created':display_sucessful_admin_created,
# 			'view.display_sucessful_delete_admin' : display_sucessful_delete_admin,
# 			'view.display_not_super_admin' : display_not_super_admin,
# 			'view.display_registerd_user' : display_registerd_user,
# 			'view.display_pin' : display_pin,
# 			'view.display_not_logged' : display_not_logged
# 		   }

methods = {

"view.display_pin" : display_pin,
"view.display_registerd_user" : display_registerd_user,
"view.display_already_admin" : display_already_admin,
"view.display_sucessful_login" : display_sucessful_login,
"view.display_unsucessful_login" : display_unsucessful_login,
"view.display_not_logged" : display_not_logged,
"view.display_not_super_admin" : display_not_super_admin,
"view.display_sucessful_admin_created" : display_sucessful_admin_created,
"view.display_sucessful_delete_admin" : display_sucessful_delete_admin,
"view.display_unsucessful_delete_admin" : display_unsucessful_delete_admin,
"view.display_sucessful_bypass" : display_sucessful_bypass,
"view.display_unsucessful_bypass" : display_unsucessful_bypass,
"view.display_sucessful_gatepass" : display_sucessful_gatepass,
"view.display_unsucessful_gatepass" : display_unsucessful_gatepass,
"view.display_sucessful_deregister" : display_sucessful_deregister,
"view.display_unsucessful_deregister" : display_unsucessful_deregister,
"view.display_sucessful_logout" : display_sucessful_logout,
"view.display_improper_username" : display_improper_username,

}

#####################################################################################		   


if __name__ == "__main__":
	# load_GUI()
	# display_rows()
	view_logs(2)
	pass
	
	
	