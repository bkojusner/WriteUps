<strong>CTF Name:</strong> CSAW 2018 </br>
<strong>Challenge Name:</strong> Ldab</br>
<strong>Challenge Description:</strong></br>
dab</br>
http://web.chal.csaw.io:8080</br>
<strong>Challenge Category:</strong> Web</br>
<strong>Challenge Points:</strong> 50</br>
<strong>Solve:</strong></br>
When first accessing the page there is a table on display and a search bar to see elements of the table.</br>
![alt text](https://i.postimg.cc/YSqsJc4v/pic1.png)</br>
This already indicates that there must be some sort of query language at work to print out the</br>
data the user would want to see. The first test was to see what language was being used so I first typed in �*� to</br>
see if I would get anything, and later tried some basic SQL injection code to see if it used SQL.</br>
![alt text](https://i.postimg.cc/3RkbxgF7/pic2.png)</br> 
This is a screenshot of the �*� attempt
![alt text](https://i.postimg.cc/k4LY6BTS/pic3.png)</br>
This is a screenshot of the SQL injection attempt. It is evident the language used is not SQL. </br>
I found that there was a language called LDAP that has OU, CN, SN, and UID as basic column names for tables.</br>
This led me to discover that it is exploitable through some basic structured queries.</br>
After some experimentation on trying to get all rows to print on the table given, I was able to get the flag with</br> 
'''*)(uid=*))(|(uid=*'''
![alt text](https://i.postimg.cc/C5DPjS2Q/pic4.png)</br>