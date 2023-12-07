import flet as ft
import random
import string

def main(page:ft.Page):
    page.title="Password Generator"
    page.window_height=500
    page.window_width=500
    page.vertical_alignment= "center"
    page.horizontal_alignment="center"



    def slider_changed(e):
        t.value = int(e.control.value)
        page.update()
    def slider1_changed(e):
        t1.value= int(e.control.value)
        page.update() 
    def slider2_changed(e):
        t2.value= int(e.control.value)
        page.update()
    def slider3_changed(e):
        t3.value= int(e.control.value)
        page.update()
    def generate_pwd(e):
        rnd_letters = random.choices(string.ascii_letters, k= t1.value)
        rnd_num = random.choices(string.digits, k=t2.value)
        rnd_special = random.choices(string.punctuation, k=t3.value)
        password ="".join( rnd_letters + rnd_num + rnd_special)
        password = list(password)
        random.shuffle(password)
        password = "".join(password)
        t4.value = password
        page.update()
    def total(e):
        result.value = t.value + t1.value +t2.value +t3.value
        page.update()
    page.add(ft.Text("Password Generator", style=ft.TextThemeStyle.HEADLINE_MEDIUM, text_align=ft.TextAlign.CENTER))
    page.add(ft.Text())
    t = ft.TextField()
    t1= ft.TextField()
    t2= ft.TextField() 
    t3= ft.TextField()
    t4= ft.TextField(label="Your Password is : ", 
                    border_color="pink", 
                    password=True, 
                    can_reveal_password=True,
                    border_radius=10,
                    )
    # page.add(
    #     ft.Text("How many Characters in the Password ?:"),
    #     ft.Slider(min=0, max=15, divisions=15, label="{value}", on_change=slider_changed), ),
    page.add(
        ft.Text("Number of Letters:"),
        ft.Slider(min=0, max=15, divisions=15, label="{value}", on_change=slider1_changed, thumb_color="red"),),
    page.add(
        ft.Text("Number of  Digits:"),
        ft.Slider(min=0, max=15, divisions=15, label="{value}", on_change=slider2_changed, thumb_color="Yellow"), ),
    page.add(
        ft.Text("Number of Special Characters:"),
        ft.Slider(min=0, max=15, divisions=15, label="{value}", on_change=slider3_changed, thumb_color="Green"),),
        
    btn =ft.Row(controls=[ft.ElevatedButton("Generate My Password",icon="refresh" , on_click=generate_pwd)], alignment= ft.MainAxisAlignment.CENTER,)

    result= ft.TextField()
    

    
    page.add(btn,t4)
ft.app(target=main)