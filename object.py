import numpy
import pygame

class Object():
    
    
    #        Class definition           ################################################################################

    def __init__(self, vertices = [], edges = [], faces = [], coordinates = (0, 0, 0), orientation = (0, 0, 0)):
        # Vertices:
        self.vertices = []
        for vertex in vertices:
            self.vertices.append(vertex)
        self.vertex_number = len(vertices)
        
        # Edges:
        self.edges = edges
        self.edge_number = len(edges)
        
        # Faces:
        self.faces = faces
        
        # Transform:
        self.coordinates = coordinates
        self.orientation = orientation
        
    #          Core functions           ################################################################################
    
    def RotateVertexTableX(self, turnSpeed = 0.015):
        """
        Summary:
            rotates the shape along the X axis
        Args:
            turnSpeed - float : default turn speed is 0.01
        """
        
        RotateMatrixX = [[               1,                   0,                   0 ],
                         [               0, numpy.cos(turnSpeed), -numpy.sin(turnSpeed)],
                         [               0, numpy.sin(turnSpeed),  numpy.cos(turnSpeed)]]
        
        rotMat = numpy.array(RotateMatrixX)
        for i in range(len(self.vertices)):
            point = numpy.array(self.vertices[i])
            rPoint = numpy.dot(rotMat, point)
            self.vertices[i] = rPoint

    def RotateVertexTableY(self, turnSpeed = 0.015):
        """
        Summary:
            rotates the shape along the Y axis
        Args:
            turnSpeed - float : default turn speed is 0.01
        """
        
        RotateMatrixY = [[ numpy.cos(turnSpeed),               0, numpy.sin(turnSpeed)],
                         [                   0,               1,                   0],
                         [-numpy.sin(turnSpeed),               0, numpy.cos(turnSpeed)]]
        
        rotMat = numpy.array(RotateMatrixY)
        for i in range(len(self.vertices)):
            point = numpy.array(self.vertices[i])
            rPoint = numpy.dot(rotMat, point)
            self.vertices[i] = rPoint

    def RotateVertexTableZ(self, turnSpeed = 0.015):
        """
        Summary:
            rotates the shape along the Z axis
        Args:
            turnSpeed - float : default turn speed is 0.01
        """
        
        RotateMatrixZ = [[ numpy.cos(turnSpeed), -numpy.sin(turnSpeed),               0],
                         [ numpy.sin(turnSpeed),  numpy.cos(turnSpeed),               0],
                         [                   0,                    0,               1]]
        
        rotMat = numpy.array(RotateMatrixZ)
        for i in range(len(self.vertices)):
            point = numpy.array(self.vertices[i])
            rPoint = numpy.dot(rotMat, point)
            self.vertices[i] = rPoint
    
    #     Quality of life functions     ################################################################################

    def add_vertecies(self, vertex_list):
        for vertex in vertex_list:
            self.vertices.append(vertex)

    def add_edge(self, edge_list):
        for edge in edge_list:
            self.edges.append(edge)