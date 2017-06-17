import csv
import re


def replace_pattern_in_str(a_string):
    result = re.search("e.e", a_string)
    if result:
        str_as_list = list(a_string)
        str_as_list[result.start()] = "a"
        str_as_list[result.start() + 2] = "a"
        a_string = ''.join(str_as_list)

    return a_string

def main():
    with open('test_example.csv') as source:
        inforeader = csv.reader(source)
        with open('output.csv', 'w', newline='') as output:
            output_writer = csv.writer(output, quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            for row in inforeader:
                row.pop(2)
                row[0] = replace_pattern_in_str(row[0])
                row[1] = replace_pattern_in_str(row[1])
                output_writer.writerow(row)

if __name__ == '__main__':
    main()
