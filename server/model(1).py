import sqlite3
import querystring as qs
conn = None

def load_database():
    global conn
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row
    
    conn.execute("pragma foreign_keys=on;")

def close_database():
    global conn
    conn.close()

def create_tables():
    global conn

    try:

	    # conn.execute(qs.dr_owner)
	    conn.execute(qs.cr_owner)

	    # conn.execute(qs.dr_vehicle)
	    conn.execute(qs.cr_vehicle)

	    # conn.execute(qs.dr_ownership)
	    conn.execute(qs.cr_ownership)

	    # conn.execute(qs.dr_admin)
	    conn.execute(qs.cr_admin)

	    # conn.execute(qs.dr_log)
	    conn.execute(qs.cr_log)

	    # conn.execute(qs.dr_maintains)
	    conn.execute(qs.cr_maintains)

	    # conn.execute(qs.dr_registry)
	    conn.execute(qs.cr_registry)

    except sqlite3.OperationalError:
        pass


def insert_owner(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_OWNER[0]],row[qs.ATT_OWNER[1]],row[qs.ATT_OWNER[2]]))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()
        return False


def insert_vehicle(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_VEHICLE[0]],))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()
        return False

def updateAsReg(lpalte):
    global conn
    conn.execute('update Vehicle set IsReg =  ? where Lplate = ?',(True,lpalte))
    conn.commit()


def insert_admin(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_ADMIN[0]],row[qs.ATT_ADMIN[1]],row[qs.ATT_ADMIN[2]],row[qs.ATT_ADMIN[3]],row[qs.ATT_ADMIN[4]]))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # print "ERROR!!! -> already exist value - ERROR CODE - 501"
        print 'Alredy exsist!!!'
        print row[qs.ATT_ADMIN[3]]

        try:
        	curr = conn.execute('select Email,Username,IsAdmin from Admin where Username = ?',(row[qs.ATT_ADMIN[3]],))
       		curr = curr.fetchone()
       		email = row[qs.ATT_ADMIN[2]]
       		user = row[qs.ATT_ADMIN[3]]
       		isad = curr['IsAdmin']

       		if curr['Email'] == email and curr['Username'] == user and not isad:
       			print 'yeah!!'
       			conn.execute('update Admin set IsAdmin = ? where Username = ?',(True,row[qs.ATT_ADMIN[3]],))
       		
       		else: return False

       		return True
       		# conn.commit()
        except sqlite3.OperationalError:
        	print 'Error!'
        	conn.rollback() 

        conn.rollback()
        return False


def insert_log(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_LOG[0]],row[qs.ATT_LOG[1]]))
        conn.commit()
    except sqlite3.IntegrityError:
        print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()

def insert_maintains(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_MAINTAINS[0]],row[qs.ATT_MAINTAINS[1]],row[qs.ATT_MAINTAINS[2]]))
        conn.commit()
    except sqlite3.IntegrityError:
        print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()

def insert_registery(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_REGISTRY[0]],row[qs.ATT_REGISTRY[1]],row[qs.ATT_REGISTRY[2]],row[qs.ATT_REGISTRY[3]]))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()
        return False

def insert_ownership(sql,row):
    global conn
    try:
        conn.execute(sql,(row[qs.ATT_OWNERSHIP[0]],row[qs.ATT_OWNERSHIP[1]]))
        conn.commit()
    except sqlite3.IntegrityError:
        print "ERROR!!! -> already exist value - ERROR CODE - 501"
        conn.rollback()

def retrive_id(id,table,att,val):
    global conn

    qr = "select " + id + " from " + table + " where " + att +" = " + val + ";"
    # qr = "select Vid from Vehicle where Lplate = 'ka 30 abcd' ;"
    cur = conn.execute(qr)

    di = dict(cur.fetchone())
    #conn.close()
    return di

def retrive_values(id,table):

    global conn
    qr = "select " + id + " from "+ table+ ";"
    cur = conn.execute(qr)
    li = cur.fetchall()

    return li

