import ball
import my_event
import turtle
import random
import heapq
import player
import time
import math
class NewGame:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        self.new_turtle = turtle.Turtle()
        self.color = (255, 0, 0)
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print("canvas w ",self.canvas_width, "canvas h ",self.canvas_height)

        self.TT = turtle.Turtle() # my edit
        self.TT.penup() # my edit
        self.TT.goto(250, 330) # my edit
        self.TT.fillcolor((0, 255, 0)) # my edit
        self.TT.pencolor((0, 255, 0)) # my edit
        self.TT.begin_fill() # my edit
        self.TT.pendown() # my edit

        SCREEN_WIDTH = 800  # My edit
        SCREEN_HEIGHT = 600 # My edit

        wn = turtle.Screen()
        wn.setup(width = SCREEN_WIDTH + 50, height = SCREEN_HEIGHT + 100) # My edit
        wn.title("Dodge the Balls") # my edit

##### Custom #####

      # Draw the star

        for i in range(5):
            self.TT.forward(35)
            self.TT.right(144)
        self.TT.forward(40)
        for i in range(5):
            self.TT.forward(35)
            self.TT.right(144)
        self.TT.forward(40)
        for i in range(5):
            self.TT.forward(35)
            self.TT.right(144)

        self.TT.end_fill()
        self.TT.penup()
        self.TT.hideturtle()

        self.screen = turtle.Screen()
        self.screen.bgcolor("Black")

