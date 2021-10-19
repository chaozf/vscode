# using default arguments
# function definition with default arguments
# default arguments with name is useful that 调用时可以改变顺序
def boxVolume(length=1, width=1, height=1):
    return length * width * height


print("The default box volume is:", boxVolume())
print("\nThe volume of a box with length 10, ")
print("width 1 and heigth 1 is:", boxVolume(10))
