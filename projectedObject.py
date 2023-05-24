import pygame

class ProjectedObject():


    #        Class definition           ################################################################################

    def __init__(self, vertices = [], vertices_3D = [], edges = [], faces = []):
        # Vertices:
        self.vertices = vertices
        self.vertices_3D = vertices_3D
        self.vertex_number = len(vertices)
        self.color = [0]*6

        # Edges:
        self.edges = edges
        self.edge_number = len(edges)

        # Faces:
        self.faces = faces

    #        Public functions           ################################################################################

    def get_furthest_coor_from_face(self, face):
        min = 0
        for i in range(4):
            if self.vertices_3D[face[min]][2] > self.vertices_3D[face[i]][2]:
                min = i
        return min
    
    
    def update_faces_order(self):
        distances = []
        for face in self.faces:
            distances.append(self.get_furthest_coor_from_face(face))
        
        pairs = [(distances[i], self.faces[i]) for i in range(len(distances))]
        sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
        self.faces = [pair[1] for pair in sorted_pairs]
        
        

    #     Quality of life functions     ################################################################################

    def add_vertecies(self, vertex_list):
        for vertex in vertex_list:
            self.vertices.append(vertex)

    def add_edges(self, edge_list):
        for edge in edge_list:
            self.edges.append(edge)