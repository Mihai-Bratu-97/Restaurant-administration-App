from tkinter import*
from tkinter import messagebox
import re
from animating_menu_images import animating_images
from store_administration import start_second_window
from time import strftime

main_window = Tk()

# THE RIGHT FRAME WHEN THE LEFT IS CALLED
image_frame = Frame(width=490, height=550)

# CALLING THE FUNCTION TO START ANIMATING THE IMAGES
animating_images(image_frame)

# MIDDLE FRAME
middle_frame = Frame(height=550, width=20, bg="#aee665")
middle_frame.place(x=490, y=50)

# GO TO LOGIN BUTTON
def to_login_btn_color1(e):
    to_login_btn.config(bg="#95a4ed")

def to_login_btn_color2(e):
    to_login_btn.config(bg="#778bf2")

to_login_btn = Button(text="Login for ordering", font=("Times New Roman", 15, "bold"), relief="groove", bg="#778bf2", activebackground="#95a4ed", takefocus=0,
                      command=lambda: start_left_frame_animation())
to_login_btn.place(x=100, y=150)
to_login_btn.bind("<Enter>", to_login_btn_color1)
to_login_btn.bind("<Leave>", to_login_btn_color2)

    # LEFT FRAME
new_width = 20
new_x = 490
def start_left_frame_animation():
    global new_width, new_x
    if new_x > 0:
        new_x -= 5
        new_width += 5
        left_frame.config(width=new_width)
        left_frame.place(x=new_x)
    if new_x == 0:
        no_login_btn.place_forget()
        email_entry.focus_set()
        image_frame.place(x=510, y=50)
        return 0
    left_frame.after(3, start_left_frame_animation)

def reverse_left_frame_animation():
    global new_width, new_x
    if new_x < 490:
        new_x += 5
        new_width -= 5
        left_frame.config(width=new_width)
        left_frame.place(x=new_x)
    if new_x == 490:
        no_login_btn.place(x=700, y=150)
        image_frame.place_forget()
        return 0
    left_frame.after(3, reverse_left_frame_animation)

left_frame = Frame(height=550, width=0, bg="#aee665")
left_frame.place(x=490, y=50)

        # THE LEFT FRAME BUT LONGER
new_x1 = 0
def start_left_side_middle_frame_animation():
    global new_x1
    if new_x1 > - 500:
        new_x1 -= 5
        left_side_middle_frame.place(x=new_x1)
    if new_x1 == -500:
        email1_entry.focus_set()
        return 0
    left_side_middle_frame.after(3, start_left_side_middle_frame_animation)

def reverse_left_side_middle_frame_animation():
    global new_x1
    if new_x1 < 0:
        new_x1 += 5
        left_side_middle_frame.place(x=new_x1)
    if new_x1 == 0:
        email_entry.focus_set()
        return 0
    left_side_middle_frame.after(3, reverse_left_side_middle_frame_animation)

left_side_middle_frame = Frame(left_frame, height=400, width=1000, bg="#aee665")
left_side_middle_frame.place(x=0, y=0)

        # THE WIDGETS OF THE LEFT FRAME
            # LOGIN
                # EMAIL
def email_entry_focusin(e):
    if email_entry.get() == "Email here...":
        email_entry.delete(0, "end")
        email_entry.config(fg="black")

def email_entry_focusout(e):
    if len(email_entry.get()) == 0:
        email_entry.insert(0, "Email here...")
        email_entry.config(fg="gray")

email_entry = Entry(left_side_middle_frame, width=20, font=("Times New Roman", 14, "bold"), fg="gray", relief="solid", highlightcolor="#f5a85f", highlightbackground="#37bbf0", 
                    highlightthickness=2, bd=0)
email_entry.place(x=100, y=113)
email_entry.insert(0, "Email here...")
email_entry.focus_set()
email_entry.bind("<FocusIn>", email_entry_focusin)
email_entry.bind("<FocusOut>", email_entry_focusout)

                    # EMAIL IMAGE ICON
email_img = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\email_icon.gif")
email_label_image = Label(left_side_middle_frame, image=email_img, bd=0)
email_label_image.place(x=60, y=111)

                # PASSWORD
