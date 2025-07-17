'''

==========================

Exercise 1: JSON Student Management System

--------------------------

1. Create a JSON string representing a classroom:

classroom_json = """
{
    "classroom": "CS101",
    "instructor": "Dr. Smith",
    "students": [
        {
            "id": "S001",
            "name": "Emma Wilson",
            "age": 20,
            "gpa": 3.8,
            "courses": ["Python", "Data Structures"]
        },
        {
            "id": "S002", 
            "name": "James Chen",
            "age": 19,
            "gpa": 3.9,
            "courses": ["Python", "Algorithms", "Web Development"]
        }
    ]
}
"""

2. Write a Python script that:

- Parse the JSON string into a Python dictionary using json.loads()
- Print the instructor's name
- Print the total number of students
- Print each student's name and GPA
- Find and print the student with the highest GPA

3. Add a new student to the data:

- Create a new student dictionary: ID="S003", Name="Sarah Johnson", Age=21, GPA=3.7, Courses=["Python", "Machine Learning"]
- Add this student to the existing classroom data
- Convert the updated data to JSON string with proper indentation using json.dumps()
- Write the updated data to a file called "updated_classroom.json" using json.dump()

4. Read and modify the JSON file:

- Read the "updated_classroom.json" file using json.load()
- Calculate and add an "average_gpa" field to the classroom data
- Add a "total_courses" field showing total unique courses across all students
- Save the modified data back to the file
'''

######################################################################################################

'''
==========================

Exercise 2: XML Library Management System

--------------------------

1. Create an XML file named "library_catalog.xml" with the following content:

<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="B001" category="fiction">
        <title>The Great Adventure</title>
        <author>John Smith</author>
        <year>2020</year>
        <price currency="USD">15.99</price>
        <available>true</available>
    </book>
    <book id="B002" category="science">
        <title>Python Programming Guide</title>
        <author>Jane Doe</author>
        <year>2022</year>
        <price currency="USD">29.99</price>
        <available>false</available>
    </book>
    <book id="B003" category="fiction">
        <title>Mystery of the Lost Code</title>
        <author>Mike Johnson</author>
        <year>2021</year>
        <price currency="USD">12.50</price>
        <available>true</available>
    </book>
</library>


2. Write a Python script that:

- Parse the XML file using ElementTree.parse()
- Get the root element
- Print the total number of books in the catalog
- Create a function to display the XML structure
- Find and print all book titles using findall()
- Find all books that are currently available
- Calculate the average price of all books
- Find all fiction books and display their details

3. Create new XML structure for members:

- Add a "members" section to the library XML
- Include: Member 1 (ID="M001", Name="Alice Brown", Type="Student", Join Date="2023-01-15")
- Include: Member 2 (ID="M002", Name="Bob Wilson", Type="Faculty", Join Date="2022-09-20")  
- Include: Member 3 (ID="M003", Name="Carol Davis", Type="Student", Join Date="2023-03-10")

4. Modify and write XML:

- Add a new book: ID="B004", Category="technology", Title="Machine Learning Basics", Author="Dr. Lisa Wang", Year="2023", Price="35.00", Available="true"
- Update book B002 availability from "false" to "true"
- Add a "total_books" element to the root containing the count of books
- Write the complete updated XML to "updated_library_catalog.xml" with proper indentation

==========================
'''