from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """A visible, Artifact or object that user can see interact with. 
    
    The responsibility of Artifact is to keep track of its own appearance, position and velocity in 2d 
    space via parent attributes, and keep track of its message describing what it is.

    Attributes:
        inherited attributes from Actor
        _message (String): The message specific to each artifact.
    """
    def __init__(self):
        """Constructs a new Artifact from parent Actor and initialize message."""
        super().__init__()
        self._message= ""


    def calculate_points(self):
        points = 0
        if(self.get_text() == '*'):
            points = 1
        else:
            points = -1
        
        return points
    