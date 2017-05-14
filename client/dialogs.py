from javax.swing import JOptionPane

#####################################################################################

def display_pin(pin):
	# print "\n"
	# print "\tplease note your PIN:"
	msg = 'please note your PIN: ' + str(pin)
	dispInformationMsg(msg)

def display_registerd_user():
	msg =  "You Number plate is already registred!"
	dispWarningMsg(msg)


def display_already_admin():
	msg = 'Either You are already an admin '
	msg += 'Or your entry details conflict with another admin'
	msg += 'Try different username or password'
	dispWarningMsg(msg)


def display_sucessful_login():
	msg =  "Sucessful login"
	dispInformationMsg(msg)

def display_unsucessful_login():
	msg = "Incorrect Username or Password !!"
	dispErrorMsg(msg)

def display_not_logged():
	msg = "Not Loged in!!"
	dispErrorMsg(msg)

def display_not_super_admin():
	msg = 'Super Password miss match'
	dispErrorMsg(msg)


def display_sucessful_admin_created():
	msg = "Sucessfully created the admin"
	dispInformationMsg(msg)

def display_sucessful_delete_admin():
	msg = "Sucessfully deleted the admin!!"
	dispInformationMsg(msg)

def display_unsucessful_delete_admin():
	msg = "No such admin found!!"
	dispErrorMsg(msg)

def display_sucessful_bypass():
	msg = "gatepassed Sucessfully!!"
	dispInformationMsg(msg)

def display_unsucessful_bypass():
	msg = "could not gatepass!!"
	dispErrorMsg(msg)

def display_sucessful_gatepass():
	msg = "gatepassed Sucessfully!!"
	dispInformationMsg(msg)

def display_unsucessful_gatepass():
	msg = "could not gatepass!!"
	dispErrorMsg(msg)

def display_sucessful_deregister():
	msg = "Sucessfully De-registered!!"
	dispInformationMsg(msg)

def display_unsucessful_deregister():
	msg = "no plate match!!"
	dispErrorMsg(msg)

def display_sucessful_logout():
	msg = "Sucessfull logout!!"
	dispInformationMsg(msg)

def display_improper_username():
	msg = "improper username!!"
	dispErrorMsg(msg)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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


def quitApplicationMsg(e):
	result = JOptionPane.showConfirmDialog(None,'Are you sure to quit?','Quit!', JOptionPane.YES_NO_OPTION)
	if result == JOptionPane.YES_OPTION:
		print 'exit'
		exit()

def improperInput(msg,title):
	# result = JOptionPane.showMessageDialog(None,'One or more fields are missing!','No Input', JOptionPane.WARNING_MESSAGE)
	result = JOptionPane.showMessageDialog(None,msg,title, JOptionPane.WARNING_MESSAGE)

def dispQuestion(msg,title):
    result = JOptionPane.showConfirmDialog(None,msg,title,JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
    if result == JOptionPane.YES_OPTION:
    	return True
    return False

def dispInformationMsg(msg):
	JOptionPane.showMessageDialog(None,msg,);

def dispErrorMsg(msg):
	JOptionPane.showMessageDialog(None,msg,"Error", JOptionPane.ERROR_MESSAGE)

def dispWarningMsg(msg):
	JOptionPane.showMessageDialog(None,msg,"Warning", JOptionPane.WARNING_MESSAGE)



# def onError(self, e):
#         JOptionPane.showMessageDialog(self.panel, "Could not open file",
#             "Error", JOptionPane.ERROR_MESSAGE)

# def onWarning(self, e):
#     JOptionPane.showMessageDialog(self.panel, "A deprecated call",
#         "Warning", JOptionPane.WARNING_MESSAGE)

# def onQuestion(self, e):
#     JOptionPane.showMessageDialog(self.panel, "Are you sure to quit?",
#         "Question", JOptionPane.QUESTION_MESSAGE)

# def onInform(self, e):
#     JOptionPane.showMessageDialog(self.panel, "Download completed",
#         "Information", JOptionPane.INFORMATION_MESSAGE)

#methods for diplaying db interaction

