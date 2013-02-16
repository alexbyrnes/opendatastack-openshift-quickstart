##OpenDataStack Quickstart Deployment Package for OpenShift
=====

###Deployment

Sign up for [OpenShift](https://openshift.redhat.com/app/)

[Install rhc](https://openshift.redhat.com/community/developers/rhc-client-tools-install)

    $ rhc app create -a opendatastack -t python-2.6
    $ cd opendatastack
    $ git remote add upstream -m master https://github.com/alexbyrnes/opendatastack-openshift-quickstart
    $ git pull -s recursive -X theirs upstream master
    $ git push

Add postgres cartridge

    $ rhc cartridge add postgresql-8.4 -a opendatastack
(Copy down the username, password, and database name)

Forward ports from your local machine

    $ rhc port-forward -a opendatastack    
(Note the IP that's being forwarded for Postgres)

Push some data to your OpenShift database
    $ curl https://data.cityofchicago.org/api/views/28km-gtjn/rows.csv?accessType=DOWNLOAD | csvsql --no-constraints --insert --table firehouses --db "postgresql://admin:7b7mVNYzXbV5@127.2.229.1:5432/opendatastack"

Get it through the API

    $ curl https://opendatastack-abyrnes.rhcloud.com/api/action/datastore_search_sql?q=select%20*%20from%20firehouses

Code! (Examples at [https://github.com/alexbyrnes/OpenDataStack])
