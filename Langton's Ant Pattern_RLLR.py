import turtle 
  
def langton():
    
    step_counter=0
    
    # Initializing the Window 
    window = turtle.Screen() 
    window.bgcolor('white') 
    window.screensize(1000,1000) 
  
    # Contains the coordinate and colour 
    maps = {} 
  
    # Initializing the Ant 
    ant = turtle.Turtle()
      
    # shape of the ant 
    ant.shape('square')     
      
    # size of the ant 
    ant.shapesize(0.5) 
      
    # speed of the ant 
    ant.speed(100000000000)                                  
      
    # gives the coordinate of the ant                 
    pos = coordinate(ant)
    
    counter=turtle.Turtle(visible=False)
    
    while True:
        counter.undo()
        counter.penup()
        counter.setposition(-600,350)
        counter.write("Steps=" +str(step_counter),font=("Arial",20,"normal"))
        # print(step_counter)
        # distance the ant will move 
        step = 10
        if pos not in maps or maps[pos] == "white": 
              
            ant.fillcolor("red")                                       
            invert(maps, ant, "red")
            ant.stamp() 
            ant.right(90) 
            ant.forward(step)                          
            pos = coordinate(ant)
            step_counter=step_counter+1
              
        elif maps[pos] == "red":
            
            ant.fillcolor("yellow") 
            invert(maps, ant, "yellow") 
            ant.stamp() 
            ant.left(90) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1
            
        elif maps[pos] == "yellow":
            
            ant.fillcolor("blue") 
            invert(maps, ant, "blue") 
            ant.stamp() 
            ant.left(90) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1

        elif maps[pos] == "blue":
            
            ant.fillcolor("white") 
            invert(maps, ant, "white") 
            ant.stamp() 
            ant.right(90) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1
 
def invert(graph, ant, color): 
    graph[coordinate(ant)] = color 
  
def coordinate(ant): 
    return (round(ant.xcor()), round(ant.ycor()))

#------------ΜΑΙΝ------------#
if __name__=="__main__":
    langton()