def execute_query(sql,fetchStyle = 1):
    if fetchStyle == 1:
        cur = conn.execute(sql)
        try:
            di = dict(cur.fetchone())
        except TypeError:
            return None
        #conn.close()
        return di

def delete_reg(lplate):

    global conn
    try:
        lplate = "'" + lplate + "'"
        vid = retrive_id("Vid","Vehicle","Lplate",lplate)
        vid = vid['Vid']
        vid = str(vid)
        oid = retrive_id("Oid","Ownership","Vid",vid)
        oid = oid['Oid']
        oid = int(oid)
        vid = int(vid)

         

        curr = conn.execute('update Vehicle set IsReg = ? where Vid = ?',(False,vid))
        curr = conn.execute('delete  from Registry where Vid = ?',(vid,))

        # curr = conn.execute('delete  from Registry')
        # print curr.fetchone()

        # curr = conn.execute('delete  from Ownership where Vid = ?',(vid,))

        # curr = conn.execute('delete  from Vehicle where Vid = ?',(vid,))

        cur = conn.execute('select count(Vid) from Ownership where Oid = ?',(oid,))
        noOfPlate = cur.fetchone()
        # print "*" * 10, noOfPlate
        oid = int(oid)
        if noOfPlate == 1:
            # conn.execute('delete  from Owner where Oid = ?',oid)
            pass
        conn.commit()
        return True
    except sqlite3.OperationalError:
        # print sqlite3
        conn.rollback()
        return False
    except TypeError:
        conn.rollback()
        return False

def delete_admin(username):
	try:
		global conn
		curr = conn.execute('select * from Admin where Username = ?',(username,))
		curr = curr.fetchone()

		if not curr['IsAdmin']:
			return False
		conn.execute('update Admin set IsAdmin = ? where Username = ?',(False,username,))
		conn.commit()
		return True
	except (sqlite3.OperationalError,TypeError):
		conn.rollback()
		return False

def emergency_bypass(lplate,time,admin):

    global conn
    try:
        try:
            conn.execute('insert into Vehicle (Lplate) values (?)',(lplate,))
        except sqlite3.IntegrityError:
            # conn.execute('update Vehicle set IsReg = ? where Lplate =  ?',(False,Lplate))
            print 'already exsist error!!'

        curr = conn.execute('select Vid from Vehicle where lplate = ?',(lplate,))
        curr = curr.fetchone()
        vid = curr['Vid']


        curr = conn.execute('select Aid from Admin where Username = ?',(admin,))
        curr = curr.fetchone()
        aid = curr['Aid']

        conn.execute('insert into Log (Vid,Time,IsBypassed) values(?,?,?)',(vid,time,True))

        curr = conn.execute('select Lid from Log where Time = ?',(time,))
        curr = curr.fetchone()
        lid = curr['Lid']
        conn.execute('insert into Maintains(Aid,Lid) values(?,?)',(aid,lid))

        conn.commit()
        return True
    except sqlite3.OperationalError as e:
        print str(e)
        return False

def is_registered_plate(lplate):
	global conn
	curr = conn.execute('select v.Vid from Vehicle v,Registry r where v.Vid = r.Vid and v.Lplate = ?',(lplate,))
	curr = curr.fetchone()
	try:
		vid = curr['Vid']
		return True
	except TypeError:
		return False

def is_valid_pin(pin):
	global conn
	curr = conn.execute('select Pin from Registry where Pin = (?)',(pin,))
	curr = curr.fetchone()
	try:
		pin = curr['Pin']
		return True
	except TypeError:
		return False

def add_gate_pass(time,admin,lplate = None,pin = None):
	global conn
	vid = None
	if not lplate is None:
		try:
			curr = conn.execute('select Vid from Vehicle where Lplate = ?',(lplate,))
			curr = curr.fetchone()
			vid = curr['Vid']
		except TypeError as e:
			pass
	elif not pin is None:
		try:
			curr = conn.execute('select Vid from Registry where PIN = ?',(pin,))
			curr = curr.fetchone()
			vid = curr['Vid']
		except TypeError as e:
			pass
	conn.execute('insert into Log(Vid,Time) values(?,?)',(vid,time))

	curr = conn.execute('select Aid from Admin where Username = ?',(admin,))
	curr = curr.fetchone()
	aid = curr['Aid']

	curr = conn.execute('select Lid from Log where Time = ?',(time,))
	curr = curr.fetchone()
	lid = curr['Lid']
	conn.execute('insert into Maintains(Aid,Lid) values(?,?)',(aid,lid))

	conn.commit()

	# if vid is None:
	# 	return False
	# else: return True

