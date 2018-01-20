# falcon-testing

Testing out the [Falcon framework](http://falconframework.org/) & Cassandra. Using pypy 5.10.0.

## Getting started

### Installing pypy
```bash
pyenv install pypy3.5-5.10.0
pyenv install 2.7.13
pyenv virtualenv pypy3.5-5.10.0 falcon-testing 
```

### Installing cassandra
```bash
brew update
brew install cassandra
brew services start cassandra
```

### Setup cassandra keyspace
```bash
cqlsh

# then in cqlsh
CREATE KEYSPACE cqlengine WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 } AND DURABLE_WRITES = true ;
```

### Set up code
```bash
git clone git@github.com:tizz98/falcon-testing.git
cd falcon-testing
pyenv local falcon-testing 2.7.13
```

### Run the application
```bash
gunicorn app:app

# OR (for live code reloads)
gunicorn app:app --reload

# OR
python app.py
```

### Testing the api
```bash
python client.py
```
