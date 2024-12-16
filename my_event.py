class Event:
    def __init__(self, time, ball_a, ball_b, paddle, type = None):
        self.time = time
        self.type = type
        self.a = ball_a
        self.b = ball_b
        self.paddle = paddle
        if ball_a is not None:
            self.count_a = ball_a.count
        else:
            self.count_a = -1
        if ball_b is not None:
            self.count_b = ball_b.count
        else:
            self.count_b = -1
        if paddle is not None:
            self.paddle_count = paddle.move_count
        else:
            self.paddle_count = -1

    def __lt__(self, that):
        return self.time < that.time

    def is_valid(self):
        if (self.a is not None) and (self.a.count != self.count_a):
            return False
        if (self.b is not None) and (self.b.count != self.count_b):
            return False
        if (self.paddle is not None) and (self.paddle.move_count != self.paddle_count):
            return False
        return True
