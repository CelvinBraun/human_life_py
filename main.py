from life_turtle import Life
from turtle import Screen
import datetime
import math

today = str(datetime.date.today())

screen = Screen()
screen.setup(height=500, width=950)
screen.title("Life in Weeks:")
screen.tracer(0)

years = screen.textinput(title="Average age of human 79 years", prompt="For different age enter age: ")
if len(years)==0:
    years = 79

format_not_right = True
while format_not_right:
    birthday = screen.textinput(title="Your birthday", prompt="Please enter in format: day,month,year:")
    birthday = birthday.split(",")
    if len(birthday)==3:
        format_not_right = False

age_date = str(datetime.date(int(birthday[2]),int(birthday[1]),int(birthday[0])))
age_date = datetime.datetime.strptime(age_date, "%Y-%m-%d").date()
today = datetime.datetime.strptime(today, "%Y-%m-%d").date()
days = (today- age_date).days

age = math.ceil(days/7)

# creating weeks for avg life span
life = Life(int(age), int(years))
screen.update()




life.fill_weeks()
screen.update()
screen.exitonclick()