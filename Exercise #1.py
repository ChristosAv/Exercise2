class List_Mean:
    # my_list = [1, 2, 3, 4, 5, 6, 7, "dog"]

    # my_list = [1, 2, 17, 52.5, 43, 4.4, 10]

    def __init__(self, my_list):
        self.list = my_list

    def get_list(self):
        return self.my_list

    def set_list(self, my_list):
        self.list = my_list

    def calc_avg(self, my_list):
        List_Mean.get_list(self)
        new_list = []
        sum = 0
        mean = 0
        # In this block of code I try to sort items out based on their type, numeric or not
        for variable in my_list:
            if type(my_list(variable)) == int or type(my_list(variable)) == float is True:
                sum += my_list(variable)
                new_list.append(variable)
            elif type(my_list(variable)) == int or type(my_list(variable)) == float is False:
                new_list.pop(variable)
                sum += my_list(variable)

            if variable is my_list.len():
                mean = sum / variable
            print(my_list)


data = [1, 2, 3, 4, 5, 6, 7, "dog"]

List_Mean.calc_avg(data)
