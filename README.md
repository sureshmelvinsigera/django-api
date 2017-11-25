# Django REST API

This is a django powered python application. Updates from this github repo will be automatically built by Jenkins and deployed by an Elastic Beanstalk instance in AWS.

The purpose is to learn smart development practices as well as trying to apply machine learning algorithms to my self leadership sofware.

More details here later.

## Database migrations
Create SQL scripts for database changes
according to models.py:

`python manage.py makemigrations`


Run SQL scripts from migrations files to make
the changes to database:

`python manage.py migrate`


Show selected migration file

`python manage.py sqlmigrate gym 0001`

## About serveless tech
This solutions is deployed on Linux server.
According to my investigation here are some ideas about 
serverless technologies on AWS.

### The serverless solution
* Front end by React
* Authentication by AWS Cognito
* API by AWS API Gateway
* Data processing by AWS Python 3.6 Lambda functions
* Data storage by AWS RDS or SQLite in S3

### Pros
* Modularity: API and authentication would be individual entities
* Possibly no need for Python framework
* More robust authentication
* Reduced costs for small number of users

### Cons
* Takes time to change the architecture
* Authentication still wouldn't be super simple
* AWS Api Gateway latency relatively high
* More modularity means more repetition