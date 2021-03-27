enum Status {
    case queen
    case empty
}

class Solution { 
    var board:[[Status]] = []
    var dimensions = 0
    
    // Checks if the Queen can be placed at [row, col]
    // Queens are being places from the left hand towards the right side
    // Only need to check diagonals on the upper and lower left
    // because no queens will be on the right side
    func can_be_placed(_ row: Int, _ col: Int) -> Bool {
        // Check the right side of the row
        for i in 0 ..< self.dimensions {
            if board[row][i] == Status.queen {
                return false
            }
        }
        
        // Check the lower left diagonal
        var r:Int = row
        var c:Int = col
        while (r >= 0 && c >= 0) {
            if board[r][c] == Status.queen {
                return false
            }
            
            r -= 1
            c -= 1
        }
        
        // Check the upper left diagonal
        r = row // Reinitialize the loop
        c = col
        while (r < self.dimensions && c >= 0) {
            if board[r][c] == Status.queen {
                
                return false
            }
            
            r += 1
            c -= 1
        }
        
        return true
    }
    
    
    func dfs(_ col: Int, _ current_count: Int) -> Int {
        var count:Int = current_count
        
        // Loop through the next col searching for places the queen can go
        for row in 0 ..< self.dimensions {
            // If the queen can go to [row, col]
            // Try the combos for col + 1
            if can_be_placed(row, col) {
                if (col + 1 == self.dimensions) {
                    count += 1
                } else {
                    board[row][col] = Status.queen
                    count = dfs(col + 1, count)
                }
                
                board[row][col] = Status.empty
            }
        }
        
        return count
    }
    
    func totalNQueens(_ n: Int) -> Int { 
        if (n == 1) {
            return 1
        } else if (n < 4) {
            return 0
        }
        
        board = Array(repeating: Array(repeating: Status.empty, count: n), count: n)
        var count: Int = 0
        self.dimensions = n

        for row in 0 ..< n {
            board[row][0] = Status.queen
            count = dfs(1, count)
            
            // Remove the 'Q' in board so it can replaced
            board[row][0] = Status.empty
        }
        
        return count
    }
}