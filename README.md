# Mission is impossible, but coding is possible  

 
Once upon a time on one of the vessel. There was mighty crew with big stomachs and chef has accidentally locked refrigerator by the password and gracefully forgot it.
Your goal is to crack within 45 minutes refrigerator doorlock and save crew's stomachs.
 
## Quest 1

The 1st engineer remembers that first password number has been missing somewhere in the calculations. Your goal is to simulate integer arithmetic overflow and retrieve the phrase to execute. In order to do that you have to post request to url  with 

Url: /api/v1/calculator

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

*Hint use ASCII table to find proper characte [http://asciiset.com/]

## Quest 3 

The crew was so happy that have been able to find the 3 digit of the password and started guessing the password. And entering different combination for the doorlock. The response was slow from the doorlock and it took for every request to respond at least 10 seconds.Thus it would take much time to guess. 

The intendant of the ship has started reviewing documents on his table to find the clue in the document. It has come out that in one file with special web encoding. Has been stored file, which should contain after the message "I need this key". After this phrase on next line is hidden 4th digit. 

The encoding widely used in the web starts with "base" and there are 2 digits.

## Quest 4

After finding the 4th digit in the position. It has came out that crew got no anymore clues to find the 2nd digit. One member of the crew has told that there is an option, but requested you to guess what option it is.

The doorlock url api/v1/doorlock?code= Enter password

