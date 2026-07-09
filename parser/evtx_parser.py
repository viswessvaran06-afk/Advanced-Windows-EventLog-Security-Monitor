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

        provider = root.find(".//ns:Provider", namespace)

        computer = root.find(".//ns:Computer", namespace)

        time_created = root.find(".//ns:TimeCreated", namespace)

        print("=" * 50)

        print("Event ID :", event_id.text)

        print("Provider :", provider.attrib.get("Name"))

        print("Computer :", computer.text)

        print("Time     :", time_created.attrib.get("SystemTime"))

        print("=" * 50)

        break