#!/usr/bin/env python3

#colorama for print color
from colorama import Fore,Back,Style
import datetime

#create my print % function
def printpercent (part,total):
    #percent>100%
    if(int(part)>int(total)):
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

#create my average function
def average(sum,nof):
    if(int(nof)==0):
        avg=0
    else:
        avg=int(sum)/int(nof)
    return round(avg,1)

#create my printer function
def printstatement(Dlist,Amlist,Avlist,noflist,total_expense):
    #create space for each statement
    et='{0: ^70s}'
    D='{0: ^13s}'
    Am='{0: ^8s}'
    nof='{0: ^8s}'
    Av='{0: ^9s}'
    ls='{0: ^19s}'
    print(et.format('┏━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓'))
    print(et.format('┃ Description ┃ Amount ┃ number ┃ Average ┃       Notes       ┃'))
    print(et.format('┣━━━━━━━━━━━━━╋━━━━━━━━╋━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫'))
    i=0
    for i in range(4):
        #get string from each list and set in middle
        print(et.format('┃'+D.format(Dlist[i])+'┃'+Am.format(Amlist[i])+'┃'+nof.format(noflist[i])+'┃'+Av.format(Avlist[i])+'┃'+ls.format(' ')+'┃'))
        if(i==3):
            print(et.format('┗━━━━━━━━━━━━━┻━━━━━━━━┻━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛')+'\n')
        else:
            print(et.format('┣━━━━━━━━━━━━━╋━━━━━━━━╋━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫'))
    print(et.format('each expense / total expense\n'))
    for i in range(1,4):
        print('{0: ^11s}'.format(Dlist[i]),end='')
        #use my print % function
        printpercent(Amlist[i],total_expense)

nof_total=0

total_income=0
nof_income=0

total_expense=0
nof_expense=0

eat=['breakfast','lunch','dinner']
eat_expense=0
nof_eat=0

transport=['taxi','bus','train','Ubike','gas']
transport_expense=0
nof_transport=0

others_expense=0
nof_others=0

et='{0: ^70s}'
r=0
item=1

#pymooney start from here
print('\nAdd an expense or income record with description and amount')
print('\nInput (now) for check the state ,(done) for finish the input')
#input pymoneymode
while True:
    pymoneymode=input('\nchoose the pymoney mode (f:input by file / u:input by user): ')
    pymoneymodelist=['u','f','U','F']
    if(pymoneymode in pymoneymodelist):
        break
    else:
        print('\nplease input the right mode character!')
#load the file and put into a tuple
if(pymoneymode=='f' or pymoneymode=='F'):
    filename=input('\nplease enter the filename: ')
    print('\nloading....')
    f=open(filename)
    text=[]
    for line in f:
        text.append(line)
#input money you have
total_money_I_have=input('\nHow much money do you have? ')
total_money_I_have=int(total_money_I_have)
#start input action
while True:
    #first check the pymoneymode
    if((pymoneymode=='f') | (pymoneymode=='F')):
        #put the item into input_data
        if(r<len(text)):
            input_data=text[r]
            r=r+1
        #when r==last item change the pymoneymode
        else:
            pymoneymode='u'
    if((pymoneymode=='u') | (pymoneymode=='U')):
        #input the data by user
        input_data=input(Fore.RESET+'[%d] '%item)
    #split the data into item and money
    input_data_split=input_data.split()

    #done for end the program
    if (input_data_split[0]=='done'):
        Dlist=['Income','Eat','Transport','Others']
        Amlist=[str(total_income),str(eat_expense),str(transport_expense),str(others_expense)]
        Avlist=[str(average(total_income,nof_income)),str(average(eat_expense,nof_eat)),str(average(transport_expense,nof_transport)),str(average(others_expense,nof_others))]
        noflist=[str(nof_income),str(nof_eat),str(nof_transport),str(nof_others)]
        print()
        print_statement=input('print the statement?(Y/N) ')
        print('\n')
        total_money_I_have_final=total_money_I_have-total_expense+total_income
        if(print_statement=='Y' or print_statement=='y'):
            printstatement(Dlist,Amlist,Avlist,noflist,total_expense)
        if(total_income>=total_expense):
            print(Fore.GREEN+et.format('Balance: %d\n') %total_money_I_have_final)
            print(Fore.LIGHTGREEN_EX+et.format('Great! You earned more than you spent.'))
        else:
            print(Fore.RED+et.format('Balance: %d\n') %total_money_I_have_final)
            print(Fore.LIGHTRED_EX+et.format('Becareful! You spent more than you earned.'))
        print('\n'+Fore.LIGHTWHITE_EX+et.format(str(datetime.date.today()))+'\n')
        break
    #now for check the state
    if (input_data_split[0]=='now'):
        total_money_I_have_now=total_money_I_have-total_expense+total_income
        print()
        print(et.format('total_money_now      %d\n') %total_money_I_have_now)
        print(Fore.GREEN+et.format('total_income_now  (+)%d\n') %total_income)
        print(Fore.RED+et.format('total_expense_now (-)%d\n') %total_expense)
        print(Fore.RESET)
        #now doesn't count [item]
        item=item-1
    #income
    if (input_data_split[0]=='income'):
        total_income=total_income+int(input_data_split[1])
        nof_income=nof_income+1
    #expense
    else:
        try:
            if(input_data_split[0]!='now'):
                if(int(input_data_split[1])<0):
                    input_data_split[1]=0-int(input_data_split[1])
                nof_expense=nof_expense+1
                total_expense=total_expense+int(input_data_split[1])
                if(input_data_split[0] in eat):
                    nof_eat=nof_eat+1
                    eat_expense=eat_expense+int(input_data_split[1])
                if(input_data_split[0] in transport):
                    nof_transport=nof_transport+1
                    transport_expense=transport_expense+int(input_data_split[1])
                if(not(input_data_split[0] in (eat+transport))):
                    nof_others=nof_others+1
                    others_expense=others_expense+int(input_data_split[1])
                    #print(nof_others)
                    #print(others_expense)
        except:
            print(Fore.LIGHTRED_EX+'\nwrong format! please enter right format str(item) int(money)\n'+Fore.RESET)
            #wrong input doesn't count [item]
            item=item-1
    item=item+1






















#┏ ━ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
#print('eat_expense {} (average {})'.format(eat_expense,average(eat_expense,nof_eat)))
#print('transport_expense {}(average {})'.format(transport_expense,average(transport_expense,nof_transport)))
#print('others_expense {}(average {})'.format(others_expense,average(others_expense,nof_others)))
#Dlist=['Income','Eat','Transport','Others']
#Amlist=[str(total_income),str(eat_expense),str(transport_expense),str(others_expense)]
#Avlist=[str(average(total_income,nof_income)),str(average(eat_expense,nof_eat)),str(average(transport_expense,nof_transport)),str(average(others_expense,nof_others))]
#noflist=[str(nof_income),str(nof_eat),str(nof_transport),str(nof_others)]
