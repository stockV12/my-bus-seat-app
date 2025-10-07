import mysql.connector as mc  #  PYTHON VERSION 3.12.3
from tkinter import *
from tkinter import messagebox
from datetime import *
server=mc.connect(host="localhost",user="root",passwd="PASSWD",database="redbus")
cursor= server.cursor(buffered= True)
cursor.execute("create table if not exists bus (Id int primary key,name varchar(50), desti varchar(100), date date)")
server.commit()   #connecting MySQl and python
p=0


root=Tk()
'''bi=PhotoImage(file="C:\\0909.png")
label=Label(root,image=bi)
label.place(x=0,y=0)'''

root.title("Vintage Voyages")    #Elements of the window 
root.geometry("600x400")



l1=Label(root,text="Your Name",font=('times new roman',18),bg="#EBD4C9")
l2=Label(root,text="Date(YYYY-MM-DD)",font=('times new roman',18),bg="#EBD4C9")
l3=Label(root,text="Destination",font=('times new roman',18),bg="#EBD4C9")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1=Entry(root,width=50,bg="#E6D7DE")     #input box
e2=Entry(root,bg="#E6D7DE")
e3=Entry(root,width=25,bg="#E6D7DE")
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

l=[]
def det():                             #collecting data from user 
    a=e1.get()
    b=e2.get()
    c=e3.get()
    x=0
    s=0
    for i in b:
        s=s+1
        if s==5 or s==8:
            try:
                p=int(i)
                x=1

            except:
                x=0
            
        else:
            try:
                p=int(i)

            except:
                x=1

    stat = None
    try:
        indate= datetime.strptime(b,"%Y-%m-%d").date()
        stat= validate(indate)
    finally:
        pass
    
    if (stat==1):
        messagebox.showerror("error",f"Past date can't be entered!")
    elif(stat==2):
        messagebox.showerror("error",f"Date cant be more than 6 days present")
    

    if (x==1):
        messagebox.showerror("error",f"error accured")

    elif a=="" or b=="" or c=="":
        messagebox.showerror("error",f"error accured 101")

    elif(x!=1 and stat!=1 and stat!=2 ):
        query=('select * from bus')
        cursor.execute(query)
        pp=cursor.fetchall()
        LL=list(pp)
        #print(type(LL[0]))
        d=[]
        U=[]
        M=len(pp)
        for o in pp:
            U.append(o[0])            #assingning Id/seat number
        UL=len(U)
        if UL==30:
            messagebox.showinfo("Vintage Voyages",f"We're sorry,tickets for this trip are sold out.")
        else:
            if(LL==d):
                Id=M+1
            else:
                for j in range(1,31):
                    if j in U:
                        continue
                    else:
                        Id=j
                        break
                
        
            l.append({"name":a,"date":b,"des":c,"Id":Id})
            messagebox.showinfo("Vintage Voyages",f"your Seat.no is {Id}")
            messagebox.showinfo("Vintage Voyages",f"Have a safe and pleasent journey!")
            for k in l:
                aa,bb,cc,dd=k["name"],k["Id"],k["des"],k["date"]
                query="insert into bus(name , Id , desti , date ) values('%s',%s,'%s','%s')"%(aa,bb,cc,dd,)
                cursor.execute(query)
                server.commit()
            

def showi():                                      #function to access your info
    query="select * from bus"
    cursor.execute(query)
    pp=cursor.fetchall()
    oo=cursor.rowcount
    server.commit()
    l=[]
    for i in pp:
        d={}
        d["Id"]=i[0]
        d["name"]=i[1]
        d["des"]=i[2]
        d["date"]=i[3]
        l.append(d)
    d=e4.get()
 
    op=0
    if l==[]:
        messagebox.showerror("error",f"error accured 202")
        
    if d=="":
        messagebox.showerror("error",f"error accured 101")
    else:
        for i in l:
            zz=i["Id"]
            if(zz==int(d)):
                op=0
                break
            else:
                op=1
                
                
        if(op==0):
            for i in l:
                
                if (i["Id"]==int(d)):
                    messagebox.showinfo("Vintage Voyages",f"{i['name']} your destination and date are {i['des']} , {i['date']}")
                    
        elif(op==1):
            messagebox.showerror("error",f"error accured 303")


def dl():                              #function for cancellation of ticket
    query="select * from bus"    
    cursor.execute(query)
    pp=cursor.fetchall()
    l=[]
    op=0
    for i in pp:
        d={}
        d["Id"]=i[0]
        d["name"]=i[1]
        d["des"]=i[2]
        d["date"]=i[3]
        l.append(d)
    d=e4.get()
    s=str(d)
    if l==[]:
        messagebox.showerror("error",f"error accured 202")
        
    if d=="":
        messagebox.showerror("error",f"error accured 101")
    else:
        for i in l:
            zz=i["Id"]
            if(zz==int(d)):
                op=0
                break
            else:
                op=1
        if(op==0):
            #==
            a=messagebox.askyesno("Vintage Voyages",f"Do you want to cancle your ticket!")
            if a==True:
                for i in l:
                    if(i["Id"]==int(d)):
                        B=int(d)
                        messagebox.showinfo("Vintage Voyages",f"{i['name']} your destination is {i['des']} deleted")
                        cursor.execute('Delete from bus where Id=%s'%(B,))
                        server.commit()

            else:
                messagebox.showinfo("Vintage Voyages",f"Ticket cancellation has been canceled. Enjoy your upcoming trip!")

            
        elif(op==1):
           messagebox.showerror("error",f"error accured 303")




b1=Button(root,text="submit details",command=det)
b2=Button(root,text="view info",command=showi)
b3=Button(root,text="delete info",command=dl)
l4=Label(root,text="seat no",font=('times new roman',18),bg="#EBD4C9")
b1.grid(row=3,column=1)
l4.grid(row=5,column=0)
e4=Entry(root,bg="#E6D7DE")
e4.grid(row=5,column=1)
b2.grid(row=6,column=1)
b3.grid(row=7,column=1)





def validate(indate):
    today= datetime.now().date()
    mdate= today + timedelta(6)

    if (indate<today):
        return 1
    elif(indate >mdate):
        return 2
    else:
        0



    








            





        
        

            
            

                
            
        

