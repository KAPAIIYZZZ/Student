import random
class Student:
    def __init__(self, type, tiredness, knowledge, strenght, money):
        self.__type = type
        self.__tiredness = tiredness
        self.__knowledge = knowledge
        self.__strenght = strenght
        self.__money = money

    @property
    def type(self):
        return self.__type
    @property
    def tiredness(self):
        return self.__tiredness
    @tiredness.setter
    def tiredness(self, tiredness):
        self.__tiredness = tiredness
    @property
    def knowledge(self):
        return self.__knowledge
    @knowledge.setter
    def knowledge(self, knowledge):
        self.__knowledge = knowledge
    @property
    def strenght(self):
        return self.__strenght
    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money

    def action(self, tiredness, knowledge, strenght, money):
        self.__tiredness += tiredness
        self.__knowledge += knowledge
        self.__strenght += strenght
        self.__money += money

    def update(self):
        probability = random.randint(0,100)
        if self.__type == 'гений':
            if probability<25:
                self.action(-10, -5, +5, -15)
                return ('студент выбрал развлечения')
            elif 25 <= probability < 50:
                self.action(+10, -5, +15, -5)
                return ('студент выбрал качалку')
            elif 50 <= probability < 75:
                self.action(+15, +15, 0, 0)
                return ('студент выбрал учебу')
            else:
                self.action(-15, -5, -10, 0)
                return ('студент выбрал отдых')

        elif self.__type == 'спортсмен':
            if probability < 5:
                self.action(-10, -5, +5, -15)
                return ('студент выбрал развлечения')
            elif 5 <= probability < 50:
                self.action(+10, -5, +15, -5)
                return ('студент выбрал качалку')
            elif 50 <= probability < 55:
                self.action(+15, +15, 0, 0)
                return ('студент выбрал учебу')
            else:
                self.action(-15, -5, -10, 0)
                return ('студент выбрал отдых')

        elif self.__type == 'заучка':
            if probability < 10:
                self.action(-10, -5, +5, -15)
                return ('студент выбрал развлечения')
            elif 10 <= probability < 15:
                self.action(+10, -5, +15, -5)
                return ('студент выбрал качалку')
            elif 15 <= probability < 75:
                self.action(+15, +15, 0, 0)
                return ('студент выбрал учебу')
            else:
                self.action(-15, -5, -10, 0)
                return ('студент выбрал отдых')


class Controller:
    def __init__(self, number_of_students):
        self.__students_list = []
        self.__number_of_students = number_of_students

    @property
    def students_list(self):
        return self.__students_list
    @property
    def number_of_students(self):
        return self.__number_of_students

    def create_students(self):
        for i in range(self.number_of_students):
            probability = random.randint(1,3)
            if probability == 1:
                student = Student('гений', 0, 80, 80, 100)
            elif probability == 2:
                student = Student('спортсмен', 20, 20, 95, 40)
            else:
                student = Student('заучка', 40, 90, 5, 20)
            self.students_list.append(student)

    def update_semester(self):

        for i in range(1,19):
            print(f'Шаг {i}')
            for x in range(1,len(self.students_list)+1):
                print(f'{x} {self.students_list[x-1].update()}. Свойства:')
                print(f'усталость - {self.students_list[x-1].tiredness}')
                print(f'знания - {self.students_list[x-1].knowledge}')
                print(f'физическая сила - {self.students_list[x-1].strenght}')
                print(f'деньги - {self.students_list[x-1].money}')


        for i in range(1,len(self.students_list)+1):
            if self.students_list[i-1].tiredness >=100:
                print(f'{i} студент словил инфаркт и умер')

            elif self.students_list[i-1].knowledge <=0:
                print(f'{i} студент завалил сессию')

            elif self.students_list[i-1].strenght <=0:
                print(f'{i} студент упал с лестницы на входе в универ и помер')

            elif self.students_list[i-1].money >=100:
                print(f'{i} студент умер от голода')

            else:
                print(f'{i} студент закрыл сессию')
def main():
    number_of_students = int(input('Сколько студентов в группе? '))
    controller = Controller(number_of_students)
    controller.create_students()
    for i in range(1,number_of_students+1):
        print(f'{i} студент - {controller.students_list[i-1].type}')
    controller.update_semester()

main()

