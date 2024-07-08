#!/usr/bin/python3
""" function to replace words in templates """

import logging
import sys
import os

def generate_invitations(template, attendees):
    """ function to replace templates with a list of dicts"""
    # Check input types
    if not isinstance(template, str):
        raise ValueError ("Not a string.")
    if not isinstance(attendees, list):
        raise ValueError ("Not a list.")
    # Handle empty inputs
    if not template:
        raise IndexError ("Template is empty, no output files generated.")
    if not attendees:
        raise IndexError ("Attendee list is empty.")
    # Process each attendee
    # count index of added attendees
    i = 0

    # iterate through each dictionary in the attendees list
    for attendee in attendees:
        i += 1
        for key, value in attendee.items():
            if value is not None:
                # using the ** operator to unpack dictionary
                processed_template = template.format(**attendee)
            else:
                # if any value in the dictionary is None - replace with N/A
                attendee[key] = "N/A"

        # Output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(processed_template)
