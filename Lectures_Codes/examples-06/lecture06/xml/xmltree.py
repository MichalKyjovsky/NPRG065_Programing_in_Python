#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: xml read and write
from xml.etree import ElementTree

########################
# Read xml from string #
########################
root = ElementTree.fromstring("<root><node>A</node><node>B</node><node>C</node></root>")
# root contains directly the root element
for element in root:
    print(element.tag)
    print(element.text)

# parsing invalid data
try:
    ElementTree.fromstring("invalid xml content")
except ElementTree.ParseError as e:
    print(f"Invalid format, parser failed: {e}")

######################
# Read XML from file #
######################
xml = ElementTree.parse("sample.xml")
# root element needs to be obtained, xml represents file not the root element
library = xml.getroot()

# Check that we are holding the library root element
assert library.tag == "library"

# Print library name attribute
print(f"Library name: {library.attrib['name']}")

# List library content
# For each (book) element in root element
for book in library:
    print(book)
    # For each (name) element in a book
    for name in book:
        # Print language attribute
        print(name.get('language'))
        # Print text content of the name element
        print(name.text)

#############
# Store xml #
#############
# Create root element
root = ElementTree.Element("new root")

# Add sub-elements
for i in range(1, 10):
    element = ElementTree.Element("number")
    element.set("value", str(i))
    element.text = str(i)
    root.append(element)

# Convert to string
print(ElementTree.tostring(root, encoding="unicode"))

# Store in file
ElementTree.ElementTree(root).write("out.xml")
