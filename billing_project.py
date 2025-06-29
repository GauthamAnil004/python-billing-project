import mysql.connector as a
con = a.connect(host = "localhost",
    user = "root",
    password = "heheboi",
    database = "billing_project")
########################################################################################################################################################################
print("{:>60}".format("**********************************************"))
print("{:>60}".format("---->> PRODUCT MANAGEMENT & BILLING <<----"))
print("{:>60}".format("**********************************************"))
print("  ")
########################################################################################################################################################################
import time
def loading_screen(word):
    for i in range(1, 4):
        print(word + "." * i)
        time.sleep(0.4)  # Adjust the sleep duration to control the speed of the loading screen

    print(":) ......")

# Call the function to see the loading screen in action


########################################################################################################################################################################

def date_m():
    import datetime
    x=datetime.datetime.now()
    year=x.strftime("%Y")
    month=x.strftime("%m")
    day=x.strftime("%d")
    hour=x.strftime("%I")
    minute=x.strftime("%M")
    sec=x.strftime("%S")
    date1=str(year)+""+str(month)+""+str(day)+" , "+str(hour)+":"+str(minute)+":"+str(sec)
    return date1

########################################################################################################################################################################
def check_user2():
    global user_a
    sql = 'SELECT * FROM accounts WHERE user_name = %s'
    c = con.cursor(buffered=True)                                                           #for add user purpose
    data = (user_a,)
    c.execute(sql, data)
    r = c.fetchall()
    for i in r:
       if i==user_a:
            return True
       else:
            return False

########################################################################################################################################################################
def add_user():
    import mysql.connector
    from datetime import datetime

    conn = mysql.connector.connect(host="localhost", user="root", passwd="heheboi", database="billing_project")
    cur = conn.cursor()

    uname = input("Enter a username: ").strip()
    passwd = input("Enter a password: ").strip()
    desig = input("Enter designation (admin/staff/guest/customer): ").strip().lower()

    if not uname or not passwd or desig not in ['admin', 'staff', 'guest', 'customer']:
        print("Invalid input. Please try again.")
        return

    cur.execute("SELECT * FROM accounts WHERE user_name = %s", (uname,))
    if cur.fetchone():
        print("Username already exists.")
    else:
        cur.execute("INSERT INTO accounts (user_name, password, date_created, desig) VALUES (%s, %s, %s, %s)",
                    (uname, passwd, datetime.now().strftime("%Y-%m-%d"), desig))
        conn.commit()
        print("Account created successfully!")

    cur.close()
    conn.close()
    input("Press Enter to return to login...")
    login() 
           

########################################################################################################################################################################
def check_pass():
    global pass_l
    sql = 'SELECT * FROM accounts WHERE password = %s'
    c = con.cursor(buffered=True)
    data = (pass_l,)                                                                #for login purpose
    c.execute(sql, data)
    r = c.fetchall()
    for i in r:
        if i==pass_l:
            return True
        else:
            return False


########################################################################################################################################################################

def check_user():
    global user_l
    sql = 'SELECT * FROM accounts WHERE user_name = %s'
    c = con.cursor(buffered=True)
    data = (user_l,)
    c.execute(sql, data)                                                            #for login purpose
    r = c.fetchall()
    for i in r:
        if i ==user_l:
            return True
        else:
            return False
########################################################################################################################################################################
def check_user2(user_del):
    sql = 'SELECT * FROM accounts WHERE user_name = %s'
    c = con.cursor(buffered=True)
    data = (user_del,)
    c.execute(sql, data)                                                            #for delete purpose
    r = c.fetchall()
    for i in r:
        if i[1]==user_del:
            return True
        else:
            return False

########################################################################################################################################################################
def delete_bill2(user_del):
    while True:
        if check_user2(user_del)==True:
            uno_id = uno_fetch_admin(name)
        table_name = f"bills_proj.{uno_id}"
        if chek_bill_table(name):
            sql = "DROP TABLE %s"
            data=(table_name,)
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            c.close()
            word = 'deleting'
            loading_screen(word)
            print(" ")
            print("DELETED BILL NO..", uno_id)
            print(" ")
            cc = input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower() == 'n':
                user_l = get_user_n()
                word = '>'
                loading_screen(word)
                if chek_desig() == "Cashier" or chek_desig() == "Accountant":
                    cash_acc_menu()
                break

            else:
                continue
        else:
            print("BILL NAMED", uno_id, "DOESN'T EXIST! TRY ANOTHER BILL NO.")
            break
    
