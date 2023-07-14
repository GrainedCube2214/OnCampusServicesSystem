import customtkinter as ctk
import pandas as pd
from pandastable import Table
import pymysql

# Connect to the MySQL database
conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='DBMS'
    )
class CustomTable(Table):
    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        self.bind("<KeyPress>", self.handle_arrow_keys)

    def handle_arrow_keys(self, event):
        key = event.keysym
        if key == "Up":
            self.moveRow(-1)
        elif key == "Down":
            self.moveRow(1)
        elif key == "Left":
            self.moveCol(-1)
        elif key == "Right":
            self.moveCol(1)

root = ctk.CTk()
root.title("On Campus Service System")
root.geometry('1280x720')

#Frames
home = ctk.CTkFrame(root)
food = ctk.CTkFrame(root)
pharmacy = ctk.CTkFrame(root)
gym = ctk.CTkFrame(root)
printing = ctk.CTkFrame(root)

frames = [home, food,  pharmacy, gym, printing]
for frame in frames:
    frame.configure(width=1280, height=720)
    frame.place(relx=0.5, rely=0.5, anchor="center")

#Functions
def goto(frame):
    frame.lift()
    frame.configure(width=1280, height=720)

def pharmacy_function():

    app = ctk.CTk()
    app.title("Pharmacy")
    app.geometry("800x400")

    command = "SELECT pharmacy.P_ID, pharmacy.Name, pharmacy.Location, medicine.M_ID, medicine.Price, medicine.Formula " \
              "FROM pharmacy CROSS JOIN medicine order by pharmacy.P_ID"

    # Create a frame to hold the table
    table_frame = ctk.CTkFrame(app)
    table_frame.grid(row=0, column=0, sticky='nswe', padx=50, pady=10)

    # Execute the query and fetch the data into a pandas DataFrame
    with conn.cursor() as cursor:
        cursor.execute(command)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=['P_ID', 'Pharmacy Name', 'Location', 'M_ID', 'Price', 'Formula'])

    # Create a CustomTable instance and show the data
    pt = CustomTable(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False, showindex=False,width=680)
    pt.show()
    app.mainloop()

def gym_function():
    app = ctk.CTk()
    app.title("Gym")
    app.geometry("600x400")

    command = "SELECT * FROM gym order by G_ID"

    # Create a frame to hold the table
    table_frame = ctk.CTkFrame(app)
    table_frame.grid(row=0, column=0, sticky='nswe', padx=20, pady=20)

    # Execute the query and fetch the data into a pandas DataFrame
    with conn.cursor() as cursor:
        cursor.execute(command)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=['G_ID','Capacity','Location','Equipment'])

    # Create a CustomTable instance and show the data
    pt = CustomTable(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False, showindex=False,width=500)
    pt.show()

    app.mainloop()

def print_function():
    app = ctk.CTk()
    app.title("Printing")
    app.geometry("1000x400")

    header = ctk.CTkLabel(app, text="Print Shop", fg_color="transparent", font=("Product Sans", 20))
    header.grid(row=0, column=0, sticky="nswe")

    header = ctk.CTkLabel(app, text="Print Outs", fg_color="transparent", font=("Product Sans", 20))
    header.grid(row=0, column=1, sticky="nswe")

    command1 = "SELECT * FROM printshop order by S_ID"
    command2 = "SELECT * FROM printouts order by Order_ID"

    # Create a frame to hold the tables
    table_frame1 = ctk.CTkFrame(app)
    table_frame1.grid(row=1, column=0, sticky='nswe', padx=20, pady=20)

    table_frame2 = ctk.CTkFrame(app)
    table_frame2.grid(row=1, column=1, sticky='nswe', padx=20, pady=20)

    # Execute the queries and fetch the data into pandas DataFrames
    with conn.cursor() as cursor:
        cursor.execute(command1)
        data1 = cursor.fetchall()
        df1 = pd.DataFrame(data1, columns=['S_ID', 'Name', 'Location'])

        cursor.execute(command2)
        data2 = cursor.fetchall()
        df2 = pd.DataFrame(data2, columns=['Order_ID', 'Type', 'Price'])

    # Create CustomTable instances and show the data
    pt1 = CustomTable(table_frame1, dataframe=df1, showtoolbar=False, showstatusbar=False, showindex=False, width=400)
    pt1.show()

    pt2 = CustomTable(table_frame2, dataframe=df2, showtoolbar=False, showstatusbar=False, showindex=False, width=400)
    pt2.show()

    app.mainloop()

