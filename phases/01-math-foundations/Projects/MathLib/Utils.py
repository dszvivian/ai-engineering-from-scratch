def is_multipliable(mat1, mat2) -> bool:
    return mat1.cols == mat2.rows

def are_of_same_dims(mat1, mat2) -> bool:
    return mat1.rows == mat2.rows and mat1.cols == mat2.cols 
