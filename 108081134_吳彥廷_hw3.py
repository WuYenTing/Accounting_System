from colorama import Fore,Back,Style
import datetime
import sys

ll='{0: ^40s}'
l='{0: ^20s}'
s='{0: ^10}'
n='{0: ^4}' 
et='{0: ^70s}'
C='{0: ^14s}'
Am='{0: ^10}'
N='{0: ^10}'
Av='{0: ^11}'
No='{0: ^8}'
tt='{0: ^57}'

class Record:
    """Represent a record."""
    def __init__(self,category,description,amount):
        self._category=category
        self._description=description
        self._amount=amount
        # 1. Define the formal parameters so that a Record can be instantiated
        #    by calling Record('meal', 'breakfast', -50).
        # 2. Initialize the attributes from the parameters. The attribute
        #    names should start with an underscore (e.g. self._amount)
        
    def get_category(self):
        return self._category
    def set_category(self,c):
        self._amount=c
    #ca=property(lambda self:self.get_category(),lambda self,c:self.set_category(self,c))        
    @property  
    def category(self):  
        return self.get_category()
    
    def get_description(self):
        return self._description
    def set_description(self,d):
        self._description=d
    #de=property(lambda self:self.get_description(),lambda self,d:self.set_description(self,d))    
    @property
    def description(self):
        return self.get_description()
           
    def get_amount(self):
        return self._amount
    def set_amount(self,a):
        self._amount=a
    #am=property(lambda self:self.get_amount(),lambda self,a:self.set_amount(self,a))    
    @property 
    def amount(self):
        return self.get_amount()    

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        self._initial_money=0
        self._records=[]
        try: #restart the program
            f=open('record.txt','r')
            print(Fore.LIGHTMAGENTA_EX+"\nwelcome back!!"+Fore.RESET)
            self._initial_money=int(f.readline())
            self._records=self.file_list_Record(f.readlines())
            #self._records=f.readlines()#input record.txt to ogmoney, list and continue the pymoney         
        except:
            print(Fore.LIGHTCYAN_EX+'\nHello, nice to meet you!!'+Fore.RESET)
            #print('\nAdd an expense or income record with category description amount')
            while True:
                try:
                    self._initial_money=int(input('\nHow much money do you have? '))                
                    break
                except ValueError: #input not integer
                    sys.stderr.write(Fore.LIGHTRED_EX+'\nInvalid value for money. Please enter an integer.\n'+Fore.RESET)    
        # 1. Read from 'records.txt' or prompt for initial amount of money.
        # 2. Initialize the attributes (self._records and self._initial_money)
        #    from the file or user input.
  
    def chart(self):
        """Draw the chart of list[category]"""
        nfd=nml=ntt=net=ncg=nsy=nbs=sfd=sml=stt=set=scg=ssy=sbs=sexp=sinc=0
        lfd=lml=ltt=let=lcg=lsy=lbs=exp=inc=[]
        for i in self._records:
            if(str(i.category)=='food'):                
                nfd=nfd+1
                sfd=sfd+int(i.amount)                
            elif(str(i.category)=='meal'):                
                nml=nml+1
                sml=sml+int(i.amount)                
            elif(str(i.category)=='transport'):                
                ntt=ntt+1
                stt=stt+int(i.amount)                
            elif(str(i.category)=='entertainment'):                
                net=net+1
                set=set+int(i.amount)                
            elif(str(i.category)=='clothing'):                
                ncg=ncg+1
                scg=scg+int(i.amount)                
            elif(str(i.category)=='salary'):                
                nsy=nsy+1
                ssy=ssy+int(i.amount)                
            elif(str(i.category)=='bonus'):                
                nbs=nbs+1
                sbs=sbs+int(i.amount)
        lfd=['food',sfd,nfd,round(nfd and sfd/nfd or 0,2)]        
        lml=['meal',sml,nml,round(nml and sml/nml or 0,2)]        
        ltt=['transport',stt,ntt,round(ntt and stt/ntt or 0,2)]        
        let=['entertainment',set,net,round(net and set/net or 0,2)]        
        lcg=['clothing',scg,ncg,round(ncg and scg/ncg or 0,2)]        
        lsy=['salary',ssy,nsy,round(nsy and ssy/nsy or 0,2)]        
        lbs=['bonus',sbs,nbs,round(nbs and sbs/nbs or 0,2)]        
        exp=[lfd,lml,ltt,let,lcg]
        inc=[lsy,lbs]
        print()
        print(et.format('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'))
        print(et.format('┃'+tt.format('expense')+'┃'))
        print(et.format('┣━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┫')) #draw the chart
        print(et.format('┃   Category   ┃  Amount  ┃  Number  ┃  Average  ┃  Note  ┃'))
        for i in exp:
            sexp=sexp+i[1]
            print(et.format('┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━┫'))       
            print(et.format('┃'+C.format(str(i[0]))+'┃'+Am.format(str(i[1]))+'┃'+N.format(str(i[2]))+'┃'+Av.format(str(i[3]))+'┃'+No.format(' ')+'┃'))
        print(et.format('┣━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━┫'))
        print(et.format('┃'+tt.format('total = '+str(sexp))+'┃'))
        print(et.format('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')+'\n')     
        print()  
        print(et.format('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'))
        print(et.format('┃'+tt.format('income')+'┃'))
        print(et.format('┣━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┫')) #draw the chart
        print(et.format('┃   Category   ┃  Amount  ┃  Number  ┃  Average  ┃  Note  ┃'))
        for i in inc:
            sinc=sinc+i[1]
            print(et.format('┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━┫'))       
            print(et.format('┃'+C.format(str(i[0]))+'┃'+Am.format(str(i[1]))+'┃'+N.format(str(i[2]))+'┃'+Av.format(str(i[3]))+'┃'+No.format(' ')+'┃'))
        print(et.format('┣━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━┫'))
        print(et.format('┃'+tt.format('total = '+str(sinc))+'┃'))
        print(et.format('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')+'\n')

    def file_list_Record(self,list): #separate the ogmoney and other information
        """Change list of record.txt to Record(struct) and return as a list[Record1,Record2,Record3...]"""
        new=[]   
        for n in list:
            sp=n.split()
            spr=Record(*sp)
            new.append(spr)
        return new

    def file_in(self,name):
        """Input Records from files"""
        try:
            f=open(name)
            for n in filter(lambda l:l!='\n',f):
                try:
                    int(n)
                    print('\nfile intial money '+str(n))
                    self._initial_money=self._initial_money+int(n)
                except:
                    #print(n.split())
                    sp=n.split() 
                    spr=Record(*sp)   
                    self._records.append(spr) #add it to the data_list               
        except FileNotFoundError:
            sys.stderr.write(Fore.LIGHTRED_EX+'\nInvalid file. Try again.\n'+Fore.RESET)

    def add(self,string):
        """Add new a Record(category,description,amount) and add the list[Record1,Record2,Record3...]"""
        #while True:
        try:
            sp=string.split()
            spr=Record(*sp)
            int(spr.amount)
            ca=Categories()    
            if(ca.is_category_valid(spr.category)):
                self._records.append(spr)
                print(Fore.LIGHTGREEN_EX+"\nvalid category"+Fore.RESET)
            else:    
                print(Fore.LIGHTRED_EX+"\ninvalid category"+Fore.RESET)
        except ValueError:
            sys.stderr.write(Fore.LIGHTRED_EX+'\nwrong value! please enter an integer after description!\n'+Fore.RESET) 
        except: #input wrong format
            sys.stderr.write(Fore.LIGHTRED_EX+'\nwrong format! please enter (category description money)\n'+Fore.RESET)  
        #print(sp)
        #print(spr._category)
        #print(spr._description)
        #print(spr._amount)
        # 1. Define the formal parameter so that a string input by the user
        #    representing a record can be passed in.
        # 2. Convert the string into a Record instance.
        # 3. Check if the category is valid. For this step, the predefined
        #    categories have to be passed in through the parameter.
        # 4. Add the Record into self._records if the category is valid.

    def view(self):
        """View current list[Record1,Record2,Record3...] and sum"""
        print('\n'+et.format(n.format('number')+l.format('categories')+l.format('Description')+s.format('money'))+'\n')    
        list=self._records
        sum=0
        for i in range(1,len(list)+1):
            sum=sum+int(list[i-1].amount)
            #print(et.format(n.format(str(i))+l.format(str(list[i-1][0]))+l.format(str(list[i-1][1]))+s.format(str(list[i-1][2]))))                
            print(et.format(n.format(str(i))+l.format(str(self._records[i-1].category))+l.format(str(list[i-1].description))+s.format(str(list[i-1].amount))))                
        print('\n'+et.format(n.format(' ')+l.format('intial money')+l.format(str(self._initial_money))+s.format(' '))+'\n')
        sum=sum+self._initial_money
        if(sum>0):      
            print('\n'+Fore.GREEN+et.format(n.format('')+l.format('sum '+str(sum)+s.format('')))+'\n'+Fore.RESET)   
        else:
            print('\n'+Fore.RED+et.format(n.format('')+l.format('sum '+str(sum)+s.format('')))+'\n'+Fore.RESET)     
        # 1. Print all the records and report the balance.

    def delete(self,item):
        """Delete a item from list[Record1,Record2,Record3...] by category or description"""
        find_list=[]
        find_list=self.find(item)
        #print(list(find_list))
        delet=0
        if(find_list==[]):
            print(Fore.LIGHTRED_EX+'\nnothing to delete !\n'+Fore.RESET)
        else:               
            while True:
                try:
                    i=int(input('\nwhich '+str(item[0])+' do you want to delete ? ')) #select the item from the list and delet it
                    del self._records[i-1]
                    find_list.clear()
                    #delet=1
                    break 
                except ValueError:
                    sys.stderr.write(Fore.LIGHTRED_EX+'\nwrong value! please enter an integer !\n'+Fore.RESET) 
                except IndexError:
                    sys.stderr.write(Fore.LIGHTRED_EX+'\ninvalid record!\n'+Fore.RESET)
                    break            
        # 1. Define the formal parameter.
        # 2. Delete the specified record from self._records.
    
    def find(self,categories):
        """Find and show (return) the list[Record1,Record2,Record3...] by category or description"""
        try:
            print('\n'+et.format(n.format(' ')+ll.format(str(categories[0]))+s.format(' '))+'\n')
            ls=list(categories)
            lr=[]
            if(ls==[]):
                print(Fore.LIGHTRED_EX+'\ninvalid item\n'+Fore.RESET)
            else:
                print('\n'+et.format(n.format('number')+l.format('categories')+l.format('Description')+s.format('money'))+'\n')    
                for i in range(1,len(self._records)+1): #list the items you search for
                    if self._records[i-1].category in ls or self._records[i-1].description in ls:
                        lr.append(self._records[i-1])
                        print(et.format(n.format(str(i))+l.format(str(self._records[i-1].category))+l.format(str(self._records[i-1].description))+s.format(str(self._records[i-1].amount))))                
            print()
            return lr
        except:
            sys.stderr.write(Fore.LIGHTRED_EX+'\ninvalid item! please enter correct categories or description !\n'+Fore.RESET)        
        # 1. Define the formal parameter to accept a non-nested list
        #    (returned from find_subcategories)
        # 2. Print the records whose category is in the list passed in
        #    and report the total amount of money of the listed records.

    def save(self):
        """Save the intial money and list[Record1,Record2,Record3...]"""
        f=open('record.txt','w')
        f.write(str(self._initial_money)+'\n')
        c=[]
        for n in self._records:
            new=str(n.category)+' '+str(n.description)+' '+str(n.amount+'\n')
            c.append(new)
        f.writelines(c)    
        f.close()

