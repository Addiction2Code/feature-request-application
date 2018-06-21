Feature Request App
===================

![Main Page of App](https://raw.githubusercontent.com/Addiction2Code/feature-request-application/master/screenshots/main-page.png)

Getting Started
===============

**Note:** This app uses Python 3.6 which will need to be installed on your system. As you are likely aware, some installations of `python` include the version as part of the name *i.e.* `python3` or `python2`, this also goes for `pip` sometimes being `pip2` or `pip3`. Take a few moments to determine the proper commands before continuing to the next step.

To start this app you'll want to install the requirements found in `requirements.txt`.

If you suffer from that odd angsty feeling of never quite knowing how much junk is installed on your system ✋, take a moment to install a virtual environment _first_.

- Install VirtualEnv: `pip install --user virtualenv`
- CreateEnv: `virtualenv env` or `python -m virtualenv env`
- Load your environment: `source env/bin/activate`

Now in your virtual environment, run the following: `pip install -r requirements.txt`.

Next, we need to grab our front-end dependencies through [Bower](https://bower.io/). First you'll need `npm`, you can find instructions [here](https://www.npmjs.com/get-npm).

`npn install -g bower`

Navigate to the `static` folder and type `bower install`.

Go back up a directory and run the following to create the database. Note that the following command will preload the local (default SQLite3) database with some entries, it will also overwrite entries from any previous uses.

`python db_create.py`

If you didn't get any errors you should be good to launch.

`flask run`


That's everything to get up and running. You're able to run tests via `pytest` as follows.

`pytest -v app/tests.py`

For more notes, check out the [JOURNEY.md](JOURNEY.md).

Usage
=====

Once you have everything up and running you should be able to start using the app. To add or remove clients head over to the `/clients` route or simply click the link in the top right of the app.

Once a client is added, there should be one in the system by default, you can click on their named tab towards the top from the index route `/`. From there, you can add, delete or re-arrange requests.

One feature to look for with this app is Drag Drop functionality. Simply hover over the item you'd like to move, press and drag to it's new position. The list should update, including the priorities of the affected requests. Though the Drag and Drop should work, if it doesn't for some reason, you may try adding an item to the list or doing a refresh. So far it's been tested on Chrome and Safari and on Mac (development) and Ubuntu (production) and everything operated as expected.

Best wishes, Paul Serra