########################################################################################################################################################################        
def delete_user():
    print(" ")
    while True:
        print(" ")
        user_del=input("Enter an user name to delete: ")
        if check_user2(user_del)==True:
            sql='delete from accounts where user_name=%s'                               #function for User's menu   FOR DELETING USERS
            c=con.cursor()
            data=(user_del,)
            c.execute(sql,data)
            con.commit()
            print(" ")
            print(" ")
            print("deleted!...")
            print(" ")
            qe=int(input("GO back to menu(1) OR Exit(2): "))
            if qe==1:
                word='.'
                loading_screen(word)
                Super_admin_menu()
            elif qe==2:
                word='.'
                loading_screen(word)
                exit()
            break
                
        else:
            print("User name dosen't exist! ")


########################################################################################################################################################################

def search_user():
    print(" ")
    while True:
        print(" ")
        user_name=input("Enter a name to SEARCH: ")
        word='seaching'
        loading_screen(word)

        if check_user()==True:
            print(" ")
            print("The entered user name doesn't EXIST!!")
            
        else:
            sql='select* from accounts where user_name= %s'
            c = con.cursor(buffered=True)                                                           #function for User's menu
            data = (user_name,)
            c.execute(sql, data)
            r = c.fetchall()
            for i in r:
                print(" ")
                print("FOUND A MATCH!!....... ")
                print(" ")
                print("USER_NUMBER: ",i[0])
                print("USER_NAME: ",i[1])
                print("PASSWORD: ********")
                print("DATE JOINED: ",i[3])
                print("DESIGNATION: ",i[4])
                print(" ")
                qw=int(input("GO back to menu(1) OR Exit(2): "))
                if qw==1:
                    user_l= get_user_n()
                    word='>'
                    loading_screen(word)
                    if chek_desig()=="Admin":
                        Admin_menu()
                        break

                    elif chek_desig()=="Super_admin":
                        Super_admin_menu()
                        break

                    else:
                        word='.'
                        loading_screen(word)
                        exit()
                        break
            
########################################################################################################################################################################
def uno_fetch():
    name = get_user_n()
    sql = 'SELECT * FROM accounts WHERE user_name = %s'
    data = (name,)
    c = con.cursor()
    c.execute(sql, data)
    row = c.fetchone()

    if row:
        if row[1] == name:
            uno = row[0]
            return uno
        else:
            print('Username mismatch')
    else:
        print('No such user found')


##########################################################################################################################################################################
def uno_fetch_admin(name):
    sql = 'SELECT * FROM accounts WHERE user_name = %s'
    data = (name,)
    c = con.cursor()
    c.execute(sql, data)
    row = c.fetchone()

    if row:
        if row[1] == name:
            uno = row[0]
            return uno
        else:
            print('Username mismatch')
    else:
        print('No such user found')


            
#########################################################################################################################################################################
def chek_tabledb2(user_l):
    sql='show tables from bills_proj'
    c=con.cursor()
    c.execute(sql,)
    h=c.fetchall()
    table_name = str(uno_fetch())
    for i in h:
        if i[0]==table_name:
            return True
    return False

#########################################################################################################################################################################
def bill_gen(user_l):
    if chek_tabledb2(user_l)==False:
        print(" ")
        print("Generating BILL.........")
        print(" ")
        u_no= uno_fetch()
        table_name=f"bills_proj.{u_no}"
        c=con.cursor()
        sql = f"CREATE TABLE {table_name} (p_id int AUTO_INCREMENT PRIMARY KEY, product VARCHAR(50), price FLOAT, quantity INT, d_o_p DATE)"
        c.execute(sql)
        print("CREATED THE BILL TABLE!!")
    else:
        print("Bill table already exists!")

