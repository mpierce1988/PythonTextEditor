import tkinter as tk
from tkinter import messagebox


class TextEditorGUI:
    def __init__(self, root):
        '''
        Initialize the GUI for the custom text editor.
        :param root: The main application window (Tk).
        '''
        self.root = root
        self.setup_ui()

        # Handle close button
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_ui(self):
        '''
        Set up the user interface for the text editor.
        '''
        # Create a simple text area
        # self.text_area = tk.Text(self.root, wrap="none", undo=True)
        self.text_area = tk.Canvas(self.root, bg="white",
                                   width=800, height=600)
        self.text_area.pack(expand=True, fill="both")

        # Add a scrollbar (optional)
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)

        # Add a basic menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="Quit", command=self.on_close)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Placeholder for custom logic integration
        self.text_area.bind("<Key>", self.on_key_press)
        self.text_area.bind("<Button-1>", self.on_mouse_click)

    def on_key_press(self, event):
        '''
        Handle key press events in the text editor.
        :param event: The key press event.
        '''
        if event.char and event.keysym.isprintable():
            self.insert_character(event.char)

    def on_mouse_click(self, event):
        '''
        Handle mouse click events in the text editor.
        :param event: The mouse click event.
        '''
        print(f"Mouse clicked at: {event.x}, {event.y}")

    def on_close(self):
        '''
        Handle the window close event.
        '''
        # Confirm the exit with a dialog box
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def insert_character(self, char):
        '''
        Insert a character into the text editor.
        :param char: The character to insert.  
        '''

        # TODO Implement text storage and rendering
        print(f"Character inserted: {char}")
