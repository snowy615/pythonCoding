info = open("/Users/snowyan/PycharmProjects/cccc/commentName", "r")
n = int(info.readline())
for i in range(n):
    name, gender, grade, comment = info.readline().split()
    if comment == "A":
        print(f"Students have been analyzing literature, including poetry, plays and novels. Assessments for IB English primarily focus on timed essay writing and include certain presentations and class discussions. The final mark in grade 11 is considered a predicted mark for their exam in May of 2024. \n Predicted Grade IB 7 \n {name} is an excellent student. {gender} seeks and implements feedback regularly. {name}'s work demonstrates maturity and insight and is consistently of the highest quality. {gender} is a thoughtful and considerate person. {name} helps others and provides intelligent and thoughtful feedback. {name} should continue to improve her analytical skills by reading and writing with purpose.\n\n")
    elif comment == "B":
        print(f"Congratulations on successfully completing Theory of Knowledge 11. {name} is an absolute pleasure to teach. {gender} constantly seeks feedback from peers and from teachers. {gender} implements the feedback and consistently seeks to improve academic endeavours. {gender} participates in class discussions and provides thoughtful and insightful comments. Going forward {name} should continue to engage peers for exchanging ideas and developing arguments. Great work on your exhibition. Very impressive objects and fantastic presentation. Well done.\n\n")
    else:
        print(f"{name} is failing. Please seek help if needed. I have no idea what she is doing.")