import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")

        # Initializing variables
        self.image = None
        self.watermarked_image = None

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Load Image Button
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        # Label for Image
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Watermark Text Entry
        self.watermark_entry = tk.Entry(self.root, width=30)
        self.watermark_entry.pack(pady=10)
        self.watermark_entry.insert(0, "Enter watermark text here")

        # Apply Watermark Button
        self.apply_button = tk.Button(self.root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_button.pack(pady=10)

        # Save Image Button
        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        img.thumbnail((400, 400))  # Resize image for display
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def apply_watermark(self):
        if self.image:
            watermark_text = self.watermark_entry.get()
            self.watermarked_image = self.image.copy()
            draw = ImageDraw.Draw(self.watermarked_image)
            width, height = self.watermarked_image.size

            # Use a simple font
            font_size = int(height / 20)
            font = ImageFont.load_default()  # Use the default font

            # Debugging: Print some information
            print(f"Image size: {width}x{height}")
            print(f"Font size: {font_size}")
            print(f"Watermark text: {watermark_text}")

            # Calculate the position for the watermark using textbbox
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_position = (width - text_width - 20, height - text_height - 20)  # Bottom-right corner

            # Draw the watermark text with a solid color (white) and no transparency
            draw.text(text_position, watermark_text, font=font, fill="white")

            # Display the watermarked image
            self.display_image(self.watermarked_image)
        else:
            messagebox.showerror("Error", "No image loaded to apply watermark.")

    def save_image(self):
        if self.watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.watermarked_image.save(save_path)
                messagebox.showinfo("Saved", "Watermarked image saved successfully!")
        else:
            messagebox.showerror("Error", "No watermarked image to save.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

# from tkinter import *
# from tkinter import filedialog
# from PIL import ImageTk, Image
#
# window = Tk()
# window.title("WaterMark GUI")
# window.minsize(width=700, height=500)
# window.config(bg='skyblue', padx=30, pady=30)
#
# # image uploader function
# def imageUploader():
#     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#     path = filedialog.askopenfilename(filetypes=fileTypes)
#
#     # if file is selected
#     if len(path):
#         img = Image.open(path)
#         img = img.resize((300, 250))
#         pic = ImageTk.PhotoImage(img)
#
#         water_mark = entry.get()
#         canvas.itemconfig(can_img, image=pic)
#         canvas.itemconfig(can_txt, text=water_mark)
#
#         # re-sizing the app window in order to fit picture
#         # and buttom
#         # app.geometry("560x300")
#         # label.config(image=pic)
#         # label.image = pic
#
#     # if no file is selected, then we are displaying below message
#     else:
#         print("No file is Choosen !! Please choose a file.")
#
#
# # welcome label
#
# label_1 = Label(text="Welcome to watermark GUI", font=('Arial', 24, 'bold'), bg="skyblue")
# label_1.config(padx=5, pady=10)
# label_1.grid(row=0, column=2)
#
# #entry label
#
# label_2 = Label(text="Enter TxT : ", font=('Arial', 16, 'bold'), bg='skyblue')
# label_2.config(padx=5, pady=5)
# label_2.grid(row=1, column=0)
# #Entries
# entry = Entry(width=50, highlightthickness=0)
# #Add some text to begin with
# entry.config()
# entry.insert(END, string="Some text to add watermark.")
# entry.grid(row=1, column=2)
#
# # img label
# img_label = Label(text="Click for upload : ", font=('Arial', 16, 'bold'), bg='skyblue')
# img_label.config(padx=5, pady=5)
# img_label.grid(row=2, column=0)
#
# #button to upload an image
#
# button = Button(text="upload", command=imageUploader)
# button.grid(row=2, column=2)
#
# canvas = Canvas(width=300, height=250, bg="skyblue", highlightthickness=0)
# can_img = canvas.create_image(150,125, image="")
# can_txt = canvas.create_text(150, 125, text='', font=('Times New Roman', 14, 'italic'))
# canvas.grid(row=3, column=2)
#
# window.mainloop()
#
# # # Importing libraries
# # import tkinter as tk
# # from tkinter import Label
# # from tkinter import filedialog
# # from PIL import Image, ImageTk
# #
# #
# # # image uploader function
# # def imageUploader():
# #     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
# #     path = tk.filedialog.askopenfilename(filetypes=fileTypes)
# #
# #     # if file is selected
# #     if len(path):
# #         img = Image.open(path)
# #         img = img.resize((200, 200))
# #         pic = ImageTk.PhotoImage(img)
# #
# #         # re-sizing the app window in order to fit picture
# #         # and buttom
# #         app.geometry("560x300")
# #         label.config(image=pic)
# #         label.image = pic
# #
# #     # if no file is selected, then we are displaying below message
# #     else:
# #         print("No file is Choosen !! Please choose a file.")
# #
# #
# # # Main method
# # if __name__ == "__main__":
# #     # defining tkinter object
# #     app = tk.Tk()
# #
# #     # setting title and basic size to our App
# #     app.title("GeeksForGeeks Image Viewer")
# #     app.geometry("560x270")
# #     app.config(bg="lightgreen")
# #
# #     # adding background color to our upload button
# #     # app.option_add("*Label*Background", "white")
# #     # app.option_add("*Button*Background", "lightgreen")
# #
# #     label = tk.Label(app)
# #     label.pack(pady=10)
# #
# #     # defining our upload buttom
# #     uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
# #     uploadButton.pack(side=tk.BOTTOM, pady=20)
# #
# #     app.mainloop()
