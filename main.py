import tkinter as tk
from tkinter import ttk
import tkinter.messagebox 
from PIL import ImageTk, Image
import os

root = tk.Tk()

root.title("Chemical Calculator")
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

pool_type_list = ["Plaster", "Vinyl", "Fiberglass"]
 
frame = ttk.Frame(root)
frame.pack(padx=20, pady=10)

img = ImageTk.PhotoImage(Image.open("test-strip-chart.jpg"))
panel = ttk.Label(frame, image = img)
panel.pack(side="right", fill="both", padx=10, pady=10, expand=True)

widgets_frame = ttk.LabelFrame(frame, text="User Input")
widgets_frame.pack(side="left", fill="both", expand=True)

results_frame = ttk.LabelFrame(frame, text="Results")
results_frame.pack(side="left", fill="both",padx=10, pady=10, expand=True)

def remove_result_frame():
        for labels in results_frame.winfo_children():
            labels.destroy()

def calculate():
    try:
        try:
            pool_size = int(size_entry.get())
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Pool Size")
        try:
            pool_type_input = type_combobox.get()
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Pool Type")

        row_counter = 0
        point = '\u2022'

        #pH Level
        try:
            ph = float(ph_entry.get())
            amount_phup = 0
            amount_phdown = 0
            ph_result = None
            if ph >= 8.4 and ph < 20:
                amount_phdown = 2.4 * (pool_size / 1000)
                row_counter = row_counter + 1
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phdown, 2)) + " oz of pH Down")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph >= 8.3:
                row_counter = row_counter + 1
                amount_phdown = 2 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phdown, 2)) + " oz of pH Down")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph >= 8:
                row_counter = row_counter + 1
                amount_phdown = 1.2 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phdown, 2)) + " oz of pH Down")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph >= 7.8:
                row_counter = row_counter + 1
                amount_phdown = 0.6 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phdown, 2)) + " oz of pH Down")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph >= 7.6:
                pass
            elif ph >= 7.1:
                row_counter = row_counter + 1
                amount_phup = 1.2 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phup, 2)) + " oz of pH Up")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph >= 6.7:
                row_counter = row_counter + 1
                amount_phup = 1.6 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phup, 2)) + " oz of pH Up")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph <= 6.5:
                row_counter = row_counter + 1
                amount_phup = 2 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phup, 2)) + " oz of pH Up")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            elif ph == 0:
                row_counter = row_counter + 1
                amount_phup = 2 * (pool_size / 1000)
                ph_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_phup, 2)) + " oz of pH Up")
                ph_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            else:
                tkinter.messagebox.showinfo("Error",  "Invalid pH Input")
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid pH Entry")

        # Calcium Hardness Increaser
        try:
            hardness = float(hardness_entry.get())
            if hardness <= 200:
                ppm_diff = 200 - hardness
                amount_of_CHIncreaser = (ppm_diff / 10) * (1.6 * (pool_size / 1000))
                conv_to_lbs = amount_of_CHIncreaser / 16
                row_counter = row_counter + 1
                hardness_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_of_CHIncreaser, 2)) + " oz or " + str(round(conv_to_lbs, 2)) + " lbs of Calcium Hardness Increaser")
                hardness_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            else:
                pass
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Hardness Entry")
    # Total Chlorine
        try:
            tc = float(total_chlorine_entry.get())
            if tc == 3:
                pass
            elif tc < 3:
                row_counter = row_counter + 1
                tc_result = tk.Label(results_frame, text=point + " Total Chlorine levels are low")
                tc_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            else:
                row_counter = row_counter + 1
                tc_result = tk.Label(results_frame, text=point + " Total Chlorine levels are high")
                tc_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Total Chlorine Entry")
        
        # Free Chlorine
        try:
            fc = float(free_chlorine_entry.get())
            if fc == 3:
                pass
            elif fc < 3:
                row_counter = row_counter + 1
                fc_result = tk.Label(results_frame, text=point + " Free Chlorine levels are low")
                fc_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            else:
                row_counter = row_counter + 1
                fc_result = tk.Label(results_frame, text=point + " Free Chlorine levels are high")
                fc_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Free Chlorine Entry")

        # Chlorine Stabalizer
        try:
            stabalizer = float(stabalizer_entry.get())
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Stabaliazer Entry")
        if stabalizer == 30:
            pass
        if stabalizer < 30:
            stabalizer_diff = 30 - stabalizer
            amount_stabalizer = (stabalizer_diff / 10) * (1.3*(pool_size/1000))
            stabalizer_lbs = amount_stabalizer / 16
            row_counter = row_counter + 1
            stabalizer_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_stabalizer, 2)) + " oz or " + str(round(stabalizer_lbs, 2)) + " lbs of Chlorine Stabalizer")
            stabalizer_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
        elif 30 < stabalizer <= 100:
            row_counter = row_counter + 1
            stabalizer_diff = 30 - stabalizer 
            stabalizer_result = tk.Label(results_frame, text=point + " Stabalizer levels are slightly high. Optimal amount is 30 ppm")
            stabalizer_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
        else:
            row_counter = row_counter + 1
            stabalizer_diff = 30 - stabalizer 
            stabalizer_result = tk.Label(results_frame, text=point + " Stabalizer levels are VERY high. Optimal amount is 30 ppm")
            stabalizer_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")

        # Alkalinity Increaser
        try:
            alkalinity = float(alkalinity_entry.get())
            if pool_type_input == "plaster":
                if alkalinity >=80 and alkalinity <= 125:
                    pass
                elif alkalinity <=80:
                    alkalinity_diff = 102.5 - alkalinity
                    amount_alkalinity = (alkalinity_diff / 10) * (3.2*(pool_size/1000))
                    alkalinity_lbs = amount_alkalinity / 16
                    row_counter = row_counter + 1
                    alkalinity_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_alkalinity, 2)) + " oz or " + str(round(alkalinity_lbs, 2)) + " lbs of Alkalinity Increaser")
                    alkalinity_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
                else:
                    row_counter = row_counter + 1
                    alkalinity_result = tk.Label(results_frame, text=point + " Alkalinity levels are high")
                    alkalinity_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
            if pool_type_input == "vinyl" or pool_type_input == "fiberglass":
                if alkalinity >=125 and alkalinity <= 150:
                    pass
                elif alkalinity <=125:
                    alkalinity_diff = 137.5 - alkalinity
                    amount_alkalinity = (alkalinity_diff / 10) * (3.2*(pool_size/1000))
                    alkalinity_lbs = amount_alkalinity / 16
                    row_counter = row_counter + 1
                    alkalinity_result = tk.Label(results_frame, text=point + " Add " + str(round(amount_alkalinity, 2)) + " oz or " + str(round(alkalinity_lbs, 2)) + " lbs of Alkalinity Increaser")
                    alkalinity_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
                else:
                    row_counter = row_counter + 1
                    alkalinity_result = tk.Label(results_frame, text=point + " Alkalinity levels are high")
                    alkalinity_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
        except:
            tkinter.messagebox.showinfo("Error",  "Invalid Alkalinity Entry")
    except:
        no_result = tk.Label(results_frame, text=point + " All levels are good!")
        no_result.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")

