from tkinter import *


root = Tk()

#menubar
menubar =Menu(root)	#Telling root that we have a menubar for you
root.config(menu=menubar)	#Configuring roo to hae the menu as the menubar told before

#submenues
subMenu = Menu(menubar, tearoff=False)	#adding a new menu

#adding cascade
menubar.add_cascade(label="File", menu=subMenu)	#adding menu name

#adding drop down list
subMenu.add_command(label="Open")	#adding option in dropdown
subMenu.add_command(label='Exit')	#adding option in dropdown

#adding help
subMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label ='Help', menu = subMenu)

#adding drop down
subMenu.add_command(label='About Us')

root.title("FLAMES")

root.config(background='light blue')

#title block
title_block = Label(root, text='FLAMES',font=('Times',16),bg ='light pink')

title_block.pack(side=TOP, fill=X)


#frame to hold the grid layout of names
main_frame = Frame(root,bg = "pink")
main_frame.pack(pady = 100, padx = 50)

#frame that holds the name frame
nm_frame = Frame(main_frame, bg ="light green")
nm_frame.grid(row=0,padx=150,pady=100)

#variables that holds the names of the users
nm = StringVar()	# name of the user
pt = StringVar()	# name of the partner

#name 1
nm1_lbl = Label(nm_frame, text ="Name",font=('Helvetica',12), bg = "light green")	# label of the name
nm1_lbl.grid(row=0, column=0, padx = 10, pady = 10)

nm1 = Entry(nm_frame, textvariable = nm)	# name entry textbox
nm1.grid(row=0,column=1, padx = 10, pady =10)

#name 2
nm2_lbl = Label(nm_frame, text ="Partner",font=('Helvetica',12), bg = "light green")
nm2_lbl.grid(row=1, column=0, padx = 10, pady = 10)

nm2 = Entry(nm_frame, textvariable = pt)	# partner entry textbox
nm2.grid(row=1,column=1, padx = 10, pady = 10)	




#logic of function

# class
class check:
    def __init__(self,name,partner):
        self.name= name
        self.partner = partner
    
    def omit_char_lst(self,nm1_lst,nm2_lst):
        char_lst = []    
        #finding the similar chars
        for indx in range(0,len(nm1_lst)):
            if nm1_lst[indx] in nm2_lst:
                if nm1_lst[indx] not in char_lst:    #skipping same char
                    char_lst.append(nm1_lst[indx])
                else:
                    pass
    
        return char_lst                                 
                  
    #omitting char from lst
    def omit_char(self,nm,char_lst):
        for ch in char_lst:
            nw_nm = nm.split(ch)
            x = ''
            for i in nw_nm:
                x+=i
            nm = x
        return nm


    def check_status(self):
        flames = ['Friend', 'Love', 'Affair', 'Marriage', 'Enemies', 'Sex']

        #name to list
        nm_1_lst = [x for x in self.name]
        nm_2_lst = [x for x in self.partner]
    
    
        chr_lst = self.omit_char_lst(nm_1_lst,nm_2_lst)
        nm_1_new = self.omit_char(self.name,chr_lst)
        nm_2_new = self.omit_char(self.partner,chr_lst)

        count = len(nm_1_new) + len(nm_2_new)

        p_typ = (count%6)-1
        status.config(text=flames[p_typ])




# calling the class function
def main():
    name = nm.get()
    partner =pt.get()
    if (name.lower(),partner.lower()) in [('sooraj','sherry'),('sherry','sooraj')]:
        status.config(text="You are a perfect match")
    elif 'sherry' in (name.lower(),partner.lower()):
        status.config(text="You are only for Sooraj")
    else:    
        p = check(name,partner)
        p.check_status()

#Submit button
sb_btn = Button(main_frame, text = "Submit", command = main)
sb_btn.grid(row=1)

#Flames status 
status = Label(main_frame,text ="",bg="yellow")
status.grid(row=2, pady=20)


root.mainloop()






