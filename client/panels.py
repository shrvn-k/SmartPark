#!/usr/local/bin/jython
from javax.swing import JPanel
from javax.swing import JButton
from javax.swing import JTextArea
from javax.swing import JScrollPane
from javax.swing import JLabel
from javax.swing import JTextField
from javax.swing import BorderFactory
from javax.swing import Box
from javax.swing import JOptionPane
from javax.swing import JTabbedPane
from javax.swing import JTable
from javax.swing import ImageIcon
from javax.swing.table import DefaultTableModel

from java.awt import GridBagConstraints;
from java.awt import GridBagLayout;
from java.awt import Insets;
from java.awt import BorderLayout
from java.awt import GridLayout
from java.awt import Dimension
from java.awt import Color

from size import *
import dialogs as dialog
import reutil as rut
import client 

def isFieldsEmpty(values):
	for i in values:
		if i == '':
			return True
	return False

class AboutPanel(JPanel):

	def __init__(self):
		self.setLayout(BorderLayout())
		self.initComponents()

	def initComponents(self):
		textArea = JTextArea(40,50)
		aboutLabel = JLabel('About us')
		footLabel = JLabel('Thank you for using Smart Park')
		textArea.setLineWrap(True)
		# textArea.setPreferredSize(Dimension( 250,250))

		#WRITING INTO TEXT AREA
		f = open('about.txt','r')
		line = f.read()
		textArea.append(line)
		f.close()
		textArea.setEditable(False)

		self.add(aboutLabel,BorderLayout.PAGE_START)
		self.add(JScrollPane(textArea),BorderLayout.CENTER)
		self.add(footLabel,BorderLayout.PAGE_END)


class AddAdminForm(JPanel):

	def __init__(self):
		self.nameLabel = JLabel('Name : ')
		self.nameField = JTextField(10)
		self.mobLabel = JLabel('Mob : ')
		self.mobField = JTextField(10)
		self.emailLabel = JLabel('Email : ')
		self.emailField = JTextField(10)
		self.userNameLabel = JLabel('Username : ')
		self.userNameField = JTextField(10)
		self.passwordLabel = JLabel('Password : ')
		self.passwordField = JTextField(10)
		self.confirmPasswordLabel = JLabel('Confirm Password : ')
		self.confirmPasswordField = JTextField(10)
		self.superPassLabel = JLabel('Super Password : ')
		self.superPassField = JTextField(10)
		self.addAdminBtn = JButton('Add',actionPerformed = self.addAdminToDb)
		self.setPreferredSize(Dimension(400,CENTER_Y))
		self.initComponents()

	def initComponents(self):

		#set the layout and add form components
		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()

		gc.weightx = 1
		gc.weighty = 1

		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.nameLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.nameField,gc)	

		# Second Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.mobLabel,gc)

		gc.gridx = 1

		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.mobField,gc)

		#Third Row
		gc.gridy += 1

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.emailLabel,gc)


		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.emailField,gc)


		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0,0,0,5)
		self.add(self.userNameLabel,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.userNameField,gc)

		# Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0,0,0,5)
		self.add(self.passwordLabel,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.passwordField,gc)

		# Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0,0,0,5)
		self.add(self.confirmPasswordLabel,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.confirmPasswordField,gc)

		# Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0,0,0,5)
		self.add(self.superPassLabel,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.superPassField,gc)

		# Next Row

		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.addAdminBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('Add Admin')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def addAdminToDb(self,e):
		# print 'yolo'
		name = self.nameField.getText()
		mob = self.mobField.getText()
		email = self.emailField.getText()
		username = self.userNameField.getText()
		password = self.passwordField.getText()
		confirmPassword = self.confirmPasswordField.getText()
		supePassword = self.superPassField.getText()

		fields = [name,mob,email,username,password,confirmPassword,supePassword]

		if isFieldsEmpty(fields):
			dialog.improperInput('One or more fields are missing!','No Input')
		elif not rut.isMobileNo(mob):
			dialog.improperInput('Invalid mobile number','Invalid Input')
		elif not rut.isEmail(email):
			dialog.improperInput('Enter a valid email address','Invalid email')
		elif confirmPassword != password:
			dialog.improperInput('Password and Confirm Password missmatch!','Mismatch Password')
		else: 
			values = [name,mob,email,username,password,supePassword]
			client.add_admin(values)

