class StringUtils:
    def capitalize(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError('Неверный тип данных')
        if string == "":
            return ""
        return string[0].upper() + string[1:]
    
    def trim(self, string: str) -> str:
        if not isinstance(string, str):
            raise AttributeError('Неверный тип данных')
        return string.strip()
    
    def contains(self, string: str, symbol: str) -> bool:
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise AttributeError('Неверный тип данных')
        return symbol in string
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise AttributeError('Неверный тип данных')
        index = string.find(symbol)
        if index == -1:
            return string
        # Удаляем только первое вхождение
        return string[:index] + string[index + len(symbol):]