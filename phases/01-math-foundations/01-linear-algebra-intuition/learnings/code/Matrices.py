from Vectors import  Vector

class Matrix:
    
    def __init__(self,component):
        self.component = component
        self.rows = len(component)
        self.cols = len(self.component[0])
        
        # TODO: add a validation check to check whether all the rows have same columns length, else raise value error.
        
    def is_multipliable(self, other):
        return self.cols == other.rows
    
    # converting matrix to list of vectors, so the calculation will be easy
    def convert_matrix_to_list_of_vectors(self) -> list[Vector]:
        return [Vector(x) for x in self.component]
    
    def transpose(self):
        matrixT = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                matrixT[j][i] = self.component[i][j]
                
        return Matrix(matrixT)
    
    def __matmul__(self,other) -> Matrix:
        
        matrix = []
        
        if self.is_multipliable(other):
            
            rowVectors: list[Vector] = self.convert_matrix_to_list_of_vectors()
            columnVectors: list[Vector] = other.transpose().convert_matrix_to_list_of_vectors()
            
            
            for A in rowVectors:
                local_row = []
                
                for B in columnVectors:
                    local_row.append(A.dot(B))
                
                matrix.append(local_row)
                
            return Matrix(matrix)
        
        else:
            raise ValueError("incompatible Matrices: Columns of MatixA != Rows of MatrixB")
        

    def __sub__(self, other):
        pass
    
    def __add__(self, other):
        pass
    
    def determinant():
        pass
    
    
    

    def __repr__(self):
        return f"Matrix: ({self.component})"
    
if __name__ == "__main__":
    mat1 = Matrix([[1,2,3], [4,5,0]])
    mat2 = Matrix([[7,3], [2,4], [6,3]])
    
    print(mat1 @ mat2)
    

    
    