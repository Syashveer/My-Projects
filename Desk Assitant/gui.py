import tkinter as tk
import threading
from assistant import mic, main  # Import the mic

# Initialize the GUI window
root = tk.Tk()
root.title("Voice Assistant")

# Create a Text
chat_text = tk.Text(root, wrap=tk.WORD)
chat_text.pack()

# Create an Entry
user_input_entry = tk.Entry(root)
user_input_entry.pack()

# Function to handle inputs
def handle_input():
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)  # Clear input
    update_chat("You: " + user_input)  # Display input

    # Call the assistant's mic 
    assistant_input = mic()
    
    if assistant_input != "none":
        # Call the assistant's main function
        assistant_response = main(assistant_input)
        update_chat("Assistant: " + assistant_response)

# submit
send_button = tk.Button(root, text="Send", command=handle_input)
send_button.pack()

# Function to update the chat area
def update_chat(text):
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, text + "\n") 
    chat_text.config(state=tk.DISABLED) 
    chat_text.see(tk.END)

# GUI main loop
root.mainloop()
