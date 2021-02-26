calcChange price given = if change > 0
                            then change
                        else
                            0 

    where change = given - price

inc x = x + 1

double x = x * 2 

square x = x * x

evenOdd x = if isEven > 0
                then 3*x - 1 
            else 
                x - 2

    where isEven = mod x 2