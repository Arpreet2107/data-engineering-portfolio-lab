class ChaiUtils:
    @staticmethod
    def clean_ingridients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "water","milk","ginger","honey"
# obj=ChaiUtils()
# obj.clean_ingridients(raw)
cleaned=ChaiUtils.clean_ingridients(raw)
print(cleaned)