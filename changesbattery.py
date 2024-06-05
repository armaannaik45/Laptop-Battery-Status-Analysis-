import tkinter as tk #standard Python interface-GUI components banane ke liye 
from tkinter import ttk #widgets k enhance krne k liye (modern and consistent look) #ttk=Themed Tkinter
import psutil #battery status/info #Accessing system & process-related information.
from PIL import Image, ImageTk

#function to update battery information and visualization
def update_battery_info(): #function responsible- battery status update karne k liye & to display in GUI
    battery = psutil.sensors_battery() #battery status & assigns it to battery variable
    charge_percent = battery.percent #% & assigns it to c_p variable

 #laptop charging pe hai ya nahi check karega
    if battery.power_plugged: #examining the power_plugged attribute of the battery object.
        status_label.config(text="Charging")  #If the laptop is charging, this line updates a label widget called status_label to display "Charging."

        # Calculate the estimated time to full charge
        if battery.secsleft == -1: #check if the est time to full charge is not avlble
            estimated_time_label.config(text="Charging (Calculating...)")
        else:
            # Calculate remaining time to fully charge the battery #based on current charge percentage and charging rate
            charging_rate = battery.power_plugged  # Charging rate=percentage of charge added per minute.
            remaining_capacity = 100 - charge_percent  # Remaining capacity to charge from current percentage to 100%
            remaining_time_minutes = remaining_capacity / charging_rate  # Time in minutes 39/1min
            hours = int(remaining_time_minutes // 60) #Floor/ciel division 
            minutes = int(remaining_time_minutes % 60) #mod=remainder
            estimated_time_label.config(text=f"Time to Full: {hours} hours {minutes} minutes")
    else:
        status_label.config(text="Discharging") #If the laptop is not on charging, this line updates a label widget called status_label to display "Discharging." as already done ↑
        time_left = battery.secsleft / 60 # calculates the time left to fully discharge the battery convert it into minutes.

        # Convert time left from minutes to hours and minutes
        hours = int(time_left // 60) #Floor/ciel division 
        minutes = int(time_left % 60)  #mod=remainder
        estimated_time_label.config(text=f"Time Left: {hours} hours {minutes} minutes")

    charge_label.config(text=f"Charge: {charge_percent}%") #current charge % display karne ke liye

   #clear karne ke liye jo previous battery visualization the
    battery_canvas.delete("all")
    
    #draw the battery outline
    battery_canvas.create_rectangle(10, 10, 100, 40, outline="black", width=2) #top-left corner-x,y & bottom-right corner-x,y
    #calculate the width of the battery based on the charge percentage (remining)
    battery_width = (charge_percent / 100) * 80 # It is a proportion of the total width (80 pixels)
    #draw the filled battery based on charge percentage
    battery_canvas.create_rectangle(10, 10, 10 + battery_width, 40, fill="green", width=0)

def refresh_battery_info():
    update_battery_info()

#main window banane ke liye
window = tk.Tk()
window.title("Battery Status Monitor")
window.geometry("800x500")

image = Image.open("batterysm.png")
image = image.resize((800, 160))  
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack(pady=10)

#labels banaya battery information ke liye=label widget for displaying the battery status.
status_label = ttk.Label(window, text="", font=("JuliaMono", 16)) #status #referred-https://realpython.com/coding-font/
status_label.pack(pady=10)

charge_label = ttk.Label(window, text="", font=("JuliaMono", 16))  #charge percentage #referred-https://realpython.com/coding-font/
charge_label.pack(pady=5)

estimated_time_label = ttk.Label(window, text="", font=("Arial", 16)) #est. time
estimated_time_label.pack(pady=5)

#widget banaya battery visualization k liye as told by ma'am
battery_canvas = tk.Canvas(window, width=120, height=50)
battery_canvas.pack(pady=5)

# update battery info button
refresh_button = ttk.Button(window, text="Refresh", command=refresh_battery_info)
refresh_button.pack(pady=10)

#Update battery info. n' visualization
update_battery_info()

# #Automatic Update battery info./details n' visualization every 15 Sec. (60,000 milliseconds)
# window.after(1500, update_battery_info) #

#Starting GUI main loop
window.mainloop()