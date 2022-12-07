0x11. Postmortem
===================

#### Summary:
On November 21st from 2:10 PM CET until 3:19 PM CET, servers web-01 and web-02 stopped responding to curl requests. One user was affected within this window. The cause of the outage was a misplaced line in the servers' configuration files.

#### Timeline:
- **2:10pm CET** - A bash script was executed on both servers to update their Nginx configurations.
- **2:11pm CET** - Issue detected. Attempts to curl either web servers' IPs to test the new configuration failed.
- **2:13pm CET** - Starting with web-01, Nginx was stopped. Upon trying to start again, an error occurred stating an error in the configuration file was preventing the server from restarting.
- **2:34pm CET** - Looking at the configuration file, it was clear that a new line that had been inserted with a bash script had been placed incorrectly.
- **3:01pm CET** - Both web-01 and web-02's Nginx configuration files were manually edited to ensure the new line was in the correct place.
- **3:19pm CET** - Nginx was restarted on both servers and both IPs respond properly to curl requests.

#### Cause:
At 1:10pm CET a bash script was executed to configure a server's Nginx installation to serve content from a particular directory. The script used sed to insert this new configuration line at a specific line number. This script worked correctly on a test server in a container. However, on the two live servers, this line was in the middle of another block of configuration code. Inserting the new line in this position caused the configuration file to be invalid.

#### Resolution:
At 1:18pm CET the configuration file was edited manually to make sure the new line was in the correct position and at 1:19pm CET Nginx was restarted. The usage of sed in the bash script was revised to no longer insert at a specific line but to instead match a pattern of text and insert the new line before it.

#### Future Measures:
- Rather than insert new lines at specific line numbers with sed, new lines will either be appended to the end or sed will be used to find a pattern and insert the new text before the pattern.
- When testing, the test server will be set up to replicate the actual server's custom configuration, rather than being a fresh default installation.
- Before a script is executed on both servers, it will be executed on only one and checked, rather than on both before checking.

#### Author
Davies Ajayi