"""
A Tkinter app to deal with everything GUI related.
"""
from tkinter import *
from tkinter import ttk, colorchooser, filedialog


class ImageWatermark:
    def __init__(self, root):
        root.title("Python Img watermark")

        # Configure the main layout
        frame = ttk.Frame(root, padding="5")
        frame.grid(row=0, column=0, sticky=(N, S, W, E))

        # Load btn
        self.load_btn = ttk.Button(frame, text="Load Image", command=self.get_file_path)
        self.load_btn.grid(column=0, row=0)

        # Save btn
        save_btn = ttk.Button(frame, text="Save Image")
        save_btn.grid(column=10, row=0)

        # Canvas
        img_canvas = Canvas(frame, background="grey")
        img_canvas.config(width=400, height=400)
        img_canvas.grid(column=3, columnspan=5, row=1)

        # txt edit label
        txt_edit_label = ttk.Label(frame, text="Text:")
        txt_edit_label.grid(row=4, column=3)

        # Txt entry field
        txt_entry_field = ttk.Entry(frame)
        txt_entry_field.insert(0, "My watermark text here...")
        txt_entry_field.grid(row=4, column=4)

        # Button to open the color picker
        self.color_button = ttk.Button(
            frame, text="Pick a Color", command=self.choose_color
        )
        self.color_button.grid(row=4, column=6)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color[1]:
            print(f"{color[1]}")

    # @property  #Decorate with a getter atrribute to first open this window
    def get_file_path(self):
        if (file_path := filedialog.askopenfilename(title="Select Image", filetypes=[("All Files", "*.*")])):
            return file_path

    def __repr__(self) -> str:
        return f"ImageWatermarkApp(...)"
        ...


# for testing only:
root = Tk()
ImageWatermark(root=root)
root.mainloop()
