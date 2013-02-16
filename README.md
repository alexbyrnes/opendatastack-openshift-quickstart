##OpenDataStack Quickstart for OpenShift
=====

###Deployment

Sign up for [OpenShift](https://openshift.redhat.com/app/)

Install the OpenShift [client](https://openshift.redhat.com/community/developers/rhc-client-tools-install)

Create your app and database

    $ rhc app create -a opendatastack -t python-2.6
    $ cd opendatastack
    $ git remote add upstream -m master https://github.com/alexbyrnes/opendatastack-openshift-quickstart
    $ git pull -s recursive -X theirs upstream master
    $ git push
    $ rhc cartridge add postgresql-8.4 -a opendatastack

Forward ports from your local machine

    $ rhc port-forward -a opendatastack    
(Note the IP for Postgres)

Push some data to your OpenShift database

    $ curl https://data.cityofchicago.org/api/views/28km-gtjn/rows.csv?accessType=DOWNLOAD | csvsql --no-constraints --insert --table firehouses --db "postgresql://admin:<DB_PASS>@<DB_IP>:5432/opendatastack"

Test!

    $ curl https://opendatastack-abyrnes.rhcloud.com/api/action/datastore_search_sql?q=select%20*%20from%20firehouses

Code! (Examples at [https://github.com/alexbyrnes/OpenDataStack](https://github.com/alexbyrnes/OpenDataStack))
