__version__ = "1.0.0"

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class SendarLiteApp(App):

    def build(self):
        self.title = "Sendar Lite"

        Window.clearcolor = (0.956, 0.956, 0.956, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(20), dp(20), dp(20)],
            spacing=dp(12),
        )

        # عنوان التطبيق
        title_label = Label(
            text="منصة Sendar المصغرة",
            font_size=dp(24),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=dp(55),
            halign="center",
            valign="middle",
        )
        title_label.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", value
            )
        )
        root.add_widget(title_label)

        # وصف الحقل
        msg_label = Label(
            text="أدخل النص أو الأمر:",
            font_size=dp(17),
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=dp(40),
            halign="right",
            valign="middle",
        )
        msg_label.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", value
            )
        )
        root.add_widget(msg_label)

        # حقل الإدخال
        self.entry = TextInput(
            hint_text="اكتب النص أو الأمر هنا",
            font_size=dp(17),
            multiline=False,
            size_hint_y=None,
            height=dp(52),
            padding=[dp(12), dp(12)],
        )
        root.add_widget(self.entry)

        # زر التنفيذ
        action_btn = Button(
            text="تشغيل العملية",
            font_size=dp(17),
            bold=True,
            size_hint_y=None,
            height=dp(55),
        )
        action_btn.bind(on_press=self.run_process)
        root.add_widget(action_btn)

        # عنوان السجل
        log_title = Label(
            text="سجل العمليات",
            font_size=dp(16),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=dp(35),
            halign="right",
            valign="middle",
        )
        log_title.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", value
            )
        )
        root.add_widget(log_title)

        # منطقة السجل
        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
        )

        self.log_box = Label(
            text="النظام جاهز للتشغيل...\n",
            font_size=dp(15),
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            halign="right",
            valign="top",
            padding=[dp(10), dp(10)],
        )

        self.log_box.bind(
            texture_size=self.update_log_height
        )

        scroll.add_widget(self.log_box)
        root.add_widget(scroll)

        return root

    def update_log_height(self, instance, texture_size):
        instance.height = max(texture_size[1] + dp(20), dp(100))
        instance.text_size = (instance.width - dp(20), None)

    def run_process(self, instance):
        user_input = self.entry.text.strip()

        if not user_input:
            self.show_warning()
            return

        self.log_box.text += f">> جاري تنفيذ: {user_input}\n"
        self.entry.text = ""

    def show_warning(self):
        content = BoxLayout(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(15),
        )

        message = Label(
            text="الرجاء إدخال بيانات صحيحة أولاً!",
            font_size=dp(16),
            halign="center",
            valign="middle",
        )
        message.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", value
            )
        )

        close_button = Button(
            text="حسنًا",
            size_hint_y=None,
            height=dp(50),
        )

        content.add_widget(message)
        content.add_widget(close_button)

        popup = Popup(
            title="تنبيه",
            content=content,
            size_hint=(0.85, 0.35),
            auto_dismiss=False,
        )

        close_button.bind(on_press=popup.dismiss)

        popup.open()


if __name__ == "__main__":
    SendarLiteApp().run()
