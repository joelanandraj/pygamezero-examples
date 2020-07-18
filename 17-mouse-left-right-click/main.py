import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=500
#Screen height in pixels
HEIGHT=500

circle_color = 'white'

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')

    #screen.draw.circle((posx,posy),radius,color)
    screen.draw.circle((250,250),50,circle_color)

#function triggered when mouse cliked
def on_mouse_down(button):
    global circle_color
    print(button)
    if(button == mouse.LEFT):
        circle_color = 'red'
    elif(button == mouse.RIGHT):
        circle_color = 'green'
        
pgzrun.go() # Do not edit this line