import turtle
import pandas

df= pandas.read_csv("50_states.csv")
states_list=df["state"].tolist()
x_cor_list=df["x"].tolist()
y_cor_list=df["y"].tolist()

screen= turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state=[]



while len(guessed_state)<50:
    answer = turtle.textinput(f"{len(guessed_state)}/50 state guessed correctly", "What's the other US State?").title()


    if answer in states_list:
        answer_index = states_list.index(answer)
        guessed_state.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor_list[answer_index],y_cor_list[answer_index])
        t.pendown()
        t.write(answer)

    elif answer=="Exit":
        break

not_guessed_states=list(set(states_list)-set(guessed_state))
data_frame=pandas.DataFrame(not_guessed_states, columns=['Remember These'])
data_frame.to_csv("NotGuessedStates")