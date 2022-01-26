class List_Mean:

    def __init__(self, my_list):
        self.list = my_list

    def get_list(self):
        return self.list

    def set_list(self):
        self.list = my_list

    def calc_avg(self):
        new = self.get_list()
        new_list = []
        sum = 0

        # In this block of code I try to sort items out based on their type, numeric or not
        for i in range(0, len(new)):
            if type(new[i]) == int:
                new_list.append(new[i])
            elif type(new[i]) == float:
                new_list.append(new[i])

        for i in range(0, len(new_list)):
            sum += new_list[i]

        mean = sum / len(new_list)

        print(mean)

# Assigning value to the variable
my_list = [1, 2, 3, 4, 5, 6, 7, "dog"]
# my_list = [1,2,17,52.5, 43, 4.4, 10]

# Instantiating the variable
list_1 = List_Mean(my_list)

list_1.calc_avg()
