
import customtkinter
from PIL import Image, ImageTk

def click():
    print("Button was clicked")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


window_width = 400
window_height = 360

window = customtkinter.CTk()
window.geometry(f"{window_width}x{window_height}")
window.title("Currency Convertor")
window.resizable(False, False)


original_image = Image.open('images/Logo2.png')
resized_image = original_image.resize((window_width, window_height), Image.LANCZOS)
icon = ImageTk.PhotoImage(resized_image)
window.iconphoto(True, icon)

background_image = customtkinter.CTkImage(light_image=resized_image, dark_image=resized_image, size=(window_width, window_height))
background_label = customtkinter.CTkLabel(window, image=background_image, text="")
background_label.place(x=0, y=0)


label = customtkinter.CTkLabel(window,
                               text="Currency Convertor",
                               font=("Roboto", 22, "bold"),
                               text_color="#ffffff",
                               bg_color="#3B8ED0",
                               width=210)

label.place(relx=0.5, rely=0.1, anchor='center')


button = customtkinter.CTkButton(window,
                                 text='Reverse',
                                 command=click,
                                 font=("Roboto", 14),
                                 text_color="#ffffff",
                                 hover_color="#0096FF",
                                 border_width=-3,
                                 width=120,
                                 )
button.place(x=140, y=295)


currencies=["RON","EUR","USD","CHF","GBP","BGN","RUB","ZAR","BRL","CNY","INR","MXN","NZD","RSD","UAH","XDR","TRY","XAU","AUD","CAD","CZK","DKK","EGP","MDL","NOK","PLN","SEK","AED","THB","HKD","ILS","MYR","PHP","SGD"]
dropdown=customtkinter.CTkOptionMenu(window,
                                     values=currencies,
                                     corner_radius=0,
                                     bg_color="transparent",
                                     height=25,
                                     dropdown_fg_color="#3B8ED0",
                                     dropdown_hover_color="#010c14",
                                     dropdown_text_color="#ffffff"
                                     )



dropdown.set("RON")
dropdown._dropdown_menu_height=100
dropdown.place(x=37,y=130)

label1=customtkinter.CTkLabel(window,
                             text="Change from",
                              text_color="#ffffff",
                              bg_color="#3B8ED0",
                              height=25,
                              font=("Roboto",14),
                              width=90


                             )
label1.place(x=59,y=90)

label2=customtkinter.CTkLabel(window,
                              text="In",
                              text_color="#ffffff",
                              bg_color="#3B8ED0",
                              height=25,
                              font=("Roboto",14),
                              width=25)

label2.place(x=285,y=90)

currencies1=["RON","EUR","USD","CHF","GBP","BGN","RUB","ZAR","BRL","CNY","INR","MXN","NZD","RSD","UAH","XDR","TRY","XAU","AUD","CAD","CZK","DKK","EGP","MDL","NOK","PLN","SEK","AED","THB","HKD","ILS","MYR","PHP","SGD"]
dropdown1=customtkinter.CTkOptionMenu(window,
                                     values=currencies1,
                                     corner_radius=0,
                                     bg_color="transparent",
                                     height=25,
                                     dropdown_fg_color="#3B8ED0",
                                     dropdown_hover_color="#010c14",
                                     dropdown_text_color="#ffffff"
                                     )



dropdown1.set("RON")

dropdown1.place(x=226,y=130)
window.mainloop()






