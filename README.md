#MemeGenerator


##Overview:

- https://review.udacity.com/#!/rubrics/2709/view
- A "meme generator" written in Python 3.
- A multimedia application to dynamically generate memes, including an image with an overlaid quote.
- Quotes are loaded from a variety of filetypes (txt, csv...).
 -Images are loaded from a folder of ready-made images
- Memes can be generated on the command line (passing an image path, quote body and quote author - all optional)
- Or using a Flask web app.



##Running the project:

- To install dependencies:

            - source venv/Scripts/activate
            - pip install -r requirements.txt


- To run on the command line:

            - python3 src/meme.py
            - python3 src/meme.py --body='This is the body' --author='Someone'
            - python3 src/meme.py --path='***TODO***' --body='This is the body' --author='Someone'
            
            
- To run some unit tests (currently just QuoteModel)
            - python3 src/models/QuoteModel.py


- Lint:
            - pycodestyle src

- To run the web app:
            - export FLASK_APP=src/app.py
            - flask run
            

##Code:

A brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples 

of how to use the module.


- src/loaders

- src/meme_engine

- src/models

- src/quote_engine

- src/utils

- src/app.py

app.py uses the Quote Engine module and Meme Generator modules to generate a random captioned image.


- src/meme.py





1. handle errors better

2. check rubric

If the program encounters a common error case (e.g. attempting to load an incompatible filetype),

it throws an exception.

Define custom exception classes for different types of exceptions—for things like *Invalid File, Invalid Text Input (e.g. too long)

