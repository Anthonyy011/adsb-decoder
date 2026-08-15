# ADS-B Decoder Project

Read signals from nearby aircraft using a RTL-SDR radio dongle to capture broadcasts at 1090 MHz and decode them into readable parameters.

# Notes

Sample messages are drawn from https://mode-s.org - reference site with real messages.   
Following international standards, every ADS-B aircraft uses the same bit layout. 

# Road Map
### Fixed Sample Messages
- [x] Decode Downlink Format + ICAO
- [ ] CRC
- [ ] Callsign
- [ ] Altitude
- [ ] Position (CPR)
- [ ] Velocity
### Live Data
- [ ] Decode Downlink Format + ICAO
- [ ] CRC
- [ ] Callsign
- [ ] Altitude
- [ ] Position (CPR)
- [ ] Velocity
- [ ] Read live messages from RTL-SDR (dump1090 TCP feed on port 30002/30003)