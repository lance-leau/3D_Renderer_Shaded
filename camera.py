import pygame
from object import Object
from projectedObject import ProjectedObject

class Camera():
    
    #        Class definition           ################################################################################
    def __init__(self, coordinates = (0, 0, 0), focal_len = 10, object_list = [], offset = (0, 0)):
        self.coordinates = coordinates
        self.focal_len = focal_len
        self.redered_objs = object_list
        self.offset = offset
        self.projected_objects = self.project_objects()

    def project_point(self, x, y, z, offset = (0, 0)):
        # if (self.focal_len + z == 0):
        #     return None
        Xprojected = ((self.focal_len * x) / (self.focal_len + z)) + offset[0]
        Yprojected = ((self.focal_len * y) / (self.focal_len + z)) + offset[1]
        return (Xprojected, Yprojected)

    def project_object(self, object):
        projected_vertices = []
        for vertex in object.vertices:
            x = self.coordinates[0] - (vertex[0] + object.coordinates[0])
            y = self.coordinates[1] - (vertex[1] + object.coordinates[1])
            z = self.coordinates[2] - (vertex[2] + object.coordinates[2])
            projected_vertices.append(self.project_point(x, y, z, self.offset))
        
        projected_object = ProjectedObject(projected_vertices, object.vertices, object.edges, object.faces)
        projected_object.update_faces_order()
        return projected_object
 
    def project_objects(self):
        ret = []
        for object in self.redered_objs:
            ret.append(self.project_object(object))
        return ret
    
    #        Public functions           ################################################################################
    def refresh(self):
        self.projected_objects = self.project_objects()
    
    def render_scene(self, window):
        for object in self.projected_objects:
            color = 0
            for i in range(6):
                p1 = object.vertices[object.faces[5-i][0]]
                p2 = object.vertices[object.faces[5-i][1]]
                p3 = object.vertices[object.faces[5-i][2]]
                p4 = object.vertices[object.faces[5-i][3]]
                pygame.draw.polygon(window, (42*i,42*i,42*i), [p1, p2, p3, p4])
                color += 42
            for edge in object.edges:
                pygame.draw.line(window, (255, 255, 255), object.vertices[edge[0]], object.vertices[edge[1]], 1)