from tkinter import*

menu_dict = {"Breakfast": ["Fried eggs", "Boiled eggs", "Omlette", "Cereals and milk", "Pancakes"],
                "Soups": ["Tripe soup", "Beef soup", "Chicken soup", "Tomatoes soup", "Greek soup", "Pork soup", "Bean soup"],
                "Pizza": ["Quattro stagioni", "Quattro formaggi", "Capriciossa", "Margerita", "Diavola", "Calzone", "Hawaii"],
                "Beef": ["Grill beef", "Beef pasta", "Beef hamburger", "Steak with gorgonzola sauce", "Veal stew"],
                "Pork": ["Pork skewers", "Grill pork", "Pork schnitzel", "Spicy pork sausages", "Gordon bleu", "Sweet chilli pork with rice"],
                "Chicken": ["Baked chicken wings", "Chicken brine with polenta", "Chicken livers with rice", "Chicken burrito", "Chicken quesadilla"],
                "Dessert": ["Papanasi", "Ice cream", "Tiramisu", "Chocolate souffle", "Cookie cake"],
                "Drinks": ["Tea", "Coffee", "Lemonade", "Juice", "Water", "Beer", "Wine"]}
new_x = -867

def start_second_window():
    store_window = Tk()

    # LEFT FRAME2
    left_frame2 = Frame(height=600, width=64, bg="#dfe65c")
    left_frame2.place(x=29, y=0)

    # SEARCH FUNCTIONS
        # SEARCH ENTRY
    def search_entry_focusin(e):
        if search_entry.get() == " Search for dishes":
            search_entry.delete(0, "end")
        search_entry.config(bg="#69ebf5", fg="black")

    def search_entry_focusout(e):
        if len(search_entry.get()) == 0:
            search_entry.insert(0, " Search for dishes")
            search_entry.config(bg="white", fg="gray")
        else:
            search_entry.config(bg="white", fg="black")

    def show_search_entry():
        search_entry.place(x=400, y=10)
        search_btn.config(command=lambda: hide_search_entry())
        if len(search_entry.get()) > 0 and search_entry.get() != " Search for dishes":
            search_entry.delete(0, "end")
            search_entry.insert(0, " Search for dishes")
            search_entry.config(bg="white", fg="gray")

    def hide_search_entry():
        search_entry.place_forget()
        search_btn.config(command=lambda: show_search_entry())
        btn_for_focus.focus_set()
        search_entry_label_info.config(text="")

            # CHECK SEARCH ENTRY
    def check_search_entry(e):
        search = search_entry.get()
        if len(search) == 0:
            search_entry_label_info.config(text="You have to type in something!", fg="red")
            return 0
        else:
            for menu in menu_dict:
                for submenu in menu_dict[menu]:
                    if search == submenu:
                        text = "That dish is in the " + menu + " menu."
                        search_entry_label_info.config(text=text, fg="#3f84f2")
                        return 0
            text = "That dish is in " + menu +"'s menu"
            search_entry_label_info.config(text="It seems you typed in wrong or that dish isn't in the menu.", fg="red")
            return 0

        # SEARCH BUTTON
    def search_btn_color1(e):
        search_btn.config(bg="#9cf8ff")

    def search_btn_color2(e):
        search_btn.config(bg="#69ebf5")

    # SEARCH VARIABLES
        # SEARCH ENTRY
    search_entry = Entry(store_window, font=("Times New Roman", 18, "bold"), fg="gray", relief="solid")
    search_entry.insert(0, " Search for dishes")
    search_entry.bind("<FocusIn>", search_entry_focusin)
    search_entry.bind("<FocusOut>", search_entry_focusout)
    search_entry.bind("<Return>", check_search_entry)
    search_entry_label_info = Label(font=("Times New Roman", 10, "bold"))
    search_entry_label_info.place(x=400, y=40)
    btn_for_focus = Button()
    btn_for_focus.place(x=40, y=15)

        # SEARCH BUTTON
    search_btn = Button(text="Search", font=("Times New Roman", 14, "bold"), relief="groove", width=5, bg="#69ebf5", activeforeground="black", activebackground="#9cf8ff", 
                        command=lambda: show_search_entry(), takefocus=0)
    search_btn.place(x=30, y=10)
    search_btn.bind("<Enter>", search_btn_color1)
    search_btn.bind("<Leave>", search_btn_color2)

    # MENU BUTTON
    def menu_color1(e):
        menu_btn.config(bg="#bbc9fa")

    def menu_color2(e):
        menu_btn.config(bg="#9aaffc")

    def start_menu_animation():
        global new_x
        if new_x == -867:
            menu_btn.config(state="disabled")
        if new_x < 31:
            new_x += 3
            menu_frame.place(x=new_x)
        if new_x == 30:
            new_x += 1
            menu_frame.place(x=new_x)
            menu_btn.config(command=lambda: reverse_menu_animation(), state="normal")
            return True
        menu_frame.after(2, start_menu_animation)

    def reverse_menu_animation():
        global new_x
        if new_x == 31:
            breakfast_frame.place_forget()
            breakfast_btn.config(command=lambda: show_breakfast_frame())
            soups_frame.place_forget()
            soups_btn.config(command=lambda: show_soups_frame())
            pizza_frame.place_forget()
            pizza_btn.config(command=lambda: show_pizza_frame())
            beef_frame.place_forget()
            beef_btn.config(command=lambda: show_beef_frame())
            pork_frame.place_forget()
            pork_btn.config(command=lambda: show_pork_frame())
            chicken_frame.place_forget()
            chicken_btn.config(command=lambda: show_chicken_frame())
            dessert_frame.place_forget()
            dessert_btn.config(command=lambda: show_dessert_frame())
            drinks_frame.place_forget()
            drinks_btn.config(command=lambda: show_drinks_frame())
            menu_btn.config(state="disabled")
        if new_x > -867:
            new_x -= 3
            menu_frame.place(x=new_x)
        if new_x == -866:
            new_x -= 1
            menu_frame.place(x=new_x)
            menu_btn.config(command=lambda: start_menu_animation(), state="normal")
            return True
        menu_frame.after(2, reverse_menu_animation)

    menu_frame = Frame(width=961, height=37, bg="#9aaffc")
    menu_frame.place(x=-867, y=61)
    menu_btn = Button(text="Menu", font=("Times New Roman", 14, "bold"), relief="solid", bg="#9aaffc", command=lambda: start_menu_animation(), disabledforeground="black",
                    activebackground="#bbc9fa", takefocus=0)
    menu_btn.place(x=30, y=60)
    menu_btn.bind("<Enter>", menu_color1)
    menu_btn.bind("<Leave>", menu_color2)

    # MENU OPTIONS 
        # BREAKFAST MENU BUTTON
    def breakfast_color1(e):
        breakfast_btn.config(bg="#ccf2a0")

    def breakfast_color2(e):
        breakfast_btn.config(bg="#b3f567")

    def show_breakfast_frame():
        breakfast_frame.place(x=101, y=96)
        breakfast_btn.config(command=lambda: hide_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_breakfast_frame():
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())

    breakfast_btn = Button(menu_frame, text=" Breakfast", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_breakfast_frame(), takefocus=0,
                        activebackground="#ccf2a0")
    breakfast_btn.place(x=70, y=2)
    breakfast_btn.bind("<Enter>", breakfast_color1)
    breakfast_btn.bind("<Leave>", breakfast_color2)
    breakfast_frame = Frame(width=85, height=380, bg="#cffc9a")

        # BREAKFAST MENU OPTIONS
            # FRIED EGGS BUTTON AND ITS PRICE
    def fried_eggs_color1(e):
        fried_eggs_btn.config(bg="#ddffb5")
        fried_eggs_price.place(x=186, y=116)

    def fried_eggs_color2(e):
        fried_eggs_btn.config(bg="#cffc9a")
        fried_eggs_price.place_forget()

    fried_eggs_btn = Button(breakfast_frame, text=" Fried eggs", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=11, height=1, activebackground="#ddffb5",
                            takefocus=0)
    fried_eggs_btn.place(x=-1, y=20)
    fried_eggs_btn.bind("<Enter>", fried_eggs_color1)
    fried_eggs_btn.bind("<Leave>", fried_eggs_color2)
    fried_eggs_price = Button(text="7.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", takefocus=0)

            # BOILED EGGS BUTTON AND ITS PRICE
    def boiled_eggs_color1(e):
        boiled_eggs_btn.config(bg="#ddffb5")
        boiled_eggs_price.place(x=186, y=191)

    def boiled_eggs_color2(e):
        boiled_eggs_btn.config(bg="#cffc9a")
        boiled_eggs_price.place_forget()

    boiled_eggs_btn = Button(breakfast_frame, text=" Boiled eggs", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=11, height=1, activebackground="#ddffb5",
                            takefocus=0)
    boiled_eggs_btn.place(x=-1, y=95)
    boiled_eggs_btn.bind("<Enter>", boiled_eggs_color1)
    boiled_eggs_btn.bind("<Leave>", boiled_eggs_color2)
    boiled_eggs_price = Button(text="6.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", takefocus=0)

            # OMLETTE BUTTON AND ITS PRICE
    def omlette_color1(e):
        omlette_btn.config(bg="#ddffb5")
        omlette_price.place(x=186, y=266)

    def omlette_color2(e):
        omlette_btn.config(bg="#cffc9a")
        omlette_price.place_forget()

    omlette_btn = Button(breakfast_frame, text=" Omlette", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=11, height=1, activebackground="#ddffb5",
                        takefocus=0)
    omlette_btn.place(x=-1, y=170)
    omlette_btn.bind("<Enter>", omlette_color1)
    omlette_btn.bind("<Leave>", omlette_color2)
    omlette_price = Button(text="10.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", takefocus=0)

            # CEREALS WITH MILK BUTTON AND ITS PRICE
    def cereals_with_milk_color1(e):
        cereals_with_milk_btn.config(bg="#ddffb5")
        cereals_with_milk_price.place(x=186, y=341)

    def cereals_with_milk_color2(e):
        cereals_with_milk_btn.config(bg="#cffc9a")
        cereals_with_milk_price.place_forget()

    cereals_with_milk_btn = Button(breakfast_frame, text=" Cereals\nwith milk", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=11, height=2, 
                                activebackground="#ddffb5", takefocus=0)
    cereals_with_milk_btn.place(x=-1, y=245)
    cereals_with_milk_btn.bind("<Enter>", cereals_with_milk_color1)
    cereals_with_milk_btn.bind("<Leave>", cereals_with_milk_color2)
    cereals_with_milk_price = Button(text="7.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # PANCAKES BUTTON AND ITS PRICE
    def pancakes_color1(e):
        pancakes_btn.config(bg="#ddffb5")
        pancakes_price.place(x=186, y=416)

    def pancakes_color2(e):
        pancakes_btn.config(bg="#cffc9a")
        pancakes_price.place_forget()

    pancakes_btn = Button(breakfast_frame, text=" Pancakes", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=11, height=1, activebackground="#ddffb5",
                        takefocus=0)
    pancakes_btn.place(x=-1, y=320)
    pancakes_btn.bind("<Enter>", pancakes_color1)
    pancakes_btn.bind("<Leave>", pancakes_color2)
    pancakes_price = Button(text="8.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", takefocus=0)

        # SOUPS MENU BUTTON
    def soups_color1(e):
        soups_btn.config(bg="#ccf2a0")

    def soups_color2(e):
        soups_btn.config(bg="#b3f567")

    def show_soups_frame():
        soups_frame.place(x=226, y=96)
        soups_btn.config(command=lambda: hide_soups_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_soups_frame():
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())

    soups_btn = Button(menu_frame, text="Soups", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_soups_frame(), takefocus=0,
                    activebackground="#ccf2a0")
    soups_btn.place(x=195, y=2)
    soups_btn.bind("<Enter>", soups_color1)
    soups_btn.bind("<Leave>", soups_color2)
    soups_frame = Frame(width=54, height=380, bg="#cffc9a")

        # SOUPS MENU OPTIONS
            # TRIPE SOUP BUTTON AND ITS PRICE
    def tripe_soup_color1(e):
        tripe_soup_btn.config(bg="#ddffb5")
        tripe_soup_price.place(x=278, y=116)

    def tripe_soup_color2(e):
        tripe_soup_btn.config(bg="#cffc9a")
        tripe_soup_price.place_forget()

    tripe_soup_btn = Button(soups_frame, text="Tripe\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5",
                            takefocus=0)
    tripe_soup_btn.place(x=0, y=20)
    tripe_soup_btn.bind("<Enter>", tripe_soup_color1)
    tripe_soup_btn.bind("<Leave>", tripe_soup_color2)
    tripe_soup_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # COW SOUP BUTTON AND ITS PRICE
    def cow_soup_color1(e):
        cow_soup_btn.config(bg="#ddffb5")
        cow_soup_price.place(x=278, y=166)

    def cow_soup_color2(e):
        cow_soup_btn.config(bg="#cffc9a")
        cow_soup_price.place_forget()

    cow_soup_btn = Button(soups_frame, text="Beef\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5", takefocus=0)
    cow_soup_btn.place(x=0, y=70)
    cow_soup_btn.bind("<Enter>", cow_soup_color1)
    cow_soup_btn.bind("<Leave>", cow_soup_color2)
    cow_soup_price = Button(text="11.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # CHICKEN SOUP BUTTON AND ITS PRICE
    def chicken_soup_color1(e):
        chicken_soup_btn.config(bg="#ddffb5")
        chicken_soup_price.place(x=278, y=216)

    def chicken_soup_color2(e):
        chicken_soup_btn.config(bg="#cffc9a")
        chicken_soup_price.place_forget()

    chicken_soup_btn = Button(soups_frame, text="Chicken\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5",
                            takefocus=0)
    chicken_soup_btn.place(x=0, y=120)
    chicken_soup_btn.bind("<Enter>", chicken_soup_color1)
    chicken_soup_btn.bind("<Leave>", chicken_soup_color2)
    chicken_soup_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # TOMATOES SOUP BUTTON AND ITS PRICE
    def tomatoes_soup_color1(e):
        tomatoes_soup_btn.config(bg="#ddffb5")
        tomatoes_soup_price.place(x=278, y=266)

    def tomatoes_soup_color2(e):
        tomatoes_soup_btn.config(bg="#cffc9a")
        tomatoes_soup_price.place_forget()

    tomatoes_soup_btn = Button(soups_frame, text="Tomatoes\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5",
                            takefocus=0)
    tomatoes_soup_btn.place(x=0, y=170)
    tomatoes_soup_btn.bind("<Enter>", tomatoes_soup_color1)
    tomatoes_soup_btn.bind("<Leave>", tomatoes_soup_color2)
    tomatoes_soup_price = Button(text="9.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # GREEK SOUP BUTTON AND ITS PRICE
    def greek_soup_color1(e):
        greek_soup_btn.config(bg="#ddffb5")
        greek_soup_price.place(x=278, y=316)

    def greek_soup_color2(e):
        greek_soup_btn.config(bg="#cffc9a")
        greek_soup_price.place_forget()

    greek_soup_btn = Button(soups_frame, text="Greek\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5",
                            takefocus=0)
    greek_soup_btn.place(x=0, y=220)
    greek_soup_btn.bind("<Enter>", greek_soup_color1)
    greek_soup_btn.bind("<Leave>", greek_soup_color2)
    greek_soup_price = Button(text="14.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # PORK SOUP BUTTON AND ITS PRICE
    def pork_soup_color1(e):
        pork_soup_btn.config(bg="#ddffb5")
        pork_soup_price.place(x=278, y=366)

    def pork_soup_color2(e):
        pork_soup_btn.config(bg="#cffc9a")
        pork_soup_price.place_forget()

    pork_soup_btn = Button(soups_frame, text="Pork\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5", takefocus=0)
    pork_soup_btn.place(x=0, y=270)
    pork_soup_btn.bind("<Enter>", pork_soup_color1)
    pork_soup_btn.bind("<Leave>", pork_soup_color2)
    pork_soup_price = Button(text="13.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # BEAN SOUP BUTTON AND ITS PRICE
    def bean_soup_color1(e):
        bean_soup_btn.config(bg="#ddffb5")
        bean_soup_price.place(x=278, y=416)

    def bean_soup_color2(e):
        bean_soup_btn.config(bg="#cffc9a")
        bean_soup_price.place_forget()

    bean_soup_btn = Button(soups_frame, text="Bean\nsoup", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=6, height=2, activebackground="#ddffb5", takefocus=0)
    bean_soup_btn.place(x=0, y=320)
    bean_soup_btn.bind("<Enter>", bean_soup_color1)
    bean_soup_btn.bind("<Leave>", bean_soup_color2)
    bean_soup_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

        # PIZZA MENU BUTTON
    def pizza_color1(e):
        pizza_btn.config(bg="#ccf2a0")

    def pizza_color2(e):
        pizza_btn.config(bg="#b3f567")

    def show_pizza_frame():
        pizza_frame.place(x=321, y=96)
        pizza_btn.config(command=lambda: hide_pizza_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_pizza_frame():
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())

    pizza_btn = Button(menu_frame, text="Pizza", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_pizza_frame(), activebackground="#ccf2a0", 
                    width=7, takefocus=0)
    pizza_btn.place(x=290, y=2)
    pizza_btn.bind("<Enter>", pizza_color1)
    pizza_btn.bind("<Leave>", pizza_color2)
    pizza_frame = Frame(width=73, height=380, bg="#cffc9a")

        # PIZZA MENU OPTIONS
            # PIZZA QUATTRO STAGIONI BUTTON AND ITS PRICE
    def pizza_quattro_stagioni_color1(e):
        pizza_quattro_stagioni_btn.config(bg="#ddffb5")
        pizza_quattro_stagioni_price.place(x=394, y=116)

    def pizza_quattro_stagioni_color2(e):
        pizza_quattro_stagioni_btn.config(bg="#cffc9a")
        pizza_quattro_stagioni_price.place_forget()

    pizza_quattro_stagioni_btn = Button(pizza_frame, text="Quattro\nstagioni", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                        activebackground="#ddffb5")
    pizza_quattro_stagioni_btn.place(x=0, y=20)
    pizza_quattro_stagioni_btn.bind("<Enter>", pizza_quattro_stagioni_color1)
    pizza_quattro_stagioni_btn.bind("<Leave>", pizza_quattro_stagioni_color2)
    pizza_quattro_stagioni_price = Button(text="16.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # PIZZA QUATTRO FORMAGGI BUTTON AND ITS PRICE
    def pizza_quattro_formaggi_color1(e):
        pizza_quattro_formaggi_btn.config(bg="#ddffb5")
        pizza_quattro_formaggi_price.place(x=394, y=166)

    def pizza_quattro_formaggi_color2(e):
        pizza_quattro_formaggi_btn.config(bg="#cffc9a")
        pizza_quattro_formaggi_price.place_forget()

    pizza_quattro_formaggi_btn = Button(pizza_frame, text="Quattro\nformaggi", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                        activebackground="#ddffb5")
    pizza_quattro_formaggi_btn.place(x=0, y=70)
    pizza_quattro_formaggi_btn.bind("<Enter>", pizza_quattro_formaggi_color1)
    pizza_quattro_formaggi_btn.bind("<Leave>", pizza_quattro_formaggi_color2)
    pizza_quattro_formaggi_price = Button(text="16.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # PIZZA CAPRICCIOSA BUTTON AND ITS PRICE
    def pizza_capricciosa_color1(e):
        pizza_capricciosa_btn.config(bg="#ddffb5")
        pizza_capricciosa_price.place(x=394, y=216)

    def pizza_capricciosa_color2(e):
        pizza_capricciosa_btn.config(bg="#cffc9a")
        pizza_capricciosa_price.place_forget()

    pizza_capricciosa_btn = Button(pizza_frame, text="Capricciosa", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0, 
                                activebackground="#ddffb5")
    pizza_capricciosa_btn.place(x=0, y=120)
    pizza_capricciosa_btn.bind("<Enter>", pizza_capricciosa_color1)
    pizza_capricciosa_btn.bind("<Leave>", pizza_capricciosa_color2)
    pizza_capricciosa_price = Button(text="15.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # PIZZA MARGERITA BUTTON AND ITS PRICE
    def pizza_margerita_color1(e):
        pizza_margerita_btn.config(bg="#ddffb5")
        pizza_margerita_price.place(x=394, y=266)

    def pizza_margerita_color2(e):
        pizza_margerita_btn.config(bg="#cffc9a")
        pizza_margerita_price.place_forget()

    pizza_margerita_btn = Button(pizza_frame, text="Margerita", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                                activebackground="#ddffb5")
    pizza_margerita_btn.place(x=0, y=170)
    pizza_margerita_btn.bind("<Enter>", pizza_margerita_color1)
    pizza_margerita_btn.bind("<Leave>", pizza_margerita_color2)
    pizza_margerita_price = Button(text="17.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # PIZZA DIAVOLA BUTTON AND ITS PRICE
    def pizza_diavola_color1(e):
        pizza_diavola_btn.config(bg="#ddffb5")
        pizza_diavola_price.place(x=394, y=316)

    def pizza_diavola_color2(e):
        pizza_diavola_btn.config(bg="#cffc9a")
        pizza_diavola_price.place_forget()

    pizza_diavola_btn = Button(pizza_frame, text="Diavola", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    pizza_diavola_btn.place(x=0, y=220)
    pizza_diavola_btn.bind("<Enter>", pizza_diavola_color1)
    pizza_diavola_btn.bind("<Leave>", pizza_diavola_color2)
    pizza_diavola_price = Button(text="16.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # PIZZA CALZONE BUTTON AND ITS PRICE
    def pizza_calzone_color1(e):
        pizza_calzone_btn.config(bg="#ddffb5")
        pizza_calzone_price.place(x=394, y=366)

    def pizza_calzone_color2(e):
        pizza_calzone_btn.config(bg="#cffc9a")
        pizza_calzone_price.place_forget()

    pizza_calzone_btn = Button(pizza_frame, text="Calzone", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    pizza_calzone_btn.place(x=0, y=270)
    pizza_calzone_btn.bind("<Enter>", pizza_calzone_color1)
    pizza_calzone_btn.bind("<Leave>", pizza_calzone_color2)
    pizza_calzone_price = Button(text="18.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # PIZZA HAWAII BUTTON AND ITS PRICE
    def pizza_hawaii_color1(e):
        pizza_hawaii_btn.config(bg="#ddffb5")
        pizza_hawaii_price.place(x=394, y=416)

    def pizza_hawaii_color2(e):
        pizza_hawaii_btn.config(bg="#cffc9a")
        pizza_hawaii_price.place_forget()

    pizza_hawaii_btn = Button(pizza_frame, text="Hawaii", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    pizza_hawaii_btn.place(x=0, y=320)
    pizza_hawaii_btn.bind("<Enter>", pizza_hawaii_color1)
    pizza_hawaii_btn.bind("<Leave>", pizza_hawaii_color2)
    pizza_hawaii_price = Button(text="15.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

        # BEEF MENU BUTTON
    def beef_color1(e):
        beef_btn.config(bg="#ccf2a0")

    def beef_color2(e):
        beef_btn.config(bg="#b3f567")

    def show_beef_frame():
        beef_frame.place(x=436, y=96)
        beef_btn.config(command=lambda: hide_beef_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_beef_frame():
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())

    beef_btn = Button(menu_frame, text="Beef", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", width=7, command=lambda: show_beef_frame(), activebackground="#ccf2a0",
                    takefocus=0)
    beef_btn.place(x=405, y=2)
    beef_btn.bind("<Enter>", beef_color1)
    beef_btn.bind("<Leave>", beef_color2)
    beef_frame = Frame(width=73, height=380, bg="#cffc9a")

        # BEEF OPTIONS MENU
            # GRILL BEEF BUTTON AND ITS PRICE
    def grill_beef_color1(e):
        grill_beef_btn.config(bg="#ddffb5")
        grill_beef_price.place(x=509, y=116)

    def grill_beef_color2(e):
        grill_beef_btn.config(bg="#cffc9a")
        grill_beef_price.place_forget()

    grill_beef_btn = Button(beef_frame, text="Grill beef", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    grill_beef_btn.place(x=0, y=20)
    grill_beef_btn.bind("<Enter>", grill_beef_color1)
    grill_beef_btn.bind("<Leave>", grill_beef_color2)
    grill_beef_price = Button(text="23.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # BEEF PASTA BUTTON AND ITS PRICE
    def beef_pasta_color1(e):
        beef_pasta_btn.config(bg="#ddffb5")
        beef_pasta_price.place(x=509, y=191)

    def beef_pasta_color2(e):
        beef_pasta_btn.config(bg="#cffc9a")
        beef_pasta_price.place_forget()

    beef_pasta_btn = Button(beef_frame, text="Beef pasta", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    beef_pasta_btn.place(x=0, y=95)
    beef_pasta_btn.bind("<Enter>", beef_pasta_color1)
    beef_pasta_btn.bind("<Leave>", beef_pasta_color2)
    beef_pasta_price = Button(text="18.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1)

            # BEEF HAMBURGER BUTTON AND ITS PRICE
    def beef_hamburger_color1(e):
        beef_hamburger_btn.config(bg="#ddffb5")
        beef_hamburger_price.place(x=509, y=266)

    def beef_hamburger_color2(e):
        beef_hamburger_btn.config(bg="#cffc9a")
        beef_hamburger_price.place_forget() 

    beef_hamburger_btn = Button(beef_frame, text="Beef\nhamburger", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                activebackground="#ddffb5")
    beef_hamburger_btn.place(x=0, y=170)
    beef_hamburger_btn.bind("<Enter>", beef_hamburger_color1)
    beef_hamburger_btn.bind("<Leave>", beef_hamburger_color2)
    beef_hamburger_price = Button(text="22.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # STEAK WITH GORGONZOLA SAUCE BUTTON AND ITS PRICE
    def gorgonzola_sauce_beef_color1(e):
        gorgonzola_sauce_beef_btn.config(bg="#ddffb5")
        gorgonzola_sauce_beef_price.place(x=509, y=341)

    def gorgonzola_sauce_beef_color2(e):
        gorgonzola_sauce_beef_btn.config(bg="#cffc9a")
        gorgonzola_sauce_beef_price.place_forget()

    gorgonzola_sauce_beef_btn = Button(beef_frame, text="Steak with\ngorgonzola\nsauce", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=3,
                                    activebackground="#ddffb5", takefocus=0)
    gorgonzola_sauce_beef_btn.place(x=0, y=245)
    gorgonzola_sauce_beef_btn.bind("<Enter>", gorgonzola_sauce_beef_color1)
    gorgonzola_sauce_beef_btn.bind("<Leave>", gorgonzola_sauce_beef_color2)
    gorgonzola_sauce_beef_price = Button(text="27.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=3, takefocus=0)

            # VEAL STEW BUTTON AND ITS PRICE
    def beef_stew_color1(e):
        beef_stew_btn.config(bg="#ddffb5")
        beef_stew_price.place(x=509, y=416)

    def beef_stew_color2(e):
        beef_stew_btn.config(bg="#cffc9a")
        beef_stew_price.place_forget()

    beef_stew_btn = Button(beef_frame, text="Veal stew", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                        activebackground="#ddffb5")
    beef_stew_btn.place(x=0, y=320)
    beef_stew_btn.bind("<Enter>", beef_stew_color1)
    beef_stew_btn.bind("<Leave>", beef_stew_color2)
    beef_stew_price = Button(text="20.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

        # PORK MENU BUTTON
    def pork_color1(e):
        pork_btn.config(bg="#ccf2a0")

    def pork_color2(e):
        pork_btn.config(bg="#b3f567")

    def show_pork_frame():
        pork_frame.place(x=551, y=96)
        pork_btn.config(command=lambda: hide_pork_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_pork_frame():
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())


    pork_btn = Button(menu_frame, text="Pork", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", width=7, command=lambda: show_pork_frame(), activebackground="#ccf2a0",
                    takefocus=0)
    pork_btn.place(x=520, y=2)
    pork_btn.bind("<Enter>", pork_color1)
    pork_btn.bind("<Leave>", pork_color2)
    pork_frame = Frame(width=73, height=380, bg="#cffc9a")

        # PORK MENU OPTIONS
            # PORK SKEWERS BUTTON AND ITS PRICE
    def pork_skewers_color1(e):
        pork_skewers_btn.config(bg="#ddffb5")
        pork_skewers_price.place(x=624, y=116)

    def pork_skewers_color2(e):
        pork_skewers_btn.config(bg="#cffc9a")
        pork_skewers_price.place_forget()

    pork_skewers_btn = Button(pork_frame, text="Pork\nskewers", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                            activebackground="#ddffb5")
    pork_skewers_btn.place(x=0, y=20)
    pork_skewers_btn.bind("<Enter>", pork_skewers_color1)
    pork_skewers_btn.bind("<Leave>", pork_skewers_color2)
    pork_skewers_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # GRILL PORK BUTTON AND ITS PRICE
    def grill_pork_color1(e):
        grill_pork_btn.config(bg="#ddffb5")
        grill_pork_price.place(x=624, y=176)

    def grill_pork_color2(e):
        grill_pork_btn.config(bg="#cffc9a")
        grill_pork_price.place_forget()

    grill_pork_btn = Button(pork_frame, text="Grill pork", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                            activebackground="#ddffb5")
    grill_pork_btn.place(x=0, y=80)
    grill_pork_btn.bind("<Enter>", grill_pork_color1)
    grill_pork_btn.bind("<Leave>", grill_pork_color2)
    grill_pork_price = Button(text="14.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # PORK SCHNITZEL BUTTON AND ITS PRICE
    def pork_schnitzel_color1(e):
        pork_schnitzel_btn.config(bg="#ddffb5")
        pork_schnitzel_price.place(x=624, y=236)

    def pork_schnitzel_color2(e):
        pork_schnitzel_btn.config(bg="#cffc9a")
        pork_schnitzel_price.place_forget()

    pork_schnitzel_btn = Button(pork_frame, text="Pork\nschnitzel", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                activebackground="#ddffb5")
    pork_schnitzel_btn.place(x=0, y=140)
    pork_schnitzel_btn.bind("<Enter>", pork_schnitzel_color1)
    pork_schnitzel_btn.bind("<Leave>", pork_schnitzel_color2)
    pork_schnitzel_price = Button(text="14.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # SPICY PORK SAUSAGES BUTTON AND ITS PRICE
    def spicy_pork_sausages_color1(e):
        spicy_pork_sausages_btn.config(bg="#ddffb5")
        spicy_pork_sausages_price.place(x=624, y=296)

    def spicy_pork_sausages_color2(e):
        spicy_pork_sausages_btn.config(bg="#cffc9a")
        spicy_pork_sausages_price.place_forget()

    spicy_pork_sausages_btn = Button(pork_frame, text="Spicy pork\nsausages", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                    activebackground="#ddffb5")
    spicy_pork_sausages_btn.place(x=0, y=200)
    spicy_pork_sausages_btn.bind("<Enter>", spicy_pork_sausages_color1)
    spicy_pork_sausages_btn.bind("<Leave>", spicy_pork_sausages_color2)
    spicy_pork_sausages_price = Button(text="18.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # GORDON BLEU BUTTON AND ITS PRICE
    def gordon_bleu_pork_color1(e):
        gordon_bleu_pork_btn.config(bg="#ddffb5")
        gordon_bleu_pork_price.place(x=624, y=356)

    def gordon_bleu_pork_color2(e):
        gordon_bleu_pork_btn.config(bg="#cffc9a")
        gordon_bleu_pork_price.place_forget()

    gordon_bleu_pork_btn = Button(pork_frame, text="Gordon bleu", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=1, takefocus=0,
                                activebackground="#ddffb5")
    gordon_bleu_pork_btn.place(x=0, y=260)
    gordon_bleu_pork_btn.bind("<Enter>", gordon_bleu_pork_color1)
    gordon_bleu_pork_btn.bind("<Leave>", gordon_bleu_pork_color2)
    gordon_bleu_pork_price = Button(text="21.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # SWEET CHILLI PORK RICE BUTTON AND ITS PRICE
    def sweet_chilli_pork_rice_color1(e):
        sweet_chilli_pork_rice_btn.config(bg="#ddffb5")
        sweet_chilli_pork_rice_price.place(x=624, y=416)

    def sweet_chilli_pork_rice_color2(e):
        sweet_chilli_pork_rice_btn.config(bg="#cffc9a")
        sweet_chilli_pork_rice_price.place_forget()

    sweet_chilli_pork_rice_btn = Button(pork_frame, text="Sweet chilli\npork with\nrice", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=3, takefocus=0,
                                    activebackground="#ddffb5")
    sweet_chilli_pork_rice_btn.place(x=0, y=320)
    sweet_chilli_pork_rice_btn.bind("<Enter>", sweet_chilli_pork_rice_color1)
    sweet_chilli_pork_rice_btn.bind("<Leave>", sweet_chilli_pork_rice_color2)
    sweet_chilli_pork_rice_price = Button(text="25.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=3, takefocus=0)

        # CHICKEN MENU BUTTON
    def chicken_color1(e):
        chicken_btn.config(bg="#ccf2a0")

    def chicken_color2(e):
        chicken_btn.config(bg="#b3f567")

    def show_chicken_frame():
        chicken_frame.place(x=666, y=96)
        chicken_btn.config(command=lambda: hide_chicken_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_chicken_frame():
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())

    chicken_btn = Button(menu_frame, text="Chicken", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_chicken_frame(), activebackground="#ccf2a0",
                        takefocus=0)
    chicken_btn.place(x=635, y=2)
    chicken_btn.bind("<Enter>", chicken_color1)
    chicken_btn.bind("<Leave>", chicken_color2)
    chicken_frame = Frame(width=69, height=380, bg="#cffc9a")

        # CHICKEN MENU OPTIONS
            # BAKED CHICKEN WINGS BUTTON AND ITS PRICE
    def baked_chicken_wings_color1(e):
        baked_chicken_wings_btn.config(bg="#ddffb5")
        baked_chicken_wings_price.place(x=735, y=116)

    def baked_chicken_wings_color2(e):
        baked_chicken_wings_btn.config(bg="#cffc9a")
        baked_chicken_wings_price.place_forget()

    baked_chicken_wings_btn = Button(chicken_frame, text="Baked\nchicken\nwings", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=3, takefocus=0,
                                    activebackground="#ddffb5")
    baked_chicken_wings_btn.place(x=-2, y=20)
    baked_chicken_wings_btn.bind("<Enter>", baked_chicken_wings_color1)
    baked_chicken_wings_btn.bind("<Leave>", baked_chicken_wings_color2)
    baked_chicken_wings_price = Button(text="14.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=3, takefocus=0)

            # CHICKEN BRINE WITH POLENTA BUTTON AND ITS PRICE
    def polenta_chicken_brine_color1(e):
        polenta_chicken_brine_btn.config(bg="#ddffb5")
        polenta_chicken_brine_price.place(x=735, y=191)

    def polenta_chicken_brine_color2(e):
        polenta_chicken_brine_btn.config(bg="#cffc9a")
        polenta_chicken_brine_price.place_forget()

    polenta_chicken_brine_btn = Button(chicken_frame, text="Chicken\nbrine with\npolenta", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=3,
                                    activebackground="#ddffb5", takefocus=0)
    polenta_chicken_brine_btn.place(x=-2, y=95)
    polenta_chicken_brine_btn.bind("<Enter>", polenta_chicken_brine_color1)
    polenta_chicken_brine_btn.bind("<Leave>", polenta_chicken_brine_color2)
    polenta_chicken_brine_price = Button(text="15.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=3, takefocus=0)

            # CHICKEN LIVERS WITH RICE BUTTON AND ITS PRICE
    def rice_chicken_livers_color1(e):
        rice_chicken_livers_btn.config(bg="#ddffb5")
        rice_chicken_livers_price.place(x=735, y=266)

    def rice_chicken_livers_color2(e):
        rice_chicken_livers_btn.config(bg="#cffc9a")
        rice_chicken_livers_price.place_forget()

    rice_chicken_livers_btn = Button(chicken_frame, text="Chicken\nlivers with\nrice", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=3, 
                                    activebackground="#ddffb5", takefocus=0)
    rice_chicken_livers_btn.place(x=-2, y=170)
    rice_chicken_livers_btn.bind("<Enter>", rice_chicken_livers_color1)
    rice_chicken_livers_btn.bind("<Leave>", rice_chicken_livers_color2)
    rice_chicken_livers_price = Button(text="17.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=3, takefocus=0)

            # CHICKEN BURRITO BUTTON AND ITS PRICE
    def chicken_burrito_color1(e):
        chicken_burrito_btn.config(bg="#ddffb5")
        chicken_burrito_price.place(x=735, y=341)

    def chicken_burrito_color2(e):
        chicken_burrito_btn.config(bg="#cffc9a")
        chicken_burrito_price.place_forget()

    chicken_burrito_btn = Button(chicken_frame, text="Chicken\nburrito", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                activebackground="#ddffb5")
    chicken_burrito_btn.place(x=-2, y=245)
    chicken_burrito_btn.bind("<Enter>", chicken_burrito_color1)
    chicken_burrito_btn.bind("<Leave>", chicken_burrito_color2)
    chicken_burrito_price = Button(text="13.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

            # CHICKEN QUESADILLA BUTTON AND ITS PRICE
    def chicken_quesadilla_color1(e):
        chicken_quesadilla_btn.config(bg="#ddffb5")
        chicken_quesadilla_price.place(x=735, y=416)

    def chicken_quesadilla_color2(e):
        chicken_quesadilla_btn.config(bg="#cffc9a")
        chicken_quesadilla_price.place_forget()

    chicken_quesadilla_btn = Button(chicken_frame, text="Chicken\nquesadilla", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=9, height=2, takefocus=0,
                                    activebackground="#ddffb5")
    chicken_quesadilla_btn.place(x=-2, y=320)
    chicken_quesadilla_btn.bind("<Enter>", chicken_quesadilla_color1)
    chicken_quesadilla_btn.bind("<Leave>", chicken_quesadilla_color2)
    chicken_quesadilla_price = Button(text="17.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=2, takefocus=0)

        # DESSERT MENU BUTTON
    def dessert_color1(e):
        dessert_btn.config(bg="#ccf2a0")

    def dessert_color2(e):
        dessert_btn.config(bg="#b3f567")

    def show_dessert_frame():
        dessert_frame.place(x=776, y=96)
        dessert_btn.config(command=lambda: hide_dessert_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    def hide_dessert_frame():
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())

    dessert_btn = Button(menu_frame, text="Dessert", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_dessert_frame(), activebackground="#ccf2a0",
                        takefocus=0)
    dessert_btn.place(x=745, y=2)
    dessert_btn.bind("<Enter>", dessert_color1)
    dessert_btn.bind("<Leave>", dessert_color2)
    dessert_frame = Frame(width=67, height=380, bg="#cffc9a")

        # DESSERT  MENU OPTIONS
            # PAPANASI BUTTON AND ITS PRICE
    def papanasi_dessert_color1(e):
        papanasi_dessert_btn.config(bg="#ddffb5")
        papanasi_dessert_price.place(x=842, y=116)

    def papanasi_dessert_color2(e):
        papanasi_dessert_btn.config(bg="#cffc9a")
        papanasi_dessert_price.place_forget()

    papanasi_dessert_btn = Button(dessert_frame, text="Papanași", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0,
                                activebackground="#ddffb5")
    papanasi_dessert_btn.place(x=0, y=20)
    papanasi_dessert_btn.bind("<Enter>", papanasi_dessert_color1)
    papanasi_dessert_btn.bind("<Leave>", papanasi_dessert_color2)
    papanasi_dessert_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # ICE CREAM BUTTON AND ITS PRICE
    def ice_cream_dessert_color1(e):
        ice_cream_dessert_btn.config(bg="#ddffb5")
        ice_cream_dessert_price.place(x=842, y=191)

    def ice_cream_dessert_color2(e):
        ice_cream_dessert_btn.config(bg="#cffc9a")
        ice_cream_dessert_price.place_forget()

    ice_cream_dessert_btn = Button(dessert_frame, text="Ice cream", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0,
                                activebackground="#ddffb5")
    ice_cream_dessert_btn.place(x=0, y=95)
    ice_cream_dessert_btn.bind("<Enter>", ice_cream_dessert_color1)
    ice_cream_dessert_btn.bind("<Leave>", ice_cream_dessert_color2)
    ice_cream_dessert_price = Button(text="10.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # TIRAMISU BUTTON AND ITS PRICE
    def tiramisu_dessert_color1(e):
        tiramisu_dessert_btn.config(bg="#ddffb5")
        tiramisu_dessert_price.place(x=842, y=266)

    def tiramisu_dessert_color2(e):
        tiramisu_dessert_btn.config(bg="#cffc9a")
        tiramisu_dessert_price.place_forget()

    tiramisu_dessert_btn = Button(dessert_frame, text="Tiramisu", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0,
                                activebackground="#ddffb5")
    tiramisu_dessert_btn.place(x=0, y=170)
    tiramisu_dessert_btn.bind("<Enter>", tiramisu_dessert_color1)
    tiramisu_dessert_btn.bind("<Leave>", tiramisu_dessert_color2)
    tiramisu_dessert_price = Button(text="12.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # CHOCOLATE SUFFLE BUTTON AND ITS PRICE
    def chocolate_souffle_dessert_color1(e):
        chocolate_souffle_dessert_btn.config(bg="#ddffb5")
        chocolate_souffle_dessert_price.place(x=842, y=341)

    def chocolate_souffle_dessert_color2(e):
        chocolate_souffle_dessert_btn.config(bg="#cffc9a")
        chocolate_souffle_dessert_price.place_forget()

    chocolate_souffle_dessert_btn = Button(dessert_frame, text="Chocolate\nsouffle", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=2, takefocus=0,
                                        activebackground="#ddffb5")
    chocolate_souffle_dessert_btn.place(x=0, y=245)
    chocolate_souffle_dessert_btn.bind("<Enter>", chocolate_souffle_dessert_color1)
    chocolate_souffle_dessert_btn.bind("<Leave>", chocolate_souffle_dessert_color2)
    chocolate_souffle_dessert_price = Button(text="13.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # COOKIE CAKE BUTTON AND ITS PRICE
    def cookie_cake_dessert_color1(e):
        cookie_cake_dessert_btn.config(bg="#ddffb5")
        cookie_cake_dessert_price.place(x=842, y=416)

    def cookie_cake_dessert_color2(e):
        cookie_cake_dessert_btn.config(bg="#cffc9a")
        cookie_cake_dessert_price.place_forget()

    cookie_cake_dessert_btn = Button(dessert_frame, text="Cookie\ncake", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=2, takefocus=0,
                                    activebackground="#ddffb5")
    cookie_cake_dessert_btn.place(x=0, y=320)
    cookie_cake_dessert_btn.bind("<Enter>", cookie_cake_dessert_color1)
    cookie_cake_dessert_btn.bind("<Leave>", cookie_cake_dessert_color2)
    cookie_cake_dessert_price = Button(text="8.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

        # DRINKS MENU BUTTON
    def drinks_color1(e):
        drinks_btn.config(bg="#ccf2a0")

    def drinks_color2(e):
        drinks_btn.config(bg="#b3f567")

    def show_drinks_frame():
        drinks_frame.place(x=886, y=96)
        drinks_btn.config(command=lambda: hide_drinks_frame())
        breakfast_frame.place_forget()
        breakfast_btn.config(command=lambda: show_breakfast_frame())
        soups_frame.place_forget()
        soups_btn.config(command=lambda: show_soups_frame())
        pizza_frame.place_forget()
        pizza_btn.config(command=lambda: show_pizza_frame())
        beef_frame.place_forget()
        beef_btn.config(command=lambda: show_beef_frame())
        pork_frame.place_forget()
        pork_btn.config(command=lambda: show_pork_frame())
        chicken_frame.place_forget()
        chicken_btn.config(command=lambda: show_chicken_frame())
        dessert_frame.place_forget()
        dessert_btn.config(command=lambda: show_dessert_frame())

    def hide_drinks_frame():
        drinks_frame.place_forget()
        drinks_btn.config(command=lambda: show_drinks_frame())

    drinks_btn = Button(menu_frame, text="Drinks", font=("Times New Roman", 12, "bold"), relief="flat", bg="#b3f567", command=lambda: show_drinks_frame(), activebackground="#ccf2a0",
                        takefocus=0)
    drinks_btn.place(x=855, y=2)
    drinks_btn.bind("<Enter>", drinks_color1)
    drinks_btn.bind("<Leave>", drinks_color2)
    drinks_frame = Frame(width=60, height=380, bg="#cffc9a")

        # DRINKS MENU OPTIONS
            # TEA BUTTON AND ITS PRICE
    def tea_drink_color1(e):
        tea_drink_btn.config(bg="#ddffb5")
        tea_drink_price.place(x=946, y=116)

    def tea_drink_color2(e):
        tea_drink_btn.config(bg="#cffc9a")
        tea_drink_price.place_forget()

    tea_drink_btn = Button(drinks_frame, text="Tea", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    tea_drink_btn.place(x=0, y=20)
    tea_drink_btn.bind("<Enter>", tea_drink_color1)
    tea_drink_btn.bind("<Leave>", tea_drink_color2)
    tea_drink_price = Button(text="4.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # COFFEE BUTTON AND ITS PRICE
    def coffee_drink_color1(e):
        coffee_drink_btn.config(bg="#ddffb5")
        coffee_drink_price.place(x=946, y=166)

    def coffee_drink_color2(e):
        coffee_drink_btn.config(bg="#cffc9a")
        coffee_drink_price.place_forget()

    coffee_drink_btn = Button(drinks_frame, text="Coffee", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    coffee_drink_btn.place(x=0, y=70)
    coffee_drink_btn.bind("<Enter>", coffee_drink_color1)
    coffee_drink_btn.bind("<Leave>", coffee_drink_color2)
    coffee_drink_price = Button(text="5.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # LEMONADE BUTTON AND ITS PRICE
    def lemonade_drink_color1(e):
        lemonade_drink_btn.config(bg="#ddffb5")
        lemonade_drink_price.place(x=946, y=216)

    def lemonade_drink_color2(e):
        lemonade_drink_btn.config(bg="#cffc9a")
        lemonade_drink_price.place_forget()

    lemonade_drink_btn = Button(drinks_frame, text="Lemonade", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0,
                                activebackground="#ddffb5")
    lemonade_drink_btn.place(x=0, y=120)
    lemonade_drink_btn.bind("<Enter>", lemonade_drink_color1)
    lemonade_drink_btn.bind("<Leave>", lemonade_drink_color2)
    lemonade_drink_price = Button(text="8.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # JUICE BUTTON AND ITS PRICE
    def juice_drink_color1(e):
        juice_drink_btn.config(bg="#ddffb5")
        juice_drink_price.place(x=946, y=266)

    def juice_drink_color2(e):
        juice_drink_btn.config(bg="#cffc9a")
        juice_drink_price.place_forget()

    juice_drink_btn = Button(drinks_frame, text="Juice", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    juice_drink_btn.place(x=0, y=170)
    juice_drink_btn.bind("<Enter>", juice_drink_color1)
    juice_drink_btn.bind("<Leave>", juice_drink_color2)
    juice_drink_price = Button(text="4.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # JUICE BUTTON AND ITS PRICE
    def water_drink_color1(e):
        water_drink_btn.config(bg="#ddffb5")
        water_drink_price.place(x=946, y=316)

    def water_drink_color2(e):
        water_drink_btn.config(bg="#cffc9a")
        water_drink_price.place_forget()

    water_drink_btn = Button(drinks_frame, text="Water", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    water_drink_btn.place(x=0, y=220)
    water_drink_btn.bind("<Enter>", water_drink_color1)
    water_drink_btn.bind("<Leave>", water_drink_color2)
    water_drink_price = Button(text="3.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # BEER BUTTON AND ITS PRICE
    def beer_drink_color1(e):
        beer_drink_btn.config(bg="#ddffb5")
        beer_drink_price.place(x=946, y=366)

    def beer_drink_color2(e):
        beer_drink_btn.config(bg="#cffc9a")
        beer_drink_price.place_forget()

    beer_drink_btn = Button(drinks_frame, text="Beer", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    beer_drink_btn.place(x=0, y=270)
    beer_drink_btn.bind("<Enter>", beer_drink_color1)
    beer_drink_btn.bind("<Leave>", beer_drink_color2)
    beer_drink_price = Button(text="7.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

            # WINE BUTTON AND ITS PRICE
    def wine_drink_color1(e):
        wine_drink_btn.config(bg="#ddffb5")
        wine_drink_price.place(x=946, y=416)

    def wine_drink_color2(e):
        wine_drink_btn.config(bg="#cffc9a")
        wine_drink_price.place_forget()

    wine_drink_btn = Button(drinks_frame, text="Wine", font=("Times New Roman", 10, "bold"), relief="flat", bg="#cffc9a", width=8, height=1, takefocus=0, activebackground="#ddffb5")
    wine_drink_btn.place(x=0, y=320)
    wine_drink_btn.bind("<Enter>", wine_drink_color1)
    wine_drink_btn.bind("<Leave>", wine_drink_color2)
    wine_drink_price = Button(text="18.90$", font=("Times New Roman", 10, "bold"), relief="flat", state="disabled", bg="#ddffb5", height=1, takefocus=0)

    # LEFT FRAME1
    left_frame1 = Frame(height=600, width=30, bg="#ebcd7c")
    left_frame1.place(x=0, y=0)

    store_window.title("Store's food and orders administration")
    store_window.geometry("1000x600")
    store_window.mainloop()