https://review.udacity.com/#!/rubrics/2709/view


1. finish app - verify stuff/check dimensions
2. handle errors better
3. check rubric
4. check strnage chars in txt


A README file is included in the project root and includes:

an overview of the project.
instructions for setting up and running the program.
a brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples of how to use the module.


pip freeze > requirements.txt 

If the program encounters a common error case (e.g. attempting to load an incompatible filetype), it throws an exception.

Define custom exception classes for different types of exceptions—for things like *Invalid File, Invalid Text Input (e.g. too long)

memEngine -> MemeGenerator rename

Loading of a file from disk
Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
Add a caption to an image (string input) with a body and author to a random location on the image.


make_meme(self, img_path, text, author, width=500) -> str #generated image path



make ImageCaptioner class

app.py uses the Quote Engine module and Meme Generator modules to generate a random captioned image.