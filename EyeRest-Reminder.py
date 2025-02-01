# Importing necessary modules from Python's standard library
import time  # Used to create delays (sleep function)
import datetime  # Not used in this script but could be useful for logging
import tkinter as tk  # Tkinter is Python’s built-in GUI library
from tkinter import font, Entry  # Import specific components from tkinter

def create_fullscreen_alert(message):
    """
    This function creates a fullscreen alert window using Tkinter.
    The window displays a message and requires the user to type "OK" and press Enter to close it.
    The purpose is to remind users to take a break at set intervals.
    """

    # Step 1: Initialize the main window
    root = tk.Tk()  # Creates the main Tkinter window (root window)
    
    # Step 2: Get screen resolution (width and height in pixels)
    screen_width = root.winfo_screenwidth()  # Get the screen width
    screen_height = root.winfo_screenheight()  # Get the screen height
    
    # Step 3: Configure the window properties
    root.attributes('-fullscreen', True)  # Make the window fullscreen (covering the entire screen)
    root.configure(bg='white')  # Set background color to white
    
    # Step 4: Define font styles for text
    message_font = font.Font(family='Arial', size=48, weight='bold')  # Font for main message
    input_font = font.Font(family='Arial', size=24)  # Font for user input text
    
    # Step 5: Create a Label widget to display the message
    label = tk.Label(
        root,  # Attach the label to the root window
        text=message,  # The message that will be displayed
        font=message_font,  # Apply the defined font
        bg='white',  # Set background color
        fg='black',  # Set text color
        wraplength=screen_width-100  # Ensure text wraps properly (avoiding overflow)
    )
    label.pack(expand=True)  # Expand makes it take up available space in the window
    
    # Step 6: Create another Label widget for user instructions
    instruction = tk.Label(
        root,  # Attach the instruction label to the root window
        text="Type 'OK' and press Enter to continue",  # Instruction for user
        font=input_font,  # Use the smaller font
        bg='white',  # White background for consistency
        fg='black'  # Black text color
    )
    instruction.pack(pady=20)  # Add some padding below the message
    
    # Step 7: Create an entry field for user input
    entry = Entry(root, font=input_font, justify='center')  # Create an entry box (input field)
    entry.pack(pady=10)  # Add some vertical spacing
    entry.focus()  # Automatically focus on the entry box so user can start typing immediately
    
    # Step 8: Define function to check user input when Enter key is pressed
    def check_input(event=None):
        """
        This function checks whether the user has typed "OK" (case insensitive).
        If correct, it closes the alert window; otherwise, it clears the input field.
        """
        if entry.get().upper() == 'OK':  # Convert user input to uppercase and check if it's "OK"
            root.destroy()  # Close the alert window
        else:
            entry.delete(0, tk.END)  # Clear input box if the input is incorrect
    
    # Step 9: Bind the Enter key to trigger input validation
    entry.bind('<Return>', check_input)  # Calls check_input() when Enter is pressed
    
    # Step 10: Prevent the window from being closed using the close button (X)
    def disable_close():
        """Override default window close event to prevent accidental closure."""
        pass  # Do nothing (this disables Alt+F4 and window close button)
    
    root.protocol("WM_DELETE_WINDOW", disable_close)  # Bind close event to disable_close()
    
    # Step 11: Start the GUI event loop
    root.mainloop()  # Runs the Tkinter loop, keeping the window open

def main():
    """
    The main function controls the timing of the alerts.
    It runs an infinite loop that displays the alert every 20 minutes.
    The interval can be changed by modifying the `interval` variable.
    """
    
    interval = 20 * 60  # Define interval as 20 minutes (converted to seconds)
    
    # Define the message that will be displayed in the alert
    message = "Give your eyes a rest, NADOOOON.\n:)))"
    
    try:
        while True:  # Infinite loop to keep displaying alerts at intervals
            create_fullscreen_alert(message)  # Show the alert message
            time.sleep(interval)  # Pause execution for 20 minutes
            
    except KeyboardInterrupt:  # Handle manual script termination using Ctrl+C
        pass  # Exit the loop safely without errors

# If this script is executed directly, run the main function
if __name__ == "__main__":
    main()
