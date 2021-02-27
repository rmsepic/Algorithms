import Data.List

-- Three functions with the same logic
ifEvenInc x =   if mod x 2 > 0
                    then x
                else
                    x + 1

ifEvenDoub x =  if mod x 2 > 0
                    then x
                else 
                    x * 2

ifEvenSquare x = if mod x 2 > 0
                    then x
                else 
                    x * x

-- Three functions can be rewritten
inc     x = x + 1
double  x = x * 2
square  x = x * x

ifEvenThen f x =    if mod x 2 > 0
                        then x 
                    else 
                        f x 

-- Can setup to call "ifEvenThen" or can setup the function to call "ifEvenThen"
ifEvenCube x = ifEvenThen (\x -> x^3) x

ifEvenNeg x = ifEvenThen (\x -> x * (-1)) x

-- Deals with the tie breaker for comparing last names
compFirstNames fn1 fn2 = if fn1 > fn2
                            then GT
                            else if fn1 < fn2
                                then LT
                                else 
                                    EQ

-- Use sortBy function to work as the reverse to 'sort'
compLastNames n1 n2 =   if ln1 > ln2
                        then GT
                        else if ln1 < ln2
                        then LT
                        else 
                            compFirstNames (fst n1) (fst n2)
    where   ln1 = snd n1
            ln2 = snd n2

sortNames n1 n2 = compare (snd n1) (snd n2)

generateAddress name add = (fst name) ++ " " ++ (snd name) ++ " - " ++ add

-- Last name L or later get special address
sf name =   if (snd name) > "L"
            then generateAddress name "PO Box 1234, San Francisco, CA, 94111"
            else 
                generateAddress name "PO Box 1010, San Francisco, CA, 94111"

ny name = (fst name) ++ " " ++ (snd name) ++ ": " ++ add
    where add = "PO Box 789, New York, NY, 10013"

reno name = generateAddress ("", snd name) "PO Box 456, Reno, NV, 89523"

dc name = generateAddress (fst name, snd name ++ " Esq.") "Washington D.C."

-- Returns a function
getLocFunc loc = case loc of
    "ny"    -> ny
    "sf"    -> sf
    "reno"  -> reno
    "DC"    -> dc
    _       -> (\name -> "Invalid Location")

genAdd name loc = (getLocFunc loc) name




