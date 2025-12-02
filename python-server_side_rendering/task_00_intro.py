#!/usr/bin/python3
"""Simple Templating Program"""
import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    
    # Check if attendees contains dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary.")
            return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Start with the template
        invitation = template
        
        # Replace placeholders with attendee data or "N/A" if missing
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')
        
        # Replace placeholders in the template
        invitation = invitation.replace('{name}', str(name))
        invitation = invitation.replace('{event_title}', str(event_title))
        invitation = invitation.replace('{event_date}', str(event_date))
        invitation = invitation.replace('{event_location}', str(event_location))
        
        # Create output filename
        filename = f"output_{i}.txt"
        
        # Write to file
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
