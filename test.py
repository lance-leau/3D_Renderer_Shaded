from object import Object
from camera import Camera
import sys,  pygame

# Create display window
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("3D Wire Frame Renderer")

# Launch the projection
def launchWindow():
    # Initialize objects and camera:
    vertices = [(0, 0, 0), (10, 0, 0), (0, 10, 0), (10, 10, 0), (0, 0, 10), (10, 0, 10), (0, 10, 10), (10, 10, 10)]
    edges = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    faces = [(0, 1, 3, 2), (0, 1, 5, 4), (2, 3, 7, 6), (0, 2, 6, 4), (1, 3, 7, 5), (4, 5, 7, 6)]
    obj1 = Object(vertices, edges, faces, (0, 0, 50))
    obj2 = Object(vertices, edges, faces, (0, 11, 50))
    obj3 = Object(vertices, edges, faces, (0, -11, 50))
    obj4 = Object(vertices, edges, faces, (11, 0, 50))
    obj5 = Object(vertices, edges, faces, (11, 11, 50))
    obj6 = Object(vertices, edges, faces, (11, -11, 50))
    obj7 = Object(vertices, edges, faces, (-11, 0, 50))
    obj8 = Object(vertices, edges, faces, (-11, 11, 50))
    obj9 = Object(vertices, edges, faces, (-11, -11, 50))
    cam = Camera((5, 5, -30), 100, [obj1], (screen.get_width()/2, screen.get_height()/2))
    
    # obj1.RotateVertexTableX(5.9)
    
    # Main loop
    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                sys.exit
        
        # Render the shape
        screen.fill((0, 0, 0))
        cam.refresh()
        cam.render_scene(screen)
        obj1.RotateVertexTableX(0.002)

        # Update the canvas
        pygame.display.update()
        pygame.time.Clock().tick(100)
    
    pygame.quit

launchWindow()