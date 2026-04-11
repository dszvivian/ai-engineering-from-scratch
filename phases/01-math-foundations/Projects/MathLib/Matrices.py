import Utils
from Vectors import  Vector

class Matrix:
    
    def __init__(self,components):
        self.components = [Vector(component) for component in components] # I have considered matrix as list of vectors for ease of calculation
        self.rows = len(components)
        self.cols = self.components[0].dims
        
        for row in self.components:
            if row.dims != self.cols:
                raise ValueError("All Rows does Not Have equal number of Columns")
    
    def transpose(self):
        matrixT = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                matrixT[j][i] = self.components[i].components[j] # is this the worst way to write code ? ie: Component of a component is a list
                
        return Matrix(matrixT)
    
    def __matmul__(self,other):
        
        matrix = []
        
        if Utils.is_multipliable(self, other):
            otherT = other.transpose()            
            
            for A in self.components:
                local_row = []
                
                for B in otherT.components:
                    local_row.append(A.dot(B))
                
                matrix.append(local_row)
                
            return Matrix(matrix)
        
        else:
            raise ValueError("incompatible Matrices: Columns of MatixA != Rows of MatrixB")
        
    def __add__(self, other):
        if Utils.are_of_same_dims(self,other):            
            for i in range(self.rows):
                self.components[i] += other.components[i]                
            return self        
        else:
           raise ValueError("Inorder to add Both the matrices should have same dimensions")        
        

    def __sub__(self, other):
        if Utils.are_of_same_dims(self,other):            
            for i in range(self.rows):
                self.components[i] -= other.components[i]                
            return self
        else:
           raise ValueError("Inorder to subtract Both the matrices should have same dimensions")
       
    def __sub__(self, other):
        if Utils.are_of_same_dims(self,other):            
            for i in range(self.rows):
                self.components[i] -= other.components[i]                
            return self
        else:
           raise ValueError("Inorder to subtract Both the matrices should have same dimensions")
    
    
    # also called as element wise operation in math language
    def __mul__(self, other):
        raise NotImplementedError("Mul Not added in Vectors and matrices")
    
    def determinant(self):
        
        if self.rows != self.cols:
            raise ValueError("To find a determinant we have rows = cols ")
        
        det = 0
        
        for i, component in enumerate(self.components[0]):
            dett = component * ((self.components[i+1].components[i+1]) - (self.components[i+1].components[i+1]))
            
    def inverse_2by2():
        pass        

    def __repr__(self):
        return f"Matrix: ({self.components})"
    
if __name__ == "__main__":
    mat1 = Matrix([[1,2,3], [4,5,0]])
    mat2 = Matrix([[7,3], [2,4], [6,3]])
    
    print(mat1 @ mat2)
    
    mat4 = Matrix([[4,5,6], [7,8,9]])
    
    #print(mat1 + mat4)
    #print(mat1 - mat4)
    
    mat5 = Matrix([[1,2], [3,4]])
    mat6 = Matrix([[5,6], [7,8]])
    
    print(mat5 @ mat6)