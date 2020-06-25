# RedPwn 2020 - SMarT-solver
**CTF Name:** RedPwn 2020 

**Challenge Name:** SMarT-solver

**Challenge Description:**

Find the correct flag. :)

NOTE: All letters in the flag are lowercase

**Challenge Category:** rev

**Challenge Points:** 475

**Solve:**
When I first looked at the challenge I realized that it was an SMT challenge just based off the name.

This being said, I knew that z3 would be the perfect tool for this as there are other [writeups](https://jomo.tv/security/mrmcd-ctf-writeup-flag-checker) which solve SMT challenges by simply putting in contraints to z3 and then getting the flag.

The whole idea behind this challenge is to find which sequence of characters  meets the proper criteria for some constriants in order to pass the check done in the program.

When opening Ghidra, and waiting an incredibly long time for main to be decompiled, one can see that there is in fact some absurdly long if statement that checks all the proper constraints to determine is the flag inputed into the program is correct or not.

I copied over the decompiled pseudo code into a txt (main.c in this repository) file for further analysis.

When looking for the first condition in the if statement we see that sVar3 needs to be 0x49 (73 in decimal) since the check fails for any value less than that. Additionally, if we count the amount of variables declared, and the amount of chars allowed for the first array called ourInput, we see that there will be a total of 73 chars. This is great news since now all that is left is to just determine what each of these variables can be by looking at this immensly long if statement. In order to do this we need to make use of a macro ton of python and the z3 api.

I wrote a python script to parse out the program and then format everything for me in the form of a solve script that I later used.

I first copied over just the if statement from the main.c file into a different file called if.txt. From this file I ran a python script I made, called ifparse.py, to create a file called CONDITIONS.txt. What the python script did is get every condition from the if.txt file and then format it to be a variable that is inputted into the z3 API.

Now that I have the constraints, I need the variables so that the constraints could be interpreted by z3.

I copied over all the variables into a var.txt file and then ran the varparse.py script which formatted the variable names accordingly, and also added the constraint of the variables to be between 97 and 124 for the lowercase ascii values (per the note that the flag would be in all lowercase). Additionally, I consulted my friend [Matt](https://github.com/MatthewRinaldi) about the situation and he pointed out that two of the variables would be the curly brackets of the flag so I needed to extend my range by two to account for that. 

Once this was done I simply copied and pasted both VARIABLES and CONDITIONS into one document and then added the four needed lines to interact with the z3 api.
I let the script run and in 30 seconds I was met with an array of numbers for all the variables. All that was left to do was rearrange the array to the proper order that it was presented in (since for some reason z3 messed up the order) and then convert it to ascii and get our flag!

The solve script is called sol.py.
