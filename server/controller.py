import model
import querystring as qs
import util
import ast
# import recognise as recog
import recognisedummy as recog
# import hardware.hardware as hw
import hardware.hardwaredummy as hw
import alwaysSense as aw

# data = {"name" : ,"param" : ()}



def init_controller():
    model.load_database()
    model.create_tables()

def add_admin(values):
    # init_controller()
    with open('meta.txt') as f:
    	di = f.read()
    	di = ast.literal_eval(di)
    	if di['super_password'] != values[-1]:
    		data = {"name" : "view.display_not_super_admin",
                    "param" : ()}
    		return data

    row = dict(zip(qs.ATT_ADMIN,values))

    sucess = model.insert_admin(qs.it_admin,row)
    if not sucess:
        
        data = {"name" : "view.display_already_admin",
                "param" : ()}
        return data
    else: 
        data = data = {"name" : "view.display_sucessful_admin_created",
                    "param" : ()}
        return data

def delete_admin(username,suadmin):
    with open('meta.txt') as f:
        di = f.read()
        di = ast.literal_eval(di)
    # if di['super_admin'] == suadmin['admin'] and di['super_password'] == suadmin['password']:
    if di['super_password'] == suadmin:
        sucess = model.delete_admin(username)
        if sucess:
            if username == get_current_admin():
                logout()
            data = {"name" : "view.display_sucessful_delete_admin","param" : ()}
            return data
        else:
            data = {"name" : "view.display_improper_username","param" : ()}
            return data
    else:
        print 'ok'
        data = {"name" : "view.display_not_super_admin","param" : ()}
        return data


def get_current_admin():
    with open('meta.txt','r') as f:
        di = f.read()
        di = ast.literal_eval(di)
        return di['login']

def is_admin(username,password):

    username = '"' + username + '"'
    result = model.execute_query('select Username,Password,IsAdmin from Admin where Username = {}'.format(username,))
    if result is None:
        return False
    result['IsAdmin'] = bool(result['IsAdmin'])

    if result is None:
        return False
    elif result['Password'] == password and result['IsAdmin'] == True:
        return True
    else:
        return False

def make_reg_true(): 
    print 'cont done'
    with open('meta.txt','r+') as f:
        di = f.read()
        di = ast.literal_eval(di)
        di['isReg'] = True
        di = str(di)
        f.seek(0)
        f.truncate()
        f.seek(0)
        f.write(di)
    return True

def make_reg_false(): 
    print 'cont done'
    with open('meta.txt','r+') as f:
        di = f.read()
        di = ast.literal_eval(di)
        di['isReg'] = False
        di = str(di)
        f.seek(0)
        f.truncate()
        f.seek(0)
        f.write(di)
    return True

# 

def register_vehicle(owner,vehicle):

  
  thereAdmin = get_current_admin()
  if thereAdmin == '':
    
    data = {"name" : "view.display_not_logged" ,"param" : ()}
    # qs.regFlag = False
    return data
  # pack the attributes
  rowOwner = dict(zip(qs.ATT_OWNER,owner))
  rowVehicle = dict(zip(qs.ATT_VEHICLE,vehicle))

  # insert into Vehicle and Owner
  # check whether the plate is already registered if so dont add the plate
  notExist = model.insert_vehicle(qs.it_vehicle,rowVehicle) # insert into vehicle
  lplate = vehicle[0]
  # if not notExist:
  #   model.updateAsReg(lplate)
  print lplate
  isReg = model.is_registered_plate(lplate)
  print isReg
  if not isReg:
    ownerExist = model.insert_owner(qs.it_owner,rowOwner)

    #
    oid = model.retrive_id("Oid","Owner",qs.ATT_OWNER[1],str(owner[1]))
    oid = oid['Oid']
    strPlate = "'" + vehicle[0] + "'"
    vid = model.retrive_id("Vid","Vehicle",qs.ATT_VEHICLE[0],strPlate)
    vid = vid['Vid']

    ownership =  [oid,vid]
    rowOwnership = dict(zip(qs.ATT_OWNERSHIP,ownership))
    model.insert_ownership(qs.it_ownership,rowOwnership)
    #Registry table

    date = util.get_current_date()
    currAdmin = get_current_admin()
    currAdmin = "'" + currAdmin + "'"
    aid = model.retrive_id("Aid","Admin",qs.ATT_ADMIN[3],currAdmin)
    aid = aid['Aid']
    pinExist = False
    while not pinExist:
        pin = util.genrate_pin()
        registry = [aid,vid,date,pin]
        rowRegistry = dict(zip(qs.ATT_REGISTRY,registry))
        pinExist = model.insert_registery(qs.it_registery,rowRegistry)
    data = {"name" : "view.display_pin" ,"param" : (pin,)}
    aw.isReg = False
    return data
  
  else:
    data = {"name" : "view.display_registerd_user" ,"param" : ()}
    aw.isReg = False
    return data
  
 


