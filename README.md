# ps-gallery
 This is a personal gallery application that allows one to display their photos for others to see, click on a single photo to expand it and  view the details of the photo, view photos based on the location they were taken and one can copy a link to the photo to share with  friends

 ## By Mercy Wairimu
## User Stories  
User Can :

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with their friends.  
* View photos based on the location they were taken.  
## Behavior Driven Development (BDD)
The BDD focuses on how a user interacts with the application.
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------:|
|Display image details|On load|Images & information about the the images will be displayed ie.location and category|
|Search for images by category|Search by Category|The images that fit search description will be displayed|
|Click Image|Click on image| A modal containing image details is shown|
## Setup and Installation

To get a copy of the project up and running on your local machine for development and testing purposes, **clone** this repository into a **virtual environment** and install the package manager, **pip**.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Use the package manager pip to install all project requirements. 
```sh
(virtual) $ pip install -r requirements.txt
```

### Installing

To get a development env running, use the **.env.example** file to create a **.env** file with appropriate values

### Running the tests

Run automated tests for this system

```sh
(virtual) $ python3 manage.py test gallery
```

### Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43) to see it live or simply run it locally
 ```
 (virtual) $ python3 manage.py runserver
 ```

## Technologies Used

* [Django 4.0.4](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python 3.8.10](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system
## Known Issues & bugs

No known bug at pesent during development.If you come across a bug reach out to the contacts below.
[mercy.mambui@student.moringaschool.com](mailto:mercy.mambui@student.moringaschool.com)
## License
MIT

Copyright (c) 2022 Mercy Wairimu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
## Authors Info
Email: mercy.mambui@student.moringaschool.com 