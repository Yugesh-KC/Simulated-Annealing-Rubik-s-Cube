from cube import cube
import math
import random

def anneal (cube:cube,iteratoins_per_temp_change=1000,initial_temp = 100,alpha = 0.99,min_temp=1e-3):  #alpha means by how much to decrease the temp
    temperature=initial_temp
    initial_loss = cube.loss()
    if initial_loss==0:
        return cube
    while(1):
        iterations = iteratoins_per_temp_change
        for i in range(iterations):
            move=cube.make_random_move()     #saving move incase we want to return to previous state
            new_loss=cube.loss()
            if new_loss==0:
                return cube
            delta = new_loss-initial_loss
            acceptance_probability = math.exp(-delta/temperature)    #when new_loss is less prob always greater than 1 
            random_acceptance = random.uniform(0,1)
            if (random_acceptance<acceptance_probability):
                initial_loss=new_loss               #the move is accepted
            else:
                cube.revert_move(move)      #the move is rejected
                
        temperature=temperature*alpha
        print(new_loss)
        if temperature<min_temp:
            return cube
Kube=cube()
for i in range(3):
    Kube.make_random_move()
print('initail loss',Kube.loss())

new_cube=anneal(Kube)
print(new_cube.loss())
        
            
        
        


