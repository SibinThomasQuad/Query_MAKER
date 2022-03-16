import csv
def make_query(data1,data2):
    query = "INSERT INTO `Achivement_list` (`Name`, `Reward`) VALUES ('"+data1+"', '"+data2+"');"
    print(query)
def scrape(row_location):
    data_list = []
    with open("data.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            data_list.append(row[int(row_location)])
    return data_list
names = scrape(0)
task_1 = scrape(1)
reward_1 = scrape(2)
task_2 = scrape(3)
reward_2 = scrape(4)
task_3 = scrape(5)
reward_3 = scrape(6)
task_4 = scrape(7)
reward_4 = scrape(8)
task_5 = scrape(9)
reward_5 = scrape(10)
locations = 0
for name in names:
  if(task_1[locations] != '-'):
    make_query(str(name)+"("+str(task_1[locations])+")",reward_1[locations])
  if(task_2[locations] != '-'):
    make_query(str(name)+"("+str(task_2[locations])+")",reward_2[locations])
  if(task_2[locations] != '-'):
    make_query(str(name)+"("+str(task_3[locations])+")",reward_3[locations])
  if(task_4[locations] != '-'):
    make_query(str(name)+"("+str(task_4[locations])+")",reward_4[locations])
  if(task_5[locations] != '-'):
    make_query(str(name)+"("+str(task_5[locations])+")",reward_5[locations])
  locations = locations + 1
