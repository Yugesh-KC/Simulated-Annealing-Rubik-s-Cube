class Cube:
    def __init__(self):
        self.face = {
            "Top": [["🟧"] * 3 for _ in range(3)],
            "Bottom": [["🟥"] * 3 for _ in range(3)],
            "Left": [["🟩"] * 3 for _ in range(3)],
            "Right": [["🟦"] * 3 for _ in range(3)],
            "Front": [["⬜"] * 3 for _ in range(3)],
            "Back": [["🟨"] * 3 for _ in range(3)],
        }
    
    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        # Rotate corners
        face[0][0], face[2][0], face[2][2], face[0][2] = face[2][0], face[2][2], face[0][2], face[0][0]
        # Rotate edges
        face[0][1], face[1][0], face[2][1], face[1][2] = face[1][0], face[2][1], face[1][2], face[0][1]

    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        # Rotate corners in reverse
        face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
        # Rotate edges in reverse
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][2], face[2][1], face[1][0], face[0][1]

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        # Save a copy of the top row from the front face
        temp = self.face["Front"][0][:]
        # Cycle the top rows of adjacent faces
        # Note: The back face row must be reversed because its orientation is opposite
        self.face["Front"][0] = self.face["Right"][0][:]
        self.face["Right"][0] = self.face["Back"][0][::-1]
        self.face["Back"][0] = self.face["Left"][0][::-1]
        self.face["Left"][0] = temp

    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        # (Optional fix: similar reversal might be needed for bottom rotations)
        temp = self.face["Front"][2][:]
        self.face["Front"][2] = self.face["Left"][2][:]
        self.face["Left"][2] = self.face["Back"][2][::-1]
        self.face["Back"][2] = self.face["Right"][2][::-1]
        self.face["Right"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]

    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[i]

    def print_cube(self):
        for face_name, face in self.face.items():
            print(face_name)
            for row in face:
                print(" ".join(row))
            print()

if __name__ == "__main__":
    cube = Cube()
    print("Initial cube:")
    cube.print_cube()
    cube.rotate_top_clockwise()
    print("After rotating top face clockwise:")
    cube.print_cube()