#########################################################################################################################################################################
def retrive_price(pro):
    table_name= uno_fetch()
    sql=f'select*from bills_proj.{table_name}'
    c=con.cursor()
    c.execute(sql)                                                               # For retriving price from products database and add it to a bill
    rr=c.fetchall()                                                             # Has an error it only retrives price of the first product from the products table.
    for i in rr:
        if i[1]==pro:
            sql=f'select*from bills_proj.{table_name} where product=%s'
            data=(pro,)
            c=con.cursor()
            c.execute(sql,data)
            tt=c.fetchall()
            for i in tt:
                price=i[2]
            return price
        else:
            price=float(input("Enter the PRICE: "))


#########################################################################################################################################################################
def add_to_bill():
    while True:
        print(" ")
        pro=input("product name: ")
        price= float(input("Enter the PRICE: "))
        qty=int(input("enter quantity: "))
        dop=date_m()
        table_n= uno_fetch()
        c=con.cursor()
        data=(pro,price,qty,dop)
        sql=f"INSERT INTO bills_proj.{table_n} (product, price, quantity, d_o_p) VALUES (%s, %s, %s, %s)"
        c.execute(sql,data)
        con.commit()
        word='adding'
        loading_screen(word)
        print(" ")
        print("added...")
        que=input("PRESS ENTER TO CONTINUE ADDING PRODUCTS OR PRESS N TO RETURN: ")
        if que.lower()=='n':
            user_l= get_user_n()
            word='<:'
            loading_screen(word)
            if chek_desig()=="Customer":
                customer_menu()
                break
        else:
            continue
#########################################################################################################################################################################
def addtobill_casacc(name):
    while True:
        print(" ")
        pro=input("product name: ")
        price= float(input("Enter the PRICE: "))
        qty=int(input("enter quantity: "))
        dop=date_m()
        table_n= uno_fetch_admin(name)
        c=con.cursor()
        data=(pro,price,qty,dop)
        sql=f"INSERT INTO bills_proj.{table_n} (product, price, quantity, d_o_p) VALUES (%s, %s, %s, %s)"
        c.execute(sql,data)
        con.commit()
        word='adding'
        loading_screen(word)
        print(" ")
        print("added...")
        cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
        if cc.lower()=='n':
            user_l= get_user_n()
            word='>'
            loading_screen(word)
            if chek_desig()=="Cashier" or "Accountant":
                cash_acc_menu()
            break

        else:
            continue
    
#########################################################################################################################################################################
def view_bill(user_l):
    table_name= uno_fetch()
    sql=f"select p_id,product,price,quantity,d_o_p from bills_proj.{table_name}"
    c=con.cursor()
    c.execute(sql,)
    q=c.fetchall()
    word='$'
    loading_screen(word)
    for i in q:
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("p_id:",i[0], r"  /\/\/\/\/\ PRODUCT:",i[1],r"  /\/\/\/\/\ PRICE:",i[2],r"  /\/\/\/\/\ QUANTITY:",i[3],r"  /\/\/\/\/\  DATE OF PURCHASE:",i[4])
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
#########################################################################################################################################################################
def view_bill2(name):
    table_name= uno_fetch_admin(name)
    sql=f"select p_id,product,price,quantity,d_o_p from bills_proj.{table_name}"
    c=con.cursor()
    c.execute(sql,)
    q=c.fetchall()
    word='$'
    loading_screen(word)
    for i in q:
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("p_id:",i[0], r"  /\/\/\/\/\ PRODUCT:",i[1],r"  /\/\/\/\/\ PRICE:",i[2],r"  /\/\/\/\/\ QUANTITY:",i[3],r"  /\/\/\/\/\  DATE OF PURCHASE:",i[4])
        print("--------------------------------------------------------------------------------------------------------------------------------------------")

        