#############################

        ball_radius = 0.04 * self.canvas_width
        for i in range(self.num_balls):
            x = -self.canvas_width + (i+1)*(2*self.canvas_width/(self.num_balls+1))
            y = 20
            vx = 1*random.uniform(1.0, 4.0)
            vy = 1*random.uniform(1.0, 4.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(ball_radius, x, y, vx, vy, ball_color, i))

        tom = turtle.Turtle()
        self.my_paddle = player.Paddle(40, 40, self.color, tom)
        self.my_paddle.set_location([0, -50])

        self.screen = turtle.Screen()

    # updates priority queue with all new events for a_ball
    def __predict(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.ball_list)):
            dt = a_ball.time_to_hit(self.ball_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, my_event.Event(self.t + dt, a_ball, self.ball_list[i], None))
        
        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, my_event.Event(self.t + dtX, a_ball, None, None))
        heapq.heappush(self.pq, my_event.Event(self.t + dtY, None, a_ball, None))
    
    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((255, 255, 255))   
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def create_ball(self, num_balls):
        self.num_balls = num_balls
        ball_radius = 0.04 * self.canvas_width
        for i in range(self.num_balls):
            x = -self.canvas_width + (i+1)*(2*self.canvas_width/(self.num_balls+1))
            y = 20.0
            vx = 1*random.uniform(1.0, 4.0)
            vy = 1*random.uniform(1.0, 4.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(ball_radius, x, y, vx, vy, ball_color, i))

    def __redraw(self):
        turtle.clear()
        self.my_paddle.clear()
        self.__draw_border()
        self.my_paddle.draw()
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw()
        turtle.update()
        heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))

    def __paddle_predict(self):
        for i in range(len(self.ball_list)):
            a_ball = self.ball_list[i]
            dtP = a_ball.time_to_hit_paddle(self.my_paddle)
            dtP2 = a_ball.time_to_hit_paddle_side(self.my_paddle)
            heapq.heappush(self.pq, my_event.Event(self.t + dtP, a_ball, None, self.my_paddle,"paddle"))
            heapq.heappush(self.pq, my_event.Event(self.t + dtP2, a_ball, None, self.my_paddle,"paddle_side"))
           
    # move_left and move_right handlers update paddle positions
    def move_left(self):
        if (self.my_paddle.location[0] - self.my_paddle.width/2 - 40) >= -self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] - 40, self.my_paddle.location[1]])
            self.__paddle_predict()

    # move_left and move_right handlers update paddle positions
    def move_right(self):
        if (self.my_paddle.location[0] + self.my_paddle.width/2 + 40) <= self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] + 40, self.my_paddle.location[1]])
            self.__paddle_predict()

    ############### CUSTOM #######################################################################
    
    def move_up(self):
       if (self.my_paddle.location[1] + self.my_paddle.height/2 + 40) <= self.canvas_height:
            self.my_paddle.set_location([self.my_paddle.location[0], self.my_paddle.location[1]+40])
            self.__paddle_predict()
    
    def move_down(self):
      
        if (self.my_paddle.location[1] - self.my_paddle.height/2 - 40) >= -self.canvas_height:
            self.my_paddle.set_location([self.my_paddle.location[0], self.my_paddle.location[1]-40])
            self.__paddle_predict()

    ############################################################################################## 

    ############### CUSTOM #######################################################################       
    def show_time(self, num_hit):
        self.new_turtle.clear()
        self.new_turtle.hideturtle()
        self.new_turtle.goto(self.canvas_width - 55, self.canvas_height - 35)
        self.new_turtle.write(f"{time.time() - start_time:.0f} s.", font = ("Arial", 18, "normal"))
        self.new_turtle.pencolor(255, 255, 255)
    
    def stage_clear(self):
        turtle.penup()
        turtle.setpos(0, 0)
        turtle.pencolor((255, 255, 255))
        turtle.write("Stage Clear", align="center", font=("Arial", 30, "bold"))
        turtle.update()
        time.sleep(2)

    def game_clear(self):
        turtle.penup()
        turtle.setpos(0, 0)
        turtle.pencolor((255, 255, 255))
        turtle.write("You Win!", align="center", font=("Arial", 30, "bold"))
        turtle.update()
        time.sleep(2)

    ##############################################################################################

    def clear_ball(self):
        self.ball_list = []

    def run(self):
        # initialize pq with collision events and redraw event
        for i in range(len(self.ball_list)):
            self.__predict(self.ball_list[i])
        heapq.heappush(self.pq, my_event.Event(0, None, None, None))

        # listen to keyboard events and activate move_left and move_right handlers accordingly
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

        # custom #
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        #############
        num_hit = 0
        is_stage_two = False
        is_stage_three = False
        is_stage_four = False
        is_final_stage = False

        while (True):
            self.show_time(num_hit)
            e = heapq.heappop(self.pq)
            if not e.is_valid():
                continue
            
            ball_a = e.a
            ball_b = e.b
            paddle_a = e.paddle
            type_paddle = e.type
            
         
            # update positions, and then simulation clock
            for i in range(len(self.ball_list)):
                self.ball_list[i].move(e.time - self.t)
            self.t = e.time

            if (ball_a is not None) and (ball_b is not None) and (paddle_a is None):
                # print("balls colliding")
                # print("ball a ",ball_a)
                # print("ball b ",ball_b)
                ball_a.bounce_off(ball_b)

            elif (ball_a is not None) and (ball_b is None) and (paddle_a is None):
                # print("verticall wall hit")
                # print("ball a ",ball_a)
                # print("ball b ",ball_b)
                ball_a.bounce_off_vertical_wall()
            elif (ball_a is None) and (ball_b is not None) and (paddle_a is None):
                # print("horizontal wall hit")
                # print("ball a ",ball_a)
                # print("ball b ",ball_b)
                ball_b.bounce_off_horizontal_wall()
            elif (ball_a is None) and (ball_b is None) and (paddle_a is None):
                # print("floating without any hit")
                # print("ball a ",ball_a)
                # print("ball b ",ball_b)
                self.__redraw()
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is not None) and type_paddle == 'paddle':
    ############### CUSTOM #######################################################################
                ball_a.bounce_off_paddle()
                num_hit += 1
                if num_hit == 1:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.fillcolor((0, 255, 0))
                    self.TT.pencolor((0, 255, 0))
                    self.TT.begin_fill()
                    self.TT.pencolor((0, 255, 0))
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                if num_hit == 2:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    self.TT.end_fill()
                    self.TT.fillcolor((0, 255, 0))
                    self.TT.pencolor((0, 255, 0))
                    self.TT.begin_fill()
                    self.TT.pencolor((0, 255, 0))
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                if num_hit == 3:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                    self.TT.penup()
                    self.TT.goto(-250, -25)
                    self.TT.pencolor((255, 255, 255))
                    turtle.penup()
                    turtle.setpos(0, 0)
                    turtle.pencolor((255, 255, 255))
                    turtle.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
                    turtle.done()
    ##############################################################################################

            elif (ball_a is not None) and (ball_b is None) and (paddle_a is not None) and type_paddle == 'paddle_side':

    ############### CUSTOM #######################################################################
                ball_a.bounce_off_paddle_side()
                print("hit the ball")
                num_hit += 1
                if num_hit == 1:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.fillcolor((0, 255, 0))
                    self.TT.pencolor((0, 255, 0))
                    self.TT.begin_fill()
                    self.TT.pencolor((0, 255, 0))
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                if num_hit == 2:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    self.TT.end_fill()
                    self.TT.fillcolor((0, 255, 0))
                    self.TT.pencolor((0, 255, 0))
                    self.TT.begin_fill()
                    self.TT.pencolor((0, 255, 0))
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                if num_hit == 3:
                    self.TT.goto(250, 330)
                    self.TT.fillcolor((0, 0, 0))
                    self.TT.pencolor((0, 0, 0))
                    self.TT.begin_fill()
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.forward(40)
                    for i in range(5):
                        self.TT.forward(35)
                        self.TT.right(144)
                    self.TT.end_fill()
                    self.TT.end_fill()
                    self.TT.penup()
                    self.TT.hideturtle()
                    self.TT.penup()
                    self.TT.goto(-250, -25)
                    self.TT.pencolor((255, 255, 255))
                    turtle.penup()
                    turtle.setpos(0, 0)
                    turtle.pencolor((255, 255, 255))
                    turtle.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
                    turtle.done()

            if time.time() - start_time >= 10 and is_stage_two == False:
                self.stage_clear()
                is_stage_two = True 
                self.clear_ball()
                self.num_balls += 1
                self.pq = []
                self.create_ball(5)
                for i in range(len(self.ball_list)):
                    self.__predict(self.ball_list[i])
                heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))
                self.__paddle_predict()
            
            if time.time() - start_time >= 22 and is_stage_three == False:
                self.stage_clear()
                is_stage_three = True
                self.clear_ball()
                self.pq = []
                self.create_ball(6)
                for i in range(len(self.ball_list)):
                    self.__predict(self.ball_list[i])
                heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))
                self.__paddle_predict()

            if time.time() - start_time >= 34 and is_stage_four == False:
                self.stage_clear()
                is_stage_four = True
                self.clear_ball()
                self.pq = []
                self.create_ball(7)
                for i in range(len(self.ball_list)):
                    self.__predict(self.ball_list[i])
                heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))
                self.__paddle_predict()

            if time.time() - start_time >= 46 and is_final_stage == False:
                self.game_clear()
                is_final_stage = True
                self.clear_ball()
                self.pq = []
                self.create_ball(7)
                for i in range(len(self.ball_list)):
                    self.__predict(self.ball_list[i])
                heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))
                self.__paddle_predict()
                turtle.done()
    ##############################################################################################
            self.__predict(ball_a)
            self.__predict(ball_b)

            # regularly update the prediction for the paddle as its position may always be changing due to keyboard events
            self.__paddle_predict()

        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()

# num_balls = int(input("Number of balls to simulate: "))
num_balls = 4
my_simulator = NewGame(num_balls)
start_time = time.time()
my_simulator.run()