def password_entry_focusin(e):
    if password_entry.get() == "Password here...":
        password_entry.delete(0, "end")
        password_entry.config(fg="black", show="*")

def password_entry_focusout(e):
    if len(password_entry.get()) == 0:
        password_entry.insert(0, "Password here...")
        password_entry.config(fg="gray", show="")
        show_hide_password_btn.config(image=hide_password_image_color1, command=lambda: show_password())
        show_hide_password_btn.bind("<Enter>", hide_password_btn_color2)
        show_hide_password_btn.bind("<Leave>", hide_password_btn_color1)

def check_password_for_showing_hide_show_btn(input_password):
    if len(input_password) > 0 and input_password != "Password here...":
        show_hide_password_btn.place(x=320, y=166)
    else:
        show_hide_password_btn.place_forget()
    return True


password_entry = Entry(left_side_middle_frame, width=20, font=("Times New Roman", 14, "bold"), fg="gray", relief="solid", highlightcolor="#f5a85f", 
                       highlightbackground="#37bbf0", highlightthickness=2, bd=0)
password_entry.place(x=100, y=163)
password_entry.insert(0, "Password here...")
password_entry.bind("<FocusIn>", password_entry_focusin)
password_entry.bind("<FocusOut>", password_entry_focusout)
password_entry_reg = main_window.register(check_password_for_showing_hide_show_btn)
password_entry.config(validate="key", validatecommand=(password_entry_reg, "%P"))

                    # PASSWORD IMAGE ICON
password_img = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\password_icon.gif")
password_label_image = Label(left_side_middle_frame, image=password_img, bd=0)
password_label_image.place(x=60, y=163)

                    # SHOW AND HIDE PASSWORD BUTTON
def show_password_btn_color2(e):
    show_hide_password_btn.config(image=show_password_image_color2)

def show_password_btn_color1(e):
    show_hide_password_btn.config(image=show_password_image_color1)

def hide_password_btn_color2(e):
    show_hide_password_btn.config(image=hide_password_image_color2)

def hide_password_btn_color1(e):
    show_hide_password_btn.config(image=hide_password_image_color1)

def show_password():
    show_hide_password_btn.config(image=show_password_image_color2, command=lambda: hide_password())
    password_entry.config(show="")
    show_hide_password_btn.bind("<Enter>", show_password_btn_color2)
    show_hide_password_btn.bind("<Leave>", show_password_btn_color1)

def hide_password():
    show_hide_password_btn.config(image=hide_password_image_color2, command=lambda: show_password())
    password_entry.config(show="*")
    show_hide_password_btn.bind("<Enter>", hide_password_btn_color2)
    show_hide_password_btn.bind("<Leave>", hide_password_btn_color1)

hide_password_image_color1 = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\hide_password_icon.gif")
show_password_image_color1 = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\show_password_icon.gif")
hide_password_image_color2 = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\hide_password_icon_color2.gif")
show_password_image_color2 = PhotoImage(file="C:\\Users\\bratu\\.vscode\\images\\email_and_password\\show_password_icon_color2.gif")
show_hide_password_btn = Button(left_side_middle_frame, image=hide_password_image_color1, activebackground="#aee665", relief="flat", bd=0, highlightthickness=0, takefocus=0,
                                command=lambda: show_password())
show_hide_password_btn.bind("<Enter>", hide_password_btn_color2)
show_hide_password_btn.bind("<Leave>", hide_password_btn_color1)

                # BACK BUTTON
def back_btn_color1(e):
    back_btn.config(bg="#95a4ed")

def back_btn_color2(e):
    back_btn.config(bg="#778bf2")

back_btn = Button(left_side_middle_frame, font=("Times New Roman", 13, "bold"), text="Back", relief="flat", bg="#778bf2", activebackground="#95a4ed", takefocus=0,
                  command=lambda: reverse_left_frame_animation())
back_btn.place(x=50, y=230)
back_btn.bind("<Enter>", back_btn_color1)
back_btn.bind("<Leave>", back_btn_color2)

                # CREATE ACCOUNT BUTTON
