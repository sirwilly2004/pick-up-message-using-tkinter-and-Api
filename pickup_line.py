import tkinter as tk
import random
import requests

def impress_crush():
    Everything here has been done using Api for pick up lines
    # pickup_lines = [
    #     "Do you have a map? I keep getting lost in your eyes.",
    #     "Is your name Google? Because you have everything I've been searching for.",
    #     "Are you a magician? Because whenever I look at you, everyone else disappears.",
    #     "Excuse me, but I think you dropped something: my jaw.",
    #     "Is your dad a baker? Because you're a cutie pie!",
    #     "Do you believe in love at first sight, or should I walk by again?",
    #     "If you were a vegetable, you'd be a cute-cumber.",
    #     "Do you have a Band-Aid? I just scraped my knee falling for you.",
    #     "Are you a camera? Because every time I look at you, I smile.",
    #     "Is your name Wi-Fi? Because I'm really feeling a connection."
    # ]
    # using Api to generate a random pick up lines
    pickup = requests.get("https://vinuxd.vercel.app/api/pickup").json()["pickup"]    
    # pickup.raise_for_status()
    # pickup_line = random.choice(pickup_lines)
    label.config(text=pickup)

# Create the main window
window = tk.Tk()
window.title("pick up line App")
window.geometry("400x300")

# Create a label to display the pickup lines
label = tk.Label(window, text="Click the button for a romantic pickup line!")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="CLick ME", command=impress_crush)
button.pack()

# Start the main event loop
window.mainloop()
