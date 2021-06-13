def getdate():
    from datetime import datetime
    return str(datetime.now())

users = {1: "Pramod", 2: "Shikha", 3: "Shreya",4:"Radhika",5:"Anusha",6:'Richa',7:"Saman",0:"New User ?"}
info = '''This is a Health Manager Program Which Records Your Diet And Exercise'''
print(f'{info:|^80}\n')
print("Registered Users Are : \nCode Users")
for code,user in users.items():
    print(f"{code:^4}.{user}")

inp = int(input("Enter Your User Code here : "))
if inp != 0: user_name = users[inp]
else:
    user_name = input("Enter Your Name Please : ")

def Health_Manager(user_name):
    print(f"\nTime - {getdate()}\n{'':->50}\nYou chose - {users[inp]}")
    record_type = int(input("What type of data you want to record ?\n[0] - Diet\n[1] - Exercise\nChoice: "))
    diet_exercise = (lambda x:'Diet' if not x else "Exercise")(record_type)

    data = (lambda: input("What have you eaten since morning\n: ") if not record_type else input("Enter your workout here \n: "))
    user_data_items = []
    print("\nType 'exit' to write changes to the file.\nPress Enter to write next item name\n")

    count = 1
    while True:
        print(count,end='.')
        item = data()
        if item=='exit':
            count = 1
            break
        user_data_items.append(f'.{item}\n')
        count+=1

    file_name = f'{user_name}_{diet_exercise}.txt'

    with open(f"{file_name}",'a+') as file:
        date = getdate()
        file.write(f"{date:=^60}\n")
        a = file.writelines(user_data_items)

        file.seek(0)
        print(f"\nSuccessfully recorded the data: {file_name}\n{file.read()}\n{'ThankYou!!':-^100}")

Health_Manager(user_name)
