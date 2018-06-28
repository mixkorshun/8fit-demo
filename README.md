# 8fit

This is demo 8fit website based on Wagtail CMS. It allows to create pages, 
product plans and offers.

View demo at [eightfit.herokuapp.com](https://eightfit.herokuapp.com/)

admin:  
`https://eightfit.herokuapp.com/admin/`  
`admin:8fitadmin`

## Features

 * Supports [the twelve-factor application methodology](https://12factor.net/).
 * Environment-based application configuration.
 * Docker and docker-compose compatible.
 * Supports Heroku deployment.

## Concept

### Pages

 - Home page – home page. It can be created only as website root page.
 - Static page – simple raw static page.
 - Landing page – page which contains some *page blocks*(heading + content).
            Can be linked with product offer.

### Product

 - Plan – product plan, it is directly linked with Stripe plan and represents it
            name and price
 - Offer – concrete offer for the user with selected plan and discount, that is 
        also linked with Stripe coupon code.

## Development

### Configuration
 Configuration can be specified using system environment or `.env` file located
 at project root.
 
 Application supports following options:

 - `DEBUG`(bool) – run in debug mode, default: `no`
 - `SECRET_KEY`(str, **required**) – Django secret key.
 - `BASE_URL`(url, **required**) – Wagtail CMS base url.
 - `ALLOWED_HOSTS`(str[]) – Comma separated list of allowed hosts, default: `*`
 - `DATABASE_URL`(uri) – URL for project database, default: `sqlite:///db.sqlite3`
 - `EMAIL_URL`(uri) – URL for email backend, default: `smtp://`
 - `LOG_LEVEL`(str) – project logging level, default: `ERROR`

### Running project locally

This project uses docker-compose for local running. Do the following to start:

 * Create `.env` file with application settings
 * `docker-compose up` will start application
 * `docker-compose run app migrate` will apply migrations
 * `docker-compose run app createsuperuser` will create new administrator