def get_registered_vehicles():
    global conn
    conn.row_factory = None
    curr = conn.execute('select v.Lplate,o.Name,a.Username,r.Date from Owner o,Vehicle v,Admin a,Registry r,Ownership os where o.Oid = os.Oid and v.Vid = os.Vid and r.Aid = a.Aid and r.Vid = os.Vid and v.IsReg = ?',(True,))
    records = curr.fetchall()
    # for record in records:
    #     for field in record:
    #         print field,'\t'
    #     print '\n'
    conn.row_factory = sqlite3.Row
    return records

def get_bypassed_vehicles():
    global conn
    conn.row_factory = None
    curr = conn.execute('select v.Lplate,a.Username,l.time from Vehicle v,Admin a,Log l,Maintains m where v.Vid = l.Vid and l.Lid = m.Lid and a.Aid = m.Aid and l.IsBypassed = ?',(True,))
    records = curr.fetchall()
    # for record in records:
    #     for field in records:
    #         print field,'\t'
    #     print '\n'
    conn.row_factory = sqlite3.Row
    return records

def get_parked_vehicles():
    global conn
    conn.row_factory = None
    curr = conn.execute('select v.Lplate,a.Username,l.time from Vehicle v,Admin a,Log l,Maintains m where v.Vid = l.Vid and l.Lid = m.Lid and a.Aid = m.Aid and l.IsIn = ?',(True,))
    records = curr.fetchall()
    for record in records:
        for field in records:
            print field,'\t'
        print '\n'
    conn.row_factory = sqlite3.Row
    return records

##
ATT_OWNER = ['Name','Mob','Email']
ATT_VEHICLE = ['Lplate']
ATT_OWNERSHIP = ['Oid','Vid']
ATT_ADMIN = ['Name', 'Mob','Email','Username','Password','IsAdmin']
ATT_LOG = ['Vid','Time','IsBypassed','IsIn']
ATT_MAINTAINS = ['Aid','Lid',]
ATT_REGISTRY = ['Aid','Vid','Date','PIN']
#3
def disp_all_rows():
    global conn
    curr = conn.execute('select * from Owner')
    Owner = curr.fetchall()
    return Owner

def disp_all():
	
	# cur = conn.execute("Select * from Owner")
	# print "owner"
	# print "=========="
	# for i in cur:
	# 	print i

	cur = conn.execute("Select * from Vehicle")
	print "Vehicle"
	print "=========="
	for i in cur:
		print i

	# 	cur = conn.execute("Select * from Ownership")
	# 	print "ownership"
	# 	print "=========="
	# 	for i in cur:
	# 		print i

	cur = conn.execute("Select * from Admin")
	print "Admin"
	print "=========="
	for i in cur:
		print i

	cur = conn.execute("Select * from Log")
	print "Log"
	print "=========="
	for i in cur:
		print i

	cur = conn.execute("Select * from Maintains")
	print "Maintains"
	print "=========="
	for i in cur:
		print i

    # cur = conn.execute("Select * from Registry")
    # print "Registry"
    # print "=========="
    # for i in cur:
    # 	print i




#main