def deregister_vehicle(lplate):
    thereAdmin = get_current_admin()
    if thereAdmin == '':
      data = {"name" : "view.display_not_logged" ,"param" : ()}
      return data
    else:
        sucess = model.delete_reg(lplate)
        # print sucess
        if sucess:
            data = {"name" : "view.display_sucessful_deregister" ,"param" : ()}
            return data
        else:
            data = {"name" : "view.display_unsucessful_deregister" ,"param" : ()}
            return data 
            

def emergency_bypass(lplate):
    admin = get_current_admin()
    if admin == '':
        data = {"name" : "view.display_not_logged" ,"param" : ()}
        return data
    time = util.get_current_time()
    # call gatepass here
    hw.gatepass()
    sucess = model.emergency_bypass(lplate,time,admin)
    if sucess:
        data = {"name" : "view.display_sucessful_bypass" ,"param" : ()}
    else:
        data = {"name" : "view.display_unsucessful_bypass" ,"param" : ()}
    # print data
    return data


# def gate_pass(lplate):
#     sucess =  model.is_registered_plate(lplate)
#     if sucess:
#         data = {"name" : "view.display_sucessful_gatepass" ,"param" : ()}
#         time = util.get_current_date_time()
#         admin = get_current_admin()
#         model.add_gate_pass(time,admin,lplate)
#     else:
#         data = {"name" : "view.display_unsucessful_gatepass" ,"param" : ()}
#     return data

def gate_pass(lplate):
    sucess =  model.is_registered_plate(lplate)
    if sucess:
        # data = {"name" : "view.display_sucessful_gatepass" ,"param" : ()}
        time = util.get_current_time()
        admin = get_current_admin()
        model.add_gate_pass(time,admin,lplate)
        return True
    else:
        # data = {"name" : "view.display_unsucessful_gatepass" ,"param" : ()}
        return False


# def gate_pass_via_pin(pin):
#     valid_pin = pin
#     sucess = model.is_valid_pin(valid_pin)
#     if sucess:
#         data = {"name" : "view.display_sucessful_gatepass","param": ()}
#         time = util.get_current_date_time()
#         admin = get_current_admin()
#         model.add_gate_pass(time,admin,pin = pin)
#     else:
#         data = {"name" : "view.display_unsucessful_gatepass","param" : ()}
#     return data

def gate_pass_via_pin(pin):
    valid_pin = pin
    sucess = model.is_valid_pin(valid_pin)
    if sucess:
        # data = {"name" : "view.display_sucessful_gatepass","param": ()}
        time = util.get_current_date_time()
        admin = get_current_admin()
        model.add_gate_pass(time,admin,pin = pin)
        return True
    else:
        # data = {"name" : "view.display_unsucessful_gatepass","param" : ()}
        return False

def control_gate_pass():
    init_controller()
    lplate = recog.recognise()
    if lplate is None:
        #hw.displayMessage('Sorry could\'nt recognize')
        hw.buzz()
        pin = hw.enterPIN() 
        sucess = gate_pass_via_pin(pin)
        set_progress([0,0,1,0])
        if not sucess:
            count = 2
            while count > 0:
                pin = hw.enterPIN(True)
                sucess = gate_pass_via_pin(pin)
                if sucess:
                    #open boom barrier
                    # hw.openBoomBarrier() 
                    #print 'boom boom'
                    hw.gatepass()
                    gate_pass(lplate)
                    break
                count -= 1
           # hw.buzz()
        else:
            hw.gatepass()
            gate_pass(lplate)     
    else:
        set_progress([0,0,1,1])
        isPlateReg = model.is_registered_plate(lplate)
        print 'no rege'
        print isPlateReg
        if isPlateReg:
            hw.gatepass()
            gate_pass(lplate)
        else:
            hw.buzz()
            pin = hw.enterPIN()
            gate_pass_via_pin(pin)
            sucess = gate_pass(lplate)
            
            if not sucess:
                hw.buzz()
        #hw.displayMessage('Failed to reconize the vehicle!')
    return

    



