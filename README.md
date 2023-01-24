# CFC
Please find attached my submisson for the CFC Insight Technical Challenge. Within this challenge I have created an application that:
```
1) Automatically scrapes a given webpage
2) Creates a JSON file including all externally loaded resources
3) Creates another JSON file including a word count for all visible text on the websites "Privacy policy" page.
 ```
 
## Dependencies

Firslty please make sure you have python downloaded and up to date (refer to https://www.python.org/downloads/ for further info). 

Then clone this repository by clicking 'Code' at the top of the repo and then clicking 'Download ZIP'. After this you want to place the zip file in a folder of your choice and unzip the contents. After this has been completed you want to open your terminal within the specific folder, an easy way to do this is to right click the folder and click "New terminal at folder (on Mac)".

After this, using pip, we can execute:

```bash
pip install -r requirements.txt
```

to download all necessary requirements.

## Running the application

To run the application, simply enter in the terminal:
```
python3 app.py
```
and the application will do the rest of the work for you and output the two json files within the folder. For ease of viewing, I have already downloaded the 2 JSON files, but feel free to delete them and run the application again to see how the app functions.

## How would I improve my code if i had more time?



 1) the Main thing would be error handling and test cases: Implementing Try-Except blocks to catch errors, and even check to ensure I get a 200 response before going ahead with the parsed data

 2) Some websites load data dynamically and I believe this would cause issues with scraping. I would need an external library to wait for the page to be fully loaded before any scraping occurs

 3) Find ways to handle sites that have Captchas before accessing. This is a more difficult problem to deal with but can be done making use of machine learning libraries

 4) With regards to international languages: Ensure the app can handle different characters and still pull the required data to the json files. I could also use langauge detection libraries like "langdetect" to find out which language we are dealing with and then use a language specific library to deal with that scenario to reduce the likelihood of errors
