class Category:
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds

    def __repr__(self):
        return f" => {self.name} :: {self.sounds}"

