#!/usr/bin/python3
""" function to replace words in templates """

import logging
import sys
import os

def generate_invitations(template, attendees):
    """ function to replace templates with a list of dicts"""
    # Check input types
    if not isinstance(template, str):
        raise ValueError
    if not isinstance(attendees, list):
        raise ValueError
    # Handle empty inputs
    if not template:
        raise IndexError
    if not attendees:
        raise IndexError
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            processed_template = processed_template = template.format(**attendee)

        # Output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(processed_template)