#########################################################################################################################################################################
def add_to_stock():
    while True:
        print(" ")
        pro_n=input("ENTER THE PRODUCT NAME: ")
        price_p=float(input("ENTER THE PRICE OF PRODUCT: "))
        pcp=input("PARENT OR CHILD PRODUCT: ")
        stock=int(input("HOW MANY IN STOCK: "))
        sql='insert into products (product_n,price,pcp,instock) values(%s,%s,%s,%s)'
        data=(pro_n,price_p,pcp,stock)
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        word='adding'
        loading_screen(word)
        print(" ")
        print("Added......")
        print(" ")
        que=input("PRESS ENTER TO CONTINUE ADDING PRODUCTS OR PRESS N TO RETURN: ")
        if que.lower()=='n':
            user_l= get_user_n()
            word='<:'
            loading_screen(word)
            if chek_desig()=="Admin":
                Admin_menu()
                break
            elif chek_desig()=="Super_admin":
                Super_admin_menu()
                break
        else:
            continue
##########################################################################################################################################################################                
def chek_stock():
    while True:
        print(" ")
        pro_n=input("ENTER THE NAME OF PRODUCT TO CHECK: ")
        sql='select*from products where product_n=%s'
        data=(pro_n,)
        c=con.cursor()
        c.execute(sql,data)
        a=c.fetchall()
        for i in a:
            if i[1]==pro_n:
                stock_num=i[4]
                word='Chekin'
                loading_screen(word)
                print(" ")
                print("STOCK OF",pro_n,"=",stock_num)
                print(" ")
                cf=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
                if cf.lower()=='n':
                    user_l= get_user_n()
                    word='>'
                    loading_screen(word)
                    if chek_desig()=="Admin":
                        Admin_menu()
                        break
                    elif chek_desig()=="Super_admin":
                        Super_admin_menu()
                        break
                    else:
                        continue
                    
            else:
                continue
                print("PRODUCT DOSN'T EXIST!! TRY AGAIN")
                break
            
                
##########################################################################################################################################################################
def chek_pcp():
    while True:
        print(" ")
        pro_i=input("ENTER THE NAME OF PRODUCT TO CHECK: ")
        sql='select*from products where product_n=%s'
        data=(pro_i,)
        c=con.cursor()
        c.execute(sql,data)
        b=c.fetchall()
        for i in b:
            if i[1]==pro_i:
                pcp_i=i[3]
                word='checkin'
                loading_screen(word)
                print(" ")
                if pro_i is not None and pcp_i is not None:
                    print(pro_i.upper(), "Is a", pcp_i.upper(), "PRODUCT")
                    
                else:
                    print(pro_i.upper(), "Is not assigned as parent or child product")
                print(" ")

                cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
                if cc.lower()=='n':
                    user_l= get_user_n()
                    word='>'
                    loading_screen(word)
                    if chek_desig()=="Admin":
                        Admin_menu()
                        break
                    elif chek_desig()=="Super_admin":
                        Super_admin_menu()
                    break
                else:
                    continue
                    
            else:
                print("PRODUCT DOSN'T EXIST!! TRY AGAIN")
                break

                
##########################################################################################################################################################################    
def chek_date():
    while True:
        print(" ")
        name=input("NAME OF USER TO SEARCH FOR PRODUCT: ")
        sql='select* from accounts where user_name=%s'
        data=(name,)
        c=con.cursor()
        c.execute(sql,data)
        vv=c.fetchall()
        for i in vv:
            if i[0]!=name:
                print(" ")
                pro_name=input("ENTER THE PRODUCT NAME: ")
                uno_f= uno_fetch_admin(name)
                table_n2=f"bills_proj.{uno_f}"
                sql=f'select*from {table_n2} where product=%s'
                data=(pro_name,)
                c=con.cursor()
                c.execute(sql,data)
                qq=c.fetchall()
                for i in qq:
                    if i[0]!=pro_name:
                        date_op=i[4]
                        word='searching'
                        loading_screen(word)
                        print("")
                        print(pro_name," was purchased on: ",date_op)
                        print("")
                        cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
                        if cc.lower()=='n':
                            user_l= get_user_n()
                            word='>'
                            loading_screen(word)
                            if chek_desig()=="Admin":
                                Admin_menu()
                                break
                            elif chek_desig()=="Super_admin":
                                Super_admin_menu()
                                break
                            else:
                                continue
                    else:
                        print(pro_name," not found in the bill!! TRY ANOTHER PRODUCT")
            else:
                print(name," not found!! TRY ANOTHER USER NAME! ")

