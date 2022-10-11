from pickletools import pydict

from gingerit.gingerit import GingerIt
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import Screen
from kivymd.uix.tooltip import MDTooltip
from textblob import TextBlob
"""
from PyDictionary import PyDictionary
pydict = PyDictionary()
"""
from kivy.core.window import Window

Window.size = (350, 600)
screen = Screen()
# this is use to register the font, Noto-sans which is used for translation
LabelBase.register(name="Noto Sans", fn_regular="NotoSans-Regular.ttf")
# this this the kv language to add the screens and the widgets

screen_manager = """
ScreenManager:
    id: screen_manager
    WelcomeScreen:
    FunctionScreen:
    MeaningScreen:
    GrammarScreen:
    CorrectScreen:
    TranslateScreen:


<WelcomeScreen>
    name: 'welcomescreen'
    MDLabel :
        text: 'WELCOME USER'
        pos_hint:{'center_x':0.5,'center_y':0.75}
        halign: 'center'
        font_style : 'H4'
        
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            type: "top"
            title: 'Text Analysis'
            elevation:25
        MDLabel:
            text:""
    MDSwitch:
        on_active:app.check(*args)
        pos_hint:{'center_x':0.5,'center_y':0.05}
        halign:'center'
    MDLabel:
        text:'CHANGE THEME'
        pos_hint:{'center_x':0.8,'center_y':0.15}


    MDRectangleFlatIconButton:
        icon:"account-arrow-right"
        text: 'CONTINUE'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        halign: 'center'
        on_press:root.manager.current = 'functionscreen'

    MDRectangleFlatIconButton:
        icon:"exit-to-app"
        text:'EXIT'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        halign:'center'
        on_press: app.stop()


<FunctionScreen>
    name: 'functionscreen'

    MDTextField:
        font_name:"NotoSans-Regular.ttf"
        id: text_field
        hint_text:'enter the text'
        helper_text:"for meaning enter only a word"
        helper_text_mode:"on_focus"
        icon_right: "text-box"
        icon_right_color: app.theme_cls.primary_color
        multiline:True
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        size_hint_x:0.75
        size_hint_y:0.25
        max_height: "200dp"
        mode: "fill"

    MDRectangleFlatIconButton
        icon: "book-search"
        text: 'MEANING'
        id: meaning_button
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_release:
            app.meaning_func()
            root.manager.current = 'meaningscreen'

    MDRectangleFlatIconButton
        icon: "book-check"
        text: 'GRAMMAR CORRECT'
        id: grammar_button
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_release:
            app.grammar_func()
            root.manager.current = 'grammarscreen'

    MDRectangleFlatIconButton
        icon: "book-check"
        text: 'WORD CORRECT'
        id: correct_button
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_release:
            app.correct_func()
            root.manager.current = 'correctscreen'

    MDRectangleFlatButton:
        text:'RETURN'
        id:return_button
        pos_hint:{'center_x':0.35,'center_y':0.2}
        halign: 'center'
        on_release:
            root.manager.current='welcomescreen'


    MDRectangleFlatButton:
        text: 'CLEAR'
        id: 'clear_button'
        pos_hint:{'center_x':0.65,'center_y':0.2}
        halign: 'center'
        on_press:app.clear_func()



    MDRectangleFlatIconButton
        icon: "translate"
        text: 'TRANSLATE'
        id:translate_button
        pos_hint:{'center_x':0.5,'center_y':0.3}
        halign:'center'
        on_release:
            root.manager.current='translatescreen'


<MeaningScreen>
    name: 'meaningscreen'

    BoxLayout:
        orientation: "vertical"
        
    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: root.manager.current = 'functionscreen'


    MDLabel:
        text: "Default"
        font_name:"NotoSans-Regular.ttf"
        id: meaning
        halign: 'center'
        multiline: True
        theme_text_color: 'Primary'
        font_style: 'Caption'
        font_Size:'10'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint:(0.75,None)
        height:500


    MDLabel:
        text: 'DEFINITION / MEANING'
        halign :'center'
        pos_hint:{'center_x':0.5,'center_y':0.9}

<GrammarScreen>
    name: 'grammarscreen'
    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: root.manager.current = 'functionscreen'


    MDTextField:
        font_name:"NotoSans-Regular.ttf"
        text: "Default"
        id: grammar
        multiline: True
        halign: 'center'
        theme_text_color: 'Secondary'
        font_style: 'Body1'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:0.75

        size_hint_y:0.3

    MDLabel:
        text: 'GRAMMATICALLY CORRECT TEXT'
        halign :'center'
        pos_hint:{'center_x':0.5,'center_y':0.9}

<CorrectScreen>
    name: 'correctscreen'
    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: root.manager.current = 'functionscreen'
    MDTextField:
        font_name:"NotoSans-Regular.ttf"
        text: "Default"
        id: correct
        halign: 'center'
        theme_text_color: 'Secondary'
        font_style: 'Body1'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint:(0.75,0.3)
    MDLabel:
        text: 'CORRECT TEXT/SPELLING'
        halign :'center'
        pos_hint:{'center_x':0.5,'center_y':0.9}

<TranslateScreen>
    name:'translatescreen'

    MDLabel:
        text:"TRANSLATION"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        size_hint:(0.75,0.3)
        halign:'center'

    MDTextField:
        #text: "you can translate to the given languages given in the buttons"
        font_name:"NotoSans-Regular.ttf"
        id: translate
        multiline: True
        halign: 'center'
        theme_text_color: 'Secondary'
        font_style: 'Body1'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint:(0.75,0.4)

    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: root.manager.current = 'functionscreen'

    MDRectangleFlatIconButton
        icon:"hinduism"
        text:'translate to hindi'
        id:translate_to_hindi_button
        pos_hint:{'center_x':0.5,'center_y':0.4}

        halign:'center'
        on_release:
            app.translate_to_hindi_func()
            root.manager.current='translatescreen'

    MDRectangleFlatIconButton
        icon:"abugida-devanagari"
        text:'translate to marathi'
        id:translate_to_marathi_button
        pos_hint:{'center_x':0.5,'center_y':0.3}
        halign:'center'
        on_release:
            app.translate_to_marathi_func()
            root.manager.current= 'translatescreen'


    MDRectangleFlatIconButton:
        icon:"pen"
        text:'translate to english'
        id:translate_to_english_button
        pos_hint:{'center_x':0.5,'center_y':0.2}
        halign:'center'
        on_release:
            app.translate_to_english_func()
            root.manager.current= 'translatescreen'


"""


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass


