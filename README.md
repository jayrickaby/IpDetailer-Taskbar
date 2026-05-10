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
<img width="185" height="123" alt="image" src="https://github.com/user-attachments/assets/8fb23333-b16b-4e51-bdc6-03547f74df9b" />

<img width="262" height="116" alt="image" src="https://github.com/user-attachments/assets/2803836a-9d75-4f88-a32c-b4b9111d5b5b" />

## Features
- A SystemTray app displaying information about: Local IP, Public IP and Network Traffic.
- Want to easily get your Local / Public IP? Just click on the menu item and its copied to your clipboard!
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