if __name__ == "__main__":

    load_database()
    create_tables()
    global conn
    ##########################
    # name = 'bhav123'
    # mob = 45451231555122
    # email = "hjchjkcvbnjkdsvb2222"
    # owner_att = ['Name','Mob','Email']
    # values = [name,mob,email]

    # row = dict(zip(owner_att,values))
    # insert_owner(qs.it_owner,row)
    # insert_owner(qs.it_owner,row)

    # ##############################
    # lpalte = "ka 19 abcd"
    # lpalte = "ka 20 abcd"
    # vehicle_att = ['Lplate']
    # vehicle_val = [lpalte]
    # row = dict(zip(vehicle_att,vehicle_val))
    # insert_vehicle(qs.it_vehicle,row)
    # insert_vehicle(qs.it_vehicle,row)

    # #####################################
    # name = 'bhdsdav'
    # mob = 12343669
    # email = "EMAIrtL.COM"
    # username = "UqqR123"
    # password = "PA123"
    #
    # admin_att = ['Name', 'Mob','Email','Username','Password']
    # admin_val = [name, mob,email,username,password]
    # row = dict(zip(admin_att,admin_val))
    # insert_admin(qs.it_admin,row)
    #
    # name = 'bhdfddav'
    # mob = 12348
    # email = "EMAIL11.COM"
    # username = "USER123"
    # password = "PAaa12343"
    #
    # admin_att = ['Name', 'Mob','Email','Username','Password']
    # admin_val = [name, mob,email,username,password]
    # row = dict(zip(admin_att,admin_val))
    # insert_admin(qs.it_admin,row)
    #
    # name = 'bh12wav'
    # mob = 19999
    # email = "EMAIL2.COM"
    # username = "US123"
    # password = "PASSsdfg23"
    #
    # admin_att = ['Name', 'Mob','Email','Username','Password']
    # admin_val = [name, mob,email,username,password]
    # row = dict(zip(admin_att,admin_val))
    #
    # insert_admin(qs.it_admin,row)


    # #########################################
    # time = "2005-03-11-09.54.18.296000"
    # is_bypass = False;
    # # is_bypass = True;
    # log_val = [time,is_bypass]
    # row = dict(zip(qs.ATT_LOG,log_val))
    # insert_log(qs.it_log,row)
    # insert_log(qs.it_log,row)
    # #######################################

    # aid = 1
    # lid = 1
    # vid = 1

    # maintains_val = [aid,lid,vid]
    # row = dict(zip(qs.ATT_MAINTAINS,maintains_val))
    # insert_maintains(qs.it_maintains,row)
    # insert_maintains(qs.it_maintains,row)


    # #######################################


    # aid = 1
    # vid = 1
    # date = 'jan 1 2009 13:22:15'
    # pin = 123456

    # registery_val = [aid,vid,date,pin]


    # row = dict(zip(qs.ATT_REGISTRY,registery_val))
    # insert_registery(qs.it_registery,row)
    # insert_registery(qs.it_registery,row)


    # #######################################

    # #######################################


    # oid = 1
    # vid = 15


    # ownership_val = [oid,vid]
    # row = dict(zip(qs.ATT_OWNERSHIP,ownership_val))
    # insert_ownership(qs.it_ownership,row)
    # insert_ownership(qs.it_ownership,row)



    #######################################
    import util
    import controller
    # lplate = 'ka 29 1024'
    time = util.get_current_date_time()
    admin = controller.get_current_admin()

    # emergency_bypass(lplate,time,'sms123')
    # disp_all()
    # check = is_registered_plate('ka 19 1024')
    # if not check:
    # 	print 'not the registered one!'
    # else:
    # 	print 'Yes regis'
    # check = is_valid_pin(490445)
    # if not check:
    # 	print 'not the valid pin'
    # else:
    # 	print 'Yes valid'
    # vid = 6
    # lplate = 'ka 19 1024'
    # # conn.execute('insert into Log (Vid,Time,IsBypassed) values(?,?,?)',(vid,time,True))
    # # conn.execute('delete * from ')
    # curr = conn.execute('select Vid from Vehicle where Lplate = ?',(lplate,))
    # curr = curr.fetchone()

    # print curr['Vid']
    # pin = 490445
    # # add_gate_pass(time,admin,pin = pin)
    # curr = conn.execute('select Vid from Registry where PIN = (?)',(pin,))
    # vid = curr.fetchone()
    # # vid = curr['Vid']
    # print "vid => ",vid
    # # disp_all()
    # get_registered_vehicles()
    # get_bypassed_vehicles()
    get_parked_vehicles()



    
