# (TF) Diagnose Data Collection Tool

The following **Data Collection Tool** is dedicated for receiving data from users, saving in the cloud storage and receiving them in **.csv** format for reading (in Jupyter Notebook) to train in a selected Machine Learning algorithm.

## Architecture
1. Front-end

    Presents visualized and structured pages built with **Angular**:

    1. Dashboard
    
        This is where a user can enter the details of the patient and submit

    2. View Raw Data

        This page is dedicated to demonstrate all patients records that have been submitted
    
    3. Statistics

        Visual form of the analysis and statistics of the records
    
    4. Contact Us

        For reporting requests, questions or issues

2. Back-end

    REST API build with **DJANGO** provides:
    - Authorization
    - Saving data submitted via form in Dashboard page
    - Exporting data in `.csv` format


## How it Works

1. Authorization

If a user has signed in earlier with the credentials of the (only one currently) admin, the credentials are saved/present in local storage. Admin can directly open the app as the sign in details have been saved in cache.

Otherwise, a user navigated to a **Sign In** page to enter the credentials of the admin.


**IMPORTANT: The credentials will be received upon request**

2. Submitting the form via Dashbord page

3. In case of requests, questions or issues contacting via Contact Page

4. Checking the records in table or charts format depending on the need of the of the statistics

    NOTE: This types of visualizations can be done in a Jupyter Notebook while training datasets as well

5. Exporting data in `.csv` format from REST API to train in ML algorithm.


*In case of any recommendations or issues, feel free to let me know in Issues section*