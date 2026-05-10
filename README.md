# IpDetailer Taskbar
Simple SystemTray application to show select information about an IP and network.
Helped me learn about pystray.

## About this project
This was made after someone I know AI-generated some code which was: (a) Slow (b) Not working (c) Not functional. This is 1 of 3 repositories I have created that rewrote, fixed, and improved on the AI-generated slop.
Some challenges I faced:
- Using pystray. This is a library I have never used before. However, I figured out some of the ins-and-outs of it and managed to get a cool application.
- Dynamically updating transfer rates. Likewise with the application, I did some hacky method. The advice I found online was to start a daemon?? I don't think its necessary, but so be it!
- Learning even more libraries. I mentioned before I learned part of pystray, but using pyperclip and PIL as well was fun.
## Gallery
<img width="147.33" height="307.66" alt="image" src="https://github.com/user-attachments/assets/c6e82147-c46b-45c4-8d9d-02a9d5e44e22" />

## Features
- A sidebar widget displaying information about: Local IP, Public IP, Location, ISP and Network Traffic.
- A nice design that doesn't show the jarring design of normal Tkinter.
- API Key that relies on the user, not the creator.

## Requirements
- Python
- Python pystray package
- Python pyperclip package
- Python dotenv package
- Python PIL package
- My [ipdetails](https://github.com/jayrickaby/ipdetails) package (included as a git submodule)

## Licence
Copyright © 2026 Jay Rickaby,
Licensed under the MIT License