class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        global food,meal,transport,entertainment,clothing,expense
        food=['snack','drink','fruit']
        meal=['breakfast','lunch','dinner']
        transport=['taxi','bus','railway','Ubike','gas']
        entertainment=['games','movie']
        clothing=['shorts','pants','skirt','hoodie']
        expense=['food',food,'meal',meal,'transport',transport,'entertainment',entertainment,'clothing',clothing]
    
        global salary,bonus,income
        salary=['full-time','part-time']
        bonus=['lottery','stock',]
        income=['salary',salary,'bonus',bonus]

        global cattegories
        cattegories=['expense',expense,'income',income]

        self._categories=cattegories
        # 1. Initialize self._categories as a nested list.

    def view(self,l,x):
        """View categories"""
        #print(self._categories)
        for i in l:        
            if(type(i)==str):
                for a in range(x):
                    print(" ",end="")
                print("┗━ ",end="")
                print(i)           
            else:
                self.view(i,x+5)           
        # 1. Define the formal parameters so that this method
        #    can be called recursively.
        # 2. Recursively print the categories with indentation.
        # 3. Alternatively, define an inner function to do the recursion.

    def is_category_valid(self,category):
        """Check if the category in categories"""
        def rec_check(ls,it):
            if isinstance(ls,list):
                for i,v in enumerate(ls):
                    p=rec_check(v,it)
                    if p==True:
                        return (i,)
                    if p!=False:
                        return (1,)+p
            return ls==it 
        if(rec_check(self._categories,category)==False):                   
            return False
        else:
            return True                            
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively check if the category name is in self._categories.
        # 3. Alternatively, define an inner function to do the recursion.

    def find_subcategories(self,category):
        """Create a list of the subcategories of category"""    
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category,categories[index + 1],found=True)
            else:
                if categories == category or found==True:   
                    yield categories                       
        return list(find_subcategories_gen(category,self._categories))
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively find the target category and call the
        #    self._flatten method to get the subcategories into a flat list.
        # 3. Alternatively, define an inner function to do the recursion.


categories = Categories()
records = Records()

while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / file / exit / chart)? ')
    if command == 'add':
        record = input('Add an expense or income record with category descriotion amount :\n')
        records.add(record)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        delete_list = categories.find_subcategories(delete_record)
        records.delete(delete_list)
    elif command == 'view categories':
        print()
        categories.view(categories._categories,15)
    elif command == 'find':
        target_categories = input('Which category or description do you want to find? ')
        target_list = categories.find_subcategories(target_categories) 
        records.find(target_list)    
    elif command == 'exit':
        records.save()
        break
    elif command == 'file':
        name = input('Please enter the filename: ')
        records.file_in(name)
    elif command == 'chart':
        records.chart()    
    else:
        sys.stderr.write(Fore.LIGHTRED_EX+'\nInvalid command. Try again.\n'+Fore.RESET)