def create_acc_btn_color1(e):
    create_acc_btn.config(bg="#95a4ed")

def create_acc_btn_color2(e):
    create_acc_btn.config(bg="#778bf2")

create_acc_btn = Button(left_side_middle_frame, font=("Times New Roman", 10, "bold"), text="No account?\nCreate one!", relief="flat", bg="#778bf2", activebackground="#95a4ed", 
                        takefocus=0, command=lambda: start_left_side_middle_frame_animation())
create_acc_btn.place(x=240, y=227)
create_acc_btn.bind("<Enter>", create_acc_btn_color1)
create_acc_btn.bind("<Leave>", create_acc_btn_color2)

            # CREATE ACCOUNT
                # EMAIL1
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check_email1(email):
	if(re.fullmatch(regex, email)):
		return True
	else:
		return False

def email1_entry_focusin(e):
    if email1_entry.get() == "Email here...":
        email1_entry.delete(0, "end")
        email1_entry.config(fg="black")

def email1_entry_focusout(e):
    if len(email1_entry.get()) == 0:
        email1_entry.insert(0, "Email here...")
        email1_entry.config(fg="gray")

email1_entry = Entry(left_side_middle_frame, width=20, font=("Times New Roman", 14, "bold"), fg="gray", relief="solid", highlightcolor="#f5a85f", highlightbackground="#37bbf0", 
                     highlightthickness=2, bd=0)
email1_entry.place(x=600, y=113)
email1_entry.insert(0, "Email here...")
email1_entry.focus_set()
email1_entry.bind("<FocusIn>", email1_entry_focusin)
email1_entry.bind("<FocusOut>", email1_entry_focusout)

                    # EMAIL1 IMAGE ICON
email1_label_image = Label(left_side_middle_frame, image=email_img, bd=0)
email1_label_image.place(x=557, y=111)

                # PASSWORD1
def password1_entry_focusin(e):
    if password1_entry.get() == "Password here...":
        password1_entry.delete(0, "end")
        password1_entry.config(fg="black", show="*")

def password1_entry_focusout(e):
    if len(password1_entry.get()) == 0:
        password1_entry.insert(0, "Password here...")
        password1_entry.config(fg="gray", show="")
        show_hide_password1_btn.config(image=hide_password_image_color1, command=lambda: show_password1())
        show_hide_password1_btn.bind("<Enter>", hide_password1_btn_color2)
        show_hide_password1_btn.bind("<Leave>", hide_password1_btn_color1)

def check_password1_for_showing_hide_show_btn(input_password1):
    if len(input_password1) > 0 and input_password1 != "Password here...":
        show_hide_password1_btn.place(x=820, y=166)
    else:
        show_hide_password1_btn.place_forget()
    return True


password1_entry = Entry(left_side_middle_frame, width=20, font=("Times New Roman", 14, "bold"), fg="gray", relief="solid", highlightcolor="#f5a85f", 
                        highlightbackground="#37bbf0", highlightthickness=2, bd=0)
password1_entry.place(x=600, y=163)
password1_entry.insert(0, "Password here...")
password1_entry.bind("<FocusIn>", password1_entry_focusin)
password1_entry.bind("<FocusOut>", password1_entry_focusout)
password1_entry_reg = main_window.register(check_password1_for_showing_hide_show_btn)
password1_entry.config(validate="key", validatecommand=(password1_entry_reg, "%P"))

                    # PASSWORD1 IMAGE ICON
password1_label_image = Label(left_side_middle_frame, image=password_img, bd=0)
password1_label_image.place(x=557, y=163)

                    # SHOW AND HIDE PASSWORD1 BUTTON
def show_password1_btn_color2(e):
    show_hide_password1_btn.config(image=show_password_image_color2)

def show_password1_btn_color1(e):
    show_hide_password1_btn.config(image=show_password_image_color1)

def hide_password1_btn_color2(e):
    show_hide_password1_btn.config(image=hide_password_image_color2)

def hide_password1_btn_color1(e):
    show_hide_password1_btn.config(image=hide_password_image_color1)

