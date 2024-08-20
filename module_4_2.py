import traceback
from consoleTextStyle import ConsoleTextStyle as CoTeSt

def test_function():
    def inner_function():
        print("Hey, man! I'm in test_function's namespace!\n"
              "...Help me!!!")
    inner_function()


if __name__ == "__main__":
    test_function()
    try:
        inner_function()
    except Exception:
        print(f"\nНе, ну я конечно попробовал вызвать функцию inner_function вне поля видимости test_function,\n"
              f"Но консоль начала материться и вывела это(...кхе-кхе...\n\n"
              f"{CoTeSt.colorful_str(traceback.format_exc(), CoTeSt.Color.PURPLE)}")
