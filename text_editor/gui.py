# gui.py
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from editor_logic import EditorLogic
from utils import get_max_chars_per_line, split_text_into_lines
from utils import get_cursor_position


class TextEditorGUI:
    def __init__(self, root: tk.Tk):
        '''
        Initialize the GUI for the custom text editor.
        :param root: The main application window (Tk).
        '''
        self.root = root
        # self.text_storage = GapBuffer(initial_size=50)  # Text storage
        # self.cursor_position = 0  # Current cursor position
        self.editor_logic = EditorLogic()
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

        # Ensure Canvas widget has focus to receive key events
        self.text_area.focus_set()

        self.font = Font(family="Courier", size=12)
        self.line_height = 10
        self.font_fill = "black"
        self.char_width = self.font.measure("a")

    def on_key_press(self, event):
        '''
        Handle key press events in the text editor.
        :param event: The key press event.
        '''
        if event.char and event.keysym.isprintable():
            self.editor_logic.insert_character(event.char)
        elif event.keysym == "BackSpace":
            self.editor_logic.delete_character()
        elif event.keysym == "Delete":
            self.editor_logic.delete_next_character()
        elif event.keysym == "Left":
            self.editor_logic.move_left()
        elif event.keysym == "Right":
            self.editor_logic.move_right()
        else:
            return

        # Redraw the canvas after every valid change
        self.redraw()

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

    def redraw(self):
        '''
        Redraw the text editor canvas.
        '''

        self.text_area.delete("all")  # Clear the canvas

        # Get the text
        text = self.editor_logic.get_text()

        # Split the text into lines
        canvas_width = self.text_area.winfo_width()

        max_chars_per_line = get_max_chars_per_line(self.char_width,
                                                    canvas_width)

        lines = split_text_into_lines(text, max_chars_per_line)

        # Render the text
        self.render_text(lines)
        self.render_cursor(lines)

    def render_text(self, lines: list[str]):
        '''
        Render the text on the canvas.
        '''
        for i, line in enumerate(lines):
            y_position = 10 + i * self.line_height
            self.text_area.create_text(10, y_position, anchor="nw", text=line,
                                       font=self.font, fill=self.font_fill)

    def render_cursor(self, lines: list[str]):
        '''
        Render the cursor on the canvas.
        :param cursor_line: The line number where the cursor is located.
        :param cursor_offset: The offset within the line where
        the cursor is located.
        '''
        cursor_position = self.editor_logic.cursor_position

        # Calculate the cursor position
        cursor_line, cursor_offset = get_cursor_position(lines,
                                                         cursor_position)

        cursor_y = 10 + cursor_line * self.line_height
        # cursor_x = 10 + (self.editor_logic.cursor_position * 7)
        cursor_x = 10 + cursor_offset * self.char_width
        self.text_area.create_line(cursor_x, cursor_y,
                                   cursor_x, cursor_y + self.line_height,
                                   fill="green", width=2)
