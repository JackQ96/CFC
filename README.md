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

After this, using pip in the terminal, we can use:

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
