## Functional Testing

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Afrik Kitchen](https://afrik-kitchen.herokuapp.com) and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:

An on Screen message  is recieved registration is successful

Actual: 

An on Screen message  is recieved registration is successful

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [Afrik Kitchen](https://afrik-kitchen.herokuapp.com)
3. Click login

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click logout on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [page](https://afrik-kitchen.herokuapp.com/booking/New Booking/) - Login if prompted.
2. Enter the following as account detail( because you have to login before creating New booking)
    - Name: admin( this has staff aacount)
    - password 111code111
    (or/ you can create Your account and use it for testing)
    
Then
- Click the New Booking
- It will navigate You to List of Tables for Booking( althoug the list of table look same but there are different capacity and position)
    - click on the any table of your choice
-     Select reservation date and time 
-     click book table

Expected:

Form successfully submits and an on sreen message shown to alert the user of successful booking.

Actual:

Form successfully submits and on on screen shown to alert the user of successful booking.

<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [Homepage](https://afrik-kitchen.herokuapp.com/) - Login if prompted.

- click the Booking
-  click the Manag Booking
    Then:
    - Navigate you to the list of the table Booked(user)
    click th cancel booking
    click confrim

Expected:

Form successfully delete and a on sreen message  is shown to alert the user ofdeteting booking.

Actual:

Form successfully submits and a messsage is shown to alert the user of cancel booking.

<hr>

Description:

Ensure user can successfully Edit a booking.

Steps:
1. Login as a user with a booking or create a new booking
2. Click the Manage Booking nav link
3. Click the edit button on a booking
4. Click the confirm button on the edit page

Expected:

Booking is successfully updated

Actual:

Booking is successfully updated

<hr>

**Menu Pages**

Description:

Ensure a new menu item can be added/ created
Steps:

1. Navigate to the create menu item page from the menu drop down nav item
2. Enter the following details:
    - Fimage : (All the images were stored in Claudinary storage) pick anyone
    - Name: Test Menu
    - Type: breakfast
    - Description: Demo
    - Price(M): 15.00
    - Price(L) : 20.00
    -  vegeteria : either check or blank 
    - created_ on : the day date
    - created_staff : Uju

3. Click Create

Expected:

New menu item is sucessfully added message appear

Actual:

New menu item is sucessfully added message appear

<hr>


<hr>

Description:

Ensure a menu can be updated

Steps:

1. Navigate to the manage Menu page from the menus drop down nav link
2. Click edit on a menu
3. Update a menu item and submit the form

Expected:

Menu has been updated and a message displayed to the user it was updated

Actual: 

Menu has been updated and a  message displayed to the user it was updated

<hr>

Description:

Ensure a menu can be deleted

Steps:

1. Navigate to the manage menus page from the menus drop down nav link
2. Click the delete button on a menu
3. On the delete confirmation page click confirm

Expected:

Menu has been deleted and cannot be seen on the menus page

Actual:

Menu has been deleted and cannot be seen on the menus page

<hr>

**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

- Home -> index.html
- Bookings Drop Down, Manage Bookings -> managebookings.html
- Bookings Drop Down, New Booking -> create_booking.html
- Menus Drop Down, View Menu -> menus.html
- Menus Drop Down, Create Menu -> create_menu.html
- Menus Drop Down, Manage Menus => manage_menus.html
- Logout -> Sign out all auth page
- Login -> Sign in all auth page
- Register -> Sign up all auth page

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab and the twitter icon opened twitter in a new tab. These behaved as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot see another customer booking detail
2. A customer cannot book if no tables are available for the amount of guests
4. Forms cannot be submitted when required fields are empty

## Unit Testing

Unit tests were created to test some basic functionality such as templates used and redirects. These can be found in the tests.py files in the respective apps.

Results:

![unit tests](docs/testing/unit-test.PNG)

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Initially there were some errors due to stray script tags, misuse of headings within spans and some unclosed elements. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

![HTML Validator](docs/testing/html.PNG)

All pages were run through the official [Pep8](http://pep8online.com/) validator to ensure all code was pep8 compliant. Some errors were shown due to blank spacing and lines too long, 1 line instead of 2 expected. All of these errors were resolved and code passed through validators with the exception of the settings.py file.

The django auto generated code for AUTH_PASSWORD_VALIDATORS were showing up as lines too long. I could not find a way to split these lines but since they were auto generated and not my own custom code, I hope this is acceptable.

![PEP8](docs/testing/pep8.PNG)

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator. lIt flagged up issues with undefined variables as I jad forgotten to use the let keyword. This was fixed and the only warnings remained were that they were unused variables. The functions were called via onclick from the html elements themselves, so are in fact being used.

![JS validator](docs/testing/javascript.PNG)

## Lighthouse Report

Lighthouse report showed areas for improvement on SEO and Best practices. Meta descriptions and keywords were added to boost the SEO to 100 but the best practice warnings were coming from the use of an embedded iframe's javascript. Unfortunately I did not find a way to improve this as I am not initialising the google map iframe with javascript.

![Lighthouse v1](docs/testing/light-house-v2.PNG)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [Afrik kitchen](https://afrik_kitchen.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

Oukitel C21 Pro
TCL 30 Pro
iPhone SE


## Bugs

