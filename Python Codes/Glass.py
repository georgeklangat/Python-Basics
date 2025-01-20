class Glasses:
    pass


class Shader:
    def printShadeIndex(self):
        pass
        # print('high')


class Sunglasses(Glasses, Shader):
    pass


obj = Sunglasses()
obj.printShadeIndex()
