"""
Escriba una rotate que gire una matriz bidimensional (una matriz) ya sea en sentido horario o 
antihorario 90 grados y devuelva la matriz rotada.
La función acepta dos parámetros: una matriz y una cadena que especifica la dirección o 
rotación. La dirección será "clockwise"o "counter-clockwise".
Aquí hay un ejemplo de cómo se usará su función:
var matrix = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]];
rotate(matrix, "clockwise"); // Would return [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Para ayudarlo a visualizar la matriz rotada, aquí está formateada como una cuadrícula:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Girado en sentido contrario a las agujas del reloj se vería así:
[[3, 6, 9],
 [2, 5, 8],
 [1, 4, 7]
 """
matrix = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
def rotate(matrix, direction):
    if direction == "clockwise":
        return [list(i) for i in zip(*matrix[::-1])]
    elif direction == "counter-clockwise":
        return [list(i) for i in zip(*matrix)[::-1]]
    else:
        return "Error"

rotate(matrix, "clockwise")

    
if __name__ == "__main__":
    main()
