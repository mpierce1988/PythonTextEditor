import tkinter as tk
from tkinter import messagebox
from gui import TextEditorGUI


def main():
    '''
    Entry point for the text editor application.
    Initializes the main window and starts the Tkinter event loop.
    '''
    # Create the main application window
    root = tk.Tk()
    root.title('Text Editor')
    root.geometry('800x600')  # Set the window size
    root.minsize(400, 300)  # Set the minimum window size

    # Initialize the custom text editor GUI
    try:
        TextEditorGUI(root)
    except Exception as e:
        messagebox.showerror("Initialization Error",
                             f"Failed to load editor: {e}")
        return

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
