from shortest_path_binary_matrix import shortestPathBinaryMatrix

if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,1]]
    n = shortestPathBinaryMatrix(grid)
    print("answer: ", n)