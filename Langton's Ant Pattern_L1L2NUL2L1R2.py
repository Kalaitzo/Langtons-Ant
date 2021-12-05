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
    ant.shape('circle')     
      
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
              
            ant.fillcolor("cyan")                                       
            invert(maps, ant, "cyan")
            ant.stamp() 
            ant.left(60) 
            ant.forward(step)                          
            pos = coordinate(ant)
            step_counter=step_counter+1
              
        elif maps[pos] == "cyan":
            
            ant.fillcolor("darkcyan") 
            invert(maps, ant, "darkcyan") 
            ant.stamp() 
            ant.left(120) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1
            
        elif maps[pos] == "darkcyan":
            
            ant.fillcolor("royalblue") 
            invert(maps, ant, "royalblue") 
            ant.stamp() 
            #ant.left(90) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1

        elif maps[pos] == "royalblue":
            
            ant.fillcolor("blueviolet") 
            invert(maps, ant, "blueviolet") 
            ant.stamp() 
            ant.right(180) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1

        elif maps[pos] == "blueviolet":
            
            ant.fillcolor("mediumorchid") 
            invert(maps, ant, "mediumorchid") 
            ant.stamp() 
            ant.left(120) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1
            
        elif maps[pos] == "mediumorchid":
            
            ant.fillcolor("pink") 
            invert(maps, ant, "pink") 
            ant.stamp() 
            ant.left(60) 
            ant.forward(step) 
            pos = coordinate(ant)
            step_counter=step_counter+1

        elif maps[pos] == "pink":
            
            ant.fillcolor("white") 
            invert(maps, ant, "white") 
            ant.stamp() 
            ant.right(120) 
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
