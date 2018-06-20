The Journey
===========

What happened, when, and most importantly, why! _(maybe)_

### June 13th, 2018.
Today is the first day working on this application. So far I've refreshed myself on Flask and KnockoutJS, and put together a very basic outline _which will likely change_. Right now very basic "features" can be added on the main single page of this applications, previous entries are shown as Bootstrap card elements below the form.

### June 14th, 2018.
Things needed more separation so everything was extrapolated a bit. Templates now have a `layout.html` file they extend, the main contents of the app are in `app` and we started using SQLAlchemy. Additionally, a "Clients" page and model was added. In order to further control the JSON the API returns marshmallow_sqlalchemy was used.

### June 17th, 2018.
Worked on prioritizing list function. Didn't realize Borders closed at 7pm on Sunday. Didn't have as much time here as I had hoped.

### June 18th, 2018.
Hopefully you're not on a diet because here we have the "meat and potatoes" of the app. The ability to add a request and have the table update (in real-time) was implemented. On the flip side, deleting also works albeit with a few issues.

### June 19th, 2018.
Today was fun, a lot of the major components came together. Drag and drop functionality was added to the request lists! This means, in addition to adding a new request with a priority and having the list update in real-time, you can also re-arrange existing requests. The interface has also been updated.
