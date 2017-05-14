regFlag = False
#########################################################
ATT_OWNER = ['Name','Mob','Email']
ATT_VEHICLE = ['Lplate']
ATT_OWNERSHIP = ['Oid','Vid']
ATT_ADMIN = ['Name', 'Mob','Email','Username','Password','IsAdmin']
ATT_LOG = ['Vid','Time','IsBypassed','IsIn']
ATT_MAINTAINS = ['Aid','Lid',]
ATT_REGISTRY = ['Aid','Vid','Date','PIN']
#########################################################

dr_owner = "DROP TABLE IF EXISTS Owner"
dr_vehicle = "DROP TABLE IF EXISTS Vehicle"
dr_ownership = "DROP TABLE IF EXISTS Ownership"
dr_admin = "DROP TABLE IF EXISTS Admin"
dr_log = "DROP TABLE IF EXISTS Log"
dr_maintains = "DROP TABLE IF EXISTS Maintains"
dr_registry = "DROP TABLE IF EXISTS Registry"

cr_owner = """ CREATE TABLE Owner(
			   Oid INTEGER PRIMARY KEY AUTOINCREMENT, 
			   Name VARCHAR(30) NOT NULL,
			   Mob INT(10) UNIQUE NOT NULL,
			   Email VARCHAR(30) UNIQUE NOT NULL);"""

cr_vehicle = """ CREATE TABLE Vehicle(
			   Vid INTEGER PRIMARY KEY AUTOINCREMENT,
			   Lplate VARCHAR(30) UNIQUE NOT NULL,
			   IsReg BOOLEAN DEFAULT 1);"""

cr_ownership = """CREATE TABLE Ownership(
				  Oid INT(6) NOT NULL,
				  Vid INT(6) NOT NULL,
				  FOREIGN KEY (Oid) REFERENCES Owner(Oid),
				  FOREIGN KEY (vid) REFERENCES Vehicle(Vid));"""

cr_admin = """ CREATE TABLE Admin(
			   Aid INTEGER PRIMARY KEY AUTOINCREMENT,
			   Name VARCHAR(30) NOT NULL,
			   Mob INT(10) UNIQUE NOT NULL,
			   Email VARCHAR(30) UNIQUE NOT NULL,
			   Username VARCHAR(30) UNIQUE NOT NULL,
			   Password VARCHAR(30) UNIQUE NOT NULL,
			   IsAdmin BOOLEAN DEFAULT 1);"""

cr_log = """ CREATE TABLE Log(
			   Lid INTEGER PRIMARY KEY AUTOINCREMENT,
			   Vid INTEGER NOT NULL,
			   Time TIMESTAMP NOT NULL,
			   IsBypassed BOOLEAN DEFAULT 0,
			   IsIn BOOLEAN DEFAULT 1,
			   FOREIGN KEY (Vid) REFERENCES Vehicle(Vid));"""

cr_maintains = """CREATE TABLE Maintains(
				  Aid INT(6) NOT NULL,
				  Lid INT(6) NOT NULL,
				  FOREIGN KEY (Aid) REFERENCES Admin(Aid),
				  FOREIGN KEY (Lid) REFERENCES Log(Lid));"""

cr_registry = """ CREATE TABLE Registry(
			   Rid INTEGER PRIMARY KEY AUTOINCREMENT,
			   Aid INT(6) NOT NULL,
			   Vid INT(6) NOT NULL,
			   Date DATETIME NOT NULL,
			   PIN INT(6) NOT NULL UNIQUE,
			   FOREIGN KEY (Aid) REFERENCES Admin(Aid),
			   FOREIGN KEY (Vid) REFERENCES Vehicle(Vid));"""

################################## Insetion into table #######################################

it_owner = """ INSERT INTO Owner (Name,Mob,Email) VALUES (?, ?, ?) """

it_vehicle = """ INSERT INTO Vehicle (Lplate) VALUES (?) """

it_admin = """ INSERT INTO Admin (Name,Mob,Email,Username,Password) VALUES (?,?,?,?,?) """

it_log = """ INSERT INTO Log (Time,IsBypassed) VALUES (?,?) """

it_maintains = """ INSERT INTO Maintains (Aid,Lid,Vid) VALUES (?,?,?) """

it_registery = """ INSERT INTO Registry (Aid,Vid,Date,PIN) VALUES (?,?,?,?) """

it_ownership = """ INSERT INTO Ownership (Oid,Vid) VALUES (?,?) """