##########################################################################################################################################################################
def chek_bill_table(name):
    sql='show tables from bills_proj'
    c=con.cursor()
    c.execute(sql,)
    h=c.fetchall()
    table_name = str(uno_fetch_admin(name))
    for i in h:
        if i[0]==table_name:
            return True
    return False

              
##########################################################################################################################################################################
def update_bill(name):
    while True:
        u_no_f= uno_fetch_admin(name)
        table_name=f"bills_proj.{u_no_f}"
        print(" ")
        wht=int(input("OUT OF THESE ([1]..product,[2]..price,[3]..quantity) select one number to update: "))

        if wht==1:
            pid=int(input("Enter p_id of product: "))
            new_pro=input("ENTER NEW PRODUCT NAME: ")            
            sql=f'UPDATE {table_name} SET product=%s WHERE p_id=%s'
            data=(new_pro,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Cashier" or "Accountant":
                    cash_acc_menu()
                break

            else:
                continue

        elif wht==2:
            pid=int(input("Enter p_id of product: "))
            new_price=float(input("ENTER NEW PRICE OF THE PRODUCT: "))           
            sql=f'UPDATE {table_name} SET price=%s WHERE p_id=%s'
            data=(new_price,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Cashier" or "Accountant":
                    cash_acc_menu()
                break

            else:
                continue
            

            

        elif wht==3:
            pid=int(input("Enter p_id of product: "))
            new_qua=int(input("ENTER NEW QUANTITY OF THE PRODUCT: "))          
            sql=f'UPDATE {table_name} SET product=%s WHERE p_id=%s'
            data=(new_qua,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Cashier" or "Accountant":
                    cash_acc_menu()
                break

            else:
                continue


        else:
            print("wrong choise! TRY AGAIN")

##########################################################################################################################################################################


def update_cus_bill(name):
    while True:
        u_no_id= uno_fetch()
        table_name=f"bills_proj.{u_no_id}"
        print(" ")
        wht=int(input("OUT OF THESE ([1]..product,[2]..price,[3]..quantity) select one number to update: "))

        if wht==1:
            pid=int(input("Enter p_id of product: "))
            new_pro=input("ENTER NEW PRODUCT NAME: ")            
            sql=f'UPDATE {table_name} SET product= %s WHERE p_id=%s'
            data=(new_pro,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Customer":
                    customer_menu()
                break

            else:
                continue

        elif wht==2:
            pid=int(input("Enter p_id of product: "))
            new_price=float(input("ENTER NEW PRICE OF THE PRODUCT: "))            
            sql=f'UPDATE {table_name} SET price=%s WHERE p_id=%s;'
            data=(new_price,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Customer":
                    customer_menu()
                break

            else:
                continue
            

            

        elif wht==3:
            pid=int(input("Enter p_id of product: "))
            new_qua=int(input("ENTER NEW QUANTITY OF THE PRODUCT: "))            
            sql=f'UPDATE {table_name} SET product= %s WHERE p_id=%s;'
            data=(new_qua,pid,)
            c=con.cursor()
            c.execute(sql,data)
            con.commit()

            word='+'
            loading_screen(word)
            print(" ")
            print("UPDATED!! ")
            print(" ")

            cc=input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower()=='n':
                user_l= get_user_n()
                word='>'
                loading_screen(word)
                if chek_desig()=="Customer":
                    customer_menu()
                break

            else:
                continue


        else:
            print("wrong choise! TRY AGAIN")


        
        
##########################################################################################################################################################################                
def delete_bill(name):
    while True:
        uno_id = uno_fetch_admin(name)
        table_name = f"bills_proj.{uno_id}"
        if chek_bill_table(name):
            sql = "DROP TABLE %s"
            data=(table_name,)
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            c.close()
            word = 'deleting'
            loading_screen(word)
            print(" ")
            print("DELETED BILL NO..", uno_id)
            print(" ")
            cc = input("PRESS ENTER TO CONTINUE OR PRESS N TO RETURN: ")
            if cc.lower() == 'n':
                user_l = get_user_n()
                word = '>'
                loading_screen(word)
                if chek_desig() == "Cashier" or chek_desig() == "Accountant":
                    cash_acc_menu()
                break

            else:
                continue
        else:
            print("BILL NAMED", uno_id, "DOESN'T EXIST! TRY ANOTHER BILL NO.")
            break
        
        

 
##########################################################################################################################################################################
def Admin_menu():
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_') 
    print(" ")
    print("PRESS 1:- Search Users")
    print("PRESS 2:- Add products to stock")
    print("PRESS 3:- Check stock of products")
    print("PRESS 4:- Check if a product is PARENT or CHILD product")
    print("PRESS 5:- Check date of purchase")
    print("PRESS 6:- GO TO LOGIN PAGE")
    print("PRESS 7:- To EXIT")
    print(" ")
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_') 
    while True:
        print(" ")
        ch=int(input("ENTER YOUR CHOISE: "))

        if ch==1:
            search_user()

        elif ch==2:
            add_to_stock()

        elif ch==3:
            chek_stock()

        elif ch==4:
            chek_pcp()

        elif ch==5:
            chek_date()

        elif ch==6:
            main_menu()
            
        elif ch==7:
            word='<:'
            loading_screen(word)
            exit()

        else:
            print("Wrong choise! TRY AGAIN")



##########################################################################################################################################################################
def Super_admin_menu():
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_') 
    print(" ")
    print("PRESS 1:- Search Users")
    print("PRESS 2:- Add products to stock")
    print("PRESS 3:- Check stock of products")
    print("PRESS 4:- Check if a product is PARENT or CHILD product")
    print("PRESS 5:- Check date of payment")
    print("PRESS 6:- Check for DEBIT or CREDIT products")
    print("PRESS 7:- Generate Record")
    print("PRESS 8:- DELETE A USER")
    print("PRESS 9:- LOG OUT :(")
    print("PRESS 10:- EXIT")
    print(" ")
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_')    
    while True:
        print(" ")
        ch=int(input("ENTER YOUR CHOISE: "))

        if ch==1:
            search_user()

        elif ch==2:
            add_to_stock()

        elif ch==3:
            chek_stock()

        elif ch==4:
            chek_pcp()

        elif ch==5:
            chek_date()

        elif ch==6:
            print("WORKING ON IT YET")

        elif ch==7:
            print("WORKING ON IT YET")
            

        elif ch==8:
            delete_user()
            

        elif ch==9:
            word='loggin out'
            loading_screen(word)
            print(" ")
            print("Logging Out........")
            main_menu()

        elif ch==10:
            word='<:'
            loading_screen(word)
            exit()
            
            

        else:
            print("Wrong choise! TRY AGAIN")

##########################################################################################################################################################################
def customer_menu():
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_') 
    print(" ")
    print("""Press[1]: Generate bill
Press[2]: Add an item to bill
Press[3]: View bill
Press[4]: Update bill
Press[5]: LOG OUT :(
Press[6]: EXIT""")
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_')  
    while True:
        print(" ")
        ch=int(input("ENTER YOUR CHOISE: "))

        if ch==1:
            user_l= get_user_n()
            bill_gen(user_l)

        elif ch==2:
            add_to_bill()

        elif ch==3:
            user_l= get_user_n()
            view_bill(user_l)

        elif ch==4:
            name= get_user_n()
            update_cus_bill(name)
            
           
        elif ch==5:
            word='loggin out'
            loading_screen(word)
            print(" ")
            print("Logging Out...")
            main_menu()

        elif ch==6:
            word='<:'
            loading_screen(word)
            exit()

        else:
            print("Wrong choise! TRY AGAIN")

##########################################################################################################################################################################
def cash_acc_menu():
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_') 
    print(" ")
    print("""Press[1]: View bill
Press[2]: Add an item to bill
Press[3]: Edit a bill
Press[4]: Remove a bill
Press[5]: LOG OUT :(
Press[6]: EXIT""")
    print(r'_/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\_')  
    while True:
        print(" ")
        ch=int(input("ENTER YOUR CHOISE: "))

        if ch==1:
            name= input("ENTER CUSTOMER NAME TO VIEW BILL: ")
            view_bill2(name)

        elif ch==2:
            name=input("ENTER THE NAME OF CUSTOMER TO ADD ITEMS TO HIS/HER BILL: ")
            addtobill_casacc(name)

        elif ch==3:
            name=input("ENTER THE NAME OF CUSTOMER TO EDIT HIS/HER BILL: ")
            update_bill(name)
           

        elif ch==4:
            name=input("ENTER THE CUSTOMER'S NAME TO DELETE THE BILL: ")
            delete_bill(name)
          
           
        elif ch==5:
            word='loggin out'
            loading_screen(word)
            print(" ")
            print("Logging Out...")
            main_menu()

        elif ch==6:
            word='<:'
            loading_screen(word)
            exit()

        else:
            print("Wrong choise! TRY AGAIN")
    



##########################################################################################################################################################################
def chek_desig():
    global user_l
    global print
    sql='select desig from accounts where user_name=%s'
    c=con.cursor(buffered=True)
    data=(user_l,)
    c.execute(sql,data)
    r=c.fetchall()
    for i in r:
        if i[0].lower()=='super_admin':

            return 'Super_admin'

        elif i[0].lower()=='admin':
            
            return 'Admin'
        elif i[0].lower()=='cashier':
            
            return 'Cashier'

        elif i[0].lower()=='guest':
            
            return 'Guest'

        elif i[0].lower()=='customer':

            return 'Customer'

        elif i[0].lower()=='accountant':

            return 'Accountant'

        else:

            return None
##########################################################################################################################################################################

def use_menu():
    if check_user()==False and check_pass()== False:
       
        print(" ")
        c = input("PRESS ENTER to continue")
        word='>'
        loading_screen(word)

        if chek_desig() == 'Super_admin':
            print(" ")
            print("Welcome Super admin")
            print(" ")
            Super_admin_menu()

        elif chek_desig() == 'Admin':
            print(" ")
            print("Welcome Admin!")
            print(" ")
            Admin_menu()

        elif chek_desig() == 'Cashier':
            print(" ")
            print("Welocome Cashier")
            print(" ")
            cash_acc_menu()

        elif chek_desig() == 'Guest':
            print(" ")
            print("Welcome Guest")
            print("GUESTS DONT HAVE ANY PERMISSIONS. SORRY:) ")

        elif chek_desig() == 'Customer':
            print(" ")
            print("Welcome Customer!!")
            print(" ")
            customer_menu()

        elif chek_desig() == 'Accountant':
            print(" ")
            print("Welcome Accountant")
            print(" ")
            cash_acc_menu()

        else:
            print(" ")
            print("Who are you!?")
    else:
        print("Failed")

##########################################################################################################################################################################
def login():
    global user_l
    global pass_l
    print(" ")
    while True:
        print(" ")
        user_l=input("USER NAME: ")
        pass_l=input("PASSWORD: ")
        check1= check_user()
        check2= check_pass()
        if check1==False and check2==False:
            word='loggin in'
            loading_screen(word)
            print("")
            print("Login successful!!")
            print(" ")
            use_menu()
         
        else:
            print("Invalid user name or password")
###########################################################################################################################################################################
def get_user_n():
    return user_l
            
            
##########################################################################################################################################################################

def main_menu():
    print("")
    print("Welcome....")
    print("  ")
    print("""[Press(1)] to Login
[Press(2)] to create an account  
[Press(3)] to EXIT: """)
    print("  ")
    print("  ")
    while True:
        met=int(input("Your choise: "))
        if met==1:
            word='>'
            loading_screen(word)
            login()
        elif met==2:
            word='>'
            loading_screen(word)
            add_user()
        elif met==3:
            word='<:'
            loading_screen(word)
            exit()
        else:
            print("Invalid choise! TRY AGAIN!")
        break
main_menu()
    
##########################################################################################################################################################################






     
    

        



















     



