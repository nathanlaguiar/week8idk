def load_data():
    file = open("nationsPop.txt", 'r')
    page = file.readlines()
    country_data = []
    for line in page:
        split_line_list = line.split(',')
        country = {
            "name": split_line_list[0],
            "pop": int(split_line_list[1]),
            "change": float(split_line_list[2]),
        }
        country_data.insert(0, country)
def main():
    main_country_data = load_data()

def print_menu():
    print("=============Please select an option below================")
    print("[1] Find the country with the largest Population")
    print("[2] Find the country with the smallest Population")
    print("[3] Add New")
    print("[4] Game Over")
    print("============================================================")
    answer = input("Enter choice 1-4")


 #Finish next week
main()




while True:
    print("=============Please select an option below================")
    print("[1] Find the country with the largest Population")
    print("[2] Find the country with the smallest Population")
    print("[3] Add New")
    print("[4] Game Over")
    print("============================================================")
    answer = input("Enter choice 1-4")
    if answer == '1' :
        largest_so_far = country_data[0]
        for country_dict in country_data:
            if country_dict["pop"] > largest_so_far ['pop']:
                largest_so_far = country_dict
        print(f"The largest country is {largest_so_far['name']} with pop {largest_so_far,['pop']}")
    elif answer == '2':

        if answer == '2':
            smallest_so_far = country_data[0]
            for country_dict in country_data:
                if country_dict["pop"] < smallest_so_far['pop']:
                    smallest_so_far = country_dict
            print(f"The smallest country is {smallest_so_far['name']} with pop {smallest_so_far,['pop']}")
        else:
            print("Invalid entry, please enter 1-4")

    elif answer == '3':
        country_name = input ("Please enter new country name")
        country_pop = input(f"Please enter population for {country_name}")
        pop_changes = float(input(f"Please enter the population change 2021-2022"))
        country = {
            "name": (split_line_list[0]),
            "pop": int(split_line_list[1]),
            "change": float(split_line_list[2]),
        }
        country_data.append(country)


    elif answer == '4':
        exit(0)
    else:
        print("Invalid entry, please enter 1-4")

