
import turtle



def draw_segment(from_coords,  to_coords):
    turtle.setpos(from_coords[0] + offset[0], from_coords[1] + offset[1])
    turtle.pendown()
    turtle.goto(to_coords[0] + offset[0], to_coords[1] + offset[1])
    
    
def draw_labelled_segment(from_coords, to_coords, label):
    draw_segment(from_coords, to_coords)
    turtle.penup()
    turtle.setpos( offset[0] + (from_coords[0]+to_coords[0])//2 + 12,
                   offset[1] + (from_coords[1]+to_coords[1])//2)
    turtle.write(label)


def init_turtle():
    global offset
    offset = [-300, -300] 
    turtle.clear()
    turtle.penup()





if __name__ == '__main__':
    init_turtle()
    #draw_segment([50, 50], [100, 100])
    draw_labelled_segment([50, 50], [150, 150], "elem 1")
    draw_labelled_segment([150, 150], [200, 50], "elem 2")
    draw_labelled_segment([200, 50], [300, 150], "elem 3")
    