### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 3


# Mini Project 3

## Description

This project analyzes the "daily_food_nutrition_dataset.csv" using Pandas to calculate the total calorie intake per meal type for a random selection of users. It then generates five bar charts using Matplotlib, visualizing the calorie distribution for each user. These charts are saved as PNG files in a "charts" directory.

The project addresses the question: **"What is the calorie intake per meal type for a random selection of users from the dataset?"**

## Getting Started


### Dependencies

1.  **Install Required Packages:**
    * Install the packages using pip:
    ```
    pip install -r requirements.txt
    ```

2.  **Setup Database:**
    * Setup the database using flask:
    ```
    flask --app flaskr init-db
    ```

### Executing program

1.  **Run the Application:**
    * Run the application using flask:
    ```
    flask --app flaskr run
    ```

### Output

* The program will create a directory named "charts" in the current working directory.
* Inside the "charts" directory, five PNG files will be generated, each representing the calorie intake per meal type for a randomly selected user.
* The program will also print the dataframes used to generate the charts to the console.
* The question that the program answers will also be printed to the console.

## Authors

Contributors names and contact info

ex. Tanzeem Siddique

## Acknowledgments

Inspiration, code snippets, etc.
* [Flask](https://flask.palletsprojects.com/en/stable/tutorial/)
* [YouTube](https://www.youtube.com/watch?v=Yry14DldSvs)