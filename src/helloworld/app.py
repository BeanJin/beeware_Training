"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx

class HelloWorld(toga.App):

    def greeting(self, name):
        if name:
            if name == "Brutus":
                return "BeeWare the IDEs of Python!"
            else:
                return f"Hello, {name}"
        else:
            return "Hello, stranger"
        
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "이건 뭘까나 : ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "버튼을 눌렀다네",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()
        
        greeting_message = self.greeting(self.name_input.value)

        self.main_window.info_dialog(
            greeting_message,
            payload["body"],
        )

def main():
    return HelloWorld()
