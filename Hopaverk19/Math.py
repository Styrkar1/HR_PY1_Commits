class Sales():
    def __init__(self,data):
        self.__data = data
    
    def add_sale(self,numb):
        self.__data.append(numb)

    def get_average(self):
        total = 0
        for i in self.__data:
            total += i
        average = total / len(self.__data)
        return average

def read_data_from_file(filename):
    with open(filename) as f:
        word_list = f.read().splitlines()

    word_list = [float(x) for x in word_list]
    return word_list

def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()
