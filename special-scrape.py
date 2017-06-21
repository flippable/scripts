# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# using code from these two tutorials:
# https://chrisalbon.com/python/monitor_a_website.html
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# while this is true (it is true by default),
while True:
    # set the url as ballotpedia,
    url = "https://ballotpedia.org/State_legislative_special_elections,_2017"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.prettify())

    # TODO: change this to monitoring the number of special election divs
    if str(soup).find("special") == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # change this to monitoring the number of special election divs...if there are additional
    else:
        # create an email message with just a subject line,
        msg = 'Subject: This is Vanessa\'s script talking, CHECK the elections page!'
        # set the 'from' address,
        fromaddr = 'specialelectionsupdate@gmail.com'
        # set the 'to' addresses...add additional if you want the emails
        toaddrs  = ['vanessa@flippable.org', 'specialelectionsupdate@gmail.com']
        
        # TODO: determine the diff to get the added election
        # TODO: add email body with diff

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("specialelectionsupdate@gmail.com", "gnnqgzCGo0bkLCffdQn5")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break