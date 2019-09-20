import time
import turtle

turtle.setup()
turtle.bgcolor("black")
turtle.color("white")
turtle.home()
turtle.down()
turtle.left(90)

taille = 20
directionP = "N"

direction = "NNEESOOESEENNEEOOSEOSEEENNESENSSENNEESSOOEEENNEEOOSEOSEEENEENOOEESOOSEEEEEEENONSESENNSSENNEESSOOEEENNSSEENNSSEEENOONEEOOSEESEEEENNEESSOOEEENNEESOOEESENNESENSSEEENOONEEOOSEESEEEENNSSEEENNEESOOEESEEEENNEEOOSEOSEEENNEESSOOEEENNEESOOESEENNEEOOSEOSEEEENNOEEOSSEEEEENNEESOOEESOOEEENNEESOOESEENNSSEENNSSENNESNESSENNEEOOSEOSEEENNSSEENNSSEEENOONEEOOSEESENNEEOOSEOSEEEEEENNEESSOOEEENNEEOOSEOSEEENNESNESSENNEESOOEESENNSSENNESENSS"
for i in range (len(direction)):
	if (i > 1):
		directionP = direction[i-1]
	#endif
	if (direction[i] == "N"):

		if (directionP == "E"):
			turtle.left(90)
		elif (directionP == "O"):
			turtle.right(90)
		elif (directionP == "S"):
			turtle.left(180)
		#endif

		turtle.forward(taille)
	#endif
	elif (direction[i] == "E"):

		if (directionP == "N"):
			turtle.right(90)
		elif (directionP == "O"):
			turtle.right(180)
		elif (directionP == "S"):
			turtle.left(90)
		#endif

		turtle.forward(taille)
	#endif
	elif (direction[i] == "S"):

		if (directionP == "N"):
			turtle.right(180)
		elif (directionP == "O"):
			turtle.left(90)
		elif (directionP == "E"):
			turtle.right(90)
		#endif

		turtle.forward(taille)
	#endif
	elif (direction[i] == "O"):

		if (directionP == "N"):
			turtle.left(90)
		elif (directionP == "S"):
			turtle.right(90)
		elif (directionP == "E"):
			turtle.right(180)
		#endif

		turtle.forward(taille)
	#endif
#endfor
turtle.up()
time.sleep(10)