import math 
import numpy as np
from pprint import pprint

class cube:
    def __init__ (self):
      
        self.face = {
            "Top": np.array([[0] * 3 for _ in range(3)]),
            "Bottom": np.array([[5] * 3 for _ in range(3)]),
            "Left": np.array([[1] * 3 for _ in range(3)]),
            "Right": np.array([[3] * 3 for _ in range(3)]),
            "Front": np.array([[2] * 3 for _ in range(3)]),
            "Back": np.array([[4] * 3 for _ in range(3)])
        }    #this numbering is crucical as the loss depends on the orientation of these numbers so top is always 0 and bottom is always 5 and so on. JUST DONT CHANGE THIS CODE
        
       
    
    def display (self):
        for row in self.state:
            print(row)
            
            
    def loss(self):
        faces_list=[]
        faces_list = [self.face[face] for face in ["Top", "Left", "Front", "Right", "Back", "Bottom"]]
        faces_list = np.vstack(faces_list)       
        
        state = np.array(faces_list).T.reshape(3,18)  # Use transpose to get the 3x18 shape
        print(state)

        loss=54
        for i in range(3):
            for j in range(18):
                if math.floor(j/3)==state[i][j]:  #if color in correct place then the loss decreases
                    loss-=1
              
        return loss
    

    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        face[0][0], face[2][0], face[2][2], face[0][2] = face[2][0], face[2][2], face[0][2], face[0][0]
        face[0][1], face[1][0], face[2][1], face[1][2] = face[1][0], face[2][1], face[1][2], face[0][1]

    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][2], face[2][1], face[1][0], face[0][1]
        
        
    # Rotate the top face clockwise
    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp
    
    # Rotate the top face counterclockwise
    def rotate_top_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp
    
    # Rotate the bottom face clockwise
    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    # Rotate the bottom face counterclockwise
    def rotate_bottom_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp

    # Rotate the left face clockwise
    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    # Rotate the left face counterclockwise
    def rotate_left_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = temp_col[i]

    # Rotate the right face clockwise
    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    # Rotate the right face counterclockwise
    def rotate_right_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = temp_col[i]

    # Rotate the front face clockwise
    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]

    # Rotate the front face counterclockwise
    def rotate_front_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = temp[i]

    # Rotate the back face clockwise
    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[i]

    # Rotate the back face counterclockwise
    def rotate_back_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = temp[i]
    
    def rotate_cube(self,move):
            """
            Rotate the cube according to the specified move.

            Args:
                cube: An instance of the Cube class.
                move: A string representing the move, such as 'U', 'U\'', 'D', 'D\'', etc.

            Valid moves:
                'U'    - Rotate the top face clockwise
                'U\''  - Rotate the top face counterclockwise
                'D'    - Rotate the bottom face clockwise
                'D\''  - Rotate the bottom face counterclockwise
                'L'    - Rotate the left face clockwise
                'L\''  - Rotate the left face counterclockwise
                'R'    - Rotate the right face clockwise
                'R\''  - Rotate the right face counterclockwise
                'F'    - Rotate the front face clockwise
                'F\''  - Rotate the front face counterclockwise
                'B'    - Rotate the back face clockwise
                'B\''  - Rotate the back face counterclockwise
            """
            
            
            

            
            pprint(self.face)

            if move == 'U':
                cube.rotate_top_clockwise(self)
            elif move == 'U\'':
                cube.rotate_top_counter_clockwise(self)
            elif move == 'D':
                cube.rotate_bottom_clockwise(self)
            elif move == 'D\'':
                cube.rotate_bottom_counter_clockwise(self)
            elif move == 'L':
                cube.rotate_left_clockwise(self)
            elif move == 'L\'':
                cube.rotate_left_counter_clockwise(self)
            elif move == 'R':
                cube.rotate_right_clockwise(self)
            elif move == 'R\'':
                cube.rotate_right_counter_clockwise(self)
            elif move == 'F':
                cube.rotate_front_clockwise(self)
            elif move == 'F\'':
                cube.rotate_front_counter_clockwise(self)
            elif move == 'B':
                cube.rotate_back_clockwise(self)
            elif move == 'B\'':
                cube.rotate_back_counter_clockwise(self)
            else:
                print(f"Invalid move: {move}")
                
            pprint(self.face)

        

