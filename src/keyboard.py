from src.item import Item


class Language:
    """Класс-миксин для хранения и изменения раскладки клавиатуры"""
    __language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, Language):
    pass
