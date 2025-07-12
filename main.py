#  import kivy
# from kivy.app import App
# # widget
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget

# class MyApp(App):
#     def build(self):
#         wdg = Widget()
#         lbl = Label(text='Muhammad yunus ritonga', pos=(200, 0))
#         btn = Button(text='22111024')
#         wdg.add_widget(lbl)
#         wdg.add_widget(btn)
#         return wdg

# MyApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        b_layout = BoxLayout(orientation='vertical')

        btn1 = Button(text='btn1',
                      size_hint=(0.5, 1),
                      pos_hint={'center_x': 0.5})
        btn2 = Button(text='btn2')
        btn3 = Button(text='btn3')
        btn4 = Button(text='btn4')

        b_layout.add_widget(btn1)
        b_layout.add_widget(btn2)
        b_layout.add_widget(btn3)
        b_layout.add_widget(btn4)

        return b_layout
MyApp().run()

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.anchorlayout import AnchorLayout

# class MyApp(App):
#     def build(self):
#         a_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        
#         btn = Button(text='wandDinulAgil')
#         btn.size_hint = (0.2, 0.2)
        
#         a_layout.add_widget(btn)
#         return a_layout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout

# class MyApp(App):
#     def build(self):
#         g_layout = GridLayout(cols=3)

#         btn1 = Button(text='btn1', size_hint=(0.2, 0.2))
#         btn2 = Button(text='btn2', size_hint=(0.2, 0.2))
#         btn3 = Button(text='btn3', size_hint=(0.2, 0.2))
#         btn4 = Button(text='btn4', size_hint=(0.2, 0.2))

#         g_layout.add_widget(btn1)
#         g_layout.add_widget(btn2)
#         g_layout.add_widget(btn3)
#         g_layout.add_widget(btn4)

#         return g_layout
    
#     from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.stacklayout import StackLayout

# class MyApp(App):
#     def build(self):
#         s_layout = StackLayout(orientation='lr-tb')  # left to right, top to bottom

#         btn1 = Button(text='btn1', size_hint=(0.2, 0.2))
#         btn2 = Button(text='btn2', size_hint=(0.2, 0.2))
#         btn3 = Button(text='btn3', size_hint=(0.2, 0.2))
#         btn4 = Button(text='btn4', size_hint=(0.2, 0.2))
#         btn5 = Button(text='btn5', size_hint=(0.5, 0.2))

#         s_layout.add_widget(btn1)
#         s_layout.add_widget(btn2)
#         s_layout.add_widget(btn3)
#         s_layout.add_widget(btn4)
#         s_layout.add_widget(btn5)

#         return s_layout
    
#     myApp().run()
    
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.pagelayout import PageLayout

# class MyApp(App):
#     def build(self):
#         p_layout = PageLayout()

#         btn1 = Button(text='wan', size_hint=(0.2, 0.2))
#         btn2 = Button(text='dinul', size_hint=(0.2, 0.2))
#         btn3 = Button(text='agil', size_hint=(0.2, 0.2))

#         p_layout.add_widget(btn1)
#         p_layout.add_widget(btn2)
#         p_layout.add_widget(btn3)

#         return p_layout
    
#     myApp().run()
    
#     from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.scatterlayout import ScatterLayout

# class MyApp(App):
#     def build(self):
#         f_layout = FloatLayout()

#         btn1 = Button(
#             text='btn1',
#             size_hint=(0.2, 0.2),
#             pos_hint={'x': 0.4, 'y': 0.4}
#         )

#         f_layout.add_widget(btn1)
#         return f_layout
    
#     from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.core.window import Window
# from kivy.utils import get_color_from_hex

# class MyApp(App):
#     def build(self):
#         f_layout = FloatLayout()

#         # Ubah warna latar belakang window
#         Window.clearcolor = get_color_from_hex('#eeeeee')

#         # Tambahkan tombol dengan ukuran dan posisi tertentu
#         btn1 = Button(
#             text='btn1',
#             size_hint=(0.2, 0.2),
#             pos_hint={'x': 0.4, 'y': 0.4}
#         )

#         # Ubah warna latar belakang tombol
#         btn1.background_color = get_color_from_hex('#aaaaaa')

#         f_layout.add_widget(btn1)
#         return f_layout
