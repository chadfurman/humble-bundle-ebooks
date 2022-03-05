## WORK IN PROGRESS

**This project does not currently run.  This is currently just the shell of a project.  See the TODOs down below.**

# Humble Lotus EBook Downloader
The goal of this is to list all book bundles and enable you to select which bundle to download

Optionally, you can download individual books in the bundle, specify formats of books (i.e. only mobi, only PDF, pdf and epub, etc)

You can, ofcourse, download all books in all bundles as well.

Ultimately, this will become a Calibre plugin to enable you to automatically import books from Humble Bundles into your Calibre library.

_Inspiration for this downloader comes from **https://github.com/MestreLion/humblebundle**_

## Usage

Default usage is to run as a CLI app
```bash
# install dependencies
pip install -e .

# run main.py and follow the prompts
python main.py
```

Additional usage, for example as a library and as part of a Calibre plugin, will be added

## TODO

* [ ] Retrieve gamekeys from purchases page (i.e. fetch bundle data) and cache -- *only on first load*
* [ ] Provide option to refresh the bundle cache on subsequent loads and from main menu
* [ ] Provide method to list all Book Bundles
* [ ] Provide method to search through Book Bundles
* [ ] Provide method to select a Book Bundle
* [ ] Provide method to download an entire Book Bundle (optionally providing a list of desired formats)
* [ ] Provide method to download a specific book (optionally providing a list of desired formats)
* [ ] Research requirements for a Calibre plugin
* [ ] Update TODO list with requirements for usage as a library to support a Calibre plugin
* [ ] Perform auth handshake to get the `csrf_cookie` and `_simpleauth_sess` cookies (currently, these need to be hard-coded)

## Development
to run the tests, do this:
```
PYTHONPATH=$(pwd) pytest
```

to include the e2e test suite (note, this hits the Humble Bundle API with your actual session token), do this:
```
E2E=1 SESSION="your-session-key" CSRF="your-csrf-key" PYTHONPATH=$(pwd) pytest
```

 Note that you must install the testing dependencies which right now install automatically all the time

 TODO: Move this to a "make test" file with an optional prompt for e2e credentials using https://term.ink

