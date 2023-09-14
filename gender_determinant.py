def get_gender(name, sername, patronymic, yours):
    cases = {
        1: ["", "аа"],
        2: ["аа", "ый"],
        3: ["уу", "ей"],
        4: ["аа", "уу"],
        5: ["мм", "йй"],
        6: ["ее", "ей"]
    }
    las = sername[-1] + patronymic[-1]
    for case in cases.keys():
        if las in cases[case]:
            # print(case)
            if case == 1:
                if yours == "n":
                    return "Женский"
                return "Женский"
            else:
                if case == 3:
                    if name[-1] + las == "ууу":
                        return "Мужской"
                    return "Женский"
                rez = cases[case].index(las)
                if rez == 0:
                    return "Мужской"
                else:
                    return "Женский"
    return "Мужской"


# with open("names.txt", 'r') as f:
#     for line in f:
#         line1 = line.strip().strip(' ').split(' ')[:-1]
#         if line1[0][-1] == 'а' and line1[1][-1] == 'а' and line1[2][-1] == 'а':
#             continue
#         print(f"{line.strip()} - {get_gender(line1[0], line1[1], line1[2])}")

FCs = input().split(" ")
yours = input("Имя в винительном падеже или дательном падеж?\n[y/n]\n")
print(get_gender(FCs[0], FCs[1], FCs[2], yours))
