reminder_system
This project helps the user to get notified about expiration of their licence and fitness ceritificates. 
The user is notified before 7, 15, 30 days before the date of expiry of their vehicle documents. 
This project can be executed by following basic execution commands for django project.

1.excute the project using: 
python manage.py runserver by changing the directory to current project folder.

2.Run the localhost server in your browser. 
3.On the current page if you want to create new truck details click create new truck details on navbar. 
4.Fill al the details. 5.In date field fill the expiration dates in following format. 
ex: licence expiry: 2018-04-09 
6.now create the truck details. 
7.If the differnece bwtween the current date and expiration date is 7 or 15 or 30 then the notification appearing in navbar will 
show the reminder message to user about the days remaining before expiration.


The test cases in this project are:
1.if the expiry date of licence and fitness certificate is same.
2.if the expiry date of licence and fitness certificate is different.
3.If the expiry date of the licence is not before 7 or 15 or 30 and fitness expiry matches will 7 or 15 or 30 days before.
4.if the niether of the expiry dates matches the condition of 7,15,30,days before.

in case 1: the system will show the notification for both the documents.
in case 2: the system will show both dates iwht different conditions like:
licence id:XXXX will expire on 7 days.
fitness id:XXXX will expire in 15 days.

In case 3: system will only show notification for fitness certificate.
Incase 4: the system will not show any notifications.

