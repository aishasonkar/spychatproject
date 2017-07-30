from spy_details import Spy,friends,chatMessage,spy
from steganography.steganography import Steganography
from termcolor import colored
from datetime import datetime
def get_now():
    return datetime.datetime.now()
#here we show my_app is true1 and it run

my_app=True
while my_app:
    print"let's our app get start"

#here we store our messages in list
    STATUS_MESSAGES=["MY name is bond","busy","available"]
    question="do you want to continue" + spy.salutation + " " +spy.name + "(y/n)?"
    existing=raw_input(question)

#we create add status funcion.due to this function we add new status
    def add_status():
        update_status_message=None
        if spy.current_status_message!=None:
           print colored("your current status message is: %s\n"%(spy.current_status_message),"red")
        else:
            print"you don't have status message"
            default=raw_input("you want to select older message y/n")
            if default.upper()=="N":
                new_status_message=raw_input("do you want change the status")
                if len(new_status_message)>0:
                    upadate_status_message=new_status_message
                    STATUS_MESSAGES.append(upadate_status_message)
                    print STATUS_MESSAGES
            if default.upper()=="Y":
                    print colored("what status message you select","blue")
                    item_position=1


                    for messages in STATUS_MESSAGES:
                        item_position
                        print str(item_position)+". "+ messages
                        item_position=item_position+1

                    status_choice=raw_input("enter your status message choice")
                    if int(status_choice)>len(STATUS_MESSAGES):
                         print"Buzzz"
                    if len(STATUS_MESSAGES)>=int(status_choice):
                        update_status_message=STATUS_MESSAGES[ int(status_choice)-1]
                        print "your stastus message is :%s"%(update_status_message)

# here we create add frien funtion due to this function we add friends in list
    def add_friend():
        new_friend=Spy('','',0,0.0)


        new_friend.name=raw_input("enter the name of new friend")
        new_friend.salutation=raw_input("enter the salutation of new friend")
        new_friend.name=new_friend.salutation+" ." +new_friend.name
        new_friend.age=raw_input("enter the age of new friend")
        new_friend.age=int(new_friend.age)
        new_friend.rating=raw_input("enter the rating of new  friend")
        new_friend.rating=float(new_friend.rating)

#here we add new friend according follow some condition. if following some conditions are not satisfied we cannot add friend
        if len(new_friend.name)>0 and 12<new_friend.age<50 and new_friend.age>=spy.rating:
            friends.append(new_friend)
            print"friend added"
        else:
            print"new friend is invalid"
        return len(friends)

#here we have a function.due to this function we select one friend
    def select_friend():
        item_index=0

#we declare variable friend for print no. of friendsname,age,rating with their indexing
        for friend in friends:
            print "%d %s aged %d with rating %f is online" % (item_index+1 , friend.name, friend.age,friend.rating)
            item_index=item_index+1

#
        friend_choice=raw_input("select your friend")
        friend_choice_position=int(friend_choice)-1
        return friend_choice_position

#here we create send message function which is help to encrypt our message and send it
    def send_message():
        friend_choice=select_friend()
        real_image=raw_input("enter name of image")
        # real_image=r'C:/Users/DELL/Desktop/secret/jerry.jpg'
#here we ask user path of real image and message store in other image
        output_path=r"C:/Users/DELL/Desktop/secret/jerry_output.jpg"
        text=raw_input("what do you want to write?")
#for encryption we use stagenography
        Steganography.encode(real_image,output_path,text)

#here  we create read message function which is read message in which firstly we select friend
    def read_message():
        sender=select_friend()
#here we decode text in img url
        secret_text=Steganography.decode('C:/Users/DELL/Desktop/secret/jerry_output.jpg')
        print colored(secret_text,"yellow")
#here we store our message in mew_chat variable
        new_chat=chatMessage(True,secret_text)
        friends[sender].chats.append(new_chat)
        print" message appended"


#here we create chat history function that show chats
    def read_chat_history():
#read for function is return indexig of friend
        read_for = select_friend()

        for chat in friends[read_for].chats:
            print chat
            if chat.sent_by_me:
                print '%s %s: %s' % (chat.time.strftime("%d %B %Y"), 'you said:', chat.message)
            else:
                    print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

#number of chat store in chat name variable
    def start_chat(spy):
        current_status_message = None

        spy.name=spy.salutation+''+ spy.name

        if 12 < spy.age < 50:
            print 'Authentication complete. Welcome ' + spy.name + ' age: ' + str(spy.age) + ' and rating of: ' + str( spy.rating) + ' Proud to have you onboard'



        if spy.rating > 4.5:
            print 'Great ace!'
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
#here we create menu
        show_menu=True
#here we select the menu choice from menu
        while show_menu:
            menu_choices=raw_input (colored("what do you want to do \n 1.Add status\n 2.Add a friend\n 3.send a secret message\n 4.Read a secret message\n 5.read chat history","blue"))
            menu_choice=menu_choices
            if menu_choice.isdigit():
                if len(menu_choice) > 0:
                    menu_choice = int(menu_choice)


                if menu_choice==1:
                    print colored("you choose update status", "blue")
                    spy.current_status_message= add_status()
                elif menu_choice==2:
                    print colored("you choose add friend","red")
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice==3:
                    print colored("you choose secret message","red")
                    send_message()
                elif menu_choice==4:
                    print colored("you choose read message","green")
                    read_message()
                elif menu_choice==5:
                    print colored("you choose read chat history","yellow")
                    read_chat_history()
                else:
                    show_menu=False
    #here we create  dictionary of name spy and code refactoring
    if existing.upper()=="Y":
        start_chat(spy)
        my_app=False

    elif existing.upper() == "N":
        spy = Spy('', '', 0, 0.0)
        spy.name = raw_input(colored('Welcome to spy chat, Enter your spyname first',"yellow"))
        # checking for the valid name
        if spy.name.isalpha():
            if len(spy.name) > 0:
                spy.salutation = raw_input(colored('are you miss and Mr',"yellow"))
                spy.age = raw_input(colored('Please enter your age',"yellow"))
                # checking for the valid age
                if spy.age.isdigit():
                    spy.age = int(spy.age)
                    spy.rating = float(raw_input(colored('Enter your spy rating',"yellow")))
                    start_chat(spy)
                else:
                    print 'enter age only in valid datatype'




