from cube import cube
import math
import random
import copy

def anneal (cube:cube,initial_temp = 10000,alpha = 0.995,min_temp=1e-3):  #alpha means by how much to decrease the temp
    temperature=initial_temp
    initial_loss = cube.loss()
    if initial_loss==0:
        return cube
    best_loss=initial_loss
    best_cube=None
    
    while(1):
            for i in range(100*initial_loss):
                move=cube.make_random_move()     #saving move incase we want to return to previous state
                new_loss=cube.loss()
                if new_loss==0:
                    return cube
                delta = new_loss-initial_loss
                acceptance_probability = math.exp(-delta*1e3/temperature)    #when new_loss is less prob always greater than 1. 1e3 because i saw it on a github repo 
                random_acceptance = random.uniform(0,1)
                if (random_acceptance<acceptance_probability):
                    initial_loss=new_loss               #the move is accepted
                else:
                    cube.revert_move(move)      #the move is rejected
                    
                # print(new_loss,temperature)
                if temperature<min_temp:
                    if best_cube:
                        return best_cube
                    return cube
                if new_loss<best_loss:
                    print("changed best ")
                    print(new_loss)
                    best_loss=new_loss
                    best_cube=copy.deepcopy(cube)
                    
            print('te',temperature)
            temperature=temperature*alpha
Kube=cube()
for i in range(3):
    Kube.make_random_move()
    x=Kube.loss()

old=copy.deepcopy(Kube)
new_cube=anneal(Kube)


old.display()
print("after")
new_cube.display()
print(old.loss(),new_cube.loss())        
            
        
        


