from display import *
from draw import *
from matrix import *


######################################################
#Matrix math test
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
IDENT = new_matrix()
ident(IDENT)
matrix_mult(A,B)
print(A)
print(B)
matrix_mult(B,A)
print(A)
print(B)
matrix_mult(IDENT,A)
print(A)
#######################################################
screen = new_screen()
color1 = [ 255, 75, 20]
color2 = [ 102, 204, 0]
color3 = [ 102, 178, 255]
color4 = [ 235, 176, 40]

matrix1 = new_matrix(4, 4);
matrix2 = new_matrix(4, 4);
matrix3 = new_matrix(4, 4);
matrix4 = new_matrix(4, 4);

#left-top
#top
add_edge(matrix1, 25, 450, 0, 75, 455, 0);
#left
add_edge(matrix1, 25, 450, 0, 25, 400, 0);
#right
add_edge(matrix1, 75, 455, 0, 75, 400, 0);
#bottom
add_edge(matrix1, 25, 400, 0, 75, 400, 0);


#right-top
add_edge(matrix2, 78, 455, 0, 130, 460, 0);
add_edge(matrix2, 78, 455, 0, 78, 400, 0);
add_edge(matrix2, 130,460, 0, 130, 400, 0);
add_edge(matrix2, 78, 400, 0, 130, 400, 0);


#left-bottom
add_edge(matrix3, 25, 397, 0, 75, 397, 0);
add_edge(matrix3, 25, 397, 0, 25, 347, 0);
add_edge(matrix3, 75, 397, 0, 75, 340, 0);
add_edge(matrix3, 25, 347, 0, 75, 340, 0);


#right-bottom
add_edge(matrix4, 78, 397, 0, 130, 397, 0);
add_edge(matrix4, 78, 397, 0, 78, 338, 0);
add_edge(matrix4, 78, 338, 0, 130, 332, 0);
add_edge(matrix4, 130, 397, 0, 130, 332, 0);

draw_lines( matrix1, screen, color1 )
draw_lines( matrix2, screen, color2 )
draw_lines( matrix3, screen, color3 )
draw_lines( matrix4, screen, color4 )
save_extension(screen, 'img.png')
display(screen)
