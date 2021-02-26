--This program drafts an example email

greeting recipient = "Hello " ++ recipient ++ ",\n\n"

signed author = "Very Respectfully,\n\n\n" ++ author

generateEmail recipient author =    greeting recipient ++ 
                                    "Awesome! Glad to hear it." ++
                                    signed author

main = do
    print "Hello world"
    print "My name is Ryland"

    print "To: "
    recipient <- getLine

    print "Sender: "
    sender <- getLine

    --Basic way to print input
    print ("Hey " ++ recipient ++ ",\n\n" ++
        "Awesome! Glad to here from you.\n\n" ++
        "Very Respectfully,\n\n\n" ++
        sender)

    --Using a function
    --Cleaner method
    print(generateEmail recipient sender)
