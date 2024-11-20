item = {"coffee":1,"coke":1,"cup":1,"pen":1,"milk":1,"paper":1,"note":1}

while True:
    option = input("Please enter the manu 1) 재고 조회 2) 입고 3) 출고 4)종료: ")
    if option == "1":
        name = input("Enter the product name")
        print(f"{name} : {item[name]}")
    elif option == "2":
        name, count = input("Enter the product name: ").split()
        item[name] += int(count)
        print(f"{name} : {item[name]}")
    elif option == "3":
        name, count = input("Enter the product name: ").split()
        item[name] -= int(count)
        print(f"{name} : {item[name]}")
    elif option == "4":
        print("end")
        break
    