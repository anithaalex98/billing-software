from tkinter import *
import math, random, os, re
from tkinter import messagebox

class Bill_App:
    #============== Function - __init__ ====================
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#a19fe0"
        title = Label(self.root, text="Billing Software", bd=12,  
                      relief="groove", fg="#1f2757", 
                      font=("times new roman",30,"bold"), 
                      bg="#9390db", pady=2).pack(fill=X)
        
        #================= Variables ====================
            #=============== Coffee =====================
        self.c_expresso = IntVar()
        self. c_americano = IntVar()
        self.c_cap = IntVar()
        self.c_cafel = IntVar()
        self.c_cafem = IntVar()
        self.c_frappe = IntVar()
        
            #================= Tea =============================
        self.t_green = IntVar()
        self.t_mint = IntVar()
        self.t_venti = IntVar()
        self.t_barley = IntVar()
        self.t_lemon = IntVar()
        self.t_boba = IntVar()
        
            #==================== Pastries =======================
        self.p_choco = IntVar()
        self.p_red = IntVar()
        self.p_fresh = IntVar()
        self.p_pine = IntVar()
        self.p_fudge = IntVar()
        self.p_truffle = IntVar()
        
            #======================== Total Price & Tax ====================
        self.tot_coffee = StringVar()
        self.tot_tea = StringVar()
        self.tot_pastry = StringVar()
        
        self.tax_coffee = StringVar()
        self.tax_tea = StringVar()
        self.tax_pastry = StringVar()
        
            #=================== Customer ===================
        self.cust_name = StringVar()
        self.cust_phone = StringVar()
        
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
        #============== Customer Details Frame ======================
        F1 = LabelFrame(self.root, text="Customer Details",
                        bd=10, relief="groove", 
                        font=("times new roman",15,"bold"),
                        fg="#eceef8", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="#1f2757", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1, textvariable=self.cust_name, width=15, font="arial 15", bd=10, relief="sunken").grid(row=0,column=1,padx=5,pady=10)
        
        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="#1f2757", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1, textvariable=self.cust_phone, width=15, font="arial 15", bd=10, relief="sunken").grid(row=0,column=3,padx=5,pady=10)
        
        c_bil_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="#1f2757", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1, textvariable=self.search_bill, width=15, font="arial 15", bd=10, relief="sunken").grid(row=0,column=5,padx=5,pady=10)
        
        bill_btn = Button(F1, command=self.find_bill, text="Search", width=10, bg="#c1c1fe", bd=7, font="arial 12 bold", activebackground="#6364d8").grid(row=0,column=6,padx=10,pady=10)
        
        #================== Coffee Frame ==============================
        F2 = LabelFrame(self.root, text="Coffee",
                        bd=10, relief="groove", 
                        font=("times new roman",15,"bold"),
                        fg="#eceef8", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)
        
        c1_lbl = Label(F2, text="Espresso", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F2, textvariable=self.c_expresso, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=0,column=1,padx=10,pady=10)
        
        c2_lbl = Label(F2, text="Americano", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F2, textvariable=self.c_americano, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=1,column=1,padx=10,pady=10)
        
        c3_lbl = Label(F2, text="Cappuccino", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F2, textvariable=self.c_cap, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=2,column=1,padx=10,pady=10)
        
        c4_lbl = Label(F2, text="Caffe Latte", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F2, textvariable=self.c_cafel, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=3,column=1,padx=10,pady=10)
        
        c5_lbl = Label(F2, text="Caffe Mocha", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F2, textvariable=self.c_cafem, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=4,column=1,padx=10,pady=10)
        
        c6_lbl = Label(F2, text="Frappe", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F2, textvariable=self.c_frappe, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=5,column=1,padx=10,pady=10)
        
        #================== Tea Frame ==============================
        F3 = LabelFrame(self.root, text="Tea",
                        bd=10, relief="groove", 
                        font=("times new roman",15,"bold"),
                        fg="#eceef8", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)
        
        t1_lbl = Label(F3, text="Green Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1_txt = Entry(F3, textvariable=self.t_green, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=0,column=1,padx=10,pady=10)
        
        t2_lbl = Label(F3, text="Mint Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2_txt = Entry(F3, textvariable=self.t_mint, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=1,column=1,padx=10,pady=10)
        
        t3_lbl = Label(F3, text="Venti Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3_txt = Entry(F3, textvariable=self.t_venti, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=2,column=1,padx=10,pady=10)
        
        t4_lbl = Label(F3, text="Barley Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4_txt = Entry(F3, textvariable=self.t_barley, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=3,column=1,padx=10,pady=10)
        
        t5_lbl = Label(F3, text="Lemon Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5_txt = Entry(F3, textvariable=self.t_lemon, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=4,column=1,padx=10,pady=10)
        
        t6_lbl = Label(F3, text="Boba Tea", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6_txt = Entry(F3, textvariable=self.t_boba, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=5,column=1,padx=10,pady=10)
                
        #================== Pastries Frame ==============================
        F4 = LabelFrame(self.root, text="Pastries",
                        bd=10, relief="groove", 
                        font=("times new roman",15,"bold"),
                        fg="#eceef8", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)
        
        t1_lbl = Label(F4, text="Chocolate", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1_txt = Entry(F4, textvariable=self.p_choco, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=0,column=1,padx=10,pady=10)
        
        t2_lbl = Label(F4, text="Red Velvet", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2_txt = Entry(F4, textvariable=self.p_red, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=1,column=1,padx=10,pady=10)
        
        t3_lbl = Label(F4, text="Fresh Fruit", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3_txt = Entry(F4, textvariable=self.p_fresh, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=2,column=1,padx=10,pady=10)
        
        t4_lbl = Label(F4, text="Pineapple", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4_txt = Entry(F4, textvariable=self.p_pine, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=3,column=1,padx=10,pady=10)
        
        t5_lbl = Label(F4, text="Fudge", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5_txt = Entry(F4, textvariable=self.p_fudge, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=4,column=1,padx=10,pady=10)
        
        t6_lbl = Label(F4, text="Truffle", font=("times new roman",16,"bold"), bg=bg_color, fg="#1f2757").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6_txt = Entry(F4, textvariable=self.p_truffle, width=10, font=("times new roman",14,"bold"), bd=5, relief="sunken").grid(row=5,column=1,padx=10,pady=10)
        
        #================== Bill Frame =======================
        F5 = LabelFrame(self.root,bd=10, relief="groove")
        F5.place(x=1000, y=180, width=360, height=380)
        
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief="groove").pack(fil=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        #=============== Button Frame ========================
        F6 = LabelFrame(self.root, text="Bill Menu",
                        bd=10, relief="groove", 
                        font=("times new roman",15,"bold"),
                        fg="#eceef8", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        
        m1_lbl = Label(F6, text="Total Price of Coffee", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1, sticky="w")
        m1_txt = Entry(F6, textvariable=self.tot_coffee, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl = Label(F6, text="Total Price of Tea", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1, sticky="w")
        m2_txt = Entry(F6, textvariable=self.tot_tea, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl = Label(F6, text="Total Price of Pastries", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1, sticky="w")
        m3_txt = Entry(F6, textvariable=self.tot_pastry, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=2,column=1,padx=10,pady=1)
        
        
        c1_lbl = Label(F6, text="Tax - Coffee", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1, sticky="w")
        c1_txt = Entry(F6, textvariable=self.tax_coffee, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl = Label(F6, text="Tax - Tea", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1, sticky="w")
        c2_txt = Entry(F6, textvariable=self.tax_tea, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl = Label(F6, text="Tax - Pastries", bg=bg_color, fg="#1f2757", font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1, sticky="w")
        c3_txt = Entry(F6, textvariable=self.tax_pastry, width=18, font="arial 10 bold", bd=7, relief="sunken").grid(row=2,column=3,padx=10,pady=1)
        
        btn_F = Frame(F6, bd=7, bg="#f2f1f3", relief="groove")
        btn_F.place(x=750, width=570, height=90)
        
        total_btn = Button(btn_F, command=self.total, text="Total", bg="#c1c1fe", bd=7, fg="#1f2757", pady=10, width=11, font="arial 12 bold", activebackground="#6364d8").grid(row=0,column=0, padx=5, pady=5)
        gbill_btn = Button(btn_F,  command=self.bill_area, text="Generate Bill", bg="#c1c1fe", bd=7, fg="#1f2757", pady=11, width=10, font="arial 12 bold", activebackground="#6364d8").grid(row=0,column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, command=self.clear_data, text="Clear", bg="#c1c1fe", bd=7, fg="#1f2757", pady=10, width=11, font="arial 12 bold", activebackground="#6364d8").grid(row=0,column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, command=self.exit_app, text="Exit", bg="#c1c1fe", bd=7, fg="#1f2757", pady=10, width=11, font="arial 12 bold", activebackground="#6364d8").grid(row=0,column=3, padx=5, pady=5)
        self.welcome_bill()
     
    
    #======================== Function - Total Price - Total Button ===========================     
    def total(self):
        #======================= Coffee =========================
        self.tp_c_expresso = self.c_expresso.get()*116
        self.tp_c_americano = self.c_americano.get()*142
        self.tp_c_cap = self.c_cap.get()*126
        self.tp_c_cafel = self.c_cafel.get()*134
        self.tp_c_cafem = self.c_cafem.get()*142
        self.tp_c_frappe = self.c_frappe.get()*173
        
        self.totprice_coffee = float(
                                        self.tp_c_expresso +
                                        self.tp_c_americano +
                                        self.tp_c_cap +
                                        self.tp_c_cafel +
                                        self.tp_c_cafem +
                                        self.tp_c_frappe
                                    ) 
        
        self.tot_coffee.set("Rs. "+str(self.totprice_coffee))
        self.tot_tax_coffee = round((self.totprice_coffee*0.06),2)
        self.tax_coffee.set("Rs. "+str(self.tot_tax_coffee))        
                
        #====================== Tea ==============================
        self.tp_t_green = self.t_green.get()*125
        self.tp_t_mint = self.t_mint.get()*145
        self.tp_t_venti = self.t_venti.get()*200
        self.tp_t_barley = self.t_barley.get()*155
        self.tp_t_lemon = self.t_lemon.get()*125
        self.tp_t_boba = self.t_boba.get()*240
        
        self.totprice_tea = float(
                                    self.tp_t_green +
                                    self.tp_t_mint +
                                    self.tp_t_venti +
                                    self.tp_t_barley +
                                    self.tp_t_lemon +
                                    self.tp_t_boba
                                 )
        
        self.tot_tea.set("Rs. "+str(self.totprice_tea))
        self.tot_tax_tea = round((self.totprice_tea*0.03),2)
        self.tax_tea.set("Rs. "+str(self.tot_tax_tea))  
                
        #====================== Pastries ============================
        self.tp_p_choco = self.p_choco.get()*116
        self.tp_p_red = self.p_red.get()*199
        self.tp_p_fresh = self.p_fresh.get()*209
        self.tp_p_pine = self.p_pine.get()*122
        self.tp_p_fudge = self.p_fudge.get()*180
        self.tp_p_truffle = self.p_truffle.get()*212
        
        self.totprice_pastry = float(
                                        self.tp_p_choco +
                                        self.tp_p_red +
                                        self.tp_p_fresh +
                                        self.tp_p_pine +
                                        self.tp_p_fudge +
                                        self.tp_p_truffle
                                    )
        
        self.tot_pastry.set("Rs. "+str(self.totprice_pastry))
        self.tot_tax_pastry = round((self.totprice_pastry*0.05),2)
        self.tax_pastry.set("Rs. "+str(self.tot_tax_pastry))  
        
        self.Total_Bill = round(float(
                                    self.totprice_coffee + 
                                    self.tot_tax_coffee +
                                    self.totprice_tea + 
                                    self.tot_tax_tea +
                                    self.totprice_pastry + 
                                    self.tot_tax_pastry 
                                ),2)
        
        
    #====================== Function - Bill Area - Welcome Part ========================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        
        self.txtarea.insert(END,"***************************************")
        self.txtarea.insert(END,"\n\tWelcome to Cafe Horizon")
        self.txtarea.insert(END,"\n***************************************")
        
        self.txtarea.insert(END,f"\n\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.cust_name.get()}")
        self.txtarea.insert(END,f"\nCustomer Phone no. : {self.cust_phone.get()}")
        
        self.txtarea.insert(END,"\n\n***************************************")
        self.txtarea.insert(END,"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n***************************************")
       
        
    #=================== Function - Validating Phone number =================================
    def isValid(self,s): 
        # 1) First number starts with 7 or 8 or 9. 
        # 2) Then contains 9 digits 
        Pattern = re.compile("^[7-9][0-9]{9}$") 
        return Pattern.match(s)    
    
    
    #====================== Function - Bill Area - Generate Bill Button ========================   
    def bill_area(self):
        
        if self.cust_name.get()=="" or self.cust_phone.get()=="":
            messagebox.showerror("Error", "Please enter Customer details.")
        elif self.isValid(self.cust_phone.get()):
            if self.cust_name.get().replace(" ", "").isalpha()==False:
                messagebox.showerror("Error", "Please enter Name correctly. Name cannot contain numbers.")    
            elif self.tot_coffee.get()=="Rs. 0.0" and self.tot_tea.get()=="Rs. 0.0" and self.tot_pastry.get()=="Rs. 0.0":
                messagebox.showerror("Error", "No Products Purchased.")
            else:
                self.welcome_bill()
       
                #============================ Coffee ================================
                if self.c_expresso.get()!=0:
                    self.txtarea.insert(END, f"\nEspresso\t\t{self.c_expresso.get()}\t\t{self.tp_c_expresso}")
                if self.c_americano.get()!=0:
                    self.txtarea.insert(END, f"\nAmericano\t\t{self.c_americano.get()}\t\t{self.tp_c_americano}")
                if self.c_cap.get()!=0:
                    self.txtarea.insert(END, f"\nCappuccino\t\t{self.c_cap.get()}\t\t{self.tp_c_cap}")
                if self.c_cafel.get()!=0:
                    self.txtarea.insert(END, f"\nCafe Latte\t\t{self.c_cafel.get()}\t\t{self.tp_c_cafel}")
                if self.c_cafem.get()!=0:
                    self.txtarea.insert(END, f"\nCafe Mocha\t\t{self.c_cafem.get()}\t\t{self.tp_c_cafem}")
                if self.c_frappe.get()!=0:
                    self.txtarea.insert(END, f"\nFrappe\t\t{self.c_frappe.get()}\t\t{self.tp_c_frappe}")
                    
                #============================== Tea ======================================
                if self.t_green.get()!=0:
                    self.txtarea.insert(END, f"\nGreen Tea\t\t{self.t_green.get()}\t\t{self.tp_t_green}")
                if self.t_mint.get()!=0:
                    self.txtarea.insert(END, f"\nMint Tea\t\t{self.t_mint.get()}\t\t{self.tp_t_mint}")
                if self.t_venti.get()!=0:
                    self.txtarea.insert(END, f"\nVenti Tea\t\t{self.t_venti.get()}\t\t{self.tp_t_venti}")
                if self.t_barley.get()!=0:
                    self.txtarea.insert(END, f"\nBarley Tea\t\t{self.t_barley.get()}\t\t{self.tp_t_barley}")
                if self.t_lemon.get()!=0:
                    self.txtarea.insert(END, f"\nLemon Tea\t\t{self.t_lemon.get()}\t\t{self.tp_t_lemon}")
                if self.t_boba.get()!=0:
                    self.txtarea.insert(END, f"\nBoba Tea\t\t{self.t_boba.get()}\t\t{self.tp_t_boba}")
                
                #============================ Pastries =======================================
                if self.p_choco.get()!=0:
                    self.txtarea.insert(END, f"\nChocolate\t\t{self.p_choco.get()}\t\t{self.tp_p_choco}")
                if self.p_red.get()!=0:
                    self.txtarea.insert(END, f"\nRed Velvet\t\t{self.p_red.get()}\t\t{self.tp_p_red}")
                if self.p_fresh.get()!=0:
                    self.txtarea.insert(END, f"\nFresh Fruit\t\t{self.p_fresh.get()}\t\t{self.tp_p_fresh}")
                if self.p_pine.get()!=0:
                    self.txtarea.insert(END, f"\nPineapple\t\t{self.p_pine.get()}\t\t{self.tp_p_pine}")
                if self.p_fudge.get()!=0:
                    self.txtarea.insert(END, f"\nFudge\t\t{self.p_fudge.get()}\t\t{self.tp_p_fudge}")
                if self.p_truffle.get()!=0:
                    self.txtarea.insert(END, f"\nTruffle\t\t{self.p_truffle.get()}\t\t{self.tp_p_truffle}")
                            
                #======================= Total Price and Tax ====================================
                self.txtarea.insert(END,"\n\n=======================================")
                
                if self.tax_coffee.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\nTax on Coffee\t\t\t{self.tax_coffee.get()}")
                if self.tax_tea.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\nTax on Tea\t\t\t{self.tax_tea.get()}")
                if self.tax_pastry.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\nTax on Pastry\t\t\t{self.tax_pastry.get()}")
                
                self.txtarea.insert(END,"\n---------------------------------------")
                self.txtarea.insert(END,f"\nTotal Price\t\t\tRs. {self.Total_Bill}")
                self.txtarea.insert(END,"\n=======================================")
                self.save_bill()
                
        else:
            messagebox.showerror("Error", "Phone number is incorrect. Phone number should contain only 10 digits and start with 7,8 or 9.")
            
            
        
    #=========================== Function - Save Bill ======================================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill {self.bill_no.get()} has been saved successfully.")
        else:
            return
    
    #======================== Function - Search Bill ========================
    def find_bill(self):
        present = 0
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = 1
        if present==0:
            messagebox.showerror("Error", f"Invalid bill number. Bill with bill no. {self.search_bill.get()} not found.")
    
    
    #============================== Function - Clear Button =======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want clear all data?")
        if op>0:
            #=============== Coffee =====================
            self.c_expresso.set(0)
            self. c_americano.set(0)
            self.c_cap.set(0)
            self.c_cafel.set(0)
            self.c_cafem.set(0)
            self.c_frappe.set(0)
            #================= Tea =============================
            self.t_green.set(0)
            self.t_mint.set(0)
            self.t_venti.set(0)
            self.t_barley.set(0)
            self.t_lemon.set(0)
            self.t_boba.set(0)
            #==================== Pastries =======================
            self.p_choco.set(0)
            self.p_red.set(0)
            self.p_fresh.set(0)
            self.p_pine.set(0)
            self.p_fudge.set(0)
            self.p_truffle.set(0)
            #======================== Total Price & Tax ====================
            self.tot_coffee.set("")
            self.tot_tea.set("")
            self.tot_pastry.set("")
            self.tax_coffee.set("")
            self.tax_tea.set("")
            self.tax_pastry.set("")
            #=================== Customer ===================
            self.cust_name.set("")
            self.cust_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            
            self.welcome_bill()
        
        
    #===================== Function - Exit Button ==================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op>0:
            self.root.destroy()
        
    
root = Tk() #Tk class is used to create a root window.
obj = Bill_App(root) #Creating object of class Bill_App
root.mainloop() #mainloop() tells Python to run the Tkinter event loop