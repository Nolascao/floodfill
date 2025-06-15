from collections import deque

def flood_fill(grid, x, y, color):
 """
 Preenche a região conectada à célula inicial (x, y) com a cor fornecida.
 Utiliza uma abordagem de BFS para explorar as células conectadas.
 """
 n = len(grid)
 m = len(grid[0])

 # Verifica se a célula inicial é válida para preenchimento
 if not (0 <= x < n and 0 <= y < m):
     raise ValueError("As coordenadas iniciais estão fora dos limites do grid.")
 if grid[x][y] != 0:
     return

 # Direções ortogonais: cima, baixo, esquerda, direita
 directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

 # Fila para BFS
 queue = deque([(x, y)])
 grid[x][y] = color  # Preenche a célula inicial com a nova cor

 while queue:
     cx, cy = queue.popleft()

     for dx, dy in directions:
         nx, ny = cx + dx, cy + dy

         # Verifica se a célula vizinha está dentro dos limites e é navegável (valor 0)
         if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
             grid[nx][ny] = color  # Preenche a célula vizinha
             queue.append((nx, ny))  # Adiciona a célula vizinha à fila

def find_next_start(grid):
 """
 Encontra a próxima célula navegável (com valor 0) no grid.
 Retorna as coordenadas da célula ou None se não houver mais células navegáveis.
 """
 for i in range(len(grid)):
     for j in range(len(grid[0])):
         if grid[i][j] == 0:
             return i, j
 return None