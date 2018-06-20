Feature Request App
===================

**Note:** This app uses Python 3.6 which will need to be installed on your system. As you are likely aware, some installations of `python` include the version as part of the name *i.e.* `python3` or `python2`, this also goes for `pip` sometimes being `pip2` or `pip3`. Take a few moments to determine the proper commands before continuing to the next step.

To start this app you'll want to install the requirements found in `requirements.txt`.

If you suffer from that odd angsty feeling of never quite knowing how much junk is installed on your system ✋, take a moment to install a virtual environment _first_.

- Install VirtualEnv: `pip install --user virtualenv`.
- CreateEnv: `virtualenv env`
- Load your environment: `source env/bin/activate`

Now in your virtual environment, run the following: `pip install -r requirements.txt`.

Next, we need to grab our front-end dependencies through [Bower](https://bower.io/). First you'll need `npm`, you can find instructions [here](https://www.npmjs.com/get-npm).

`npn install -g bower`

Navigate to the `static` folder and type `bower install`.

Go back up a directory and run the following to create the database. Note that the following command will preload the local (default SQLite3) database with some entries, it will also overwrite entries from any previous uses.

`python db_create.py`

If you didn't get any errors you should be good to launch.

`flask run`

For more notes, check out the [JOURNEY.md](JOURNEY.md).

Best wishes, Paul Serra
