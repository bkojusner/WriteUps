# CSAW 2018 - Ldab<br>
**CTF Name:** CSAW 2018 </br>
**Challenge Name:** Ldab</br>
**Challenge Description:**</br>
*dab*</br>
[http://web.chal.csaw.io:8080]</br>
**Challenge Category:** Web</br>
**Challenge Points:** 50</br>
**Solve:**</br></br>
When first accessing the page there is a table on display and a search bar to see elements of the table</br></br>
![alt text](https://i.postimg.cc/YSqsJc4v/pic1.png)</br></br>
This indicates that there must be some sort of query language at work to print out the data</br>
so the first test was to see what language was being used. I first typed in “\*” to see</br>
if I would get anything, and later tried some basic SQL injection code to see if it used SQL.</br></br>
![alt text](https://i.postimg.cc/3RkbxgF7/pic2.png)</br></br>
This is a screenshot of the “\*” attempt</br></br>
![alt text](https://i.postimg.cc/k4LY6BTS/pic3.png)</br></br>
This is a screenshot of the SQL injection attempt. This showed SQL is not used. </br>
I found there was a language called LDAP that has the same column names for tables as here.</br>
I then discovered that it is exploitable through some basic structured queries.</br>
After trying to get all rows to print on the table given, I was able to get the flag with</br></br>
```
*)(uid=*))(|(uid=*
```
</br>![alt text](https://i.postimg.cc/C5DPjS2Q/pic4.png)
