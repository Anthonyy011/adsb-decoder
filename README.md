*ADS-B Decoder Project*

Read signals from nearby aircraft that broadcast at 1090 MHz and decodes them (using python) into readable data.

Data such as ID/callsign, where its located, as well as speed and altitude.

Given signals are receieved through a RTL-SDR radio dongle. 

Sample messages are drawn from https://mode-s.org - reference site with real messages and decoded answers. 

Messages contain 28 hex characters, first 5 bits repersents the Downlink Format (tells us what the message means) and the next 24 bits repersent the ICAO address (global ID on the aircraft transponder). 

DF and ICAO postions are international standards, every ADS-B aircraft uses the same bit layout. 

1. Store that message in a variable
2. Convert the hex string into a string of 1s and 0s
3. Take the first 5 characters of that binary string and convert them to a decimal number → DF
4. Get the ICAO — you can slice the binary, or take hex characters 2 through 7 directly, since 24 bits divides evenly into hex
5. Print both

[ ] Decode Downlink Format + ICAO
[ ] First git commit + push to GitHub
[ ] CRC integrity check
[ ] Callsign
[ ] Altitude
[ ] Position (CPR)
[ ] Velocity
[ ] Read live messages from RTL-SDR (dump1090 TCP feed on port 30002/30003)