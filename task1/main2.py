import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
import os

class RegistrationForm:
    def __init__(me, form):
        me.form = form
        me.form.title("Registration Form")
        me.form.geometry('925x500+300+200')
        me.form.configure(bg='#fff')
        me.form.resizable(False, False)

        #image 
        image_path = "D:/internship/task1/form3.png"
        if os.path.exists(image_path):  # Ensure the image path exists
            me.image = Image.open(image_path)
            me.image = me.image.resize((240, 240), Image.LANCZOS)
            me.photo = ImageTk.PhotoImage(me.image)
            me.image_label = tk.Label(me.form, image=me.photo,border = 0)
            me.image_label.place(x=160, y=140)

        me.frame = Frame(me.form, width=350, height=390, bg='#fff')
        me.frame.place(x=480, y=50)

        me.heading = Label(me.frame, text='Registration Form', fg='#57a1f8', bg='white',
                             font=('Microsoft Yahei UI Light', 16, 'bold'))
        me.heading.place(x=83, y=5)

        me.user = EntryWithPlaceholder(me.frame, 'Full Name')
        me.user.place(x=40, y=80)

        me.id = EntryWithPlaceholder(me.frame, 'AICTE ID')
        me.id.place(x=40, y=130)

        me.email = EntryWithPlaceholder(me.frame, 'Email')
        me.email.place(x=40, y=180)

        me.phone = EntryWithPlaceholder(me.frame, 'Phone No.')
        me.phone.place(x=40, y=230)

        me.college = EntryWithPlaceholder(me.frame, 'College Name')
        me.college.place(x=40, y=281)

        me.signup_button = Button(me.frame, width=33, pady=7, text='Sign up', bg='#6c63ff', fg='white',
                                    border=0, cursor='hand2', command=me.validate_data)
        me.signup_button.place(x=55, y=330)

        me.signin_label = Label(me.frame, text='have an account?', fg='black', bg='white',
                                  font=('Microsoft Yahei UI Light', 9))
        me.signin_label.place(x=90, y=370)

        me.signin_button = Button(me.frame, width=6, text='Sign In', border=0, bg='white',
                                    cursor='hand2', fg='#6c63ff')
        me.signin_button.place(x=200, y=370)

    def validate_data(me):
        name = me.user.get()
        aicte_id = me.id.get()
        email = me.email.get()
        phone = me.phone.get()
        college = me.college.get()

        filled_fields = [field.strip() for field in [name, aicte_id, email, phone, college]]

   
        if all(filled_fields):
            me.generate_pdf(name, aicte_id, email, phone, college)
            messagebox.showinfo("Success", "PDF generated successfully")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def generate_pdf(me, name, aicte_id, email, phone, college):
        pdf_name = f"{name}_Registration.pdf"
        c = canvas.Canvas(pdf_name, pagesize=letter)
        c.drawString(100, 750, "Name: " + name)
        c.drawString(100, 730, "AICTE ID: " + aicte_id)
        c.drawString(100, 710, "Email: " + email)
        c.drawString(100, 690, "Phone: " + phone)
        c.drawString(100, 670, "College: " + college)
        c.save()

class EntryWithPlaceholder(Entry):
    def __init__(me, form=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(form,borderwidth = 0)

        me.placeholder = placeholder
        me.placeholder_color = color
        me.default_fg_color = me['fg']

        me.bind("<FocusIn>", me.focus_in)
        me.bind("<FocusOut>", me.focus_out)

        me.put_placeholder()

    def put_placeholder(me):
        me.insert(0, me.placeholder)
        me['fg'] = me.placeholder_color

    def focus_in(me, _):
        if me['fg'] == me.placeholder_color:
            me.delete('0', 'end')
            me['fg'] = me.default_fg_color

    def focus_out(me, _):
        if not me.get():
            me.put_placeholder()
    
def main():
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
