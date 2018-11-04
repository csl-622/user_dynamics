# user_dynamics
This project is about the characterisation of user contributions on a Wikipedia page.

1. The first part involves getting all the contributing user names or ip addresses(for anonymous users) for a particular wikipedia page. This is achieved by using xml.etree.ElementTree module and then parsing the whole xml data dump and getting the root. From that root, iterating the data for username and ip tags.

2. From the username and ip data we are finding out the part of contributions they made to different topics. This is done by creating a string of url that gets the user contribution of a particular page and then replacing the target="username" part with the name or ip of the contributor. The page loaded using requests.get() function opens the page and the page data downloaded as html file. Then the html file is parsed using beautifulsoup and then the names of all the topics he/she has worked till now gets listed.

-----------------------------------------------------------------
