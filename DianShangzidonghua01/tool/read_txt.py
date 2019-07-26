def read_txt(filename):
    filepath = "../data/"+filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt("login.txt"))
    print("--" * 50)
    # 新建空列表
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    print(arrs)