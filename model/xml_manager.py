import os
import xml.etree.ElementTree as ET
import pandas as pd


class XMLHandler:
    def __init__(self, directory):
        self.directory = directory

    def parse_all_xml(self):
        roots = {}
        for filename in os.listdir(self.directory):
            if filename.endswith('.pplx'):
                tree = ET.parse(os.path.join(self.directory, filename))
                roots[filename] = tree.getroot()
        return roots


class Pole:
    def __init__(self, xml_root, filename):
        self.name = os.path.splitext(filename)[0]
        self.latitude = self.get_attribute_value(xml_root, 'Latitude')
        self.longitude = self.get_attribute_value(xml_root, 'Longitude')

    @staticmethod
    def get_attribute_value(xml_root, attribute_name):
        for value in xml_root.findall('.//VALUE'):
            if value.get('NAME') == attribute_name:
                return value.text
        return None


class PoleDataWriter:
    def __init__(self, directory):
        self.directory = directory

    def write_to_excel(self):
        handler = XMLHandler(self.directory)
        roots = handler.parse_all_xml()
        poles = [Pole(root, filename) for filename, root in roots.items()]
        column_headers = ['Name', 'Latitude', 'Longitude']
        df = pd.DataFrame([(pole.name, pole.latitude, pole.longitude) for pole in poles], columns=column_headers)
        spreadsheet_location = os.path.join(self.directory, 'poles-lat-long.xlsx')
        df.to_excel(spreadsheet_location, index=False)