def login(username,password):
    is_add = is_admin(username,password)
    # print 'isadd',is_add
    if is_add:
        data = {"name" : "view.display_sucessful_login","param" : () }
        with open('meta.txt','r+') as f:
            di = f.read()
            di = ast.literal_eval(di)
            di['login'] = username
            di = str(di)
            f.seek(0)
            f.truncate()
            f.seek(0)
            f.write(di)
    else:
        data = {"name" : "view.display_unsucessful_login","param" : () }
    return data

def logout():

    with open('meta.txt','r+') as f:
            di = f.read()
            di = ast.literal_eval(di)
            di['login'] = ''
            di = str(di)
            f.seek(0)
            f.truncate()
            f.seek(0)
            f.seek(0)
            f.write(di)
    data = {"name" : "view.display_sucessful_logout", "param" : ()}
    return data

def disp_all_rows():
    owners = model.disp_all_rows()
    owners = list(owners)
    data = {"Owner" : {"head" : qs.ATT_OWNER ,"values" : owners},}
    return data

def get_log_data(choice):
    record = []
    if choice == 1:
        try:
            print 'sdfvsdvf'
            records = get_registered_vehicles()
            print type(records)
            data = {'Records' : records}
        except :
            print 'error'

    if choice == 2:
            records =  get_bypassed_vehicles()
            records = list(records)
            data = {'Records' : records}

    if choice == 3:
            records =  get_parked_vehicles()
            records = list(records)
            data = {'Records' : records}

    return data

def get_registered_vehicles():
    records = model.get_registered_vehicles()
    return records

def get_bypassed_vehicles():
    records = model.get_bypassed_vehicles()
    return records
    
def get_parked_vehicles():
    records = model.get_parked_vehicles()
    return records
# recognitation of plate
def recognize_plate():
    plate = recog.recognise()
    print plate
    if plate is None:
        return False
    return plate
#####################

def train(lplate):
    recog.train(lplate)
    return True

def get_progress():
    with open('meta.txt','r+') as f:
            di = f.read()
            di = ast.literal_eval(di)
            progress = di['progress']
            return progress

def set_progress(values):

    with open('meta.txt','r+') as f:
            di = f.read()
            di = ast.literal_eval(di)
            progress = di['progress']
            for i in range(len(values)):
                progress[i] += values[i]
            di['progress'] = progress
            di = str(di)
            f.seek(0)
            f.truncate()
            f.seek(0)
            f.seek(0)
            f.write(di)
    return True



if __name__ == "__main__":
    init_controller()
    # name = 'bsdfdgdgsf'
    # mob = 42455562
    # email = "sasdfsdfsfs212"

    # ############################
    # name = 'bhdfddav'
    # mob = 12348
    # email = "EMAIL11.COM"
    # username = "USER123"
    # password = "PAaa12343"

    # admin_att = ['Name', 'Mob','Email','Username','Password']
    # admin_val = [name, mob,email,username,password]
    # row = dict(zip(admin_att,admin_val))
    # model.insert_admin(qs.it_admin,row)
    # ########################

    # lpalte = "ka 30 abcd"
    # str(lpalte)
    # owner = [name,mob,email]
    # vehicle = [lpalte]
    # register_vehicle(owner,vehicle)
    # isadd = is_admin('sms123','sms13')
    # print isadd

    # login('sms123','sms123')
    # logout()

    # records = get_registered_vehicles()
    # records = get_parked_vehicles()
    # # records = get_bypassed_vehicles()
    # print type(records)
    # # print len(records)
    # for rec in records:
    #     for r in rec:
    #         print r,'\t\t'
    #     print '\n'
    # get_log_data(1)
    # recognize_plate()
    # control_gate_pass()
    # make_reg_true()
    # set_progress([1,1,1,1])
    register_vehicle(['mary','32165','shd'],['shuf'])
    register_vehicle(['sad','3213365','shasdadd'],['shasdaduf'])
    register_vehicle(['shrav','2365','sch@gmai;.com'],['sc132'])
    print get_registered_vehicles()

