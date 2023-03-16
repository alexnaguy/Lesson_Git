
def execute_application():

def print_file_extension(file):
    if "." not in file:
        raise ValueError("Определить расширение файла невозможно .")
    try:
        file_ext = file.split(".")[-1] #Разбивам файл по точкеи берем последний элемент
        return file_ext
    except Exception as e:
        print(e)




if __name__== "__main__":
    execute_application()