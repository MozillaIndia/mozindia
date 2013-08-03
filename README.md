MozIndia
==========

This is the official Mozilla India site based on Mozilla's [Playdoh][gh-playdoh].

## Running locally
Clone the github repo and get all the Python dependencies:

    $ git clone https://github.com/MozillaIndia/mozindia.git

    $ cd mozindia

    $ git submodule update --init

    $ cd vendor

    $ git submodule sync

    $ git submodule update --init

    $ cd ..

    $ mv mozindia/settings/local.py{-dist,}


### Settings
The settings file for your local development is `mozindia/settings/local.py`.
Edit it and change the `DATABASES` setting. Change the `NAME` to, say,
`'mozindia'` and add your MySQL user/password in the right place if needed.

**Note**: *Never* commit this file `mozindia/settings/local.py`. It is meant
for your local development only.


### Setting up the database
Now you need to actually create a database. Do

    $ mysql -u root -p

If you have a password for the *MySQL* root user(not the UNIX root),
else just:

    $ mysql -u root

At the mysql prompt, type this IF you want to create a MySQL user:

    mysql> create user 'mozindia'@'localhost' identified by 'password_here';

**Note:** *Please make sure the user/password you created here is the same as 
the one present in the settings(local.py) file discussed in the previous
section*.

Then assuming both the username and database name are called 'mozindia',

    mysql> create database mozindia;

    mysql> grant all on mozindia.* to 'mozindia'@'localhost';

    mysql> quit;


### Creating a virtualenv to work on
Now install virtualenv if you do not have it:

    $ aptitude install python-virtualenv virtualenvwrapper

Create a virtualenv to work on:

    $ mkvirtualenv mozindia

Don't break your head over what a virtualenv is - just know that it is a self 
contained environment for a Python project. Your prompt should now indicate
what virtualenv you are working on:

    (mozindia)$ 

You can come out of it by typing

    (mozindia)$ deactivate
    $ 

And go back to work by typing

    $ workon mozindia
    (mozindia)$ 


### Installing dependencies
Now install the Mozilla funfactory package:

    (mozindia)$ pip install funfactory

**Note**: If you do not have `pip` installed, it can be installed(on Debian)
like so:

    $ aptitude install python-pip

If you run Fedora, chances are your pip will be called `python-pip`, so you
will have to run

    (mozindia)$ python-pip install funfactory

on Fedora.

Next up, we need to install some compiled dependencies in the virtualenv we
just created. So run (from the root mozindia directory)

    (mozindia)$ pip install -r requirements/compiled.txt 

The output of this command, when it finishes, should **end** with something
like
    
    Successfully installed MySQL-python Jinja2 py-bcrypt
    Cleaning up...
    (mozindia)$ 


### Syncing the database
We need to create the tables used by mozindia on the database we created
sometime ago:

    (mozindia)$ python manage.py syncdb

This will ask you to create a superuser for the Django admin. Create one now(
just follow the prompts).


### Running
Finally, we can now run the mozindia site locally:

    (mozindia)$ python manage.py runserver
    Validating models...

    0 errors found
    Django version 1.4.5, using settings 'mozindia.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


You can now go to `localhost:8000` in the browser to see the site. 


## Hacking
Patches are welcome! Fork this repo, perform the exact above steps with the
repo URL changed to the URL of your fork, hack and send an awesome pull
request.

mozindia is proudly a [Playdoh][gh-playdoh] project. Refer to the Playdoh
docs [here][docs].

Discussions can take place in the Mozilla India mailing list([join][mozindia-mailman])
and on IRC(`#india`@irc.mozilla.org).


## License
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[gh-playdoh]: https://github.com/mozilla/playdoh
[docs]: http://playdoh.rtfd.org/
[BSD]: http://creativecommons.org/licenses/BSD/
[mozindia-mailman]: https://lists.mozilla.org/listinfo/community-india
