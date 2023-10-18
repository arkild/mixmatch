# mixmatch

This is a collaborative 3-person group project involving the development of a full-stack application via psql and Django, with HTML/CSS/Javascript design on the front end. The initial purpose of this app was to create an application that could filter user-entered ingredients with a list of drinks that have their own ingredients, but it was reduced to a drink creation and review page to meet a more viable app, with intentions to add on the initially desired functionality later.

## Route Table
| URL                                     | Rest Route | HTTP Verb | CRUD Action | Views                        | Routes Tested | Created Yet |
|-----------------------------------------|------------|-----------|-------------|------------------------------|---------------|-------------|
| /                                       | Show       | Get       |             | home.html                    | **YES**       | **YES**     |
| /about                                  | Show       | Get       |             | about.html                   | **YES**       | **YES**     |
| /drinks                                 | index      | Get       | Read        | drinks/index.html            | **YES**       | **YES**     |
| /drinks/drink_id                        | show       | Get       | Read        | drinks/details.html          | **YES**       | **YES**     |
| /drinks/create                          | New        | Get       |             | main_app/drink_form.html     | **YES**       | **YES**     |
| /drinks/drink_id                        | create     | Post      | Create      | drinks/details.html          | **YES**       | **YES**     |
| /drinks/drink_id/update                 | Edit       | Get       | Read        | main_app/drink_form.html     | **YES**       | **YES**     |
| /drinks/drink_id                        | Update     | Patch/Put | Update      | main_app/details.html        | **YES**       | **YES**     |
| /drinks/drink_id/delete                 | Show       | Get       |             | main_app/drink_confirm_delete.html| **YES**  | **YES**     |
| /drinks                                 | Destroy    | Delete    | Delete      | drinks/index.html            | **YES**       | **YES**     |
| (reviews on same page) /drinks/drink_id | Create     | Post      | Create      | main_app/details.html        | **YES**       | **YES**     |
| /drinks/review_id/update                | Edit       | Get       | Read        | main_app/review_form.html    | **YES**       | **YES**     |
| /drinks/drinks_id                       | Update     | Patch/Put | Update      | main_app/details.html        | **YES**       | **YES**     |
| /drinks/review_id/delete                | Show       | Get       |             | main_app/review_confirm_delete.html|  **YES**| **YES**     |
| /drinks/drinks_id                       | Destroy    | Delete    | Delete      | main_app/details.html        | **YES**       | **YES**     |
| /registration/login                     | N/A        | N/A       | N/A         | registration/login.html      | No            | No          |
| /accounts/signup                        | N/A        | N/A       | N/A         | registration/signup.html     | No            | No          |
| /user/index (tentative name)            | N/A        | N/A       | N/A         | user/index.html              | No            | No          |
