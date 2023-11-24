"""
A Tkinter app to deal with everything GUI related.
"""
from tkinter import *
from tkinter import ttk, colorchooser, filedialog
from PIL import Image, ImageTk
from PIL.Image import LANCZOS


class ImageWatermark:
    def __init__(self, root):
        root.title("Python Img watermark")

        # Configure the main layout
        frame = ttk.Frame(root, padding="5")
        frame.grid(row=0, column=0, sticky=(N, S, W, E))

        # Load btn
        self.load_btn = ttk.Button(frame, text="Load Image", command=self.get_img)
        self.load_btn.grid(column=0, row=0)

        # Save btn
        save_btn = ttk.Button(frame, text="Save Image")
        save_btn.grid(column=10, row=0)

        # self.img_canvas
        self.img_canvas = Canvas(frame)
        self.img_canvas.config(width=600, height=400)
        self.img_canvas.grid(column=3, columnspan=5, row=1)

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
    def get_img(self):
        # Open an image file using Pillow
        if file_path := filedialog.askopenfilename(
            title="Select Image", filetypes=[("All Files", "*.*")]
        ):
            original_image = Image.open(file_path)

            # Convert the Pillow Image to a Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(original_image)

            # Resize the image to fit within the self.img_canvas
            canvas_width, canvas_height = (
                self.img_canvas.winfo_reqwidth(),
                self.img_canvas.winfo_reqheight(),
            )
            # Resize the image while preserving its aspect ratio
            width_percent = canvas_width / float(original_image.width)
            height_percent = canvas_height / float(original_image.height)
            resize_percent = min(width_percent, height_percent)

            new_width = int(original_image.width * resize_percent)
            new_height = int(original_image.height * resize_percent)

            resized_image = original_image.resize((new_width, new_height), LANCZOS)

            # Convert the resized Pillow Image to a Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(resized_image)

            # Update the self.img_canvas with the new image
            self.img_canvas.create_image(0, 0, anchor="nw", image=tk_image)

            # Keep a reference to the PhotoImage to prevent it from being garbage collected
            self.img_canvas.image = tk_image

    def __repr__(self) -> str:
        return f"ImageWatermarkApp({self.img_canvas}...)"
        ...


# for testing only:
root = Tk()
ImageWatermark(root=root)
root.mainloop()
