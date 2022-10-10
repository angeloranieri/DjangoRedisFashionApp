# DjangoRedisFashionApp

The project is the creation of a web app for a hypothetical second-hand clothing company. 
A data board is built with Django that allows users to enter an ID code to trace all previous owners identified by a nickname. 
Items can only be registered, updated, and transferred from one owner to another by an administrator. 
Each time a new owner is registered, a transaction is sent on Ethereum Ropsten containing a JSON file with the ID code and the nickname of the new owner. 
After logging in, the User is automatically directed to a page with the list of registered objects. 
On this page, a logging system has been implemented with Redis to store the last IP and 
eventually show an alert message in case it is accessed from a different Ip than the previous one. 