class RegForm(JPanel):
	
	def __init__(self):

		self.nameLabel = JLabel('Owner Name : ')
		self.nameField = JTextField(10)
		self.mobLabel = JLabel('Mob No : ')
		self.mobField = JTextField(10)
		self.emailLabel = JLabel('Email : ')
		self.emailField = JTextField(10)
		self.vehicleLabel = JLabel('Vehicle No : ')
		self.vehicleField = JTextField(10)
		self.regBtn = JButton('Register',actionPerformed = self.registerVehicle)
		icon = ImageIcon("Refreshp.png")
		self.automateRecogBtn = JButton('Auto',icon,actionPerformed = self.automateRecognition)
			
		self.setPreferredSize(Dimension(400,CENTER_Y))
		self.initComponents()

	def initComponents(self):

		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()

		gc.weightx = 1
		gc.weighty = 1

		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.nameLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.nameField,gc)	

		# Second Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.mobLabel,gc)

		gc.gridx = 1

		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.mobField,gc)

		#Third Row
		gc.gridy += 1

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.emailLabel,gc)


		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.emailField,gc)


		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0
		gc.anchor = GridBagConstraints.FIRST_LINE_END
		gc.insets = Insets(0,0,0,5)
		self.add(self.vehicleLabel ,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.vehicleField,gc)

		gc.weightx = 1
		gc.weighty = 0.2
		gc.gridx = 2
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		gc.insets = Insets(0,0,0,0)
		self.add(self.automateRecogBtn,gc)


		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.regBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('Register Vehicle')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))


	def registerVehicle(self,e):
		print 'panel done'

		name = self.nameField.getText()
		mob = self.mobField.getText()
		email = self.emailField.getText()
		lplate = self.vehicleField.getText()

		fields = [name,mob,email,lplate]
		if isFieldsEmpty(fields):
			dialog.improperInput('One or more fields are missing!','No Input')
		elif not rut.isMobileNo(mob):
			dialog.improperInput('Invalid mobile number','Invalid Input')
		elif not rut.isEmail(email):
			dialog.improperInput('Enter a valid email address','Invalid email')
		else:
			lplate = rut.removeSpace(lplate)
			owner = [name,mob,email]
			vehicle = [lplate]
			client.register_vehicle(owner,vehicle)



	def automateRecognition(self,e):
		print 'Add automate recog here !!'
		plate = client.recognize_plate()
		if plate:
			msg = 'confirm plate:' + plate
			dialog.dispQuestion(msg,'confirm')
		else:
			dialog.dispErrorMsg('coudnot reocnize!')


class DeleteAdminForm(JPanel):
	def __init__(self):
		self.usernameLabel = JLabel('Username : ')
		self.usernameField = JTextField(10)
		self.superPassLabel = JLabel('Super Password : ')
		self.superPassField = JTextField(10)
		self.deleteAdminBtn = JButton('Delete',actionPerformed = self.deleteAdmin)
		self.initComponents()

	def initComponents(self):
		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()

		gc.weightx = 1
		gc.weighty = 1

		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.usernameLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.usernameField,gc)	

		# Second Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.superPassLabel,gc)

		gc.gridx = 1

		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.superPassField,gc)

		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.deleteAdminBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('Delete Admin')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def deleteAdmin(self,e):
		username = self.usernameField.getText()
		superPass = self.superPassField.getText()

		if isFieldsEmpty([username,superPass]):
			dialog.improperInput('One or more fields are missing!','No Input')
		else:
			client.delete_admin(username,superPass)
class DeregisterForm(JPanel):
	
	def __init__(self):
		self.vehicleLabel = JLabel('Vehicle No : ')
		self.vehicleField = JTextField(10)
		self.deregisterBtn = JButton('De-Register',actionPerformed = self.deRegister)
		self.inintComponents()

	def inintComponents(self):

		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()

		gc.weightx = 1
		gc.weighty = 1

		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.vehicleLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.vehicleField,gc)	

		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.deregisterBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('De-Register Vehicle')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def deRegister(self,e):
		lplate = self.vehicleField.getText()


		if isFieldsEmpty([lplate]):
			dialog.improperInput('One or more fields are missing!','No Input')
		else:
			lplate = rut.removeSpace(lplate)
			client.deregister_vehicle(lplate)

