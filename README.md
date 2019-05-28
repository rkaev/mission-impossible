# Mission is impossible, but coding is possible  

 
Once upon a time on one of the vessel. There was mighty crew with big stomachs and chef has accidentally locked refrigerator by the password and gracefully forgot it.
Your goal is to crack within 60 minutes refrigerator doorlock and save crew's stomachs.

## Before we begin

### Requirements:

- Clone project from github (https://github.com/Sender7/mission-impossible)
- Python 3.5 or later 
- PyCharm or any other IDE for Python
- Run command in Terminal or Command line inside project folder "*pip install -r requirements.txt*
"

## Quest 1

The 1st engineer remembers that first password number has been missing somewhere in the calculations. Your goal is to simulate integer arithmetic overflow and retrieve the phrase to execute. In order to do that you have to post request to url  with 

Url: /api/v1/calculator
* In the file by parameter name QUEST_1_URL_CALCULATOR *

Body:
{ a: 1, b: 1 }

After you receive the overflow you have to execute method with specific code phrase in MissionImpossible.py file

## Quest 2

After retrieving successfully from calculations the first digit. The captain has called to memory that the third digit of the password can be found in the history of web. Long time ago in 1989 when the web was only in Universty of CERN and available for few scientists. Scientists has hidden in the content of the page the 3rd digit of the password. 

The scientists were smart and masked it into under the special algorithm:

1. Required to read all characters of the page
2. Count occurence of 3 characters ["s", "e", "a" ]
3. Multiply every character occurence on representation of the character symbol in byte value (e.g. "s" = 115)
4. Sum all results from the previous step
4. Take modulus of 8 from the sum of values from previous step

**Hints:** 
Use ASCII table to find proper characte [http://asciiset.com/]
Url for the first webpage content can be found in python file  QUEST_2_FIRST_WEB_PAGE_URL

## Quest 3 

The crew was so happy that have been able to find the 3 digit of the password and started guessing the password. And entering different combination for the doorlock. The response was slow from the doorlock and it took for every request to respond at least 10 seconds.Thus brute force guessing would take much time. 

The intendant of the ship has started reviewing documents on his table. He found the clue in the document. It came out that in one file with special web encoding has been stored 4th digit. The 4th digit has been stored on a new line after the phrase "I need this key". 

**Hint:** The encoding widely used in the web starts with "base" and there are 2 digits.

## Quest 4

After finding the 4th digit in the position. It came out that crew had no anymore clues to find the last digit. One member of the crew has told that there is an option, which require to try different variants.
 
**Hint:** The doorlock url is https://missionimpossible.appspot.com/api/doorlock?code= and HTTP Request Get method


