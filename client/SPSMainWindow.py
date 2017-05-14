#!/usr/local/bin/jython
from java.lang import System

from javax.swing import JFrame

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

		topPanel = TopPanel()
		centerPanel = CenterPanel()
		bottomPanel = BottomPanel()
		
		topPanel.setPreferredSize(Dimension(TOP_X,TOP_Y))
		centerPanel.setPreferredSize(Dimension(600,500))
		bottomPanel.setPreferredSize(Dimension(TOP_X,TOP_Y))

		# colors for testing
		topPanel.setBackground(Color.RED)
		centerPanel.setBackground(Color.GREEN)
		bottomPanel.setBackground(Color.BLUE)
		#

		self.setLayout(BorderLayout())

		#add panels
		self.add(topPanel,BorderLayout.PAGE_START)
		self.add(centerPanel,BorderLayout.CENTER)
		self.add(bottomPanel,BorderLayout.PAGE_END)

		self.setTitle('Smart Parking System')
		self.pack()
		self.setSize(800,700)
		self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		self.setLocationRelativeTo(None)
		self.setVisible(True)

if __name__ == '__main__':
	MainWindow()