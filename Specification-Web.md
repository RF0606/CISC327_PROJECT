
## 💺 Project Requirement - Web Option

The product you are to design and build is the SeetGeek not SeatGeek online Customer-to-Customer ticket selling system.
A registered user can buy and sell tickets through this online application.

![image](https://user-images.githubusercontent.com/8474647/94135518-8ebfab80-fe31-11ea-9347-ad83f7922cf5.png)

The above control flows roughly define the functionalities and workflows of the system. An actor is able to access his/her home directory after logged-in. 
One can also register directly through the portal. More specifications and requirements will be provided for assignment #1. 

:fire: :fire: :fire:  [Template for the web option](https://github.com/CISC-CMPE-327/CI-Python)

## :fire: Specification - Web Option


### Front-end:
The web application handles a sequence of actions performed by the user on their browser. Consider there are two input domains: the URL input box and the rendered webpage to interact with the users. 

| Pages | The frontend mainly consists of the following pages: |                            |
|-------|------------------------------------------------------|----------------------------|
|       | /login                                               | The user login page        |
|       | /register                                            | The user registration form |
|       | /                                                    | The user profile page      |

| Routes | The frontend mainly consists of the following routes: |             |
|--------|-------------------------------------------------------|-------------|
|        | /login                                                | [GET, POST] |
|        | /register                                             | [GET, POST] |
|        | /                                                     | [GET]       |
|        | /logout                                               | [GET, POST] |
|        | /buy                                                  | [POST]      |
|        | /sell                                                 | [POST]      |

Requirements and Constraints:

|  |  |  |
|-|-|-|
| R1 | /login  | [GET] |
|  |  | If the user hasn't logged in, show the login page |
|  |  | the login page has a message that by default says 'please login' |
|  |  | If the user has logged in, redirect to the user profile page |
|  |  | The login page provides a login form which requests two fields: email and passwords |
|  |  | [POST] |
|  |  | The login form can be submitted as a POST request to the current URL (/login) |
|  |  | Email and password both cannot be empty |
|  |  | Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation) |
|  |  | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character |
|  |  | For any formatting errors, render the login page and show the message 'email/password format is incorrect.' |
|  |  | If email/password are correct, redirect to / |
|  |  | Otherwise, redict to /login and show message 'email/password combination incorrect' |
|  |  |  |
|  |  |  |
| R2 | /register | [GET] |
|  |  | If the user has logged in, redirect back to the user profile page / |
|  |  | otherwise, show the user registration page |
|  |  | the registration page shows a registration form requesting: email, user name, password, assword2 |
|  |  | [POST] |
|  |  | The registration form can be submitted as a POST request to the current URL (/register) |
|  |  | Email, password, password2 all have to satisfy the same required as defined in R1 |
|  |  | Password and password2 have to be exactly the same |
|  |  | User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | User name has to be longer than 2 characters and less than 20 characters. |
|  |  | For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) |
|  |  | If the email already exists, show message 'this email has been ALREADY used' |
|  |  | If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page  |
|  |  |  |
|  |  |  |
| R3 | / | [GET] |
|  |  | If the user is not logged in, redirect to login page |
|  |  | This page shows a header 'Hi {}'.format(user.name) |
|  |  | This page shows user balance. |
|  |  | This page shows a logout link, pointing to /logout |
|  |  | This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. |
|  |  | This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date |
|  |  | This page contains a form that a user can buy new tickets. Fields: name, quantity |
|  |  | The ticket-selling form can be posted to /sell |
|  |  | The ticket-buying form can be posted to /buy |
|  |  | The ticket-update form can be posted to /update |
|  |  |  |
| R4 | /sell | [POST] |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to 100. |
|  |  | Price has to be of range [10, 100] |
|  |  | Date must be given in the format YYYYMMDD (e.g. 20200901) |
|  |  | For any errors, redirect back to / and show an error message |
|  |  | The added new ticket information will be posted on the user profile page |
|  |  |  |
| R5 | /update | [POST] |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to 100. |
|  |  | Price has to be of range [10, 100] |
|  |  | Date must be given in the format YYYYMMDD (e.g. 20200901) |
|  |  | The ticket of the given name must exist |
|  |  | For any errors, redirect back to / and show an error message |
|  |  |  |
| R6 | /buy | [POST] |
|  |  | Constraint: |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to 100. |
|  |  | The ticket name exists in the database and the quantity is more than the quantity requested to buy |
|  |  | The user has more balance than the ticket price * quantity  + service fee (35%) + tax (5%) |
|  |  | For any errors, redirect back to / and show an error message |
|  |  |  |
|  |  |  |
| R7 | /logout | [POST] |
|  |  | Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages. |
|  |  |  |
| R8 | /* | [any] |
|  |  | For any other requests except the ones above, the system should return a 404 error |

### :car: Example frontend test case in natural language:

(full list of selenium action api is [here](https://github.com/seleniumbase/SeleniumBase/blob/733b28ffd45533a9e82a834f0b1f3285189895f8/help_docs/method_summary.md))

For frontend test cases, we use mocking (to use a faked backend rather than actually running the backend, see [here](https://github.com/CISC-CMPE-327/CI-Python#pytest))

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

```

#### Test case R1.3 - If the user has logged in, redirect to the user profile page


Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /login again
 - validate that current page contains `#welcome-header` element
 
 


