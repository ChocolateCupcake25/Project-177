# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:54:29 2022

@author: Fierce Bird// Ziyah Virani 
"""
from tkinter import*
root = Tk()
root.title("Encapsulation")
root.geometry("600x700")
root.configure(bg="#d5f274")

#------Labels-------
label_name=Label(root,text="Name : ",font=("Arial Greek",18,"bold"), bg="#d5f274",fg="#024d3b")
label_password=Label(root,text="Password : ",font=("Arial Greek",18,"bold"),bg="#d5f274",fg="#024d3b")       
label_captcha=Label(root,text="Captcha : ",font=("Arial Greek",18,"bold"),bg="#d5f274",fg="#024d3b")       

label_updated_name=Label(root,font=("Arial Greek",18,"bold"),bg="#d5f274",fg="#75014b")
label_updated_password=Label(root,font=("Arial Greek",18,"bold"),bg="#d5f274",fg="#75014b")
label_updated_captcha=Label(root,font=("Arial Greek",18,"bold"),bg="#d5f274",fg="#75014b")
#----------input box----
entry_name=Entry(root,bg="#bcf763")
entry_password=Entry(root,bg="#bcf763")
entry_captcha=Entry(root,bg="#bcf763")

#---------placements--------
entry_name.place(relx=0.75,rely=0.2,anchor=CENTER)
entry_password.place(relx=0.75,rely=0.3,anchor=CENTER)
entry_captcha.place(relx=0.75,rely=0.4,anchor=CENTER)

label_name.place(relx=0.25,rely=0.2,anchor=CENTER)
label_password.place(relx=0.22,rely=0.3,anchor=CENTER)
label_captcha.place(relx=0.24,rely=0.4,anchor=CENTER)

label_updated_name.place(relx=0.45,rely=0.6,anchor=CENTER)
label_updated_password.place(relx=0.45,rely=0.7,anchor=CENTER)
label_updated_captcha.place(relx=0.45,rely=0.8,anchor=CENTER)

#-----classes-----
class userDB():
    def __init__(self):
        self.username= "Georgy"
        self.password= "Geo1758"
        self.captcha= "ge17"
    def showUser(self):
        label_updated_name["text"]="Name : " + self.username
        label_updated_password["text"]="Password : " + self.password
        label_updated_captcha["text"]="Captcha : " + self.captcha

user=userDB()

def addUser():
    global user
    user.username = entry_name.get()
    user.password = entry_password.get()
    user.captcha = entry_captcha.get()
    
    name = user.username
    password = user.password
    captcha = user.captcha
    
    label_updated_name["text"]="Name : " + name
    label_updated_password["text"]="Password : " + password
    label_updated_captcha["text"]="Captcha : " + captcha

    print("Data Updated")
    
    
Btn_Show_Profile = Button(root,text="Show Profile",font=("Arial Greek",18,"bold"), bg="#87ad2f",fg="#024d3b",command=user.showUser)
Btn_Update_Profile = Button(root,text="Update Profile",font=("Arial Greek",18,"bold"), bg="#87ad2f",fg="#024d3b",command=addUser)

Btn_Show_Profile.place(relx=0.15,rely=0.5,anchor=CENTER)
Btn_Update_Profile.place(relx=0.85,rely=0.5,anchor=CENTER)

root.mainloop()
