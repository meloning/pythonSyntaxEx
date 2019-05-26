class BookReader:
    __country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def read_book(self):
        print(self.name +' is reading Book!!')
    def set_country(self, country):
        self.__country = country
    def get_country(self):
        return self.__country

reader = BookReader('Chris')
reader.read_book()

print(dir(reader))

# Class 내 __속성명 -> private (이름 장식)

br = BookReader('Junsu')
print(br.get_country())
br.set_country('Korean')
print(br.get_country())

# Inheritance 상속/ Multiple Inheritance 다중 상속 허용

# Polymorphism 다형성
# super().method_name() 부모꺼접근
