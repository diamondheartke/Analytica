from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class HelloWorldApp(MDApp):
    def build(self):
        return MDLabel(
            text="Hello, World!",
            halign="center",
            theme_text_color="Primary",
            font_style="H4"
        )


if __name__ == "__main__":
    HelloWorldApp().run()
