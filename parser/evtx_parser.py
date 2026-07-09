from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

log_file = "logs/Security.evtx"

with Evtx(log_file) as log:
    for record in log.records():

        xml_data = record.xml()

        root = ET.fromstring(xml_data)

        namespace = {
            "ns": "http://schemas.microsoft.com/win/2004/08/events/event"
        }

        event_id = root.find(".//ns:EventID", namespace)

        print("Event ID:", event_id.text)

        break