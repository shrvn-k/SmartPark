#!/usr/local/bin/jython
from java.lang import System

from javax.swing import JFrame
from javax.swing import ImageIcon

from java.awt import Color
from java.awt import BorderLayout
from java.awt import GridLayout
from java.awt import FlowLayout

from panels import *

from size import *



class MainWindow(JFrame):
	def __init__(self):

		# super(MainWindow,self).__init__()
		self.initGui()

	def  initGui(self):

		self.topPanel = TopPanel()
		centerPanel = CenterPanel()
		bottomPanel = BottomPanel()
		
		self.topPanel.setPreferredSize(Dimension(300,50))
		centerPanel.setPreferredSize(Dimension(600,200))
		bottomPanel.setPreferredSize(Dimension(300,100))

		# colors for testing
		# topPanel.setBackground(Color.RED)
		self.topPanel.setBackground(Color.decode('#202941'))
		# centerPanel.setBackground(Color.GREEN)
		# centerPanel.setBackground(Color.GREEN)
		bottomPanel.setBackground(Color.decode('#fddee6'))





		self.setLayout(BorderLayout())

		#add panels
		self.add(self.topPanel,BorderLayout.PAGE_START)
		self.add(centerPanel,BorderLayout.CENTER)
		self.add(bottomPanel,BorderLayout.PAGE_END)

		self.setTitle('Smart Parking System')
		icon = ImageIcon('sp_transparent.png')
		self.setIconImage(icon.getImage())
		self.pack()
		self.setSize(800,700)
		self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		self.setLocationRelativeTo(None)
		self.setVisible(True)
		self.topPanel.refresh()

if __name__ == '__main__':
	m1 = MainWindow()

	# m1.topPanel.refresh()
	# m1.refresh()
	