class EmergencyBypassForm(JPanel):

	def __init__(self):
		self.vehicleLabel = JLabel('Vehicle No: ')
		self.vehicleField = JTextField(10)
		self.bypassBtn = JButton('Bypass',actionPerformed = self.emergencyBypass)
		self.initComponents()

	def initComponents(self):

		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()

		gc.weightx = 1
		gc.weighty = 1

		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.vehicleLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.vehicleField,gc)

		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.bypassBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('Emergency Bypass')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def emergencyBypass(self,e):
		lplate = self.vehicleField.getText()
		if isFieldsEmpty([lplate]):
			dialog.improperInput('One or more fields are missing!','No Input')
		else:
			lplate = rut.removeSpace(lplate)
			print lplate


class LoginForm(JPanel):
	def __init__(self):
		self.usernameLabel = JLabel('Username : ')	
		self.usernameField = JTextField(10)
		self.passwordLabel = JLabel('Password : ')
		self.passwordField = JTextField(10)
		self.loginBtn = JButton('Login',actionPerformed = self.login)
		self.initComponents()

	def initComponents(self):

		self.setLayout(GridBagLayout())

		gc = GridBagConstraints()


		# First Row
		gc.gridy = 0

		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.fill = GridBagConstraints.NONE
		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.usernameLabel,gc)

		gc.gridx = 1
		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.usernameField,gc)	

		# Second Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 0.1
		gc.gridx = 0

		gc.anchor = GridBagConstraints.LINE_END
		gc.insets = Insets(0, 0, 0, 5)
		self.add(self.passwordLabel,gc)

		gc.gridx = 1

		gc.anchor = GridBagConstraints.LINE_START
		gc.insets = Insets(0, 0, 0, 0)
		self.add(self.passwordField,gc)


		#Next Row
		gc.gridy += 1
		gc.weightx = 1
		gc.weighty = 2.0
		gc.gridx = 1
		gc.anchor = GridBagConstraints.FIRST_LINE_START
		self.add(self.loginBtn,gc)

		innerBorder = BorderFactory.createTitledBorder('Login ')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def login(self,e):
		username = self.usernameField.getText()
		password = self.passwordField.getText()

		fields = [username,password]

		if isFieldsEmpty(fields):
			dialog.improperInput('One or more fields are missing!','No Input')
		else:
			client.login(username,password)


class ViewLogsPanel(JPanel):
	def __init__(self):
		self.logTabbedPane = JTabbedPane()
		self.regTab = JPanel()
		self.bypassTab = JPanel()
		self.parkedTab = JPanel()
		self.regCols = ['Vehicle No','Owner','Admin','Date']
		self.parkCols = ['Vehicle No','Owner','Time']
		self.bypassCol = ['Vehicle No','Admin','Time']
		self.regTableData = []
		self.parkTableData = []
		self.bypassTableData = []

		self.loadRegData()
		self.loadParkData()
		self.loadBypassData()

		self.initComponents()

	def initComponents(self):
		dataModel = DefaultTableModel(self.regTableData, self.regCols)
		self.regTable = JTable(dataModel)
		scrollPaneReg = JScrollPane()
		scrollPaneReg.getViewport().setView((self.regTable))
		self.regTab.add(scrollPaneReg)
		# self.logTabbedPane.addTab('Registred',self.regTab)
		self.logTabbedPane.insertTab("Registred", None, self.regTab, None, 0)

		dataModel = DefaultTableModel(self.parkTableData, self.parkCols)
		self.parkTable = JTable(dataModel)
		scrollPanePark = JScrollPane()
		scrollPanePark.getViewport().setView((self.parkTable))
		self.parkedTab.add(scrollPanePark)
		# self.logTabbedPane.addTab('Parked',self.parkedTab)
		self.logTabbedPane.insertTab("Parked", None, self.parkedTab, None, 1)

		dataModel = DefaultTableModel(self.bypassTableData, self.bypassCol)
		self.bypassTable = JTable(dataModel)
		scrollPaneBypass = JScrollPane()
		scrollPaneBypass.getViewport().setView((self.bypassTable))
		self.bypassTab.add(scrollPaneBypass)
		# self.logTabbedPane.addTab('Bypassed',self.bypassTab)
		self.logTabbedPane.insertTab("Bypassed", None, self.bypassTab, None, 2)


		self.add(self.logTabbedPane)

		innerBorder = BorderFactory.createTitledBorder('View Logs ')
		outerBorder = BorderFactory.createEmptyBorder(5,5,5,5)
		self.setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder))

	def loadRegData(self):
		data = client.get_log_data(1)
		self.regTableData = data

	def loadParkData(self):
		data = client.get_log_data(3)
		self.parkTableData = data

	def loadBypassData(self):
		self.bypassTableData = client.get_log_data(2)

