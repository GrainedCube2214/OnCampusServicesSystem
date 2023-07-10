"""
Notes for Teja:
-Fill in the function to refresh windows, change the arguments of the command from the string in it to the table dataframe
-Keep the table size big enough to hide the main frame
"""
import customtkinter as ctk

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

def refresh_table(tablename):
    pass

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

food_table_refresh = ctk.CTkButton(food, text="🔃", font=("Product Sans", 40), command = lambda: refresh_table("food_table"))
food_table_refresh.configure(width=75, height=75)
food_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#pharmacy
pharmalab = ctk.CTkLabel(pharmacy, text="💊 Pharmacy", font=("Product Sans", 64))
pharmalab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

pharma_to_home = ctk.CTkButton(pharmacy, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
pharma_to_home.configure(width=75, height=75)
pharma_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

pharma_table_refresh = ctk.CTkButton(pharmacy, text="🔃", font=("Product Sans", 40), command = lambda: refresh_table('pharma_table'))
pharma_table_refresh.configure(width=75, height=75)
pharma_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#gym
gymlab = ctk.CTkLabel(gym, text="🏋️   Gym", font=("Product Sans", 64))
gymlab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

gym_to_home = ctk.CTkButton(gym, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
gym_to_home.configure(width=75, height=75)
gym_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

gym_table_refresh = ctk.CTkButton(gym, text="🔃", font=("Product Sans", 40), command = lambda: refresh_table('gym_table'))
gym_table_refresh.configure(width=75, height=75)
gym_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

#printing
printlab = ctk.CTkLabel(printing, text="🖨️  Printing", font=("Product Sans", 64))
printlab.grid(row=0, column=0, padx=100, pady=25, sticky="NW" )

print_to_home = ctk.CTkButton(printing, text="🏠", font=("Product Sans", 40), command = lambda: goto(home))
print_to_home.configure(width=75, height=75)
print_to_home.grid(row=0, column=4, padx=50, pady=50, sticky="NE")

print_table_refresh = ctk.CTkButton(printing, text="🔃", font=("Product Sans", 40), command = lambda: refresh_table('print_table'))
print_table_refresh.configure(width=75, height=75)
print_table_refresh.grid(row=10, column=0, padx=50, pady=50, sticky="NSEW")

root.mainloop()