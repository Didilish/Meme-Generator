Meme Generator 

This project is a simple meme generator (a multimedia application to dynamically generate memes, including an image with an overlaid quote) written in python. This project was created as part of Udacity's Python Nanaodgree program. It includes a Flask based web interface and a cli interface. 

This project will have the the following attributes:

- Interact with a variety of complex filetypes. 
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save images.
- Accept dynamic user input through a command-line tool and a web service. 

Packages used:
Project uses `python 3`, `random`, `PIL`, `abc`, `argparse`, `typing`, `pandas`, `docx`, `os`, `subprocess`, `requests`, `flask`.

This project will give you a hands-on opportunity to practice what you've learned in this course, such as:

Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
DRY (don’t repeat yourself) principles of class and method design.
Working with modules and packages in Python.

This project is designed to cover many areas of Python development. 

Data Engineering Roles:
To ingest data from a variety of data sources (TXT, DOCX, PDF) which is similar to the types of problems you'll experience when building machine learning pipelines.
The application will be packaged into an advanced command-line tool in the same way you might package data science models.

Full Stack Web Developers:
The application built will be packaged into a Flask server for anyone to easily use!
The application will accept HTTP requests, which is the backbone of the internet.
A submodule that generates images will be implemented, which is similar to creating things like profile pictures or cropping images for a gallery.

# Instructions

Starter Code

Option 1: Use the provided Workspace
We've provided some code and data to get you started, so the first step is to review the starter code in the workspace provided after the project instructions, and get generally familiar with what it includes.

Option 2: Code Locally
We've provided some code and data to get you started. So the first step is to download the starter code and get generally familiar with what it includes.

Task List
 Download the starter code.
-   Locate the smaple quotes and images of Xander the pup in src/\_data/.
-   There's a basic flask server that will consume your modules and make them usable through a web interface. Check out the main code for this flaks service in app.py.
-   Check out the HTML template files in templates/.

# Modules

# Quote Engine

The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author.This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

Quote Format
Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

# Ingestors
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

The responsibility of this module is to load and parse quotes from files. Here's what you'll need to do to complete it:

-   Create a Python module(including **init**.py) in a directory called QuoteEngine.
-   Example quotes are provided in a varity of files. Take a moment to review the file
    formats in ./data/SimpleLines and ./data/DogQuotes.
-   Implement a simple QuoteModel class to encapsulate the body and author.
-   Implement an abstract base class, IngestorInterface. This class should define two
    methods with the following class method signatures: def can_ingest(cls, path) -> boolean
    and def parse(cls, path: str) -> List[QuoteModel].
-   Implement separate strategy objects that realize the IngestorInterface for each file
    type(csv, docx, pdf, txt).
-   Implement a final Ingestor class that realizes the IngestorInterface abstract class
    and encapsulates your helper classes. It should implement logic to select the appropiate
    helper for a given file, based on filetype.
-   If you file, you can check your work against the Quote Engine Module section of the **rubric**.
-   All Quote classes have clear, concise, and PEP compliant dosctrings.
-   All code is PEP-8 Compliant.
-   Common exceptions should be handled using **try-catch** blocks.

# Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.

The class must implement code for:

-   Loading an image using Pillow (PIL)
-   Resizing the image so the width is at most 500px and the height is scaled proportionally.
-   Adding a quote body and a quote author to the image.
-   Save the manipulated image.
-   The class must implement this instance method signature, which returns the path to the manipulated image:

```
make_meme(self, img_path, text, author, width = 500) -> str
```

-   You can check your work against the **Meme Generator Module** section of the **rubric**.
-   All Meme Generator classes have clear, concise, and PEP compliant dosctrings.
-   All code is PEP-8 Compliant.
-   Common excpetions should be handled using **try-catch** blocks.

Package your Application
Larger, complex systems need an interface for users to interact with. We'll package the project as a command line tool and as a simple web service.

Create a Command-Line Interface tool
The project contains a simple cli app starter code in meme.py. This file contains @TODO tasks for you to complete. The utility can be run from the terminal by invoking python3 meme.py

The script must take three optional CLI arguments:

--body a string quote body
--author a string quote author
--path an image path
The script returns a path to a generated image. If any argument is not defined, a random selection is used.

Complete the Flask app
The project contains a flask app starter code in app.py. This file contains @TODO tasks for you to complete. The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image. 
It uses the requests package to fetch an image from a user submitted URL. The flask server must run with no errors

Make sure you complete the following tasks:

-   Open the **meme.py** command line starter code and complete the **@TODOs**.
-   Open the app.py flask web server starter code and complete the **@TODOS**. Yous
    can start the server by calling **python3 app.py** from a terminal window.
-   You can check your work against the **Package your Application** section of the **rubric**.
-   Create a **requierements.txt** file in the project root including all project dependencies.

### Description of the roles-and-responsibilities of all sub-modules including dependencies:

# Quote Engine Module

This module encapsulates the generation of the quote. It can read from multiple file formats using `IngestorInterface` . The `QuoteModel` class defines the format for storing the quotation with details like `body` and `author`
`
# Ingestors sub-module

The submodule Ingestors parse any file (csv, txt, docx, pdf).

-   In the Ingestors interface file exists a class which represents an object and validates if exist the file.
-   The csv ingestor file reads the csv file and returns a parse.
-   The docx ingestor file reads the docx file and returns a parse.
-   The pdf ingestor file reads the pdf file and returns a parse.
-   The text ingestor file reads the text file and returns a parse.

The dependencies this sub-module uses are:

-   Pandas (read the csv file).
-   Docx (read the docx file).

# Meme Engine Module

This module deals with image formatting. It fixes the width of the image to `500` and then scales the height of the image to generate and save a Meme to `output_dir` folder.

# Meme sub-module

The submodule Meme creates and generates the meme according to the
path, text, author, width passed.The meme engine file returns the outfile, which the meme image is created and saved.
