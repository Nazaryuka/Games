class test():
    def __init__(self, a):
        self.num = a

arra = []
def work(mun):
    global arra
    for i in range(mun):
        k = test(i)
        arra.append(k)


work(5)
print(arra[4].num)