class Vector:

    def __init__(self, components:list) -> None:
        self.components = components

    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.components, other.components)])

    def dot(self, other) -> float:
        return sum(a*b for a,b in zip(self.components, other.components))
    
    def magnitude(self):
        return (sum(a**2 for a in self.components))**0.5

    def normalize(self):
        return Vector([a/self.magnitude() for a in self.components])

    def cosine_similiarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def __repr__(self) -> str:
        return f"Vector({self.components})"
    

if __name__ == "__main__":
    veca = Vector([1,2,3])
    vecb = Vector([4,5,6])
    vecstd = Vector([1,1])

    print(veca + vecb)
    print(veca - vecb)
    print(veca.dot(vecb))
    print(veca.magnitude())
    print(vecb.magnitude())
    print(vecstd.normalize())
    print(veca.cosine_similiarity(vecb))

