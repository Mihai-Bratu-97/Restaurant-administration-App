from tkinter import Frame, Label, Button
import datetime
import random
from store_images import*

even_odd = 0
choose_random_between_menu_list = [["breakfast", 20000], ["soups", 28000], ["pizza", 28000], ["beef", 20000], ["pork", 24000], ["chicken", 20000], 
                                   ["dessert", 20000], ["drinks", 28000]]
used_menu_list = []

new_x2 = -2449
count_breakfast_images = 1

new_x3 = -3429
count_soups_images = 1

new_x4 = -3429
count_pizza_images = 1

new_x5 = -2449
count_beef_images = 1

new_x6 = -2939
count_pork_images = 1

new_x7 = -2449
count_chicken_images = 1

new_x8 = -2449
count_dessert_images = 1

new_x9 = -3429
count_drinks_images = 1

count_calling = 0

cancel_after_widget = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], None]

def animating_images(image_frame):
    global fried_eggs_img, boiled_eggs_img, omlette_img, cereals_with_milk_img, pancakes_img,\
    tripe_soup_img, beef_soup_img, chicken_soup_img, tomatoes_soup_img, greek_soup_img, pork_soup_img, bean_soup_img,\
    pizza_quattro_stagioni_img, pizza_quattro_formaggi_img, pizza_capricciosa_img, pizza_margerita_img, pizza_diavola_img, pizza_calzone_img, pizza_hawaii_img,\
    grill_beef_img, beef_pasta_img, beef_hamburger_img, gorgonzola_sauce_beef_img, beef_stew_img,\
    pork_skewers_img, grill_pork_img, pork_schnitzel_img, spicy_pork_sausages_img, gordon_bleu_img, sweet_chilli_pork_rice_img,\
    baked_chicken_wings_img, polenta_chicken_brine_img, rice_chicken_livers_img, chicken_burrito_img, chicken_quesadilla_img,\
    papanasi_img, ice_cream_img, tiramisu_img, chocolate_souffle_img, cookie_cake_img,\
    tea_img, coffee_img, lemonade_img, juice_img, water_img, beer_img, wine_img, count_calling, cancel_after_widget

    # BREAKFAST
        # BREAKFAST FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
    if count_calling == 0:
        def start_breakfast_img_animation():
            global new_x2
            if new_x2 == -2449:
                breakfast_image_frame.place(x=-2450, y=0)
            if new_x2 % 490 != 0:
                new_x2 += 1
                breakfast_image_frame.place(x=new_x2)
            if new_x2 == 0:
                new_x2 = -2449
                return True
            if new_x2 % 490 == 0:
                new_x2 += 1
                return True
            cancel_after_widget[0][0] = image_frame.after(4, start_breakfast_img_animation)

        def stop_time_for_breakfast_img():
            global count_breakfast_images
            if count_breakfast_images == 6:
                count_breakfast_images = 1
                breakfast_image_frame.place_forget()
                return True
            start_breakfast_img_animation()
            count_breakfast_images += 1
            cancel_after_widget[0][1] = image_frame.after(4000, stop_time_for_breakfast_img)

            # BREAKFAST FRAME
        breakfast_image_frame = Frame(image_frame, width=2940, height=550)

            # BREAKFAST IMAGES
        fried_eggs_img, boiled_eggs_img, omlette_img, cereals_with_milk_img, pancakes_img = breakfast_images()

            # BREAKFAST OPTIONS AND ITS WIDGETS
                # FRIED EGGS
        fried_eggs_label_img = Label(breakfast_image_frame, image=fried_eggs_img, bd=0)
        fried_eggs_label_img.place(x=2450, y=0)
        fried_eggs_btn = Button(breakfast_image_frame, text="Fried eggs", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        fried_eggs_btn.place(x=2653, y=20)

                # BOILED EGGS
        boiled_eggs_label_img = Label(breakfast_image_frame, image=boiled_eggs_img, bd=0)
        boiled_eggs_label_img.place(x=1960, y=0)
        boiled_eggs_btn = Button(breakfast_image_frame, text="Boiled eggs", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        boiled_eggs_btn.place(x=2160, y=20)

                # OMLETTE
        omlette_label_img = Label(breakfast_image_frame, image=omlette_img, bd=0)
        omlette_label_img.place(x=1470, y=0)
        omlette_btn = Button(breakfast_image_frame, text="Omlette", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        omlette_btn.place(x=1682, y=20)

                # CEREALS WITH MILK
        cereals_with_milk_label_img = Label(breakfast_image_frame, image=cereals_with_milk_img, bd=0)
        cereals_with_milk_label_img.place(x=980, y=0)
        cereals_with_milk_btn = Button(breakfast_image_frame, text="Cereals with milk", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        cereals_with_milk_btn.place(x=1156, y=20)

                # PANCAKES
        pancakes_label_img = Label(breakfast_image_frame, image=pancakes_img, bd=0)
        pancakes_label_img.place(x=490, y=0)
        pancakes_btn = Button(breakfast_image_frame, text="Pancakes", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pancakes_btn.place(x=696, y=20)

                # FRIED EGGS COPY
        fried_eggs_label_img_copy = Label(breakfast_image_frame, image=fried_eggs_img, bd=0)
        fried_eggs_label_img_copy.place(x=0, y=0)
        fried_eggs_btn_copy = Button(breakfast_image_frame, text="Fried eggs", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        fried_eggs_btn_copy.place(x=203, y=20)

        # SOUPS
            # SOUPS FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_soups_img_animation():
            global new_x3, cancel_after_widget1
            if new_x3 == -3429:
                soups_image_frame.place(x=-3430, y=0)
            if new_x3 % 490 != 0:
                new_x3 += 1
                soups_image_frame.place(x=new_x3)
            if new_x3 == 0:
                new_x3 = -3429
                return True
            if new_x3 % 490 == 0:
                new_x3 += 1
                return True
            cancel_after_widget[1][0] = image_frame.after(4, start_soups_img_animation)

        def stop_time_for_soups_img():
            global count_soups_images, cancel_after_widget2
            if count_soups_images == 8:
                soups_image_frame.place_forget()
                count_soups_images = 1
                return True
            start_soups_img_animation()
            count_soups_images += 1
            cancel_after_widget[1][1] = image_frame.after(4000, stop_time_for_soups_img)

            # SOUPS FRAME
        soups_image_frame = Frame(image_frame, width=3920, height=550)

            # SOUPS IMAGES
        tripe_soup_img, beef_soup_img, chicken_soup_img, tomatoes_soup_img, greek_soup_img, pork_soup_img, bean_soup_img = soups_images()

            # SOUPS OPTIONS AND ITS WIDGETS
                # TRIPE SOUP
        tripe_soup_label_img = Label(soups_image_frame, image=tripe_soup_img, bd=0)
        tripe_soup_label_img.place(x=3430, y=0)
        tripe_soup_btn = Button(soups_image_frame, text="Tripe soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tripe_soup_btn.place(x=3633, y=20)

                # BEEF SOUP
        beef_soup_label_img = Label(soups_image_frame, image=beef_soup_img, bd=0)
        beef_soup_label_img.place(x=2940, y=0)
        beef_soup_btn = Button(soups_image_frame, text="Beef soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        beef_soup_btn.place(x=3146, y=20)

                # CHICKEN SOUP
        chicken_soup_label_img = Label(soups_image_frame, image=chicken_soup_img, bd=0)
        chicken_soup_label_img.place(x=2450, y=0)
        chicken_soup_btn = Button(soups_image_frame, text="Chicken soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        chicken_soup_btn.place(x=2643, y=20)

                # TOMATOES SOUP
        tomatoes_soup_label_img = Label(soups_image_frame, image=tomatoes_soup_img, bd=0)
        tomatoes_soup_label_img.place(x=1960, y=0)
        tomatoes_soup_btn = Button(soups_image_frame, text="Tomatoes soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tomatoes_soup_btn.place(x=2149, y=20)

                # GREEK SOUP
        greek_soup_label_img = Label(soups_image_frame, image=greek_soup_img, bd=0)
        greek_soup_label_img.place(x=1470, y=0)
        greek_soup_btn = Button(soups_image_frame, text="Greek soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        greek_soup_btn.place(x=1671, y=20)

                # PORK SOUP
        pork_soup_label_img = Label(soups_image_frame, image=pork_soup_img, bd=0)
        pork_soup_label_img.place(x=980, y=0)
        pork_soup_btn = Button(soups_image_frame, text="Pork soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pork_soup_btn.place(x=1185, y=20)

                # BEAN SOUP
        bean_soup_label_img = Label(soups_image_frame, image=bean_soup_img, bd=0)
        bean_soup_label_img.place(x=490, y=0)
        bean_soup_btn = Button(soups_image_frame, text="Bean soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        bean_soup_btn.place(x=693, y=20)

                # TRIPE SOUP COPY
        tripe_soup_label_img_copy = Label(soups_image_frame, image=tripe_soup_img, bd=0)
        tripe_soup_label_img_copy.place(x=0, y=0)
        tripe_soup_btn_copy = Button(soups_image_frame, text="Tripe soup", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tripe_soup_btn_copy.place(x=203, y=20)

        # PIZZA
            # PIZZA FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_pizza_img_animation():
            global new_x4
            if new_x4 == -3429:
                pizza_image_frame.place(x=-3430, y=0)
            if new_x4 % 490 != 0:
                new_x4 += 1
                pizza_image_frame.place(x=new_x4)
            if new_x4 == 0:
                new_x4 = -3429
                return True
            if new_x4 % 490 == 0:
                new_x4 += 1
                return True
            cancel_after_widget[2][0] = image_frame.after(4, start_pizza_img_animation)

        def stop_time_for_pizza_img():
            global count_pizza_images
            if count_pizza_images == 8:
                count_pizza_images = 1
                pizza_image_frame.place_forget()
                return True
            start_pizza_img_animation()
            count_pizza_images += 1
            cancel_after_widget[2][1] = image_frame.after(4000, stop_time_for_pizza_img)

            # PIZZA FRAME
        pizza_image_frame = Frame(image_frame, width=3920, height=550)

            # PIZZA IMAGES
        pizza_quattro_stagioni_img, pizza_quattro_formaggi_img, pizza_capricciosa_img, pizza_margerita_img, pizza_diavola_img, pizza_calzone_img, pizza_hawaii_img = pizza_images()

            # PIZZA OPTIONS AND ITS WIDGETS
                # PIZZA QUATTRO STAGIONI
        pizza_quattro_stagioni_label_img = Label(pizza_image_frame, image=pizza_quattro_stagioni_img, bd=0)
        pizza_quattro_stagioni_label_img.place(x=3430, y=0)
        pizza_quattro_stagioni_btn = Button(pizza_image_frame, text="Pizza quattro stagioni", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                            activeforeground="white")
        pizza_quattro_stagioni_btn.place(x=3592, y=20)

                # PIZZA QUATTRO FORMAGGI
        pizza_quattro_formaggi_label_img = Label(pizza_image_frame, image=pizza_quattro_formaggi_img, bd=0)
        pizza_quattro_formaggi_label_img.place(x=2940, y=0)
        pizza_quattro_formaggi_btn = Button(pizza_image_frame, text="Pizza quattro formaggi", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                            activeforeground="white")
        pizza_quattro_formaggi_btn.place(x=3099, y=20)

                # PIZZA CAPRICCIOSA
        pizza_capricciosa_label_img = Label(pizza_image_frame, image=pizza_capricciosa_img, bd=0)
        pizza_capricciosa_label_img.place(x=2450, y=0)
        pizza_capricciosa_btn = Button(pizza_image_frame, text="Pizza capricciosa", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pizza_capricciosa_btn.place(x=2631, y=20)

                # PIZZA MARGERITA
        pizza_margerita_label_img = Label(pizza_image_frame, image=pizza_margerita_img, bd=0)
        pizza_margerita_label_img.place(x=1960, y=0)
        pizza_margerita_btn = Button(pizza_image_frame, text="Pizza margerita", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pizza_margerita_btn.place(x=2143, y=20)

                # PIZZA DIAVOLA
        pizza_diavola_label_img = Label(pizza_image_frame, image=pizza_diavola_img, bd=0)
        pizza_diavola_label_img.place(x=1470, y=0)
        pizza_diavola_btn = Button(pizza_image_frame, text="Pizza diavola", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pizza_diavola_btn.place(x=1663, y=20)

                # PIZZA CALZONE
        pizza_calzone_label_img = Label(pizza_image_frame, image=pizza_calzone_img, bd=0)
        pizza_calzone_label_img.place(x=980, y=0)
        pizza_calzone_btn = Button(pizza_image_frame, text="Pizza calzone", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pizza_calzone_btn.place(x=1174, y=20)

                # PIZZA HAWAII
        pizza_hawaii_label_img = Label(pizza_image_frame, image=pizza_hawaii_img, bd=0)
        pizza_hawaii_label_img.place(x=490, y=0)
        pizza_hawaii_btn = Button(pizza_image_frame, text="Pizza hawaii", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pizza_hawaii_btn.place(x=684, y=20)

                # PIZZA QUATTRO STAGIONI COPY
        pizza_quattro_stagioni_label_img_copy = Label(pizza_image_frame, image=pizza_quattro_stagioni_img, bd=0)
        pizza_quattro_stagioni_label_img_copy.place(x=0, y=0)
        pizza_quattro_stagioni_btn_copy = Button(pizza_image_frame, text="Pizza quattro stagioni", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                                 activeforeground="white")
        pizza_quattro_stagioni_btn_copy.place(x=162, y=20)

        # BEEF
            # BEEF FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_beef_img_animation():
            global new_x5
            if new_x5 == -2449:
                beef_image_frame.place(x=-2450, y=0)
            if new_x5 % 490 != 0:
                new_x5 += 1
                beef_image_frame.place(x=new_x5)
            if new_x5 == 0:
                new_x5 = -2449
                return True
            if new_x5 % 490 == 0:
                new_x5 += 1
                return True
            cancel_after_widget[3][0] = image_frame.after(4, start_beef_img_animation)

        def stop_time_for_beef_img():
            global count_beef_images
            if count_beef_images == 6:
                count_beef_images = 1
                beef_image_frame.place_forget()
                return True
            start_beef_img_animation()
            count_beef_images += 1
            cancel_after_widget[3][1] = image_frame.after(4000, stop_time_for_beef_img)

            # BEEF FRAME
        beef_image_frame = Frame(image_frame, width=2940, height=550)

            # BEEF IMAGES
        grill_beef_img, beef_pasta_img, beef_hamburger_img, gorgonzola_sauce_beef_img, beef_stew_img = beef_images()

            # BEEF OPTIONS AND ITS WIDGETS
                # GRILL BEEF
        grill_beef_label_img = Label(beef_image_frame, image=grill_beef_img, bd=0)
        grill_beef_label_img.place(x=2450, y=0)
        grill_beef_btn = Button(beef_image_frame, text="Grill beef", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        grill_beef_btn.place(x=2657, y=20)

                # BEEF PASTA
        beef_pasta_label_img = Label(beef_image_frame, image=beef_pasta_img, bd=0)
        beef_pasta_label_img.place(x=1960, y=0)
        beef_pasta_btn = Button(beef_image_frame, text="Beef pasta", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        beef_pasta_btn.place(x=2162, y=20)

                # BEEF HAMBURGER
        beef_hamburger_label_img = Label(beef_image_frame, image=beef_hamburger_img, bd=0)
        beef_hamburger_label_img.place(x=1470, y=0)
        beef_hamburger_btn = Button(beef_image_frame, text="Beef hamburger", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        beef_hamburger_btn.place(x=1652, y=20)

                # GORGONZOLA SAUCE BEEF
        gorgonzola_sauce_beef_label_img = Label(beef_image_frame, image=gorgonzola_sauce_beef_img, bd=0)
        gorgonzola_sauce_beef_label_img.place(x=980, y=0)
        gorgonzola_sauce_beef_btn = Button(beef_image_frame, text="Beef with\ngorgonzola sauce", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                           activeforeground="white")
        gorgonzola_sauce_beef_btn.place(x=1124, y=20)

                # BEEF STEW
        beef_stew_label_img = Label(beef_image_frame, image=beef_stew_img, bd=0)
        beef_stew_label_img.place(x=490, y=0)
        beef_stew_btn = Button(beef_image_frame, text="Beef stew", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        beef_stew_btn.place(x=695, y=20)

                # GRILL BEEF COPY
        grill_beef_label_img_copy = Label(beef_image_frame, image=grill_beef_img, bd=0)
        grill_beef_label_img_copy.place(x=0, y=0)
        grill_beef_btn_copy = Button(beef_image_frame, text="Grill beef", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        grill_beef_btn_copy.place(x=207, y=20)

        # PORK
            # PORK FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_pork_img_animation():
            global new_x6
            if new_x6 == -2939:
                pork_image_frame.place(x=-2940, y=0)
            if new_x6 % 490 != 0:
                new_x6 += 1
                pork_image_frame.place(x=new_x6)
            if new_x6 == 0:
                new_x6 = -2939
                return True
            if new_x6 % 490 == 0:
                new_x6 += 1
                return True
            cancel_after_widget[4][0] = image_frame.after(4, start_pork_img_animation)

        def stop_time_for_pork_img():
            global count_pork_images
            if count_pork_images == 7:
                count_pork_images = 1
                pork_image_frame.place_forget()
                return True
            start_pork_img_animation()
            count_pork_images += 1
            cancel_after_widget[4][1] = image_frame.after(4000, stop_time_for_pork_img)

            # PORK FRAME
        pork_image_frame = Frame(image_frame, width=3430, height=550)

            # PORK IMAGES
        pork_skewers_img, grill_pork_img, pork_schnitzel_img, spicy_pork_sausages_img, gordon_bleu_img, sweet_chilli_pork_rice_img = pork_images()

            # PORK OPTIONS AND ITS WIDGETS
                # PORK SKEWERS
        pork_skewers_label_img = Label(pork_image_frame, image=pork_skewers_img, bd=0)
        pork_skewers_label_img.place(x=2940, y=0)
        pork_skewers_btn = Button(pork_image_frame, text="Pork skewers", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pork_skewers_btn.place(x=3132, y=20)

                # GRILL PORK
        grill_pork_label_img = Label(pork_image_frame, image=grill_pork_img, bd=0)
        grill_pork_label_img.place(x=2450, y=0)
        grill_pork_btn = Button(pork_image_frame, text="Grill pork", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        grill_pork_btn.place(x=2655, y=20)

                # PORK SCHNITZEL
        pork_schnitzel_label_img = Label(pork_image_frame, image=pork_schnitzel_img, bd=0)
        pork_schnitzel_label_img.place(x=1960, y=0)
        pork_schnitzel_btn = Button(pork_image_frame, text="Pork schnitzel", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pork_schnitzel_btn.place(x=2150, y=20)

                # SPICY PORK SAUSAGES
        spicy_pork_sausages_label_img = Label(pork_image_frame, image=spicy_pork_sausages_img, bd=0)
        spicy_pork_sausages_label_img.place(x=1470, y=0)
        spicy_pork_sausages_btn = Button(pork_image_frame, text="Spicy pork sausages", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        spicy_pork_sausages_btn.place(x=1639, y=20)

                # GORDON BLEU
        gordon_bleu_label_img = Label(pork_image_frame, image=gordon_bleu_img, bd=0)
        gordon_bleu_label_img.place(x=980, y=0)
        gordon_bleu_btn = Button(pork_image_frame, text="Gordon bleu", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        gordon_bleu_btn.place(x=1178, y=20)

                # SWEET CHILLI PORK RICE
        sweet_chilli_pork_rice_label_img_copy = Label(pork_image_frame, image=sweet_chilli_pork_rice_img, bd=0)
        sweet_chilli_pork_rice_label_img_copy.place(x=490, y=0)
        sweet_chilli_pork_rice_btn = Button(pork_image_frame, text="Sweet chilli pork with rice", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                            activeforeground="white")
        sweet_chilli_pork_rice_btn.place(x=636, y=20)

                # PORK SKEWERS COPY
        pork_skewers_label_img_copy = Label(pork_image_frame, image=pork_skewers_img, bd=0)
        pork_skewers_label_img_copy.place(x=0, y=0)
        pork_skewers_btn_copy = Button(pork_image_frame, text="Pork skewers", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        pork_skewers_btn_copy.place(x=192, y=20)

        # CHICKEN
            # CHICKEN FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_chicken_img_animation():
            global new_x7
            if new_x7 == -2449:
                chicken_image_frame.place(x=-2450, y=0)
            if new_x7 % 490 != 0:
                new_x7 += 1
                chicken_image_frame.place(x=new_x7)
            if new_x7 == 0:
                new_x7 = -2449
                return True
            if new_x7 % 490 == 0:
                new_x7 += 1
                return True
            cancel_after_widget[5][0] = image_frame.after(4, start_chicken_img_animation)

        def stop_time_for_chicken_img():
            global count_chicken_images
            if count_chicken_images == 6:
                count_chicken_images = 1
                chicken_image_frame.place_forget()
                return True
            start_chicken_img_animation()
            count_chicken_images += 1
            cancel_after_widget[5][1] = image_frame.after(4000, stop_time_for_chicken_img)

            # CHICKEN FRAME
        chicken_image_frame = Frame(image_frame, width=2940, height=550)

            # CHICKEN IMAGES
        baked_chicken_wings_img, polenta_chicken_brine_img, rice_chicken_livers_img, chicken_burrito_img, chicken_quesadilla_img = chicken_images()

            # CHICKEN OPTIONS AND ITS WIDGETS
                # BAKED CHIKCEN WINGS
        baked_chicken_wings_label_img = Label(chicken_image_frame, image=baked_chicken_wings_img, bd=0)
        baked_chicken_wings_label_img.place(x=2450, y=0)
        baked_chicken_wings_btn = Button(chicken_image_frame, text="Baked chicken wings", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                         activeforeground="white")
        baked_chicken_wings_btn.place(x=2615, y=20)

                # POLENTA CHICKEN BRINE
        polenta_chicken_brine_label_img = Label(chicken_image_frame, image=polenta_chicken_brine_img, bd=0)
        polenta_chicken_brine_label_img.place(x=1960, y=0)
        polenta_chicken_brine_btn = Button(chicken_image_frame, text="Polenta chicken brine", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                           activeforeground="white")
        polenta_chicken_brine_btn.place(x=2124, y=20)

                # RICE CHICKEN LIVERS
        rice_chicken_livers_label_img = Label(chicken_image_frame, image=rice_chicken_livers_img, bd=0)
        rice_chicken_livers_label_img.place(x=1470, y=0)
        rice_chicken_livers_btn = Button(chicken_image_frame, text="Rice chicken livers", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                         activeforeground="white")
        rice_chicken_livers_btn.place(x=1644, y=20)

                # CHICKEN BURRITO
        chicken_burrito_label_img = Label(chicken_image_frame, image=chicken_burrito_img, bd=0)
        chicken_burrito_label_img.place(x=980, y=0)
        chicken_burrito_btn = Button(chicken_image_frame, text="Chicken burrito", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        chicken_burrito_btn.place(x=1164, y=20)

                # CHICKEN QUESADILLA
        chicken_quesadilla_label_img = Label(chicken_image_frame, image=chicken_quesadilla_img, bd=0)
        chicken_quesadilla_label_img.place(x=490, y=0)
        chicken_quesadilla_btn = Button(chicken_image_frame, text="Chicken quesadilla", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        chicken_quesadilla_btn.place(x=662, y=20)

                # BAKED CHICKEN WINGS COPY
        baked_chicken_wings_label_img_copy = Label(chicken_image_frame, image=baked_chicken_wings_img, bd=0)
        baked_chicken_wings_label_img_copy.place(x=0, y=0)
        baked_chicken_wings_copy_btn = Button(chicken_image_frame, text="Baked chicken wings", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580",
                                              activeforeground="white")
        baked_chicken_wings_copy_btn.place(x=165, y=20)

        # DESSERT
            # DESSERT FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_dessert_img_animation():
            global new_x8
            if new_x8 == -2449:
                dessert_image_frame.place(x=-2450, y=0)
            if new_x8 % 490 != 0:
                new_x8 += 1
                dessert_image_frame.place(x=new_x8)
            if new_x8 == 0:
                new_x8 = -2449
                return True
            if new_x8 % 490 == 0:
                new_x8 += 1
                return True
            cancel_after_widget[6][0] = image_frame.after(4, start_dessert_img_animation)

        def stop_time_for_dessert_img():
            global count_dessert_images
            if count_dessert_images == 6:
                count_dessert_images = 1
                dessert_image_frame.place_forget()
                return True
            start_dessert_img_animation()
            count_dessert_images += 1
            cancel_after_widget[6][1] = image_frame.after(4000, stop_time_for_dessert_img)

            # DESSERT FRAME
        dessert_image_frame = Frame(image_frame, width=2940, height=550)

            # DESSERT IMAGES
        papanasi_img, ice_cream_img, tiramisu_img, chocolate_souffle_img, cookie_cake_img = dessert_images()

            # DESSERT OPTIONS AND ITS WIDGETS
                # PAPANASI
        papanasi_label_img = Label(dessert_image_frame, image=papanasi_img, bd=0)
        papanasi_label_img.place(x=2450, y=0)
        papanasi_btn = Button(dessert_image_frame, text="Papanași", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        papanasi_btn.place(x=2656, y=20)

                # ICE CREAM
        ice_cream_label_img = Label(dessert_image_frame, image=ice_cream_img, bd=0)
        ice_cream_label_img.place(x=1960, y=0)
        ice_cream_btn = Button(dessert_image_frame, text="Ice cream", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        ice_cream_btn.place(x=2165, y=20)

                # TIRAMISU
        tiramisu_label_img = Label(dessert_image_frame, image=tiramisu_img, bd=0)
        tiramisu_label_img.place(x=1470, y=0)
        tiramisu_btn = Button(dessert_image_frame, text="Tiramisu", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tiramisu_btn.place(x=1677, y=20)

                # CHOCOLATE SOUFFLE
        chocolate_souffle_label_img = Label(dessert_image_frame, image=chocolate_souffle_img, bd=0)
        chocolate_souffle_label_img.place(x=980, y=0)
        chocolate_souffle_btn = Button(dessert_image_frame, text="Chocolate souffle", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        chocolate_souffle_btn.place(x=1160, y=20)

                # COOKIE CAKE
        cookie_cake_label_img = Label(dessert_image_frame, image=cookie_cake_img, bd=0)
        cookie_cake_label_img.place(x=490, y=0)
        cookie_cake_btn = Button(dessert_image_frame, text="Cookie cake", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        cookie_cake_btn.place(x=689, y=20)

                # PAPANASI COPY
        papanasi_label_img_copy = Label(dessert_image_frame, image=papanasi_img, bd=0)
        papanasi_label_img_copy.place(x=0, y=0)
        papanasi_btn_copy = Button(dessert_image_frame, text="Papanași", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        papanasi_btn_copy.place(x=206, y=20)

        # DRINKS
            # DRINKS FRAME AND ITS FUNCTIONS FOR ANIMATING THE IMAGES
        def start_drinks_img_animation():
            global new_x9
            if new_x9 == -3429:
                drinks_image_frame.place(x=-3430, y=0)
            if new_x9 % 490 != 0:
                new_x9 += 1
                drinks_image_frame.place(x=new_x9)
            if new_x9 == 0:
                new_x9 = -3429
                return True
            if new_x9 % 490 == 0:
                new_x9 += 1
                return True
            cancel_after_widget[7][0] = image_frame.after(4, start_drinks_img_animation)

        def stop_time_for_drinks_img():
            global count_drinks_images
            if count_drinks_images == 8:
                count_drinks_images = 1
                drinks_image_frame.place_forget()
                return True
            start_drinks_img_animation()
            count_drinks_images += 1
            cancel_after_widget[7][1] = image_frame.after(4000, stop_time_for_drinks_img)

            # DRINKS FRAME
        drinks_image_frame = Frame(image_frame, width=3920, height=550)

            # DRINKS IMAGES
        tea_img, coffee_img, lemonade_img, juice_img, water_img, beer_img, wine_img = drinks_images()

            # DRINKS OPTIONS AND ITS WIDGETS
                # TEA
        tea_label_img = Label(drinks_image_frame, image=tea_img, bd=0)
        tea_label_img.place(x=3430, y=0)
        tea_btn = Button(drinks_image_frame, text="Tea", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tea_btn.place(x=3657, y=20)

                # COFFEE
        coffee_label_img = Label(drinks_image_frame, image=coffee_img, bd=0)
        coffee_label_img.place(x=2940, y=0)
        coffee_btn = Button(drinks_image_frame, text="Coffee", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        coffee_btn.place(x=3158, y=20)

                # LEMONADE
        lemonade_label_img = Label(drinks_image_frame, image=lemonade_img, bd=0)
        lemonade_label_img.place(x=2450, y=0)
        lemonade_btn = Button(drinks_image_frame, text="Lemonade", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        lemonade_btn.place(x=2654, y=20)

                # JUICE
        juice_label_img = Label(drinks_image_frame, image=juice_img, bd=0)
        juice_label_img.place(x=1960, y=0)
        juice_btn = Button(drinks_image_frame, text="Juice", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        juice_btn.place(x=2182, y=20)

                # WATER
        water_label_img = Label(drinks_image_frame, image=water_img, bd=0)
        water_label_img.place(x=1470, y=0)
        water_btn = Button(drinks_image_frame, text="Water", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        water_btn.place(x=1686, y=20)

                # BEER
        beer_label_img = Label(drinks_image_frame, image=beer_img, bd=0)
        beer_label_img.place(x=980, y=0)
        beer_btn = Button(drinks_image_frame, text="Beer", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        beer_btn.place(x=1203, y=20)

                # WINE
        wine_label_img = Label(drinks_image_frame, image=wine_img, bd=0)
        wine_label_img.place(x=490, y=0)
        wine_btn = Button(drinks_image_frame, text="Wine", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        wine_btn.place(x=710, y=20)

                # TEA COPY
        tea_label_img_copy = Label(drinks_image_frame, image=tea_img, bd=0)
        tea_label_img_copy.place(x=0, y=0)
        tea_btn_copy = Button(drinks_image_frame, text="Tea", font=("Dancing Script", 15), bd=0, bg="#acfaf5", activebackground="#3a8580", activeforeground="white")
        tea_btn_copy.place(x=227, y=20)

        # CLOCK FOR CHECKING WHICH IMAGES WILL BE SHOWN
        def check_clock():
            today = datetime.datetime.today()
            return today.hour

        # A FUNCTION FOR CHOOSING RANDOM MENU TO SHOW IMAGES ACCORDING TO THE CLOCK
        def choose_between_food_images():
            global used_menu_list, even_odd, cancel_after_widget
            clock = check_clock()
            if 12 > clock >= 7:
                if even_odd % 2 == 0:
                    random_menu = choose_random_between_menu_list[0]
                    stop_time_for_breakfast_img()
                else:
                    random_menu = choose_random_between_menu_list[-1]
                    stop_time_for_drinks_img()
                even_odd += 1
            else:
                if len(used_menu_list) == 7:
                    used_menu_list = []
                random_menu = random.choice(choose_random_between_menu_list)
                while random_menu in used_menu_list or random_menu == ["breakfast", 20000]:
                    random_menu = random.choice(choose_random_between_menu_list)
                used_menu_list.append(random_menu)
                if random_menu[0] == "soups":
                    stop_time_for_soups_img()
                elif random_menu[0] == "pizza":
                    stop_time_for_pizza_img()
                elif random_menu[0] == "beef":
                    stop_time_for_beef_img()
                elif random_menu[0] == "pork":
                    stop_time_for_pork_img()
                elif random_menu[0] == "chicken":
                    stop_time_for_chicken_img()
                elif random_menu[0] == "dessert":
                    stop_time_for_dessert_img()
                elif random_menu[0] == "drinks":
                    stop_time_for_drinks_img()
            cancel_after_widget[8] = image_frame.after(random_menu[1], choose_between_food_images)

        count_calling += 1

        choose_between_food_images()
    else:
        for i in range(len(cancel_after_widget) - 1):
            for j in range(2):
                if cancel_after_widget[i][j] != None:
                    image_frame.after_cancel(cancel_after_widget[i][j])
        image_frame.after_cancel(cancel_after_widget[-1])
