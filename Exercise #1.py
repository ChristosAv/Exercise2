class List_Mean:

    def __init__(self, my_list):
        self.list = my_list

    def get_list(self):
        return self.my_list

    def set_list(self, my_list):
        self.list = my_list

    def calc_avg(self):
        new = List_Mean.get_list(self)
        new_list = []
        sum = 0

        # In this block of code I try to sort items out based on their type, numeric or not
        for variable in new:
            if type(new[variable]) == int is True:
                new_list.append(new[variable])

        for item in new_list:
            sum += new_list[item]

        mean = sum / len(new_list)

        print(mean)


# Assigning value to the variable
my_list = [1, 2, 3, 4, 5, 6, 7, "dog"]

# Instantiating the variable
list_1 = List_Mean(my_list)
