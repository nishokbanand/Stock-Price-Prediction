from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager

from kivy.lang.builder import Builder
import app
import perfectie
stringie="""
<main_screen>:
    md_bg_color:(245/255, 171/255, 201/255,1)
    
    MDBoxLayout:
        padding:"10sp","10sp"
        md_bg_color:(255/255, 229/255, 226/255,1)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint:0.8,0.8
        radius:[30]
        orientation:"vertical"
        spacing:"10sp"
        
        MDLabel:
            id:lb1
            text:"Stock Detection"
            halign: "center"
            theme_text_color: "Custom"
            text_color: (233/255, 59/255, 129/255,1)
            font_style:"H4"
            adaptive_height:1
        MDTextField:
            id:tf1
            multiline: True
            hint_text: "Type here...!"
            size_hint:0.8,0.7
            color_mode: 'custom'
            line_color_normal:(182/255, 201/255, 240/255,1)
            pos_hint:{"center_x":0.5,"center_y":0.5}
            line_color_focus: (182/255, 201/255, 240/255,1)
            helper_text: "Check for Detection msg"
            helper_text_mode: "on_focus"
        MDFillRoundFlatIconButton:
            icon: "trash-can-outline"
            text: "Check"
            md_bg_color:(233/255, 59/255, 129/255,1)
            pos_hint:{"center_x":0.5,"center_y":0.5}
            on_release:root.check(tf1.text)
    MDFillRoundFlatButton:
        text: "Graph"
        md_bg_color: (233/255, 59/255, 129/255,0.5)
        pos_hint:{"center_x":0.9,"center_y":0.9}
        on_release:app.change_screen2()

<main_manager>:
    id:SM
        
"""
Builder.load_string(stringie)
class main_screen(MDScreen):
    def check(self,string):
        self.result=app.initially(string)
        self.ids.lb1.text="the value is"+self.result

class main_manager(ScreenManager):
    def init(self):
        self.check=main_screen(name="Screen1")
        self.add_widget(self.check)
        self.graph=perfectie.Graph(0,0).str
        self.graph.name="Screen2"
        self.add_widget(self.graph)
        
class GUI_MLapp(MDApp):
    def build(self):
        self.Main_screen=main_manager()
        self.Main_screen.init()
        return self.Main_screen
    def change_screen1(self):
        self.Main_screen.current="Screen1"
    def change_screen2(self):
        self.Main_screen.remove_widget(self.Main_screen.graph)
        self.Main_screen.graph=perfectie.Graph(self.Main_screen.check.ids.tf1.text,self.Main_screen.check.result).str
        self.Main_screen.graph.name="Screen2"
        self.Main_screen.add_widget(self.Main_screen.graph)
        self.Main_screen.current="Screen2"
        


if __name__=="__main__":
    gui_object=GUI_MLapp()
    gui_object.run()