#Labels

size_label = ttk.Label(widgets_frame, text="Pool Size in Gallons:")
size_label.grid(row=0, column=0, padx=(5,0), sticky="e")

pool_type_label = ttk.Label(widgets_frame, text="Pool Type:")
pool_type_label.grid(row=1, column=0, sticky="e")

hardness_label = ttk.Label(widgets_frame, text="Total Hardness:")
hardness_label.grid(row=2, column=0, sticky="e")

total_chlorine_label = ttk.Label(widgets_frame, text="Total Chlorine Level:")
total_chlorine_label.grid(row=3, column=0, sticky="e")

free_chlorine_label = ttk.Label(widgets_frame, text="Free Chlorine Level:")
free_chlorine_label.grid(row=4, column=0, sticky="e")

ph_label = ttk.Label(widgets_frame, text="pH Level:")
ph_label.grid(row=5, column=0, sticky="e")

alkalinity_label = ttk.Label(widgets_frame, text="Total Alkalinity:")
alkalinity_label.grid(row=6, column=0, sticky="e")

stabalizer_label = ttk.Label(widgets_frame, text="Stabalizer:")
stabalizer_label.grid(row=7, column=0, sticky="e")




#User Entry

size_entry = ttk.Entry(widgets_frame)

size_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

type_combobox = ttk.Combobox(widgets_frame, values=pool_type_list)
type_combobox.current(0)
type_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

hardness_entry = ttk.Entry(widgets_frame)
hardness_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

total_chlorine_entry = ttk.Entry(widgets_frame)
total_chlorine_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

free_chlorine_entry = ttk.Entry(widgets_frame)
free_chlorine_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

ph_entry = ttk.Entry(widgets_frame)
ph_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

alkalinity_entry = ttk.Entry(widgets_frame)
alkalinity_entry.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

stabalizer_entry = ttk.Entry(widgets_frame)
stabalizer_entry.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

button = ttk.Button(widgets_frame, text="Calculate", command= lambda:[remove_result_frame(), calculate()])
button.grid(row=8, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

root.mainloop()
