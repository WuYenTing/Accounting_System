#!/usr/bin/env python3
#colorama for print color
from colorama import Fore,Back,Style
import datetime
import sys

ll='{0: ^28}'
l='{0: ^20s}'
s='{0: ^10}'
n='{0: ^4}'

income={'salary','dividend'}
eat=['breakfast','lunch','dinner']
transport=['taxi','bus','train','Ubike','gas']

et='{0: ^70s}'
D='{0: ^13s}'
Am='{0: ^8s}'
nof='{0: ^8s}'
Av='{0: ^9s}'
ls='{0: ^19s}' 

def chart(list): #print the chart and detail information
    print(et.format('┏━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓')) #draw the chart
    print(et.format('┃ Description ┃ Amount ┃ number ┃ Average ┃       Notes       ┃'))  
    i=0
    for i in range(1,3):
        print(et.format('┣━━━━━━━━━━━━━╋━━━━━━━━╋━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫'))       
        print(et.format('┃'+D.format(list[i][0])+'┃'+Am.format(list[i][1])+'┃'+nof.format(list[i][2])+'┃'+Av.format(list[i][3])+'┃'+ls.format(' ')+'┃'))
    print(et.format('┗━━━━━━━━━━━━━┻━━━━━━━━┻━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛')+'\n') 
    print(et.format('income / expense\n'))
    print('{0: ^11s}'.format('in/out'),end='')
    printpercent(abs(int(list[1][1])),abs(int(list[2][1]))+abs(int(list[1][1]))) #myfuntion to draw the percent bar of in/out money ratio
    print(et.format('each expense / total expense\n'))
    for i in range(3,6): #draw detail percent bar of expense
        print('{0: ^11s}'.format(list[i][0]),end='')
        printpercent(abs(int(list[i][1])),abs(int(list[2][1])))
    if(list[1][1]>=list[2][1]): #if income>expense print in green   
        print(Fore.GREEN+et.format('Balance: %d\n') %int(list[0]))
        print(Fore.LIGHTGREEN_EX+et.format('Great! You earned more than you spent.')+Fore.RESET)
    else:
        print(Fore.RED+et.format('Balance: %d\n') %int(list[0]))
        print(Fore.LIGHTRED_EX+et.format('Becareful! You spent more than you earned.')+Fore.RESET)
    print('\n'+Fore.LIGHTWHITE_EX+et.format(str(datetime.date.today()))+'\n'+Fore.RESET)  
            
#[str(item),str(total),str(number),str(average)]
##[all,incomelist,expenselist,transportlist,eatlist,otherslist]

def printpercent (part,total): #draw the percent bar
    #percent>100% 
    if(int(part)>int(total)): #detect error
        print(Fore.RED+'ERROR')
    else:
        if(int(total)==0):
            percent=0
        else:      
            percent=int(part)/int(total)
        #length 50    
        colored=percent*50        
        for i in range(1,51):
            if(i<=colored):
                print(Fore.RED+'█',end='')
            else:
                print(Fore.BLACK+'█',end='')
        print('▏',end='')
        #show the %        
        print(Fore.RESET+Back.RESET+' {}%\n'.format(round(percent*100,2)))    

def require_struct(original_list): #this is for wk5 required
    modified_list=[]
    for n in original_list:     
        modified_list.append(tuple(n.split()))
    return modified_list

def pack(item,total,number,average): #pack all relate informations to a list
    l=[str(item),str(total),str(number),str(average)]
    return l

def state(og,list): #update every while loop
    total_income=0
    nof_income=0
    avge_income=0

    eat_expense=0
    nof_eat=0
    avge_eat=0

    transport_expense=0
    nof_transport=0
    avge_transport=0

    others_expense=0
    nof_others=0
    avge_others=0

    total_expense=0
    nof_expense=0
    avge_expense=0

    l=[]
    all=0
    try: #if nothing in the data_list all value are zero
        for n in list:
            all=all+int(n[1])
            if(n[0] in income):
                total_income=total_income+int(n[1])
                nof_income=nof_income+1
                avge_income=round((total_income/nof_income),2)  
            else:     
                total_expense=total_expense+int(n[1])
                nof_expense=nof_expense+1
                avge_expense=round((total_expense/nof_expense),2)
                if(n[0] in transport):
                    transport_expense=transport_expense+int(n[1])
                    nof_transport=nof_transport+1
                    avge_transport=round((transport_expense/nof_transport),2)
                elif(n[0] in eat):
                    eat_expense=eat_expense+int(n[1])
                    nof_eat=nof_eat+1
                    avge_eat=round((eat_expense/nof_eat),2)   
                else:
                    others_expense=others_expense+int(n[1])
                    nof_others=nof_others+1
                    avge_others=round((others_expense/nof_others),2)
    except:    
        pass                
    all=all+int(og)  #pack lists to a list (2D store)   
    incomelist=pack('income',total_income,nof_income,avge_income)
    expenselist=pack('expense',total_expense,nof_expense,avge_expense)
    transportlist=pack('transport',transport_expense,nof_transport,avge_transport)
    eatlist=pack('eat',eat_expense,nof_eat,avge_eat)
    otherslist=pack('others',others_expense,nof_others,avge_others)             #┏[str(item),str(total),str(number),str(average)]
    l=[all,incomelist,expenselist,transportlist,eatlist,otherslist] ##[all,┣incomelist┫,expenselist,transportlist,eatlist,otherslist]
    return l

