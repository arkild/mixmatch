# mixmatch

This is a collaborative 3-person group project involving the development of a full-stack application via psql and Django, with HTML/CSS/Javascript design on the front end. The initial purpose of this app was to create an application that could filter user-entered ingredients with a list of drinks that have their own ingredients, but it was reduced to a drink creation and review page to meet a more viable app, with intentions to add on the initially desired functionality later.

## Route Table
| URL                                     | Rest Route | HTTP Verb | CRUD Action | Views                        | Routes Tested | Created Yet |
|-----------------------------------------|------------|-----------|-------------|------------------------------|---------------|-------------|
| /                                       | Show       | Get       |             | home.html                    | **YES**       | NO          |
| /about                                  | Show       | Get       |             | about.html                   | **YES**       | NO          |
| /drinks                                 | index      | Get       | Read        | drinks/index.html            | **YES**       | NO          |
| /drinks/drink_id                        | show       | Get       | Read        | drinks/details.html          | **YES**       | NO          |
| /drinks/create                          | New        | Get       |             | main_app/drink_form.html     | pending       | NO          |
| /drinks/drink_id                        | create     | Post      | Create      | drinks/details.html          | pending       | NO          |
| /drinks/drink_id/update                 | Edit       | Get       | Read        | main_app/drink_form.html     | pending       | NO          |
| /drinks/drink_id                        | Update     | Patch/Put | Update      | main_app/details.html        | pending       | NO          |
| /drinks/drink_id/delete                 | Show       | Get       |             | main_app/drinkcon_delete.html| NO            | NO          |
| /drinks                                 | Destroy    | Delete    | Delete      | drinks/index.html            | pending       | NO          |
| (reviews on same page) /drinks/drink_id | Create     | Post      | Create      | main_app/details.html        | pending       | NO          |
| /drinks/review_id/update                | Edit       | Get       | Read        | main_app/review_form.html    | NO            | NO          |
| /drinks/drinks_id                       | Update     | Patch/Put | Update      | main_app/details.html        | NO            | NO          |
| /drinks/review_id/delete                | Show       | Get       |             | main_app/revcon_delete.html  | NO            | NO          |
| /drinks/drinks_id                       | Destroy    | Delete    | Delete      | main_app/details.html        | NO            | NO          |
