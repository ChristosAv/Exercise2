import csv

with open('wk2_test2_in.log', 'r') as data_file_1:
    data_file_reader = csv.reader(data_file_1, delimiter=':')

    # This part is for writing the new file that will be the final output
    with open('wk2_test1_out.csv', 'w') as wk2_test1_out:
        # The delimiter must remain the same for the reading and writing method
        csv_writer = csv.writer(wk2_test1_out, delimiter=':')

        new_list = []
        # In order to manipulate the data in a certain format, first we have to count hte length of each "string".
        # The action below will produce a sting with length of 10 characters
        for line in data_file_reader:
            if len(line[3]) < 11:
                difference = 10 - len(line[3])
                new_line = line[3] + difference * " "
                new_format = line[0], line[1], line[2], new_line, line[4]
                csv_writer.writerow(new_format)
            elif len(line[3]) >= 10:
                new_format = line[0], line[1], line[2], line[3], line[4]
                csv_writer.writerow(new_format)
            # This list will contain all the information needed to be manipulated to the disable format
            new_list.append(line[4])

            # if new_list[0] == 'GC':
            #     format_0 = 'GC' + 5 * ' '
            # elif new_list[0] == 'Full':
            #     format_0 = ''.join(new_list[0:1])
            #     if len(new_list[1]) >= 15:
            #         s = new_list[1]
            #         format_1 = s[0:14]
            #  Rounding the time into the second decimal digit
            # format_2 = round(new_list[2], 2)
            # detailed_str = format_0 + format_1 + format_2 + new_list[3]
    wk2_test1_out.close()
data_file_1.close()
