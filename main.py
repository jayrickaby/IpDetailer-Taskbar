import pystray
import pyperclip
import os
import sys
import threading
import time
from dotenv import load_dotenv
from ipdetails import ipdetails as ipd
from PIL import Image

load_dotenv()

class SystemTrayApp(pystray.Icon):
    def __init__(self):
        super().__init__(name="IP Detailer Taskbar")
        
        API_KEY = os.getenv("IPINFO_API_KEY")

        self.details = ipd.IPDetails(API_KEY)
        self.icon = Image.open(self.resourcePath("assets/icon.png"))
        self.menu = self.createMenu()

        threading.Thread(target=self.updateLoop, args=(self,), daemon=True).start()


    def createMenu(self):
        mi_publicIp = pystray.MenuItem(("P: " + self.details.getPublicIP()), self.copyPublicIP)
        mi_localIp = pystray.MenuItem(("L: " + self.details.getLocalIP()), self.copyLocalIP)
        mi_close = pystray.MenuItem("Exit", self.close)

        menu = pystray.Menu(
            mi_publicIp,
            mi_localIp,
            mi_close)

        return menu

    def resourcePath(self, relativePath):
        try:
            basePath = sys._MEIPASS
        except Exception:
            basePath = os.path.abspath(".")

        return os.path.join(basePath, relativePath)

    def copyLocalIP(self, item):
        self.copyToClipboard(self.details.getLocalIP())
        
    def copyPublicIP(self, item):
        self.copyToClipboard(self.details.getPublicIP())

    def copyToClipboard(self, text):
        pyperclip.copy(text)
    
    def updateLoop(self, app):
        while not self.visible:
            time.sleep(0.1)
        
        while self.visible:
            up, down = self.details.getTransferRates()
            currentRates = f"{up:.1f} KB/s ↑ | {down:.1f} KB/s ↓"
            self.title = currentRates

    def close(self, query):
        self.stop()

app = SystemTrayApp()

app.run()
