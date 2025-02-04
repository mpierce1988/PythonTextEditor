# gui.py
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from text_editor.editor_logic import EditorLogic
from text_storage.text_storage import TextStorage
from text_editor.utils import get_max_chars_per_line, split_text_into_lines
from text_editor.utils import get_cursor_position


class TextEditorGUI:
    # Class level attributes
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    DEFAULT_BG_COLOR = "white"
    DEFAULT_FONT_FAMILY = "Courier"
    DEFAULT_FONT_SIZE = 12
    DEFAULT_LINE_HEIGHT = 10
    DEFAULT_FONT_COLOR = "black"

    def __init__(self, root: tk.Tk, text_storage: TextStorage):
        '''
        Initialize the GUI for the custom text editor.
        :param root: The main application window (Tk).
        '''
        self.root = root
        # self.text_storage = GapBuffer(initial_size=50)  # Text storage
        # self.cursor_position = 0  # Current cursor position
        self.editor_logic = EditorLogic(text_storage)
        self._setup_ui()

        # Handle close button
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # Protected Setup Methods
    def _setup_ui(self):
        '''
        Set up the user interface for the text editor.
        '''
        self._setup_canvas()
        self._setup_scrollbar()
        self._setup_menu()
        self._setup_bindings()
        self._setup_font()

    def _setup_canvas(self):
        # Create a simple text area
        # self.text_area = tk.Text(self.root, wrap="none", undo=True)
        self.text_area = tk.Canvas(self.root, bg=self.DEFAULT_BG_COLOR,
                                   width=self.DEFAULT_WIDTH,
                                   height=self.DEFAULT_HEIGHT)
        self.text_area.pack(expand=True, fill="both")

    def _setup_scrollbar(self):
        # Add a scrollbar (optional)
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)

    def _setup_menu(self):
        # Add a basic menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="Quit", command=self.on_close)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _setup_bindings(self):
        # Event Bindings
        self.text_area.bind("<Key>", self.on_key_press)
        self.text_area.bind("<Button-1>", self.on_mouse_click)
        self.text_area.bind("<Configure>", lambda event: self.redraw())

        # Ensure Canvas widget has focus to receive key events
        self.text_area.focus_set()

    def _setup_font(self):
        self.font = Font(
            family=self.DEFAULT_FONT_FAMILY, size=self.DEFAULT_FONT_SIZE)
        self.line_height = self.DEFAULT_LINE_HEIGHT
        self.font_fill = self.DEFAULT_FONT_COLOR
        self.char_width = self.font.measure("m")

    # Event Handlers
    def on_key_press(self, event):
        '''
        Handle key press events in the text editor.
        :param event: The key press event.
        '''
        if event.char and event.keysym.isprintable():
            self.editor_logic.insert_character(event.char)
        elif event.keysym == "Return":
            self.editor_logic.insert_character("\n")
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
        cursor_position = self._get_text_cursor_position(event.x, event.y)

        self.editor_logic.move_cursor(cursor_position)
        self.redraw()

    def on_close(self):
        '''
        Handle the window close event.
        '''
        # Confirm the exit with a dialog box
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    # Rendering Methods
    def redraw(self):
        '''
        Redraw the text editor canvas.
        '''
        self.text_area.delete("all")  # Clear the canvas
        lines = self._get_text_lines()

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

    # Protected Utility Methods
    def _get_text_lines(self):
        '''
        Get the text lines based on the current text content.
        '''
        text = self.editor_logic.get_text()
        canvas_width = self.text_area.winfo_width()
        max_chars_per_line = get_max_chars_per_line(self.char_width,
                                                    canvas_width)
        return split_text_into_lines(text, max_chars_per_line)

    def _get_text_cursor_position(self, x: int, y: int):
        '''
        Get the cursor position based on the mouse click coordinates.
        '''
        lines = self._get_text_lines()

        line_height = self.line_height
        clicked_line_index = (y // line_height) - 1
        clicked_offset_index = (x // self.char_width) - 1

        if clicked_line_index < len(lines):
            line_text = lines[clicked_line_index]
            cursor_position = sum(
                len(line) for line in lines[:clicked_line_index]
                ) + min(clicked_offset_index, len(line_text))
        else:
            # Place at the end of the text if clicked below the last line
            cursor_position = len(
                self.editor_logic.get_text()
                )

        return cursor_position
