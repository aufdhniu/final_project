Project: Dodge Balls
	
	Objective of the game is to survive and avoid hitting the ball for the period of time.

  Dodge balls game is the game that require player to dodge the ball that will bounce around in the field, player will have three stars which means the player life. If player hit the ball, the stars will decrease by one and if player's stars run out, game over. If player survive in the period of time, stage will clear and there'll be a new stage which have more balls than the former stage. Player can get hit from all side so it's a little bit hard to play.

	

How to install and run the project

  	After you fork this file, you can play the game in new_ball.py files. To get better information, watch video from the link below. 

Usage

	https://www.youtube.com/watch?v=3-ce-keld14


This is my uml diagram

	https://drive.google.com/file/d/19kyxf41qFctTdlqyG3jAud6Ae8pCxDN8/view?usp=sharing

class Ball:

used for draw the ball and label how bouncing physics of the ball works

class NewGame:

our main work is here create star which is symbol of life point in the game (use self.TT) and will fill the color black when you get hit, also include the border of the game field, control the paddle (which I modified to make it be able to move up and down too), adjust the speed, amount of balls in one wave, including amount of wave itself.

class Paddle:

use for create paddle (player) and set its location

class my_event:

count the hit of object

In first version that I uploaded, the player is able to get hit in left, right , up, down direction but there's a bug from heapq that make balls hit the air at the previous location or nearby, the conclusion that I come up is when the balls hit the wall, it'll predict that whether the ball will hit the player or not. If yes, then no matter it'll hit or not it still count as a hit (and the it get even worse since I make the ball be able to get hit by left and right side too). I manage to fix it but can't maintain the player's ability of getting on left and right side. (Latest version: I fixed the bug. Also, be able to hit the side of paddle without a bug too.)

	so right now as I see, program seems to run as good as I'm expected.

If I have to rate my project, I think I'll go for 90 because the player can get hit from every side.
