class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def SqSum(self):
        self.sqx=self.x**2
        self.sqy=self.y**2
        self.sqz=self.z**2
        print (self.sqx+self.sqy+self.sqz)
a=Point(1,3,5)
a.SqSum()
