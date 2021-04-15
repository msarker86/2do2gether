"""File to seed the habits database to run tests on functions"""
from datetime import datetime
import crud
from model import db, User, User_habit, Habit, Habit_log, Journal_log, Messages, connect_to_db


user_1 = User(fname="Andrew" lname='Gerber', email='andrew.gerber@gmail.com', password='and123')
user_2 = User(fname="Lana" lname='Landor', email='lana.landor@gmail.com', password='lan123')
user_3 = User(fname="Wana" lname='Sour', email='wana.sour@gmail.com', password='wan123')

habit_1 = Habit(name='yoga')
habit_2 = Habit(name='running')
habit_3 = Habit(name='meditation')
habit_4 = Habit(name='reading')

journal_1 = Journal_log(journal_entry="Completing the task today was an achievement")
journal_2 = Journal_log(journal_entry="Breathing has gotten much better")
journal_3 = Journal_log(journal_entry="Forgot to do yoga today, will add 10 extra mins tom")
journal_4 = Journal_log(journal_entry="Really tough run today")

user_habit_1=User_habit(user_id=1, habit_id=1, accountability_partner_id=2, goal=20, completed=False, name='yoga', type_of_execution='hours', start_date='04-13-2021', end_date='05-14-2021')
user_habit_2=User_habit(user_id=1, habit_id=3, accountability_partner_id=2, goal=25, completed=False, name='meditation', type_of_execution='days', start_date='04-13-2021', end_date='05-14-2021')
user_habit_3=User_habit(user_id=2, habit_id=1, accountability_partner_id=1, goal=20, completed=False, name='yoga', type_of_execution='hours', start_date='04-13-2021', end_date='05-14-2021')
user_habit_4=User_habit(user_id=2, habit_id=2, accountability_partner_id=1, goal=10, completed=False, name='running', type_of_execution='hours', start_date='04-13-2021', end_date='05-14-2021')

habit_log_1=Habit_log(user_habit_id=1,journal_id=1,date_of='04-13-2021',progress=1)
habit_log_2=Habit_log(user_habit_id=2,journal_id=2,date_of='04-13-2021',progress=1)
habit_log_3=Habit_log(user_habit_id=3,journal_id=3,date_of='04-13-2021',progress=1)
habit_log_4=Habit_log(user_habit_id=4,journal_id=4,date_of='04-13-2021',progress=0.5)

messages_1=Messages(user_habit_id=1, sender_id=2, receiver_id=1, message_date='04-13-2021', message='Fantastic job finishing the task at hand today')
messages_2=Messages(user_habit_id=2, sender_id=2, receiver_id=1, message_date='04-13-2021', message='I bet meditating was great to keep the stress at bay')
messages_3=Messages(user_habit_id=3, sender_id=1, receiver_id=2, message_date='04-13-2021', message='Just 20 mins of yoga will make a huge difference, you still have time')
messages_4=Messages(user_habit_id=3, sender_id=1, receiver_id=2, message_date='04-13-2021', message='Fantastic job on a great run!')


if __name__=='__main__':
    from server import app
    connect_to_db(app)
    os.system('dropdb habits')
    os.system('createdb habits')
    connect_to_db(server.app)
    db.create_all()