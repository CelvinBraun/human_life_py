from life_turtle import Life
from turtle import Screen

screen = Screen()
screen.setup(height=500, width=800)
screen.title("Life in Weeks:")
screen.tracer(0)

years = screen.textinput(title="Average age of human 79 years", prompt="For different age enter age: ")
if len(int(years))==0:
    years = 79

print(len(years))
#life = Life(years)
format_not_right = True

screen.update()

while format_not_right:
    birthday = screen.textinput(title="Your birthday", prompt="Please enter in format: day,month,year:")
    birthday = birthday.split(",")
    if len(birthday)==3:
        format_not_right = False


life.fill_weeks()

screen.exitonclick()