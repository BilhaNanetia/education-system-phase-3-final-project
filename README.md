# EDUCATION SYSTEM CLI APPLICATION
## This is a command-line-interface (CLI) application for managing an education system.It includes basic CRUD operations (Create,Read,Update and Delete) for schools,courses and students, and uses Object-Relational Mapping (ORM) methods to interact with a SQLite database.
# Requirements
* Python installed
* SQLite installed
* Git
* VS Code 
* Pipenv (for managing dependencies)
## Features
* Create,update,list,find and delete schools
* Create,update,list,find and delete courses
* Create,update,list,find and delete students 
* Object-Relational Mapping (ORM): The application uses Python's built-in ORM techniques to map Python classes to SQLite database tables.
* Data Model: Includes three main classes: School, Course, and Student, with relationships defined such as:
     - A School can have multiple Courses.
     - A Course can have multiple Students.
     - A Student is enrolled in one Course.

## Running the application
* Fork the repository from github
* Clone the repository to your machine
* View the files in the VS Code
* Run:
    * pipenv install to create the virtual environment
    * pipenv shell to enter into the virtual environment and start using the python shell
    * python lib/config.py to initialize the database and create the tables
    * python lib/cli.py to run the CLI program
* Choose an option from the main menu displayed in the terminal.The application has a menu-driven interface.Users can navigate through the menus by entering the corresponding number.
* Examples of navigation:
    - Creating a School
      - To create a school, select the "Manage Schools" option from the main menu, then select the "Add School" option. Enter the school name and location, and the school will be created."School added successfully" will be displayed as a success message.
    - Creating a Course
       - To create a course, select the "Manage Courses" option from the main menu, then select the "Add Course" option. Enter the course title, description, and school ID, and the course will be created."Course added successfully" will be displayed as a success message.
    - Updating and Deleting
       - To update or delete a school, course, or student, select the corresponding option from the menu and follow the prompts.A success message will be displayed or a not found message if otherwise.
    - Listing and finding
       - To list or find a school, course, or student, select the corresponding option from the menu and follow the prompts.A success message will be displayed or a not found message if otherwise. 
    - To exit the menu interface: ctrl+d, or select the prompt to return to the main menu then select exit
## Contributing
Contributions are welcome! If you'd like to contribute to the application:
    * Fork the repository 
    * Create a new branch
    * Commit your changes
    * Push to the branch
    * Create a pull request
## Contact
If you have any questions or need further assistance, please contact my throuogh my email bilhaleposo@gmail.com


