import pygame

#main class
class dot:
    
    def __init__(self, x, y, R, G, B, radius, neighbor_coords=[], dif_neighbors=[]):
        self.x = x
        self.y = y
        self.color = (R, G, B)
        self.radius = radius
        self.same_neigbor = neighbor_coords
        self.different_neighbors = dif_neighbors
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    
    def center_snap(self, coords):
        self.x, self.y = coords 
        return [self.x, self.y]

    def point_state(self, grid):
        if self.x and self.y not in grid:
            return True
        else:
            return False
    
    
    def coord_detection(self):

        display_coords=[]
        for i in range(3):
            x = self.x - 10
            y = self.y - 10 + 10*i
            for j in range(3):
                display_coords.append([x, y])
                x += 10

            
        return display_coords

    def limit_detector(self,grid):
        doot_coords = [self.x, self.y]
        if doot_coords not in grid.get_limits_coords():
            return True         
        else:
            return False
    


class bluedot(dot):
    def __init__(self, x, y, R, G, B, radius, neighbor_coords, dif_neighbors):
        super().__init__(x, y, R, G, B, radius, neighbor_coords,dif_neighbors)

class reddot(dot):
    def __init__(self, x, y, R, G, B, radius, neighbor_coords, dif_neighbors):
        super().__init__(x, y, R, G, B, radius, neighbor_coords, dif_neighbors)
