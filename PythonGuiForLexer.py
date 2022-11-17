
#This is an example of using the tkinter python extension to create a basic window with button

from ast import operator
from cProfile import label
from tkinter import *
import re
from tkinter.ttk import Labelframe
from turtle import right


class MyFirstGUI: #class definition


    def __init__(self, root):
        #Master is the default prarent object of all widgets.
        #You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("Lexical Analyzer for Tinypie")

        self.master.geometry('570x300')
        
        # starting from line 1 to grab text
        self.linec1 =1.0
        self.linec2 = 2.0
        self.linec3 = 1.0

        # For source code printing
        self.yinc = .1

        # line processing label
        self.linep = 0

        
        #Source code input label
        self.label = Label(self.master, text="Source code input: ")
        self.label.grid(row=0,column=0,sticky = W)

        #Lexical Analyzed Result: label
        self.outlabel = Label(self.master, text = "Tokens:")
        self.outlabel.grid(column = 6, row = 0, sticky = W)

        self.outlabel2 = Label(self.master, text = "Parser:")
        self.outlabel2.grid(column = 15, row = 0, sticky = W)

        #Current Processing line label
        self.pline = Label(self.master, text = "Current Processing line: ")
        self.pline.grid(column = 0, row = 15, sticky = W)
        #Quit button
        self.qbutton = Button(self.master, text = "Quit", command = self.master.quit)
        self.qbutton.grid(column = 25, row = 15)
        
        #Next Line Button
        nlButton = Button(self.master, text = "Next Line",command = self.printSource)
        nlButton.grid(column = 0, row = 20, sticky = W)
        
        #Intial display of processing line label
        self.printlinep = Label(self.master,text = self.linep)
        self.printlinep.grid(column = 1, row = 15)
       
        #source code input text box
        self.inputSource = Text(self.master,width = 30, height = 15, borderwidth = 10)
        self.inputSource.grid(column = 0, row = 3)

        # display text box
        self.dtext = Text(self.master,width = 30, height = 15, borderwidth = 10)
        self.dtext.grid(column = 6, row = 3)

        # scrollbar 1 
        self.sb1 = Scrollbar(self.master,command = self.dtext.yview)
        self.sb1.grid(column = 10, row = 3, ipady = 50)

        # scrollbar 2
        self.sb2 = Scrollbar(self.master,command = self.inputSource.yview)
        self.sb2.grid(column = 5, row = 3, sticky = W,ipady = 50)

        
        #display text box for parser
        self.dtextp = Text(self.master,width = 30, height = 15, borderwidth = 10)
        self.dtextp.grid(column = 15, row = 3 )

        # scrollbar 3
        self.sb3 = Scrollbar(self.master,command = self.dtextp.yview)
        self.sb3.grid(column = 20, row = 3,ipady = 50)
        
    def CutOneLineTokens(self,str1):

        l1 = [];
        
        keywords = re.match(r'int\s|if|float\s|else',str1);
        if(keywords != None):
            # if its an if statement
            if(keywords[0] == 'if'):
                str2 = "<key,if>" + "\n"
                l1.append(str2); #if(a>1)
                str2 = str1[2:] # (a>1)

                separators = re.findall(r'\(|\)|:|"|;',str2);
                if(separators != None):
                    for i in range(0,len(separators)):
                        str3 = "<sep," + str(separators[i]) + ">" + "\n"
                        l1.append(str3)
                identifiers = re.findall(r'(?:[A-z]+[0-9]+|[A-z]+)',str2);
                if(identifiers != None):
                    for i in range(0,len(identifiers)):
                        str3 = "<id," + str(identifiers[i]) + ">" + "\n"
                        l1.append(str3)
                        str3 = str3.replace(identifiers[i],"")
                operators = re.findall(r'=|\+|>|\*',str2);
                if(operators != None):
                    for i in range(0,len(operators)):
                        str3 = "<op," + str(operators[i]) + ">" + "\n"
                        l1.append(str3)
                Int_literal = re.search(r'(?<!\.)\b[0-9]+\b(?!\.)',str2);
                if(Int_literal != None):
                    str3 = "<lit," + Int_literal[0] + ">" + "\n"
                    l1.append(str3)
                Float_literal = re.search(r'(?<![A-z])(?<!\.)\b\d+[\.]\d+\b',str1);
                if(Float_literal!= None):
                    str3 = "<lit," + Float_literal.group(0) + ">" + "\n"
                    l1.append(str3)

            # if it's an integer
            elif(keywords[0] == 'int '):
                str2 = "<key,int>" + "\n"
                l1.append(str2);
                str1 = str1[4:]

                identifiers = re.findall(r'\b(?:[A-z]+[0-9]+|[A-z]+)\b',str1);
                if(identifiers != None):
                    for i in range(0,len(identifiers)):
                        str2 = "<id," + identifiers[i] + ">" + "\n"
                        l1.append(str2)
                        

                operators = re.findall(r'=|\+|>|\*',str1);
                if(operators != None):
                    for i in range(0,len(operators)):
                        str2 = "<op," + operators[i]+ ">" + "\n"
                        l1.append(str2)

                separators = re.search(r'\(|\)|:|"|;',str1);
                if(separators != None):
                    str2 = "<sep," + separators.group(0) + ">" + "\n"
                    l1.append(str2)

                Int_literal = re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)',str1);
                if(Int_literal != None):
                    for i in range(0,len(Int_literal)):
                        str2 = "<lit," + Int_literal[i] + ">" + "\n"
                        l1.append(str2)
                        str2 = str2.replace(Int_literal[i],"")

                Float_literal = re.findall(r'\b\d+[\.]\d+\b',str1);
                if(Float_literal!= None):
                    for i in range(0,len(Float_literal)):
                        str3 = "<lit," + Float_literal[i] + ">" + "\n"
                        l1.append(str3)
                        str3 = str2.replace(Float_literal[i],"")
           
            #if its a float
            elif(keywords[0] == 'float '):
                str2 = "<key,float>" + "\n"
                l1.append(str2)
                str2 = str1[6:]
                
                identifiers = re.findall(r'\b(?:[A-z]+[0-9]+|[A-z]+)\b',str2);
                if(identifiers != None):
                    for i in range(0,len(identifiers)):
                        str3 = "<id," + str(identifiers[i]) + ">" + "\n"
                        l1.append(str3)
                        str3 = str2.replace(identifiers[i],"")
                        
                
               
                separators = re.findall(r'\(|\)|:|"|;',str3);
                if(separators != None):
                    for i in range(0,len(separators)):
                        str3 = "<sep," + str(separators[i]) + ">" + "\n"
                        l1.append(str3)
                        str3 = str2.replace(separators[i],"")
                
                
                operators = re.findall(r'-|=|\+|>|\*',str3); #(r'\s*=|\+|>|\*',
                if(operators != None):
                    for i in range(0,len(operators)):
                        str3 = "<op," + str(operators[i]) + ">" + "\n"
                        l1.append(str3)
                        str3 = str2.replace(operators[i],"")
                       

                Float_literal = re.findall(r'\b\d+[\.]\d+\b',str3);
                if(Float_literal!= None):
                    for i in range(0,len(Float_literal)):
                        str3 = "<lit," + Float_literal[i] + ">" + "\n"
                        print(str3)
                        l1.append(str3)
                        str3 = str2.replace(Float_literal[i],"")

                Int_literal = re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)',str1);
                if(Int_literal != None):
                    for i in range(0,len(Int_literal)):
                        str2 = "<lit," + Int_literal[i] + ">" + "\n"
                        l1.append(str2)
                        str2 = str2.replace(Int_literal[i],"")

        else: # for strings
            # if string is print("tinypie")
            printe = re.search(r'print',str1) #strings
            if(printe != None):
                str0 = "<id,print>" + "\n"
                l1.append(str0)
                str1 = str1.replace(printe.group(0),"")
            
            separators = re.findall(r'\(|\)|:|"|;',str1);#else
            if(separators != None):
                for i in range(0,len(separators)):
                    str2 = "<sep," + separators[i] + ">" + "\n"
                    l1.append(str2)
                    str1 = str1.replace(separators[i],"")
            str7 = str1
            str1 = re.match(r'^(\s*\w+( \w+)*\s*)$',str1);
            if(str1 != None):
                str10 = "<lit," + str1.group(0) + ">" + "\n"
                l1.append(str10)

            # if string a = "tinypie"
            else:
                
                if(str7.find("=") != None):
                    str6 = "<op,=>" + "\n"
                    l1.append(str6)
               
                str8 = str7[:str7.find("=")] # identifier
                
                str4 = "<id,"+ str8 + ">" + "\n"
                l1.append(str4)

                str7=str7.replace(str8,"")
                str7=str7.replace("=","") #actual string
                str5 = re.match(r'^(\s*\w+( \w+)*\s*)$',str7);
                if(str5 != None):
                    str9 = "<lit," + str5.group(0) + ">" + "\n"
                    l1.append(str9)

      
        return l1
        
    def printSource (self):
                                      # function call       input from first textbox
        out = self.CutOneLineTokens(self.inputSource.get(self.linec1,self.linec2))
        for i in out:
            self.dtext.insert('end',i)
        #increment what lines it grabs from the text box
        self.linec1 += 1.0
        self.linec2 += 1.0
        

        #To insert for the second text box
        self.linec3 += 7.0

        
    
        # print current processing line
        self.linep +=1
        self.printlinep = Label(self.master,text = self.linep)
        self.printlinep.grid(column = 1, row = 15)

        self.parser(out)



    def parser(self,L1):

        # convert the list to a list that contains tuples
        b = [] # empty list
        tl = () #empty tuple
        for i in range(0,len(L1)):
            str1 = L1[i][L1[i].find("<")+1:L1[i].find(",")];
            str2 = L1[i][L1[i].find(",")+1:L1[i].find(">")];
            tl = (str1,str2)
            b.append(tl)
        
        #tuple
        Mytokens = b
        global inToken 
        inToken = ("empty","empty")
        
        def accept_token():
            global inToken
            self.dtextp.insert(self.linec3,"     accept token from the list:"+inToken[1])
            inToken=Mytokens.pop(0)
        
        def parser2():
            global inToken
            inToken=Mytokens.pop(0)
            exp()
            if(inToken[1]==";"):
                self.dtextp.insert(self.linec3,"\nparse tree building success!")
            return
            parser2()
        #second func 
        #identify if its math or exp 
        def math():
        #print("\n----parent node math, finding children nodes:")
            global inToken
 
            multi()
            if(inToken[1]=="+"): #+
                self.dtextp.insert('end',"\n----parent node math, finding children nodes:")
                self.dtextp.insert('end',"child node (internal): math")
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
            multi()
 
 
        def multi():
            self.dtextp.insert('end',"\n----parent node math, finding children nodes:")
            global inToken
            if(inToken[0]=="float"): #float
                self.dtextp.insert('end',"child node (internal): float")
                self.dtextp.insert('end',"   float has child node (token):"+inToken[1])
                accept_token()
 
            elif (inToken[0]=="int"): #int
                self.dtextp.insert('end',"child node (internal): int")
                self.dtextp.insert('end',"   int has child node (token):"+inToken[1])
                accept_token()
 
                if(inToken[1] == "*"): #*
                    self.dtextp.insert('end',"child node (internal): math")
                    self.dtextp.insert('end',"child node (token):"+inToken[1])
                    accept_token()
 
                multi()
            else:
                self.dtextp.insert('end',"error, math expects float or int")
 
 
        #firstf func   
        def exp():
             self.dtextp.insert('end',"\n----parent node exp, finding children nodes:")
             global inToken;
             typeT,token=inToken; #(string, string)
             if(typeT=="key"):
                self.dtextp.insert('end',"child node (internal): keyword")
                self.dtextp.insert('end',"   identifier has child node (token):"+token)
                accept_token() #helper func to get the token and move to the next token
 
             if(inToken[0]=="id"):
                self.dtextp.insert('end',"child node (internal): identifier")
                self.dtextp.insert('end',"   identifier has child node (token):"+inToken[0])
                accept_token() #helper func to get the token and move to the next token 
 
             if(inToken[1]=="="):
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
             else:
                self.dtextp.insert('end',"expect = as the second element of the expression!")
                return
 
        #print("Child node (internal): math")
        math() #calling the func of math node

 
        #2 FUNCTIONS FOR STEP 3
        def if_exp():
            self.dtextp.insert('end',"\n----parent node exp, finding children nodes:")
            global inToken;
            #typeT,token=inToken; #(string, string)
 
            if(inToken[1]=="if"): #if
                self.dtextp.insert('end',"child node (internal): identifier")
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
 
            if(inToken[1] == "("): #(
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
 
            comparison_exp()#calling comparison_exp()
 
            if(inToken[1] == ")"): #)
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
 
            #comnparison_exp() #more math, calling math func
 
 
    
        #else:print("error, you need + after the int in the math")
 
 
 
        def comparison_exp():
            print("\n----parent node exp, finding children nodes:")
            global inToken;
            if(inToken[0]=="id"): #if statement(id)
                self.dtextp.insert('end',"child node (internal): identifier")
                self.dtextp.insert('end',"   identifier has child node (token):"+inToken[1])
                accept_token()
 
            if(inToken[1]== ">"): #>
                self.dtextp.insert('end',"child node (token):"+inToken[1])
                accept_token()
 
                comparison_exp()

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()