def show_password1():
    show_hide_password1_btn.config(image=show_password_image_color2, command=lambda: hide_password1())
    password1_entry.config(show="")
    show_hide_password1_btn.bind("<Enter>", show_password1_btn_color2)
    show_hide_password1_btn.bind("<Leave>", show_password1_btn_color1)

def hide_password1():
    show_hide_password1_btn.config(image=hide_password_image_color2, command=lambda: show_password1())
    password1_entry.config(show="*")
    show_hide_password1_btn.bind("<Enter>", hide_password1_btn_color2)
    show_hide_password1_btn.bind("<Leave>", hide_password1_btn_color1)

show_hide_password1_btn = Button(left_side_middle_frame, image=hide_password_image_color1, activebackground="#aee665", relief="flat", bd=0, highlightthickness=0, takefocus=0,
                                 command=lambda: show_password1())
show_hide_password1_btn.bind("<Enter>", hide_password1_btn_color2)
show_hide_password1_btn.bind("<Leave>", hide_password1_btn_color1)

                # RETYPE PASSWORD
def retype_password_entry_focusin(e):
    if retype_password_entry.get() == "Password again here...":
        retype_password_entry.delete(0, "end")
        retype_password_entry.config(fg="black", show="*")

def retype_password_entry_focusout(e):
    if len(retype_password_entry.get()) == 0:
        retype_password_entry.insert(0, "Password again here...")
        retype_password_entry.config(fg="gray", show="")
        show_hide_retype_password_btn.config(image=hide_password_image_color1, command=lambda: show_retype_password())
        show_hide_retype_password_btn.bind("<Enter>", hide_retype_password_btn_color2)
        show_hide_retype_password_btn.bind("<Leave>", hide_retype_password_btn_color1)

def check_retype_password_for_showing_hide_show_btn(input_retype_password):
    if len(input_retype_password) > 0 and input_retype_password != "Password again here...":
        show_hide_retype_password_btn.place(x=820, y=216)
    else:
        show_hide_retype_password_btn.place_forget()
    return True


retype_password_entry = Entry(left_side_middle_frame, width=20, font=("Times New Roman", 14, "bold"), fg="gray", relief="solid", highlightcolor="#f5a85f", 
                              highlightbackground="#37bbf0", highlightthickness=2, bd=0)
retype_password_entry.place(x=600, y=213)
retype_password_entry.insert(0, "Password again here...")
retype_password_entry.bind("<FocusIn>", retype_password_entry_focusin)
retype_password_entry.bind("<FocusOut>", retype_password_entry_focusout)
retype_password_entry_reg = main_window.register(check_retype_password_for_showing_hide_show_btn)
retype_password_entry.config(validate="key", validatecommand=(retype_password_entry_reg, "%P"))

                    # RETYPE PASSWORD IMAGE ICON
retype_password_label_image = Label(left_side_middle_frame, image=password_img, bd=0)
retype_password_label_image.place(x=557, y=213)

                    # SHOW AND HIDE RETYPE PASSWORD BUTTON
def show_retype_password_btn_color2(e):
    show_hide_retype_password_btn.config(image=show_password_image_color2)

def show_retype_password_btn_color1(e):
    show_hide_retype_password_btn.config(image=show_password_image_color1)

def hide_retype_password_btn_color2(e):
    show_hide_retype_password_btn.config(image=hide_password_image_color2)

def hide_retype_password_btn_color1(e):
    show_hide_retype_password_btn.config(image=hide_password_image_color1)

def show_retype_password():
    show_hide_retype_password_btn.config(image=show_password_image_color2, command=lambda: hide_retype_password())
    retype_password_entry.config(show="")
    show_hide_retype_password_btn.bind("<Enter>", show_retype_password_btn_color2)
    show_hide_retype_password_btn.bind("<Leave>", show_retype_password_btn_color1)

def hide_retype_password():
    show_hide_retype_password_btn.config(image=hide_password_image_color2, command=lambda: show_retype_password())
    retype_password_entry.config(show="*")
    show_hide_retype_password_btn.bind("<Enter>", hide_retype_password_btn_color2)
    show_hide_retype_password_btn.bind("<Leave>", hide_retype_password_btn_color1)

