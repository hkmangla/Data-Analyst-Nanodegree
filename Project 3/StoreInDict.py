import csv
import codecs
import re
import xml.etree.cElementTree as ET
import pprint

OSM_PATH = "sample.osm"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    # YOUR CODE HERE
    if element.tag == 'node':
        for i in node_attr_fields:
            node_attribs[i] = element.attrib[i]
        idn = node_attribs['id']
        for tag in element.iter("tag"):
            dicttag = {}
            dicttag['id'] = idn
            if problem_chars.match(tag.attrib['k']):
                continue
            elif LOWER_COLON.match(tag.attrib['k']):
                dicttag['type'] = tag.attrib['k'][:tag.attrib['k'].find(":")]
                dicttag['key'] = tag.attrib['k'][tag.attrib['k'].find(":") + 1:]
            else:
               dicttag['key'] = tag.attrib['k']
               dicttag['type'] = 'regular'
            dicttag['value'] = tag.attrib['v']
            tags.append(dicttag)
        # pprint.pprint({'node': node_attribs, 'node_tags': tags})
        return {'node': node_attribs, 'node_tags': tags}
    elif element.tag == 'way':
        for i in way_attr_fields:
            way_attribs[i] = element.attrib[i]
        idn = way_attribs['id']
        for tag in element.iter("tag"):
            dicttag = {}
            dicttag['id'] = idn
            if problem_chars.match(tag.attrib['k']):
                continue
            elif LOWER_COLON.match(tag.attrib['k']):
                dicttag['type'] = tag.attrib['k'][:tag.attrib['k'].find(":")]
                dicttag['key'] = tag.attrib['k'][tag.attrib['k'].find(":") + 1:]
            else:
               dicttag['key'] = tag.attrib['k']
               dicttag['type'] = 'regular'
            dicttag['value'] = tag.attrib['v']
            tags.append(dicttag)
        t = -1
        for nodetag in element.iter("nd"):
            node = {}
            t += 1
            node['id'] = idn
            node['node_id'] = nodetag.attrib['ref']
            node['position'] = t
            way_nodes.append(node)
        # pprint.pprint({'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags})
        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}

f =  open("data.txt",'w')
for _,element in ET.iterparse(OSM_PATH):
    el = shape_element(element)
    if el == None: 
        print element.tag
    f.write(str(el))


















