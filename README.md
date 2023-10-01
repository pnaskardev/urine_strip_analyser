
# Urine Stripe Analyzer

This project is a web application that analyzes an image of a urine strip and returns the RGB values of each segment on the strip. It is built using Django, HTML, CSS, JavaScript, NumPy, and OpenCV.

Tech Stack and Methodology
----------

### Frontend

The Frontend is build with Vanilla Javascript and HTML and CSS with GoogleFonts

### Backend

The Backend is built with the help of Django.

##### Methodology

The main methodology that has been used can be divided into 2 parts :-

1. **Cropping** - to get the useful part of the image.
2. **PreProcessing** - A billinear extrapolator is used to replace value of each pixel with the average value of the row to remove artifacts like granular noise and dark patches
3. **Segmentation** - small segments of 10x10 are used to get the average RGB value of each segment.

## Installation

1. Clone this repository using

   ```
   git clone https://github.com/pnaskardev/urine_strip_analyser.git
   ```

2. Navigate to the backend folder,install the required dependencies and start the webserver on port 8000

   ```
   cd urine_strip_analyser
   pip install -r requirements.txt
   ```

3. Start the server
    ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. Navigate to for testing
    ```
   http://localhost:8000/analyse/
   ```

## To run the Dockerized version

Clone the project

```bash
  git clone https://github.com/pnaskardev/urine_strip_analyser.git
```

Go to the project directory

```bash
  cd urine_strip_analyser
```

Start Docker

```bash
  docker-compose up
```

Navigate to the given link for testing

```bash
http://localhost:8000/analyse/
```


## Screenshots

![image](https://github.com/pnaskardev/urine_strip_analyser/assets/71266237/3228077c-bbb9-4ead-9140-83e23b125888)
![image](https://github.com/pnaskardev/urine_strip_analyser/assets/71266237/66fa0382-0b38-4bde-b676-f1b088910f97)




## Authors

- [@pnaskardev](https://www.github.com/pnaskardev)

