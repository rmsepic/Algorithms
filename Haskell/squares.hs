-- Using where
sumSquareOrSquareSum x y =  if sumSquare < squareSum
                                then squareSum
                            else
                                sumSquare 

    where   sumSquare = x^2 + y^2
            squareSum = (x + y)^2

-- Using let
sumSquareSquareSum x y =    let sumSquare = (x^2 + y^2)
                                squareSum = ((x + y)^2)
                            in 
                                if sumSquare < squareSum
                                    then squareSum
                                else
                                    sumSquare   

-- Another way of writing the same function above
body sumSq sqSum =  if sumSq > sqSum
                                then sumSq 
                            else sqSum

sumSqOrSqSum x y = body (x^2 + y^2) ((x+y)^2)

-- Another version using Lambda
sumSquareLambda x y = (\sumSq sqSum -> 
                            if sumSq > sqSum 
                                then sumSq 
                            else 
                                sqSum) (x^2 + y^2) ((x + y)^2)

-- Double the number twice using Lambda
doubleDouble x = (\x -> x * 2) ((\x -> x * 2) x)

-- Variables can be overwritten in Haskell
-- Proof
overwriteVar x =    let x = 2
                    in 
                        let x = 'a'
                        in
                            let x = [1,2]
                            in
                                x

overwriteLambda x = (\x -> x) ((\x -> x) ((\x -> x) [1,2]))

owLam x = (\x -> (\x -> (\x -> x) 2) 'a' ) [1,2]

itr x = (\x -> x + 1) x



