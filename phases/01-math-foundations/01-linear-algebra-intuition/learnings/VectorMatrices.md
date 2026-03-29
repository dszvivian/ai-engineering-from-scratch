Vectors are used to store single part information
Matrices are used to store group of information

## Dot Products.

a.b = a * b * costheta,
Here we are finding, projection of a into b or 
direction a wrt to b

if a.b > 0, then same direction,  
	= 0, Unrelated
	< 0, Disimiliar




## Linear Independence:

Only if two vectors are Independent, they can span a 3D space
Or else they will cancel out each other.

To check if two vectors are Independence is:  
Suppose: a= [1,0] b=[0,1]  
Here, the only possible way c1.a + c2.b = [0,0] is 
if both c1, c2 = 0,0. So in this case both are linearly independent.  

Suppose, a = [1,1] b=[2,2] here, c1.a + c2.b = [0,0]  
this can be achieved using c1=2, c2=-1,
So these will cancel out in some point in the same line  
So these are linearly dependent.  



## Basis:

Minimal set of linearly Independent Vectors, using which we can span the entire nd space.  

## Rank:  

Dimensions of a Matrix that it operates in. Or Numbers of Linearly independent vectors present in a matrix.  

Number of linearly independent columns = No of linearly independent ros.  



## Projections:


Projection is nothing but shodow of vector a onto vector b. It giomponent of a on direction of b.  

proj_b(a) = (a dot b / b dot b) * b  


