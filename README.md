Feature Request App
===================

To start this app you'll want to install the requirements found in `requirements.txt`.

If you suffer from that odd angsty feeling of never quite knowing how much junk is installed on your system ✋, take a moment to install a virtual environment _first_.

- Install VirtualEnv: `pip install --user virtualenv`.
- CreateEnv: `virtualenv env`
- Load your environment: `source env/bin/activate`

Now in your virtual environment, run the following: `pip install -r requirements.txt`.

Next, we need to grab our front-end dependencies through [Bower](https://bower.io/). First you'll need `npm`, you can find instructions [here](https://www.npmjs.com/get-npm).

`npn install -g bower`

Navigate to the `static` folder and type `bower install`.

Go back up a directory and run the following to create the database.

`python db_create.py`

If you didn't get any errors you should be good to launch.

`flask run`

For more notes, check out the [JOURNEY.md](JOURNEY.md).

Best wishes, Paul Serra
