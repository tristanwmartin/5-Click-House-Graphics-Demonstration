import graphics
from graphics import *

def main():

# You are to write a program that allows the user to draw a simple house
# using five mouse clicks. The first two clicks will be the opposite corners of
# the rectangular frame of the house. The third click will indicate the center
# of the top edge of a rectangular door. The door should have a total width
# that is 1/5 the width of the house frame. The sides of the door should
# extend from the corners of the top down to the bottom of the frame. The
# fourth click will indicate the center of a square window. The window is
# half as wide as the door. The last click will indicate the peak of the roof.
# The edges of the roof will extend from the point at the peak to the corners
# of the top edge of the house frame.

    winName = "The 5 Click House"
    win = GraphWin(winName, 600, 600)

    # Draw a cute background of grass and sky for the user to draw on top of.
    grass = Rectangle(Point(0,600), Point(600, 400))
    grass.draw(win)
    grass.setWidth(0)
    grass.setFill(color_rgb(114, 237, 83))
    sky = Rectangle(Point(0,400), Point(600, 0))
    sky.draw(win)
    sky.setWidth(0)
    sky.setFill(color_rgb(156, 244, 247))

    # Get the position of first mouse click                
    firstClick = win.getMouse()
    corner_1x, corner_1y = firstClick.getX(), firstClick.getY()

    # Get the position of second mouse click 
    secondClick = win.getMouse()
    corner_2x, corner_2y = secondClick.getX(), secondClick.getY()

    # Draw a rectangle at both of those positions
    rect = Rectangle(Point(corner_1x, corner_1y), Point(corner_2x, corner_2y))
    rect.setWidth(2)
    rect.draw(win)
    rect.setFill(color_rgb(240, 213, 170))

    houseWidth = corner_2x - corner_1x

    # Get the position of third mouse click 
    thirdClick = win.getMouse()
    leftDoor = thirdClick.getX() - (0.5 * (0.2 * houseWidth))
    rightDoor = thirdClick.getX() + (0.5 * (0.2 * houseWidth))

    # Draw a rectangle door
    door = Rectangle(Point(leftDoor, firstClick.getY()), Point(rightDoor, thirdClick.getY()))
    doorCenter = door.getCenter()
    doorKnob = Circle(doorCenter, 4)
    doorKnob.move(houseWidth * .05, 0)
    door.draw(win)
    door.setWidth(2)
    door.setFill(color_rgb(240, 179, 170))
    doorKnob.draw(win)
    doorKnob.setFill(color_rgb(222, 202, 102))

    # Get the position of fourth mouse click
    fourthClick = win.getMouse()
    leftWindow_X = fourthClick.getX() - (.05 * houseWidth)
    leftWindow_Y = fourthClick.getY() - (.05 * houseWidth)

    rightWindow_X = fourthClick.getX() + (.05 * houseWidth)
    rightWindow_Y = fourthClick.getY() + (.05 * houseWidth)

    # Draw rectangle for window. Additional window panes for fun.
    window = Rectangle(Point(leftWindow_X, leftWindow_Y), Point(rightWindow_X, rightWindow_Y))
    paneVertical = Line(Point(fourthClick.getX(), fourthClick.getY() + (.05 * houseWidth)), Point(fourthClick.getX(), fourthClick.getY() - (.05 * houseWidth)))
    paneHorizontal = Line(Point(fourthClick.getX() - (.05 * houseWidth), fourthClick.getY()), Point(fourthClick.getX() + (.05 * houseWidth), fourthClick.getY()))
    window.draw(win)
    window.setFill(color_rgb(232, 250, 250))
    window.setWidth(2)
    paneVertical.draw(win)
    paneVertical.setFill("grey")
    paneHorizontal.draw(win)
    paneHorizontal.setFill("grey")

    # Get the position of fifth mouse click.
    fifthClick = win.getMouse()

    # Draw two lines from each top corner of first rectangle to the position of mouseclick5
    peakRoof = Point(fifthClick.getX(), fifthClick.getY())
    leftRoof = Line(Point(corner_1x, corner_2y), peakRoof)
    rightRoof = Line(Point(corner_2x, corner_2y), peakRoof)
    leftRoof.draw(win)
    leftRoof.setWidth(2)
    rightRoof.draw(win)
    rightRoof.setWidth(2)
    
main()
