def nature():
    x = "TREE"
    y = "dolphine"
    def forest():
        print(x)

        def sea():
            print(y)

        sea()

    forest()
nature()


#built in function
print(len([1,2,3]))