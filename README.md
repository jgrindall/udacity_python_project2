#MemeGenerator



- To install dependencies:
            - source venv/Scrips/activate
            - pip install -r requirements.txt


- To run on the command line:
            - python3 src/meme.py
            - TODO
            - TODO
            
            
- To run some unit tests (currently just QuoteModel)
            - python3 src/models/QuoteModel.py



- To run the web app:
            - export FLASK_APP=src/app.py
            - flask run
            

##Code

a brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples of how to use the module.



https://review.udacity.com/#!/rubrics/2709/view


2. handle errors better
3. check rubric



an overview of the project.
instructions for setting up and running the program.


pip freeze > requirements.txt 

If the program encounters a common error case (e.g. attempting to load an incompatible filetype), it throws an exception.

Define custom exception classes for different types of exceptions—for things like *Invalid File, Invalid Text Input (e.g. too long)

memEngine -> MemeGenerator rename


app.py uses the Quote Engine module and Meme Generator modules to generate a random captioned image.