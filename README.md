# Log Analysis

This is the third graduation project for the [FullStack Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) from Udacity.

A reporting tool was created that prints reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


This reporting tool answer three questions:
1. What are the three most popular articles of all time?
2. Who are the authors of most popular articles of all time?
3.  On what days more than 1% of requests resulted in errors?

## Getting Started

### Prerequisites

For the execution of the project you will need to use the following tools:

- [Vagrant](https://www.vagrantup.com/)
- [Virtual Box](https://www.virtualbox.org/)

## Installing process

### Cloning the porject

```
git clone https://github.com/brunoxd13/log-analysis.git
cd log-analysis
```

### Start the Project

- `vagrant up` to start up the virtual machine.
- `vagrant ssh` to login into virtual machine.
- `cd /vagrant/new` to change to the src directory.
- `python news.py` to run the reporting tool.

## Packages

Packages used for the construction of the project:

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Psycopg](http://initd.org/psycopg/)

## Author

[Bruno Russi Lautenschlager](https://github.com/brunoxd13)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details