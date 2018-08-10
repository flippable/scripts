# Scraper:

A simple script to scrape ballotpedia’s special elections site once an hour and notifies the email list when there is a new election. Currently set to the [page](https://ballotpedia.org/State_legislative_special_elections,_2018)
Needs to be updated for 2019. It looks for a particular css class that is only set for a new election instance. This could change if ballotpedia refactored their css, so keep an eye out! User can change which emails get alerts within the script. When a new change is made to the script, re-push it to EC2. 

## Login to EC2

You must log in to [Amazon EC2](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Home:)

Then you must create a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)



## Running in Ec2

You can run a tool such as GNU Screen, and detach your terminal and log out, only to continue where you left off later. I use this a lot.
For example:

How to Push the script to EC2 from your local:

`scp -i {/path/to/your/keypair.pem} {/path/to/your/local/special-scrape.py} ec2-user@ec2-35-166-40-144.us-west-2.compute.amazonaws.com:~/.
special-scrape.py` 

Log in to EC2
`ssh -i "{/path/to/your/keypair.pem}" ec2-user@ec2-35-166-40-144.us-west-2.compute.amazonaws.com` 

run: 
`screen`

How to run While inside:
`screen -rD`
`python special-scrape.py`

Start your script and either just close your terminal or properly detach your session with: Ctrl+A, D, D.
Disconnect from your terminal.
Reconnect at some later time, and run 
`screen -rD`
You should see your stuff just as you left it.
