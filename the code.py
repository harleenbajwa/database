'''
Title: Elk Island National
Name: Harleern Bajwa
Date: 12/11/18
'''

### --- Import --- ###
import  csv

fil = open("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data.csv", newline = '')

readcsv = csv.reader(fil)


op = '''
Welcome to the Elk Island National Park Large Mammal population database!

Please choose an option:
    1. Search population growth
    2. Add new year data
    3. Exit
Option: '''

def intro():
    global op
    option = input(op)
    if option == '1':
        option_one()
    elif option == '2':
        option_two()
    elif option == '3':
      print("Exit from database.")
    else:
        print("Choose a different option.")
        intro()
def option_one():
    limit = 0
    row= []
    styr, edyr = input_yrs()
    #styr, edyr = diff_yr(st, ed)
    #diff_yr(st, ed) didnt work properly; so, i deleted it
    print(styr)
    print(edyr)
    animal = choose_animal()
    row = read_csv()
    for i in range(len(row)):
        if limit <= 5:
            if animal == row[i][5]:
                if styr == row[i][1] or edyr == row[i][1]:
                    print(row[i])
            elif animal == "All":
                if styr == row[i][1] or edyr == row[i][1]:
                    print(row[i])
              

        limit = limit + 1
def read_csv():
  row = []
  for line in readcsv:
        row.append(line)
  return row
def input_yrs():

    styr = input("Start year:")
    edyr = input("End year:")

    return styr, edyr
def choose_animal():
    animal = input("Would you like to see (Deer), (Elk), (Bison), (Moose), or (All):")
    if animal == "Elk" or animal =="Moose" or animal == "Deer" or animal == "Bison" or animal == "All":
        animal = animal ## problem here try again 
    else:
        print("Bad choice. Try again.")
        choose_animal()
    return animal

def diff_yr(st, ed):
    if st < "1905":
        print("The data starts from the year 1905. Choose a different year.")
        input_yrs()
    elif st < ed:
        st = int(st)
        ed = int(ed)
    else:
        print("You did something wrong. Try again.")
        input_yrs()
    return st, ed
def option_two():
    a = input("Area of park:")
    b = input("Population year:")
    c = input("Survey Year:")
    d = input("Survey Month:")
    e = input("Survey Day:")
    f = input("Species name:")
    g = input("Unknown age and sex count:")
    h = input("Adult male count:")
    i = input("Adult female count:")
    j = input("Adult unknown count:")
    k = input("Yearling count:")
    l = input("Calf count:")
    m = input("Survey total:")
    n = input("Sightability correction factor:")
    o = input("Additional captive count:")
    p = input("Animals removed prior to survey:")
    q = input("Fall population estimate:")
    r = input("Survey comment:")
    s = input("Estimate method:")
    li = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]
    print(li)
    
###---  ---###
intro()
