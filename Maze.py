
def f_clear() :
    if at_goal() :
        done()
    if front_is_clear() :
        move()

def r_clear() :
     while right_is_clear() and front_is_clear():
        turn_left()
        turn_left()
        turn_left()
        f_clear()
        
while not at_goal():
    
    #going right
    if right_is_clear() == True and front_is_clear() == True:
        r_clear()
     #jump  
    if right_is_clear() == False and front_is_clear() == True:
        f_clear()
        
    if front_is_clear() == False and right_is_clear() == False :
        turn_left()
        f_clear()
        
    if front_is_clear() == False and right_is_clear() == True :
        turn_left()
        turn_left()        
        turn_left()
        f_clear()
        
    
  
  