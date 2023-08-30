class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_call(self,number):
        print("calling..{}".format(number))

mobile_obj = Mobile("iPhone 12 Pro", "12 MP")
mobile_obj.make_call(9876543210)
