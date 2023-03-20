from tkinter import *

# Define the function to calculate energy savings from LED bulbs
def calculate_led_savings():
    # Get the inputs from the user
    traditional_wattage = float(traditional_entry.get())
    led_wattage = float(led_entry.get())
    hours_per_day = float(hours_entry.get())
    cost_per_kwh = float(cost_entry.get())

    # Calculate the energy savings from switching to LED bulbs
    traditional_energy = traditional_wattage * hours_per_day / 1000
    led_energy = led_wattage * hours_per_day / 1000
    energy_savings = traditional_energy - led_energy
    cost_savings = energy_savings * cost_per_kwh

    # Update the output labels with the results
    energy_label.config(text='Energy savings: {:.2f} kWh per day'.format(energy_savings))
    cost_label.config(text='Cost savings: Rs. {:.2f} per day'.format(cost_savings))

# Create the GUI window
root = Tk()
root.title('LED Bulb Energy Savings Calculator')

# Create input labels and entry fields
traditional_label = Label(root, text='Traditional bulb wattage:')
traditional_entry = Entry(root)
led_label = Label(root, text='LED bulb wattage:')
led_entry = Entry(root)
hours_label = Label(root, text='Hours per day:')
hours_entry = Entry(root)
cost_label = Label(root, text='Cost per kWh:')
cost_entry = Entry(root)

# Create the calculate button
calculate_button = Button(root, text='Calculate', command=calculate_led_savings)

# Create output labels
energy_label = Label(root, text='')
cost_label = Label(root, text='')

# Arrange the widgets in the window
traditional_label.grid(row=0, column=0)
traditional_entry.grid(row=0, column=1)
led_label.grid(row=1, column=0)
led_entry.grid(row=1, column=1)
hours_label.grid(row=2, column=0)
hours_entry.grid(row=2, column=1)
cost_label.grid(row=3, column=0)
cost_entry.grid(row=3, column=1)
calculate_button.grid(row=4, column=0, columnspan=2)
energy_label.grid(row=5, column=0, columnspan=2)

# Run the GUI loop
root.mainloop()
