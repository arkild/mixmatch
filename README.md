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
| /user/index (tentative name)            | Show       | Get       | Read        | user/index.html              | **YES**       | **YES**     |
| /search                                 | Show       | Get       | Read        | search.html                  | **YES**       | **YES**     |

## Screenshots
### Desktop View
![image](https://github.com/arkild/mixmatch/assets/141771685/c9487f6a-94ad-4c20-b15b-7cafa9e8377c)
![image](https://github.com/arkild/mixmatch/assets/141771685/a95b2e92-7fe3-487a-9d70-b7edf2b8faf6)

### Mobile View
![image](https://github.com/arkild/mixmatch/assets/141771685/65242f03-3c91-4a9e-b3ee-090ae9aba380)
![image](https://github.com/arkild/mixmatch/assets/141771685/1ff8f451-ce1c-4fc0-814f-74ee4d0a8d5d)



## List of technologies used
- HTML
- CSS
- Javascript
- Django
- Python
- PostgreSQL
- Amazon S3 (AWS)

## Getting started

Our project can be accessed by clicking [this link.](https://mixmatch-e776a4b93538.herokuapp.com/)

## Upcoming Future Enhancements

Some of the things we will be pursuing in the future:
- Binding the ability to add/delete drinks and add/delete reviews to only the users who create them. As of right now, the site's drinks and reviews can be edit and deleted by anyone, but the edit/delete links are only available on the user's own drink listing as an alternative to this issue.
- setting up models for ingredients, glasses, and categories so that the options to add more to the lists can be done through an administrator rather than through hard-coding, as the glasses and categories are currently set for our dropdown on `models.py`.
- create a page where the user can view a list of drinks from the database that match the ingredients that they put on their list.
- adding a video embed option for people who create their custom drinks to show a video tutorial on how to make the drink.
