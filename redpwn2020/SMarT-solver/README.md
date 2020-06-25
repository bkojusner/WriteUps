# RedPwn 2020 - SMarT-solver<br>
**CTF Name:** rRedPwn 2020 </br>
**Challenge Name:** SMarT-solver </br>
**Challenge Description:**</br>
Find the correct flag. :)</br>
NOTE: All letters in the flag are lowercase</br>
**Challenge Category:** rev</br>
**Challenge Points:** 475</br>
**Solve:**</br></br>
When I first looked at the challenge I realized that it was an SMT challenge just based off the name.</br>
This being said, I knew that z3 would be the perfect tool for this as there are other writeups which solve SMT challenges by simply putting in contraints to z3 and then getting the flag.</br>
The whole idea behind this challenge is to find which sequence of characters  meets the proper criteria for some constriants in order to pass the check done in the program.</br>
When opening Ghidra, and waiting an incredibly long time for main to be decompiled, one can see that there is in fact some absurdly long if statement that checks all the proper constraints to determine is the flag inputed into the program is correct or not.</br>
I copied over the decompiled pseudo code into a txt (main.c in this repository) file for further analysis.</br>
When looking for the first condition in the if statement we see that sVar3 needs to be greater(or equal to?) than 0x49 since the check failed. If we cound the amount of variables declared, and the amount of chars allowed for the first array called ourInput, we see that there will be a total of 73 chars. This is great news since now all that is left is to just determine what each of these variables can be. In order to do this however we need to make use of the z3 api in python and write a script that could do this.</br>
The only way I knew how to at the time was to just write a python script to parse out the program and then format everything for me in the form of a solve script that I later used.</br>
I first copied over just the if statement from the main.c file into a different file called if.txt. From this file I ran a python script I made called ifparse.py to create a file called CONDITIONS.txt. What this did was just get every condition from the if.txt file and then format them to fit the use for the z3 api and write it all into CONDITIONS.txt.</br>
Now that I have the constraints for z3 to be able to take charge of the action, I still needed to first create the variables so that the constraints could be interpreted, and then had to finish off the solve script so that it can interact with z3 and tell me what the flag is.</br>
I copied over all the variables into a var.txt file and then ran the varparse.py script which formatted the variable names accordingly, and also added the constraint of the variables to be between 97 and 124 for the lowercase ascii values. Additionally, I consulted my friend Matt about the situation and he pointed out that two of the variables would be the brackets of the flag so I needed to extend my range by two to account for that.</br> 
Once this was done I simply copied and pasted both VARIABLES and CONDITIONS into one document and then added the four needed lines to interact with the z3 api.</br>
I let the script run and in 30 seconds I was met with an array of numbers for all the variables. All that was left to do was rearrange the array to the proper alignment in variables (since for some reason z3 messed up the order) and then convert it to ascii and we have our flag!</br>
The solve script is called sol.py



[/] ![alt text](https://i.postimg.cc/YSqsJc4v/pic1.png)</br></br>