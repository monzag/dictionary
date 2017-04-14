import csv


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:

    # Ekran startowy
    print(bcolors.HEADER, """
    Dictionary for a little programmer:
    1) search expllanation by apellation,
    2) add new definition,
    3) show all apellations alphabetically,
    4) show available definitions by first letter of appellation,
    5) exit;""", bcolors.ENDC)

    decision = input("\n Give a number: ")                  # Wybór opcji

    if decision == "1":
        with open('my_dict.csv') as csvfile:                # Wczytywanie pliku csv
            reader = csv.reader(csvfile)
            knowledge_2 = dict(reader)
            csvfile.close()
            choice2 = str(input("Write apellation: ")).upper()
            if choice2 in knowledge_2.keys():               # Poszukiwanie definicji po kluczu
                print(knowledge_2.get(choice2.strip()))
            else:
                print(bcolors.WARNING, "Don't find apellation.", bcolors.ENDC)

    elif decision == "2":
        new_apellation = str(input("Write apellation: ")).upper()
        new_expllanation = str(input("Write expllanation: "))
        new_source = str(input("Write a source: "))
        new_def = {}
        new_def[new_apellation] = (new_expllanation, new_source)

        with open('my_dict.csv', "a") as csvfile:           # Dodanie nowej definicji do csv
            writer = csv.writer(csvfile)
            for key, value in new_def.items():
                writer.writerow([key, value])
                csvfile.close()
            print("You add new definition.")

    elif decision == "3":
        with open('my_dict.csv') as csvfile:
            reader = csv.reader(csvfile)
            knowledge_2 = dict(reader)
            csvfile.close()
            print(sorted(knowledge_2))                      # Wyświetlanie kluczy w kolejności alfabetycznej

    elif decision == "4":
        letter = str(input("Write first letter of apellation: ")).upper()
        with open('my_dict.csv') as csvfile:
            reader = csv.reader(csvfile)
            knowledge_2 = dict(reader)
            csvfile.close()
            for key in knowledge_2.keys():
                if key.startswith(letter):
                    print(key)

    elif decision == "5":                                   # Wyjście z programu
        print("See you later;)")
        break

    else:                                                   # Błędny wybór (poza zakresem)
        print(bcolors.WARNING, "Bad choice! Try again.", bcolors.ENDC)