show_hide_retype_password_btn = Button(left_side_middle_frame, image=hide_password_image_color1, activebackground="#aee665", relief="flat", bd=0, highlightthickness=0, takefocus=0,
                                       command=lambda: show_retype_password())
show_hide_retype_password_btn.bind("<Enter>", hide_retype_password_btn_color2)
show_hide_retype_password_btn.bind("<Leave>", hide_retype_password_btn_color1)

                # BACK BUTTON1
def back1_btn_color1(e):
    back1_btn.config(bg="#95a4ed")

def back1_btn_color2(e):
    back1_btn.config(bg="#778bf2")

back1_btn = Button(left_side_middle_frame, font=("Times New Roman", 13, "bold"), text="Back", relief="flat", bg="#778bf2", activebackground="#95a4ed", takefocus=0,
                   command=lambda: reverse_left_side_middle_frame_animation())
back1_btn.place(x=550, y=290)
back1_btn.bind("<Enter>", back1_btn_color1)
back1_btn.bind("<Leave>", back1_btn_color2)

                # CONFIRM CREATE ACCOUNT BUTTON
def create_acc1_btn_color1(e):
    create_acc1_btn.config(bg="#95a4ed")

def create_acc1_btn_color2(e):
    create_acc1_btn.config(bg="#778bf2")

def account_verification():
    email1 = check_email1(email1_entry.get())
    password1 = check_password1()
    if len(email1_entry.get()) == 0 or len(password1_entry.get()) == 0 or len(retype_password_entry.get()) == 0:
        messagebox.showinfo("Invalid information", "It seems some fields are not completed! Try again!")
    elif email1 == False:
        messagebox.showinfo("Invalid email", "Your email isn't a valid one!")
    elif password1 == False:
        messagebox.showinfo("Invalid password", "Your password doesn't meet the minimum requirements!")
    elif password1_entry.get() != retype_password_entry.get():
        messagebox.showinfo("Invalid passwords", "Your passwords don't match!")

create_acc1_btn = Button(left_side_middle_frame, font=("Times New Roman", 13, "bold"), text="Create account", relief="flat", bg="#778bf2", activebackground="#95a4ed", takefocus=0,
                         command=lambda: account_verification())
create_acc1_btn.place(x=690, y=290)
create_acc1_btn.bind("<Enter>", create_acc1_btn_color1)
create_acc1_btn.bind("<Leave>", create_acc1_btn_color2)

# TOP FRAME
top_frame = Frame(width=1000, height=40, bg="#59d496")
top_frame.place(x=0, y=10)

# TITLE
title_label = Label(text="Voiniceii Restaurant", font=("Times New Roman", 18, "bold"), bg="#59d496")
title_label.place(x=405, y=14)

# WITHOUT LOGIN
def no_login_color1(e):
    no_login_btn.config(bg="#95a4ed")

def no_login_color2(e):
    no_login_btn.config(bg="#778bf2")

no_login_btn = Button(text="Order without login", font=("Times New Roman", 15, "bold"), relief="groove", bg="#778bf2", activebackground="#95a4ed",
                      command=lambda: close_first_window())
no_login_btn.place(x=700, y=150)
no_login_btn.bind("<Enter>", no_login_color1)
no_login_btn.bind("<Leave>", no_login_color2)

# CLOCK
clock_widget_cancel = None
def clock():
    global clock_widget_cancel
    string = strftime('%H:%M:%S %p')
    clock_label.config(text = string)
    clock_widget_cancel = main_window.after(1000, clock)

clock_label = Label(font=("ds-digital", 21), bg="#f5bc42", fg="white", width=10)
clock_label.place(x=100, y=13)

# RIGHT FRAME
def close_first_window():
    animating_images(image_frame)
    main_window.after_cancel(clock_widget_cancel)
    main_window.destroy()
    start_second_window()

clock()

main_window.title("Voiniceii main window")
main_window.geometry("1000x600")
main_window.resizable(False, False)
main_window.mainloop()