import shutil as sh
from getpass import getuser
import random
def main(picture_path, desktop_path, download_path):
	sh.copy2(picture_path, desktop_path)
	sh.copy2(picture_path, download_path)
desktop = "C:\\Users\\{}\\Desktop".format(getpass.getuser())
downloads = "C:\\Users\\{}\\Downloads".format(getpass.getuser())
arr = ["..\\__MATERIALS__\\cat1.gif", "..\\__MATERIALS__\\cat2.gif",
	"..\\__MATERIALS__\\cat3.gif",
	"..\\__MATERIALS__\\cat4.gif",
	"..\\__MATERIALS__\\cat5.gif",
	"..\\__MATERIALS__\\cat6.gif",
	"..\\__MATERIALS__\\cat7.gif",
	"..\\__MATERIALS__\\cat8.gif",
	"..\\__MATERIALS__\\cat9.gif",
	"..\\__MATERIALS__\\cat10.gif"
for i in range(0, 100):
	main(random.choice(arr), desktop, downloads)