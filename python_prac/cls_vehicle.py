# Assignment
# create class vehicle...with properties


class vehicle:
    type='four wheeler'
    make='audi'
    model='e3'
    colour='red'
    release=2011

    # def __init__(self):
    #     self.type=''
    #     self.make=''
    #     self.model=''
    #     self.colour=''
    #     self.release=0

    def set_info(self,t,mk,mo,c,r):
        self.type=t
        self.make=mk
        self.model=mo
        self.colour=c
        self.release=r

    def get_info(self):
        print(self.type)
        print(self.make)
        print(self.model)
        print(self.colour)
        print(self.release)

v1=vehicle()
v1.get_info()

# v1.set_info('two wheeler','honda','g8','blue',2019)
# v1.get_info()