class WelcomeScreen(Screen):
    pass


class FunctionScreen(Screen):
    pass


class MeaningScreen(Screen):
    pass


class GrammarScreen(Screen):
    pass


class CorrectScreen(Screen):
    pass


class TranslateScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FunctionScreen(name='functionscreen'))
sm.add_widget(MeaningScreen(name='meaningscreen'))
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(GrammarScreen(name='grammarscreen'))
sm.add_widget(CorrectScreen(name='correctscreen'))
sm.add_widget(TranslateScreen(name='translatescreen'))


class TextApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Text Analysis"
        super(TextApp, self).__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'BlueGray'
        sm = Builder.load_string(screen_manager)
        return sm

    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = 'LightGreen'
        else:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = 'BlueGray'

    # functions are used to translate for corrections

    # this functions takes the text and gives the meaning of the word written in the text field
    def show_data_meaning(self):
        searchword = self.root.get_screen("functionscreen").ids.text_field.text
        if searchword == "":
            return "enter text"
     
        meaning = pydict.meaning(searchword)
        synonym = pydict.synonym(searchword)
        antonym = pydict.antonym(searchword)
        blob = TextBlob(searchword)
        plural = blob.words[0].pluralize()
        singular = blob.words[0].singularize()
        a = str(meaning) + str("\nSYNONYMS ==>  ") + str(synonym) + str("\nANTONYMS ==>  ") + str(antonym) + str(
            "\nPLURAL==>") + str(plural) + str(
            "\nSINGULAR==>") + str(singular)
        return a

    # this function is used to take the text from the textfield in the functionscreen and is passed to the another
    # function written above
    def meaning_func(self):
        self.root.get_screen("meaningscreen").ids.meaning.text = str(
            self.show_data_meaning())

    # similarly all the other functions are written below
    def show_data_grammar(self):
        searchword = self.root.get_screen("functionscreen").ids.text_field.text
        if searchword == "":
            return "enter text"
        print(searchword)
        synonym = str(searchword)
        parser = GingerIt()
        a = parser.parse(synonym)['result']
        b = str(a)
        print(b)
        return b

    def grammar_func(self):
        self.root.get_screen("grammarscreen").ids.grammar.text = str(
            self.show_data_grammar())

    def show_data_correct(self):
        searchword = self.root.get_screen("functionscreen").ids.text_field.text
        if searchword == "":
            return "enter text"
        print(searchword)
        synonym = TextBlob(searchword)
        a = synonym.correct()
        return a

    def correct_func(self):
        self.root.get_screen("correctscreen").ids.correct.text = str(
            self.show_data_correct())

    def clear_func(self, **args):
        self.root.get_screen("functionscreen").ids['text_field'].text = ""

    def translate_to_hindi_func(self):
        self.root.get_screen("translatescreen").ids.translate.text = str(
            self.show_data_to_hindi())

    def show_data_to_hindi(self):
        a = ""
        try:
            searchword = str(self.root.get_screen(
                "functionscreen").ids.text_field.text)
            hindi = TextBlob(searchword)
            hindi = hindi.translate(to='hi')
            a = str(hindi)
            print(a)
            return a
        except:
            if a == "":
                a = "enter text"
                return a
            else:
                a = "error \n try another"
                return a

    def translate_to_marathi_func(self):
        self.root.get_screen("translatescreen").ids.translate.text = str(
            self.show_data_to_marathi())

    def show_data_to_marathi(self):
        searchword = self.root.get_screen("functionscreen").ids.text_field.text
        a = str(searchword)
        try:
            searchword = self.root.get_screen(
                "functionscreen").ids.text_field.text
            print(searchword)
            searchword = searchword
            marathi = TextBlob(searchword)
            marathi = marathi.translate(to='mr')
            a = str(marathi)
            print(a)
            return a
        except:
            if a == "":
                a = "enter text"
                return a
            else:
                a = "error \n try another"
                return a

    def translate_to_english_func(self):
        self.root.get_screen("translatescreen").ids.translate.text = str(
            self.show_data_to_english())

    def show_data_to_english(self):
        a = ""
        try:
            searchword = str(self.root.get_screen(
                "functionscreen").ids.text_field.text)
            english = TextBlob(searchword)
            english = english.translate(to='en')
            a = str(english)
            print(a)
            return a
        except:
            if a == "":
                a = "enter text"
                return a
            else:
                a = "error \n try another"
                return a


if __name__ == '__main__':
    TextApp().run()
