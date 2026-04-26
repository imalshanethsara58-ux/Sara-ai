import os  # මෙතන 'I' අකුර simple කළා
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.utils import platform
import google.generativeai as genai
from gtts import gTTS

# 1. AI මොළය සැකසීම
API_KEY = "AIzaSyBgKdusBvHgY1-CqWeTqVGnW0hCXN_aR_c"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

class SaraAI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10
        Window.clearcolor = (0.05, 0.05, 0.05, 1)

        self.add_widget(Label(text="SARA AI 🤖", font_size='28sp', color=(0, 0.8, 1, 1), size_hint_y=None, height=50))
        
        self.scroll = ScrollView()
        self.chat_log = Label(
            text="සාරා: ආයුබෝවන්! මම සාරා. ඔයාට කොහොමද මම උදව් කරන්න ඕනේ?\n\n", 
            size_hint_y=None, halign='left', valign='top', markup=True,
            font_name='iskoola.ttf' # සිංහල පෙනීමට
        )
        self.chat_log.bind(texture_size=self.chat_log.setter('size'))
        self.bind(width=lambda *x: self.chat_log.setter('text_size')(self.chat_log, (self.width - 40, None)))
        self.scroll.add_widget(self.chat_log)
        self.add_widget(self.scroll)

        input_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        self.user_input = TextInput(
            hint_text='මොනවා හරි අහන්න...', multiline=False, font_size='18sp',
            font_name='iskoola.ttf' # සිංහල පෙනීමට
        )
        input_layout.add_widget(self.user_input)

        self.send_btn = Button(
            text="යවන්න", size_hint_x=None, width=100, background_color=(0, 0.6, 0.9, 1),
            font_name='iskoola.ttf' # සිංහල පෙනීමට
        )
        self.send_btn.bind(on_press=self.send_message)
        input_layout.add_widget(self.send_btn)
        self.add_widget(input_layout)

    def send_message(self, instance):
        msg = self.user_input.text.strip()
        if msg:
            self.chat_log.text += f"[color=00ff00]ඔයා:[/color] {msg}\n"
            self.user_input.text = ""
            self.chat_log.text += "[color=aaaaaa]සාරා හිතමින් පවතියි...[/color]\n"
            threading.Thread(target=self.process_ai, args=(msg,)).start()

    def process_ai(self, user_msg):
        try:
            prompt = f"Reply in Sinhala briefly. You are Sara, a friendly girl. Question: {user_msg}"
            response = model.generate_content(prompt)
            reply = response.text
            Clock.schedule_once(lambda dt: self.update_ui(reply))
            threading.Thread(target=self.speak, args=(reply,)).start()
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_ui("සමාවෙන්න, මට සම්බන්ධ වෙන්න බැහැ."))

    def update_ui(self, sara_reply):
        self.chat_log.text = self.chat_log.text.replace("[color=aaaaaa]සාරා හිතමින් පවතියි...[/color]\n", "")
        self.chat_log.text += f"[color=00ccff]සාරා:[/color] {sara_reply}\n\n"

    def speak(self, text):
        try:
            if platform == 'android':
                from android.permissions import request_permissions, Permission
                request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
                app_dir = App.get_running_app().user_data_dir
            else:
                app_dir = os.getcwd()
                
            audio_path = os.path.join(app_dir, "sara_voice.mp3")
            
            if os.path.exists(audio_path):
                os.remove(audio_path)

            tts = gTTS(text=text, lang='si')
            tts.save(audio_path)
            
            Clock.schedule_once(lambda dt: self.play_audio(audio_path))
        except Exception as e:
            print(f"Speak Error: {e}")

    def play_audio(self, path):
        sound = SoundLoader.load(path)
        if sound:
            sound.play()

class SaraApp(App):
    def build(self):
        return SaraAI()

if __name__ == '__main__':
    SaraApp().run()

