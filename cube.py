import math 
import numpy as np
from pprint import pprint
import random

class cube:
    def __init__ (self):
      
        self.face = {
            "Top": [[0] * 3 for _ in range(3)],
            "Bottom":[[5] * 3 for _ in range(3)],
            "Left": [[1] * 3 for _ in range(3)],
            "Right": [[3] * 3 for _ in range(3)],
            "Front": [[2] * 3 for _ in range(3)],
            "Back": [[4] * 3 for _ in range(3)]
        }    #this numbering is crucical as the loss depends on the orientation of these numbers so top is always 0 and bottom is always 5 and so on. JUST DONT CHANGE THIS CODE
        

        self.moves={
                0: 'U',     # Rotate the top face clockwise
                1: 'L',     # Rotate the left face clockwise
                2: 'R',     # Rotate the right face clockwise
                3: 'F',     # Rotate the front face clockwise
                4: 'B',     # Rotate the back face clockwise
                5: 'D',     # Rotate the bottom face clockwise
                6: 'D\'',   # Rotate the top face counterclockwise
                7: 'B\'',   # Rotate the left face counterclockwise
                8: 'F\'',   # Rotate the right face counterclockwise
                9: 'R\'',  # Rotate the front face counterclockwise
                10: 'L\'',  # Rotate the back face counterclockwise
                11: 'U\''   # Rotate the bottom face counterclockwise
            } 
       #arranged in such a way that complement gives the opposite move. 
    
  
    
    def display(self):
        """Displays the cube faces using color emojis."""
        color_map = {
            0: "🟧",           
            1: "🟩",  
            2: "⬜",  
            3: "🟦",  
            4: "🟨" ,  
            5: "🟥" 
        }
        
        def print_face(face):
            for row in face:
                print(" ".join(color_map[val] for val in row))
        
        print("\n    Top:")
        print_face(self.face["Top"])
        
        print("\nLeft:      Front:     Right:")
        for l, f, r in zip(self.face["Left"], self.face["Front"], self.face["Right"]):
            print(" ".join(color_map[val] for val in l), "  ", 
                  " ".join(color_map[val] for val in f), "  ", 
                  " ".join(color_map[val] for val in r))
        
        print("\n    Back:")
        print_face(self.face["Back"])
        
        print("\n    Bottom:")
        print_face(self.face["Bottom"])    
            
    def loss(self):
        faces_list=[]
        faces_list = [self.face[face] for face in ["Top", "Left", "Front", "Right", "Back", "Bottom"]]
        faces_list = np.vstack(faces_list)       
        
        state = np.array(faces_list).T.reshape(3,18)  # Use transpose to get the 3x18 shape

        loss=54
        for i in range(3):
            for j in range(18):
                if math.floor(j/3)==state[i][j]:  #if color in correct place then the loss decreases
                    loss-=1
              
        return loss
    

    # def rotate_face_clockwise(self, face_name):
    #     face = self.face[face_name]
    #     face[0][0], face[2][0], face[2][2], face[0][2] = face[2][0], face[2][2], face[0][2], face[0][0]
    #     face[0][1], face[1][0], face[2][1], face[1][2] = face[1][0], face[2][1], face[1][2], face[0][1]

    # def rotate_face_counter_clockwise(self, face_name):
    #     face = self.face[face_name]
    #     face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
    #     face[0][1], face[1][2], face[2][1], face[1][0] = face[1][2], face[2][1], face[1][0], face[0][1]
        

    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        
        # Using a temporary variable to store elements during rotation
        temp = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = temp
        
        temp = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = temp
        
    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        
        # Using a temporary variable to store elements during rotation
        temp = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = temp
        
        temp = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = temp


        
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
    
    def make_random_move(self):
        random_move_idx = random.randint(0, 11)
        self.rotate_cube(self.moves[random_move_idx])
        return random_move_idx    #needed if we need to revert the move

    def revert_move(self,move_idx):
        self.rotate_cube(self.moves[11-move_idx])  #thats how the dict was made

        