class CenterPanel(JPanel):

	def __init__(self):
		self.initComponents()
		self.addDefaultPanel(None)


	def initComponents(self):

		self.menuPanel = JPanel()
		self.initMenuPanel()
		self.currentPanel = AboutPanel()


		# colors for testing 
		self.menuPanel.setBackground(Color.PINK)
		self.setBackground(Color.YELLOW)
		
		# self.setLayout(GridLayout(1,2))
		self.setLayout(BorderLayout())
		self.add(self.menuPanel,BorderLayout.LINE_START)

	def initMenuPanel(self):

		buttonPanel = JPanel(GridLayout(10, 1, 5, 5))
		addAdmin = JButton('Add Admin', actionPerformed = self.addAdminPanel)
		deleteAdmin = JButton('Delete Admin',actionPerformed = self.addDeleteAdminPanel)
		regUser = JButton('Register User',actionPerformed = self.addRegPanel)
		deRegUser = JButton('De-Register User', actionPerformed = self.addDeregisterPanel)
		emgBypass = JButton('Emergency Bypass',actionPerformed = self.addEmergencyPanel)
		viewLogs = JButton('View Logs', actionPerformed = self.addViewLogsPanel)
		login = JButton('Login',actionPerformed = self.addLoginForm)
		logout = JButton('Logout',actionPerformed = self.logout)
		quit = JButton('Quit',actionPerformed = dialog.quitApplicationMsg)
		about = JButton('About',actionPerformed = self.addDefaultPanel)

		# buttonPanel.setPreferredSize(Dimension(200,350))
		# self.setPreferredSize(Dimension(250,250))

		#add widgets
		buttonPanel.add(addAdmin)
		buttonPanel.add(deleteAdmin)
		buttonPanel.add(regUser)
		buttonPanel.add(deRegUser)
		buttonPanel.add(emgBypass)
		buttonPanel.add(viewLogs)
		buttonPanel.add(login)
		buttonPanel.add(logout)
		buttonPanel.add(quit)
		buttonPanel.add(about)
		self.menuPanel.add(buttonPanel)


	def addDefaultPanel(self,e):
		client.make_reg_false()
		self.remove(self.currentPanel)
		self.currentPanel.setVisible(False)
		self.currentPanel = AboutPanel()
		self.currentPanel.setVisible(True)
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()


	def addAdminPanel(self,e):
		client.make_reg_true()
		self.remove(self.currentPanel)
		self.currentPanel.setVisible(False)
		self.currentPanel = AddAdminForm()
		self.currentPanel.setVisible(True)
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

	def addRegPanel(self,e):
		# client.make_reg_true()
		client.make_reg_true()
		self.remove(self.currentPanel)
		self.currentPanel = RegForm()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

	def addDeleteAdminPanel(self,e):
		self.remove(self.currentPanel)
		self.currentPanel = DeleteAdminForm()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

	def addDeregisterPanel(self,e):
		self.remove(self.currentPanel)
		self.currentPanel = DeregisterForm()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

		
	def addEmergencyPanel(self,e):
		self.remove(self.currentPanel)
		self.currentPanel = EmergencyBypassForm()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

	def addLoginForm(self,e):
		self.remove(self.currentPanel)
		self.currentPanel = LoginForm()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()

	def logout(self,e):
		result = dialog.dispQuestion('Do you want to logout?','Logut')
		if result:
			client.logout()
			# dialog.dispInformationMsg('Sucessfully Logout')
			self.addDefaultPanel(None)

	def addViewLogsPanel(self,e):
		self.remove(self.currentPanel)
		self.currentPanel = ViewLogsPanel()
		self.add(self.currentPanel,BorderLayout.CENTER)
		self.validate()



	
class BottomPanel(JPanel):
	pass

class TopPanel(JPanel):
	pass