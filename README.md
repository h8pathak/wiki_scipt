
Requirements:
-------------

* Python 3
* BeautifulSoup4
* Requests

Steps to use the program:
-------------------------

1. Run the scipt
2. Enter the wikipedia article (as a url)
3. Wait for the program to fetch the data from the url. (Internet should be connected)
4. Enter your choice of search. ie.
	1 for getting the sentence by providing a citation number (Objective 1)
	2 for getting the citation number of a sentence	(Objective 2)
5. See the result


NOTE: When entering a sentence to get its citation number, enter it completely to get
	the correct results (including the punctuations at the end).
	[see the testcases for examples]

P.S : Testcases included in the file named test_cases.txt




Explanation:
------------

> Used Requests library to fetch the url entered.
> Used BeautifulSoup library to convert the fetched data into readable text.
> For Objective 1 (mentioned above) , used Regular Expression to search the 
  above text for that citation number along with the sentence preceding it. 
	
  In the pattern two capture groups are defined: the first for the sentence, the second
  for the number.

> For Objective 2, searched the processed text for the entered sentence and returned the 
  citation number following it. 


