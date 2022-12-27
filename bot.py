"""
import pywhatkit

group_url = "Eg6oYr4uIoaKkFzOxsOFQH"
mesaj = "@zeynep hamsi"
asil_Mesaj = mesaj.encode("utf-8")

pywhatkit.sendwhatmsg_to_group_instantly(group_id= group_url, message = mesaj, wait_time = 15, tab_close = False)
"""
