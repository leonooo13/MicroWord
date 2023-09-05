import json
def get_word_list(a:int,b:int):
    with open("Book/kaoyan.json", "r", encoding="utf-8") as dic_book:
        s=dic_book.read()
        word_list=json.loads(s)
        return word_list[a:b]