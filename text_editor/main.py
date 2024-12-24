import tkinter as tk
from tkinter import messagebox
from text_storage.gap_buffer import GapBuffer
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

    # Create the text_storage object
    text_storage = GapBuffer(initial_size=50)

    # Initialize the custom text editor GUI
    try:
        TextEditorGUI(root, text_storage)
    except Exception as e:
        messagebox.showerror("Initialization Error",
                             f"Failed to load editor: {e}")
        return

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
