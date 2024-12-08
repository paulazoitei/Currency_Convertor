
import customtkinter
from PIL import Image, ImageTk

def click():
    print("Button was clicked")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("420x270")
window.title("Currency Convertor")
window.resizable(False, False)

original_image = Image.open('images/Logo2.png')
resized_image = original_image.resize((420, 350), Image.LANCZOS)
icon = ImageTk.PhotoImage(resized_image)
window.iconphoto(True, icon)

background_image = customtkinter.CTkImage(light_image=resized_image, dark_image=resized_image, size=(420,350))
background_label = customtkinter.CTkLabel(window, image=background_image, text="")
background_label.place(x=0, y=0)

label = customtkinter.CTkLabel(window,
                               text="Currency Convertor",
                               font=("Arial", 20),
                               fg_color="#f2d072",
                               text_color="green")

label.place(relx=0.5, rely=0.1, anchor='center')

button = customtkinter.CTkButton(window,
                                 text='Reverse',
                                 command=click,
                                 font=("Roboto", 13),
                                 fg_color="brown",
                                 text_color="#f2d072",
                                 hover_color="#303338")
button.place(x=140, y=222)

window.mainloop()

