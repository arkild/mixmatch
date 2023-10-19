# mixmatch

This is a collaborative 3-person group project involving the development of a full-stack application via psql and Django, with HTML/CSS/Javascript design on the front end. The initial purpose of this app was to create an application that could filter user-entered ingredients with a list of drinks that have their own ingredients, but it was reduced to a drink creation and review page to meet our deadline with our current level of skill, with intentions to add on the initially desired functionality later.

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
| /registration/login                     | N/A        | N/A       | N/A         | registration/login.html      | **YES**       | **YES**     |
| /accounts/signup                        | N/A        | N/A       | N/A         | registration/signup.html     | **YES**       | **YES**     |
| /user/index (tentative name)            | N/A        | N/A       | N/A         | user/index.html              | No            | No          |

## Screenshots

(Once our project is completed enough, we can put some screenshots of our app here)

## List of technologies used
- HTML
- CSS
- Javascript
- Django
- Python
- PostgreSQL
- Amazon S3 (AWS)

## Getting started

Our project can be accessed by clicking THIS LINK (which doesn't exist right now until deployment)

## Upcoming Future Enhancements

I will also fill this in with things we didn't finish by Friday. I don't expect us to do any heavy work on this over the weekend so I can have a pretty good idea of what stretch goals weren't done by then.
