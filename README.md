# QEexamples
Examples of automation code

page.links.selen.py is designed to analyze the links on any web page given by the arg and test each link (href) found on the page.
It prints out any invalid link.
It saves the list of valid links to a file.

google.links.selen.py is similar to page.links.selen.py but it is specific to google.com page

comparelasttwo.sh is a shell script that compares the last two files output by google.links.selen.py. This is useful for tracking how google.com changes, usually on a daily basis.
