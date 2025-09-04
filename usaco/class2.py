lis = []
A_lis = []
def sort_tool():
    total_num = int(input("Enter number of students: "))
    for i in range(total_num):
        name = input("Enter student name: ")
        if name[0] == "A":
            A_lis.append(name)
        lis.append(name)
    if len(A_lis) != 0:
        print(f"name(s) of people that start with A: {A_lis}")
    else:
        print("N/A")
    lis.sort()
    print(lis)

sort_tool()