def total(og,list): #sum all items 
    try:
        all=0
        for n in list:
            all=all+int(n[1])
        return int(og)+all
    except:
        return 0    

def add(list): #add new item to data_list  
    while True:
        try:
            data=input()
            data.split()[1] 
            int(data.split()[1])  
            list.append(tuple(data.split()))            
            break 
        except ValueError: #input not integer
            sys.stderr.write('wrong value! please enter an integer after description!\n') 
        except: #input wrong format
            #int(data.split()[1])
            sys.stderr.write('wrong format! please enter (description money)\n')  

def view(list,sum): #check current state
    print('\n'+et.format(n.format('number')+l.format('Description')+s.format('money'))+'\n')    
    for i in range(1,len(list)+1):
        try:    
            print(et.format(n.format(str(i))+l.format(str(list[i-1][0]))+s.format(str(list[i-1][1]))))                
        except:
            pass
    if(sum>0):      
        print('\n'+Fore.GREEN+et.format(n.format('')+l.format('sum '+str(sum)+s.format('')))+'\n'+Fore.RESET)   
    else:
        print('\n'+Fore.RED+et.format(n.format('')+l.format('sum '+str(sum)+s.format('')))+'\n'+Fore.RESET)     

def delet(list): #delet the item form list
    find=0          
    item=input('item: ')
    for i in range(1,len(list)+1): #list the items you search for
        if list[i-1][0]==item:
            find=1
            print(n.format(str(i))+l.format(str(list[i-1][0]))+s.format(str(list[i-1][1])))  
    if(find==1): 
        i=int(input('which '+item+' do you want to delete? ')) #select the item from the list and delet it
        del list[i-1] 
    else: #item is not in the list
        print(item+' is not in record.')    

def file(list): #file mode for input a file    
    try:
        str=input('please enter the filename: ')
        f=open(str)
        for n in f:
            list.append(tuple((n.split()))) #add it to the data_list               
    except FileNotFoundError:
        sys.stderr.write('Invalid file. Try again.\n')
            
def record(list,ogmoney): #store the ogmoney and other information 
    f=open('record.txt','w')
    f.write(str(ogmoney)+'\n') #ogmoney store in first line 
    nlist=[]
    for n in list: #other information
        try:
            #f.write(str(n[0])+' '+str(n[1])+'\n')
            new=str(n[0])+' '+str(n[1]+'\n')
            nlist.append(new)
            #print(new)
        except:
            pass
    f.writelines(nlist)    
    f.close()

def filelist(list): #separate the ogmoney and other information
    new=[]   
    for n in list:
        new.append(tuple(n.split()))
    return new  

def intialize(): #start
    try: #restart the program
        f=open('record.txt','r')
        print(Fore.LIGHTMAGENTA_EX+"welcome back!!"+Fore.RESET)
        ogmoney=int(f.readline())        
        data_list=f.readlines()#input record.txt to ogmoney, list and continue the pymoney         
        data_list=filelist(data_list)
    except: #first time use 
        print('Add an expense or income record with description and amount')
        while True:
            try:
                ogmoney=int(input('How much money do you have? '))                
                break
            except ValueError: #input not integer
                print('Invalid value for money. Please enter an integer.')
        input_data=input('please enter wk5 require format\n')
        input_data_split=input_data.split(',')
        data_list=require_struct(input_data_split) #wk5 required
        print(data_list)
    return ogmoney,list(data_list)         

#program start from here


ogmoney,data_list=intialize() #wk8 required

while True:    
    operation=input('What do you want to do (add / view / delete / exit / file / chart)? ')
    sum=total(ogmoney,data_list)
    data_state=state(ogmoney,data_list)
    if(operation=='add'):
        add(data_list)  #wk6,7 required
    elif(operation=='view'):
        view(data_list,sum) #wk6 required    
    elif(operation=='delete'):
        delet(data_list) #wk6,7 required
    elif(operation=='file'):
        file(data_list) #add
    elif(operation=='chart'):
        chart(data_state) #add   
    elif(operation=='exit'):
        record(data_list,ogmoney) #wk6 required
        #print(state(ogmoney,data_list))
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n') #wk8 required        
    



#┏ ━ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋    
