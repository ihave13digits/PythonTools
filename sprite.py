#!/usr/bin/python3

class Sprite:

    def __init__(self, w, h, x, y):
        self.width = w
        self.height = h
        self.position = Vector2(x, y)
        self.matrix = []

        self.flip_x = False
        self.flip_y = False
        self.flipped = False

    def fill(self, r, g, b, a, char):
        for y in range(self.height):
            for x in range(self.width):
                self.matrix.append(Pixel(x, y, r, g, b, a, char))

    def transpose(self, X, Y, f):
        new_matrix = []

###
        if X > 0:
            i = 0
            w = self.width
        elif X < 0:
            i = self.width
            w = 0
        if Y > 0:
            j = 0
            h = self.height
        elif Y < 0:
            j = self.height
            h = 0

        xpos = 0
        ypos = 0

        if f == False:
            for y in range(j, h, Y):
                for x in range(i, w, X):
                    self.matrix[j * self.width + i].position.x = xpos
                    self.matrix[j * self.width + i].position.y = ypos
                    new_matrix.append(self.matrix[j * self.width + i])
                    
                    xpos += X
                    if X > 0:
                        if xpos > w:
                            xpos = i
                    elif X < 0:
                        if xpos < w:
                            xpos = i
                ypos += Y
                if Y > 0:
                    if ypos > h:
                        ypos = j
                elif Y < 0:
                    if ypos < h:
                        ypos = j

        if f == True:
            for x in range(i, w, X):
                for y in range(j, h, Y):
                    self.matrix[j * self.width + i].position.x = xpos
                    self.matrix[j * self.width + i].position.y = ypos
                    new_matrix.append(self.matrix[j * self.width + i])

        return new_matrix
###
'''
        if self.flipped == True and self.flip_x == False and self.flip_y == False:
            i = 0
            j = 0
            for y in range(self.height):
                for x in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i += 1
                    if i >= self.width:
                        i = 0
                j += 1
                if j >= self.height:
                    j = 0
        if self.flipped == True and self.flip_x == True and self.flip_y == False:
            i = self.width-1
            j = 0
            for y in range(self.height):
                for x in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i -= 1
                    if i < 0:
                        i = self.width-1
                j += 1
                if j >= self.height:
                    j = 0
        if self.flipped == True and self.flip_x == False and self.flip_y == True:
            i = 0
            j = self.height-1
            for y in range(self.height):
                for x in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i += 1
                    if i >= self.width:
                        i = 0
                j -= 1
                if j < 0:
                    j = self.height-1
        if self.flipped == True and self.flip_x == True and self.flip_y == True:
            i = self.width-1
            j = self.height-1
            for y in range(self.height):
                for x in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i -= 1
                    if i < 0:
                        i = self.width-1
                j -= 1
                if j < 0:
                    j = self.height-1

        if self.flipped == False and self.flip_x == False and self.flip_y == False:
            i = 0
            j = 0
            for x in range(self.height):
                for y in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i += 1
                    if i >= self.width:
                        i = 0
                j += 1
                if j >= self.height:
                    j = 0
        if self.flipped == False and self.flip_x == True and self.flip_y == False:
            i = self.width-1
            j = 0
            for x in range(self.height):
                for y in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i -= 1
                    if i < 0:
                        i = self.width-1
                j += 1
                if j >= self.height:
                    j = 0
        if self.flipped == False and self.flip_x == False and self.flip_y == True:
            i = 0
            j = self.height-1
            for x in range(self.height):
                for y in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i += 1
                    if i >= self.width:
                        i = 0
                j -= 1
                if j < 0:
                    j = self.height-1
        if self.flipped == False and self.flip_x == True and self.flip_y == True:
            i = self.width-1
            j = self.height-1
            for x in range(self.height):
                for y in range(self.width):
                    self.matrix[j * self.width + i].position.x = x
                    self.matrix[j * self.width + i].position.y = y
                    new_matrix.append(self.matrix[j * self.width + i])
                    i -= 1
                    if i < 0:
                        i = self.width-1
                j -= 1
                if j < 0:
                    j = self.height-1
'''