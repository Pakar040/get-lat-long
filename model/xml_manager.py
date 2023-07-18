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
        column_headers = ['Filename', 'Latitude', 'Longitude']
        df = pd.DataFrame([(pole.name, pole.latitude, pole.longitude) for pole in poles], columns=column_headers)
        filename = f'coordinates{self._extract_deliverable()}.xlsx'
        spreadsheet_location = os.path.join(self.directory, filename)
        df.to_excel(spreadsheet_location, index=False)

    def write_to_csv(self):
        handler = XMLHandler(self.directory)
        roots = handler.parse_all_xml()
        poles = [Pole(root, filename) for filename, root in roots.items()]
        column_headers = ['Filename', 'Latitude', 'Longitude']
        df = pd.DataFrame([(pole.name, pole.latitude, pole.longitude) for pole in poles], columns=column_headers)
        filename = f'coordinates{self._extract_deliverable()}.csv'
        spreadsheet_location = os.path.join(self.directory, filename)
        df.to_csv(spreadsheet_location, index=False)

    def _extract_deliverable(self):
        # Split the file path into components
        components = self.directory.split('/')

        # Find the index of 'Deliverable' in the list
        if 'Deliverable' in components:
            start_index = components.index('Deliverable')

            # Check if there are at least two components after 'Deliverable'
            if len(components) >= start_index + 2:
                # Keep the first component as is
                first_part = components[start_index + 1]

                # Extract the first letter and the number after the space for the second component
                second_part = components[start_index + 2][0] + ''.join(filter(str.isdigit, components[start_index + 2]))

                # Combine the two parts
                result = first_part + second_part

                return result

        # Return None if 'Deliverable' is not found or there are not enough components after it
        return None
