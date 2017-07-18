# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

from email.mime.text import MIMEText

# using code from these two tutorials:
# https://chrisalbon.com/python/monitor_a_website.html
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
    # print(soup.prettify())
    # print(str(soup).count('class="mw-headline"'))

    # declare previous number of classes variable if does not exist
    try:
      previous
    except NameError:
      previous = 0

    # if the number of times the class mw-headline, which is unique to the special elections list items, is equal to the previous comparison then run for another cycle
    if str(soup).count('collapsible collapsed') == previous:
        # wait 86400 seconds (one day),
        time.sleep(3600)
        # continue with the script,
        print("running: " + time.strftime("%Y-%m-%d %H:%M"))
        print(str(soup).count('collapsible collapsed'))
        continue

    # if the number of times the mw-headline class appears is different, reassign the number to previous and send out an email
    elif ((str(soup).count('collapsible collapsed') != previous) and previous > 1):
        previous = str(soup).count('collapsible collapsed')

        # set the 'from' address,
        fromaddr = 'specialelectionsupdate@gmail.com'
        # set the 'to' address
        toaddrs  = ['vanessa@flippable.org', 'specialelectionsupdate@gmail.com', 'ian@flippable.org', 'chris@flippable.org', 'catherine@flippable.org', 'joseph@flippable.org']

        SUBJECT = "There's a new special election!"

        # msg = str(soup)
        msg = "check:  https://ballotpedia.org/State_legislative_special_elections,_2017"
        msg = MIMEText(msg)
        msg['Subject'] = SUBJECT
        msg['To'] = ", ".join(toaddrs)
        msg['From'] = fromaddr

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("specialelectionsupdate@gmail.com", "gnnqgzCGo0bkLCffdQn5")

        # Print the email's contents
        # print('From: ' + fromaddr)
        # print('To: ' + str(toaddrs))
        # print('Message: ' + msg)
        print("new election: " + time.strftime("%Y-%m-%d %H:%M"))

        # send the email
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        # disconnect from the server
        server.quit()
        continue
    else:
        previous = str(soup).count('collapsible collapsed')
        # set the 'from' address,
        fromaddr = 'specialelectionsupdate@gmail.com'
        # set the 'to' address
        toaddrs  = ['vanessa@flippable.org']

        SUBJECT = "Initializing script!"

        # msg = str(soup)
        msg = "you're awesome"
        msg = MIMEText(msg)
        msg['Subject'] = SUBJECT
        msg['To'] = ", ".join(toaddrs)
        msg['From'] = fromaddr

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("specialelectionsupdate@gmail.com", "gnnqgzCGo0bkLCffdQn5")

        # send the email
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        # disconnect from the server
        server.quit()
        print("initializing: " + time.strftime("%Y-%m-%d %H:%M"))
        print(previous)
        print(str(soup).count('collapsible collapsed'))
        continue