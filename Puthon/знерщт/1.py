from tkinter import *
import time
import random
window=Tk()
window.wm_attributes("-topmost", "true")
window.geometry("500x400")  
canvas=Canvas(width = 500, height = 400)
canvas.pack()
window.resizable(0,0)
window.update()
def game():
    class Ball:
        def __init__(self,canvas,racket,color):
            self.win=canvas
            self.racket=racket
            self.myball=canvas.create_oval(20,20,35,35,fill=color)
            self.win.move(self.myball, 145, 100)
            chisl = [-3,-2,-1,1,2,3]
            self.x = random.choice(chisl)
            self.y=-3
            self.tch_botm=False
        def touch (self, ball_pos):
            racket_pos = self.win.coords(self.racket.line)
            if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
                if ball_pos[3] >= racket_pos[1] and ball_pos[3] <= racket_pos[3]:
                    return True
            return False
        def draw(self):
            self.win.move(self.myball, self.x,self.y)
            pos = self.win.coords(self.myball)
            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= 400:
                self.y = -3
                self.tch_botm = True
            if self.touch(pos) == True:
                self.y = -3
            if pos[0] <= 0:
                self.x = 3
            if pos[2] >= 500:
                self.x = -3
    class Racket:
        def __init__(self, canvas, color):
            self.win = canvas
            self.line= canvas.create_rectangle(100,0,200,10, fill=color)
            self.win.move(self.line, 200, 300)
            self.x = 0
            self.win.bind_all('<Key-Left>', self.turn_left)
            self.win.bind_all('<Key-Right>', self.turn_right)
        def draw(self):
            self.win.move(self.line, self.x, 0)
            pos = self.win.coords(self.line)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= 500:
                self.x = 0
        def turn_left(self, evt):
            self.x = -3
        def turn_right(self, evt):
            self.x = 3
    racket = Racket(canvas, 'black')
    ball = Ball(canvas, racket, 'orange')
    while 1:
        if ball.tch_botm == False:
            ball.draw()
            racket.draw()
        else:
            canvas.create_text(250,200,text="You lose!",font="Verdana 42", fill="red")
            break   
        window.update() 
        time.sleep(0.01)
game()
window.mainloop()   