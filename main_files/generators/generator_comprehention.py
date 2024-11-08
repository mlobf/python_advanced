# Toda vez que é feito um compre dentro de um (), é gerado um
#   generator


def set_new_generator(rep:int)->str:
    x = (i for i in range(rep))

    for _ in range(rep):
        print(next(x))
        print("marcos leme")

if __name__ == '__main__':
    set_new_generator(1000)
