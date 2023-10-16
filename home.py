#imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#creates an empty dictionary for user info
user_data = {'first name': "", 
             'last name': "", 
             'username': "", 
             'password': ""}

#function for creating the gui homepage, which has the four different grids
def gui_home(login_username_entry):
  gui_window = Tk()
  gui_window.geometry("800x600")
  gui_window.title("GUI Home")

  #creates four different grids with different colors to tell them apart

  #top left grid
  top_left_grid = Frame(gui_window, bg="white", width=400, height=300)
  top_left_grid.grid(row=0, column=0, sticky="nsew")

  #top right grid
  top_right_grid = Frame(gui_window, width=400, height=300)
  top_right_grid.grid(row=0, column=1, sticky="nsew")

  #bottom left grid
  bottom_left_grid = Frame(gui_window, bg="red", width=400, height=300)
  bottom_left_grid.grid(row=1, column=0, sticky="nsew")

  #bottom right grid
  bottom_right_grid = Frame(gui_window, bg="black", width=400, height=300)
  bottom_right_grid.grid(row=1, column=1, sticky="nsew")



  #creates the left right, forward, backward, stop buttons for the robot and puts them into the control layout on the top left grid

  #left_button
  left_button = Button(top_right_grid, text="Left")
  left_button.grid(row=1, column=0)

  #right button
  right_button = Button(top_right_grid, text="Right")
  right_button.grid(row=1, column=2)

  #forward button
  forward_button = Button(top_right_grid, text="Forward")
  forward_button.grid(row=0, column=1)

  #backward button
  backward_button = Button(top_right_grid, text="Backward")
  backward_button.grid(row=2, column=1)

  #stop button
  stop_button = Button(top_right_grid, text="Stop")
  stop_button.grid(row=1, column=1)



  #labels the top left grid as the camera grid
  camera_label = Label(top_left_grid, text="Camera")
  camera_label.grid(row=3, column=3)

  #labels the log grid with a welcome username message
  log_welcome_label = Label(bottom_right_grid, text =f"Welcome {login_username_entry}")
  log_welcome_label.grid(row=3, column=3)

#creates login window
def login_window():
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("700x500")

    #login_label
    login_label = ttk.Label(login_window, text="Login")
    login_label.pack()

    #username
    login_username_entry_label = ttk.Label(login_window, text="Username:")
    login_username_entry_label.pack()
    login_username_entry = ttk.Entry(login_window, width=30)
    login_username_entry.pack()

    #password
    login_password_entry_label = ttk.Label(login_window, text="Password:")
    login_password_entry_label.pack()
    login_password_entry = ttk.Entry(login_window, width=30, show = '*')
    login_password_entry.pack()

    def logging_in():
        from sql_database import get_data
        username = login_username_entry.get()
        password = login_password_entry.get()
        key = get_data(username, password)
        # print(key)

        if key is not None and len(key) > 0:
          #logged in
            messagebox.showinfo("Logged In", "You successfully logged in.")
            gui_home(login_username_entry.get())
        else:
          messagebox.showerror("Error", "Invalid username or password.")

  #login button
    login_button = Button(login_window, text="Login", command = logging_in)
    login_button.pack()



#creates create account window
def create_account_window():
    create_account_window = Tk()
    create_account_window.title("Create Account")
    create_account_window.geometry("700x500")

    #create_account_label
    create_account_label = ttk.Label(create_account_window, text="Create Account")
    create_account_label.pack()

    #firstname
    firstname_entry_label = ttk.Label(create_account_window, text="First Name:")
    firstname_entry_label.pack()
    firstname_entry = ttk.Entry(create_account_window, width=30)
    firstname_entry.pack()

    #lastname
    lastname_entry_label = ttk.Label(create_account_window, text="Last Name:")
    lastname_entry_label.pack()
    lastname_entry = ttk.Entry(create_account_window, width=30)
    lastname_entry.pack()

    #username
    username_entry_label = ttk.Label(create_account_window, text="Username:")
    username_entry_label.pack()
    username_entry = ttk.Entry(create_account_window, width=30)
    username_entry.pack()

    #password
    password_entry_label = ttk.Label(create_account_window, text="Password:")
    password_entry_label.pack()
    password_entry = ttk.Entry(create_account_window, width=30)
    password_entry.pack()

    #create function that creates and saves the account in the create account window
    def created():
        from sql_database import save_credentials

        user_data['first name'] = firstname_entry.get()
        user_data['last name'] = lastname_entry.get()
        user_data['username'] = username_entry.get()
        user_data['password'] = password_entry.get()

        save_credentials()

        messagebox.showinfo("Success", f"Account created successfully!\nFirst Name: {firstname_entry.get()}\nLast Name: {lastname_entry.get()}\nUsername: {username_entry.get()}\nPassword: {password_entry.get()}")

    #create account button
    create_account_button = Button(create_account_window, text="Create Account", command = created)
    create_account_button.pack()



#creates menu window
def menu_window():
  root = Tk()
  root.geometry("700x500")
  root.title("Menu")

  #creates label and buttons
  home_label = Label(root, text= "Please login to an existing account or create a new one.")
  home_label.pack()

  login_button = Button(root, text="Login", command = login_window)
  login_button.pack()

  create_account_button = Button(root, text="Create Account", command = create_account_window)
  create_account_button.pack()

  exit_Button = Button(root, text ="Exit", command = root.destroy)
  exit_Button.pack()

  root.mainloop()