from datetime import datetime
class Spy:

    def __init__(self,name ,age ,rating ,salutation):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.chats=[]
        self.current_status_message = None
        self.is_online=True



class chatMessage:

    def __init__(self,sent_by_me,message):
        self.message=message
        self.sent_by_me=sent_by_me
        self.time=datetime.now()




spy=Spy("simran",19,4.5,"miss")
friend1 = Spy("pooja",20,4.6,"miss")
friend2= Spy("sahil",19,4.4,"mr")
friend3= Spy("ria",20,4.5,"miss")




friends=[friend1,friend2,friend3]