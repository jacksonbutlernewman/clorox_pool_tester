pool_size_input = input("Enter Pool Size in gallons: ")
pool_type_input = input("Is your pool plaster, vinyl, or fiberglass?: ")
hardness_input = input("Total Hardness: ")
total_chlorine_input = input("Total Chlorine Level: ")
free_chlorine_input = input("free Chlorine Level: ")
ph_input = input("pH Level: ")
alkalinity_input = input("Total Alkalinity: ")
stabalizer_input = input("Stabalizer: ")

# Pool Size
pool_size = int(pool_size_input)


print("\nRESULTS\n")

# pH Level
amount_phup = 0
amount_phdown = 0
try:
    ph = float(ph_input)
except:
    print("not in number format")
    quit()
if ph >= 8.4 and ph < 20:
    amount_phdown = 2.4 * (pool_size / 1000)
    print("add",round(amount_phdown, 2), "oz of pH Down")
elif ph >= 8.3:
    amount_phdown = 2 * (pool_size / 1000)
    print("add",round(amount_phdown, 2), "oz of pH Down")
elif ph >= 8:
    amount_phdown = 1.2 * (pool_size / 1000)
    print("add",round(amount_phdown, 2), "oz of pH Down")
elif ph >= 7.8:
    amount_phdown = 0.6 * (pool_size / 1000)
    print("add",round(amount_phdown, 2), "oz of pH Down")
elif ph >= 7.6:
    quit()
elif ph >= 7.1:
    amount_phup = 1.2 * (pool_size / 1000)
    print("add",round(amount_phup, 2), "oz of pH Up")
elif ph >= 6.7:
    amount_phup = 1.6 * (pool_size / 1000)
    print("add",round(amount_phup, 2), "oz of pH Up")
elif ph <= 6.5:
    amount_phup = 2 * (pool_size / 1000)
    print("add",round(amount_phup, 2), "oz of pH Up")
elif ph == 0:
    amount_phup = 2 * (pool_size / 1000)
    print("add",round(amount_phup, 2), "oz of pH Up")
else:
    print("error")


# Calcium Hardness Increaser
try:
    hardness = float(hardness_input)
except:
    print("not in number format")
    quit()
if hardness <= 200:
    ppm_diff = 200 - hardness
    amount_of_CHIncreaser = (ppm_diff / 10) * (1.6 * (pool_size / 1000))
    conv_to_lbs = amount_of_CHIncreaser / 16
    print("add",round(amount_of_CHIncreaser, 2), "oz or", round(conv_to_lbs, 2), "lbs of Calcium Hardness Increaser")
else:
    print("error")

# Total Chlorine
try:
    tc = float(total_chlorine_input)
except:
    print("not in number format")
    quit()
if tc == 3:
    quit()
elif tc < 3:
    print("your total chlorine levels are low")
else:
    print("your total chlorine levels are high")

# Free Chlorine
try:
    fc = float(free_chlorine_input)
except:
    print("not in number format")
    quit()
if fc == 3:
    quit()
elif fc < 3:
    print("your free chlorine levels are low")
else:
    print("your free chlorine levels are high")

# Chlorine Stabalizer
try:
    stabalizer = float(stabalizer_input)
except:
    print("not in number format")
    quit()
if stabalizer <= 30:
    stabalizer_diff = 30 - stabalizer
    amount_stabalizer = (stabalizer_diff / 10) * (1.3*(pool_size/1000))
    stabalizer_lbs = amount_stabalizer / 16
    print("add", round(amount_stabalizer, 2),"oz or",round(stabalizer_lbs, 2),"lbs of Chlorine Stablizer")
else:
    print("Stabalizer levels are high")

#Pool Type
try: 
    pool_type_input == "vinyl"
    pool_type_input == "fiberglass"
    pool_type_input == "plaster"
except:
    print("Invalid Input")
    quit()

# Alkalinity Increaser
try:
    alkalinity = float(alkalinity_input)
except:
    print("not in number format")
    quit()
if pool_type_input == "plaster":
    if alkalinity >=80 and alkalinity <= 125:
        quit()
    elif alkalinity <=80:
        alkalinity_diff = 102.5 - alkalinity
        amount_alkalinity = (alkalinity_diff / 10) * (3.2*(pool_size/1000))
        alkalinity_lbs = amount_alkalinity / 16
        print("add", round(amount_alkalinity, 2),"oz or",round(alkalinity_lbs, 2),"lbs of Alkalinity Increaser")
    else:
        print("Alkalinity levels are high")
if pool_type_input == "vinyl" or pool_type_input == "fiberglass":
    if alkalinity >=125 and alkalinity <= 150:
        quit()
    elif alkalinity <=125:
        alkalinity_diff = 137.5 - alkalinity
        amount_alkalinity = (alkalinity_diff / 10) * (3.2*(pool_size/1000))
        alkalinity_lbs = amount_alkalinity / 16
        print("add", round(amount_alkalinity, 2),"oz or",round(alkalinity_lbs, 2),"lbs of Alkalinity Increaser")
    else:
        print("Alkalinity levels are high")
