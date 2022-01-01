with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


# 在原来的文件追加一行
# with open("my_file.txt",mode = "a") as file:
#     file.write("\nnew text.")


# 创建一个新的文件
# with open("new_file.txt",mode = "w") as file:
#     file.write("\nnew text.")
