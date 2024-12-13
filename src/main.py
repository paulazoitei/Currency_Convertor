import customtkinter
from PIL import Image, ImageTk
from crawler import get_rates

def click():
        print("button was clicked")


def convert(amount, from_currency, to_currency, rates):
        if from_currency == to_currency:
            return amount
        else:
            amount_in_ron = amount * rates[from_currency]
            amount_in_currency = amount_in_ron / rates[to_currency]
        return amount_in_currency

def make_conversion():
        amount = suma.get()
        if amount:
            try:
                amount1 = float(amount)
                from_currency = dropdown.get()
                to_currency = dropdown1.get()
                result = convert(amount1, from_currency, to_currency, rates)
                label5.configure(text=str(round(result, 4)))
            except ValueError:

                label5.configure(text="")
        else:

            label5.configure(text="")

def on_key_release(event):
        make_conversion()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

rates = get_rates()

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

background_image = customtkinter.CTkImage(light_image=resized_image, dark_image=resized_image,
                                          size=(window_width, window_height))
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

currencies = ["RON", "EUR", "USD", "CHF", "GBP", "BGN", "RUB", "ZAR", "BRL", "CNY", "INR","100KRW", "MXN", "NZD", "RSD", "UAH",
               "XDR", "TRY", "XAU", "AUD", "CAD", "CZK", "DKK", "EGP","100HUF","100JPY" "MDL", "NOK", "PLN", "SEK", "AED", "THB", "HKD",
              "100IDR", "ILS","100ISK", "MYR", "PHP", "SGD"]
dropdown = customtkinter.CTkOptionMenu(window,
                                       values=currencies,
                                       corner_radius=0,
                                       bg_color="transparent",
                                       height=25,
                                       dropdown_fg_color="#3B8ED0",
                                       dropdown_hover_color="#010c14",
                                       dropdown_text_color="#ffffff",
                                       command=lambda x: make_conversion()
                                       )

dropdown.set("RON")
dropdown._dropdown_menu_height = 100
dropdown.place(x=37, y=130)

label1 = customtkinter.CTkLabel(window,
                                text="Change from",
                                text_color="#ffffff",
                                bg_color="#3B8ED0",
                                height=25,
                                font=("Roboto", 14),
                                width=90

                                )
label1.place(x=59, y=90)

label2 = customtkinter.CTkLabel(window,
                                text="In",
                                text_color="#ffffff",
                                bg_color="#3B8ED0",
                                height=25,
                                font=("Roboto", 14),
                                width=90)

label2.place(x=248, y=90)

currencies1 = ["RON", "EUR", "USD", "CHF", "GBP", "BGN", "RUB", "ZAR", "BRL", "CNY", "INR","100KRW", "MXN", "NZD", "RSD", "UAH",
               "XDR", "TRY", "XAU", "AUD", "CAD", "CZK", "DKK", "EGP","100HUF","100JPY" "MDL", "NOK", "PLN", "SEK", "AED", "THB", "HKD",
              "100IDR", "ILS","100ISK", "MYR", "PHP", "SGD"]
dropdown1 = customtkinter.CTkOptionMenu(window,
                                        values=currencies1,
                                        corner_radius=0,
                                        bg_color="transparent",
                                        height=25,
                                        dropdown_fg_color="#3B8ED0",
                                        dropdown_hover_color="#010c14",
                                        dropdown_text_color="#ffffff",
                                        command=lambda x: make_conversion()
                                        )

dropdown1.set("RON")

dropdown1.place(x=226, y=130)

label3 = customtkinter.CTkLabel(window,
                                text="Sum",
                                text_color="#ffffff",
                                bg_color="#3B8ED0",
                                height=25,
                                font=("Roboto", 14),
                                width=90)

label3.place(x=59, y=190)
suma = customtkinter.CTkEntry(window,
                              height=25,
                              width=143,
                              corner_radius=0,
                              fg_color="#3B8ED0",
                              text_color="#ffffff",
                              justify="center",
                              font=("Roboto", 14,"bold"),

                             )
suma.place(x=37, y=230)
suma.bind("<KeyRelease>", on_key_release)
label4 = customtkinter.CTkLabel(window,
                                text="Result",
                                text_color="#ffffff",
                                bg_color="#3B8ED0",
                                height=25,
                                font=("Roboto", 14),
                                width=90)

label4.place(x=248, y=190)

label5=customtkinter.CTkLabel(window,
                                text="",
                                text_color="#ffffff",
                                bg_color="#3B8ED0",
                                height=25,
                                font=("Roboto", 14),
                                width=143)

label5.place(x=226, y=230)



window.mainloop()