def food_function():
    app = ctk.CTk()
    app.title("Food")
    app.geometry("850x400")

    header = ctk.CTkLabel(app, text="Food Menu", fg_color="transparent", font=("Product Sans", 20))
    header.grid(row=0, column=0, sticky="nswe")

    header = ctk.CTkLabel(app, text="Food Items", fg_color="transparent", font=("Product Sans", 20))
    header.grid(row=0, column=1, sticky="nswe")

    command1 = "SELECT * FROM foodmenu order by Menu_ID"
    command2 = "SELECT * FROM fooditems order by F_ID"

    # Create a frame to hold the tables
    table_frame1 = ctk.CTkFrame(app)
    table_frame1.grid(row=1, column=0, sticky='nswe', padx=20, pady=20)

    table_frame2 = ctk.CTkFrame(app)
    table_frame2.grid(row=1, column=1, sticky='nswe', padx=20, pady=20)

    # Execute the queries and fetch the data into pandas DataFrames
    with conn.cursor() as cursor:
        cursor.execute(command1)
        data1 = cursor.fetchall()
        df1 = pd.DataFrame(data1, columns=['Menu_ID', 'Cuisine'])

        cursor.execute(command2)
        data2 = cursor.fetchall()
        df2 = pd.DataFrame(data2, columns=['F_ID', 'Name', 'Price'])

    # Create CustomTable instances and show the data
    pt1 = CustomTable(table_frame1, dataframe=df1, showtoolbar=False, showstatusbar=False, showindex=False, width=300)
    pt1.show()

    pt2 = CustomTable(table_frame2, dataframe=df2, showtoolbar=False, showstatusbar=False, showindex=False, width=400)
    pt2.show()

    app.mainloop()

home.lift()

#home
homelab = ctk.CTkLabel(home, text="🏠   Home", font=("Product Sans", 64))
homelab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

food_button = ctk.CTkButton(home, text="Food    🍽️", font=("Product Sans", 40), command = lambda: goto(food))
food_button.configure(width=450, height=125)
food_button.grid(row=1, column=0, padx=25, pady=50, sticky="NSEW")

pharmacy_button = ctk.CTkButton(home, text="Pharmacy 💊", font=("Product Sans", 40), command = lambda: goto(pharmacy))
pharmacy_button.configure(width=450, height=125)
pharmacy_button.grid(row=1, column=1, padx=100, pady=50, sticky="NSEW")

gym_button = ctk.CTkButton(home, text="Gym  🏋️", font=("Product Sans", 40), command = lambda: goto(gym))
gym_button.configure(width=450, height=125)
gym_button.grid(row=2, column=0, padx=25, pady=50, sticky="NSEW")

printing_button = ctk.CTkButton(home, text="Printing    🖨️", font=("Product Sans", 40), command = lambda: goto(printing))
printing_button.configure(width=450, height=125)
printing_button.grid(row=2, column=1, padx=100, pady=50, sticky="NSEW")

#food
foodlab = ctk.CTkLabel(food, text="Food Menu", font=("Product Sans", 64))
foodlab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

food_to_home = ctk.CTkButton(food, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
food_to_home.configure(width=75, height=75)
food_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

food_table_refresh = ctk.CTkButton(food, text="🔃", font=("Product Sans", 40), command = lambda: food_function())
food_table_refresh.configure(width=75, height=75)
food_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#pharmacy
pharmalab = ctk.CTkLabel(pharmacy, text="💊 Pharmacy", font=("Product Sans", 64))
pharmalab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

pharma_to_home = ctk.CTkButton(pharmacy, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
pharma_to_home.configure(width=75, height=75)
pharma_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

pharma_table_refresh = ctk.CTkButton(pharmacy, text="🔃", font=("Product Sans", 40), command = lambda: pharmacy_function())
pharma_table_refresh.configure(width=75, height=75)
pharma_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#gym
gymlab = ctk.CTkLabel(gym, text="🏋️   Gym", font=("Product Sans", 64))
gymlab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

gym_to_home = ctk.CTkButton(gym, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
gym_to_home.configure(width=75, height=75)
gym_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

gym_table_refresh = ctk.CTkButton(gym, text="🔃", font=("Product Sans", 40), command = lambda: gym_function())
gym_table_refresh.configure(width=75, height=75)
gym_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#printing
printlab = ctk.CTkLabel(printing, text="🖨️  Printing", font=("Product Sans", 64))
printlab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

print_to_home = ctk.CTkButton(printing, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
print_to_home.configure(width=75, height=75)
print_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

print_table_refresh = ctk.CTkButton(printing, text="🔃", font=("Product Sans", 40), command = lambda: print_function())
print_table_refresh.configure(width=75, height=75)
print_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

root.mainloop()