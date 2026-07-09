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

        # Extract Information
        event_id = root.find(".//ns:EventID", namespace)

        provider = root.find(".//ns:Provider", namespace)

        computer = root.find(".//ns:Computer", namespace)

        time_created = root.find(".//ns:TimeCreated", namespace)

        # ADD THESE TWO LINES
        level = root.find(".//ns:Level", namespace)

        channel = root.find(".//ns:Channel", namespace)

        print("=" * 60)

        print("Event ID :", event_id.text)

        print("Provider :", provider.attrib.get("Name"))

        print("Computer :", computer.text)

        print("Time :", time_created.attrib.get("SystemTime"))

        # ADD THESE TWO PRINTS
        print("Channel :", channel.text)

        print("Level :", level.text)

        print("=" * 60)

        break
    event_id = root.find(".//ns:EventID", namespace)

provider = root.find(".//ns:Provider", namespace)

computer = root.find(".//ns:Computer", namespace)

time_created = root.find(".//ns:TimeCreated", namespace)
level = root.find(".//ns:Level", namespace)

channel = root.find(".//ns:Channel", namespace)
print("Event ID :", event_id.text)

print("Provider :", provider.attrib.get("Name"))

print("Computer :", computer.text)

print("Time :", time_created.attrib.get("SystemTime"))
print("Channel :", channel.text)

print("Level :", level.text)