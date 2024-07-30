from collections import defaultdict

# get dicitonary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

# create matrix from entered string
def create_matrix(input_string, rows, cols):
    if len(input_string) != rows * cols:
        raise ValueError("string len is not valid")
    matrix = []
    index = 0
    for i in range(rows):
        row = list(input_string[index:index + cols])
        matrix.append(row)
        index += cols
    return matrix

# Build the graph
def build_graph(matrix):
    rows, cols = len(matrix), len(matrix[0])
    graph = defaultdict(list)

    for i in range(rows):
        for j in range(cols):
            if i - 1 >= 0 and j - 1 >= 0:  # Top-left
                graph[(i, j)].append(((i - 1, j - 1), matrix[i - 1][j - 1]))
            if i - 1 >= 0:  # Top
                graph[(i, j)].append(((i - 1, j), matrix[i - 1][j]))
            if i - 1 >= 0 and j + 1 < cols:  # Top-right
                graph[(i, j)].append(((i - 1, j + 1), matrix[i - 1][j + 1]))
            if j - 1 >= 0:  # Left
                graph[(i, j)].append(((i, j - 1), matrix[i][j - 1]))
            if j + 1 < cols:  # Right
                graph[(i, j)].append(((i, j + 1), matrix[i][j + 1]))
            if i + 1 < rows and j - 1 >= 0:  # Bottom-left
                graph[(i + 1, j - 1)].append(((i + 1, j - 1), matrix[i + 1][j - 1]))
            if i + 1 < rows:  # Bottom
                graph[(i + 1, j)].append(((i + 1, j), matrix[i + 1][j]))
            if i + 1 < rows and j + 1 < cols:  # Bottom-right
                graph[(i + 1, j + 1)].append(((i + 1, j + 1), matrix[i + 1][j + 1]))
    
    return graph


def dfs(startNodePos, pathToNode, visited, graph, dictionary, matrix):
    i, j = startNodePos
    letter = matrix[i][j]

    if visited[i][j]:
        return
    visited[i][j] = True

    pathToNode.append(letter)

    combined = ''.join(pathToNode).lower()
    if combined in dictionary and len(combined) > 4:
        print(f"Found a word: {combined}")

    neighbors = graph[(i, j)]
    for nextPos, nextLetter in neighbors:
        if not visited[nextPos[0]][nextPos[1]]:
            dfs(nextPos, pathToNode, visited, graph, dictionary, matrix)
    
    pathToNode.pop()
    visited[i][j] = False

def main():
    dictionary = load_dictionary('dictionary.txt')

    rows = 5
    cols = 5
    input_string = input("Enter matrix: ").strip().lower()
    matrix = create_matrix(input_string, rows, cols)

    graph = build_graph(matrix)
    
    for i in range(rows):
        for j in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            dfs((i, j), [], visited, graph, dictionary, matrix)

main()
