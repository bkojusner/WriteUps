I spent so much time thinking it was srand but that was not the case.

The man page for rand() says "If srand is not called, rand acts as if srand(1) has been called." This basically means that the value will always be constant.

You can get the value in a gdb session, just break main and keep stepping until the variable is assigned,
get the value and then it's just solve for 
`0x6b8b4567 ^ input = 0xacedface`

So doing a little bit of math we know that the input is `0xc766bfa9`

The scanf takes in a decimal number to I converted hex to decimal and then just sent that number thru and we get the flag.