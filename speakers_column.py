def get_speakers_from_event(linked_session, linked_camp_event):
    try:
        # Determine source and get people list
        if linked_session:
            people = linked_session.Speakers if linked_session else None
        elif linked_camp_event:
            fac = linked_camp_event.Facilitators if linked_camp_event else None
            people = [x.Person for x in fac] if fac else None
        else:
            return ""

       if not people:
            return ""
        # Process people data
        speaker_info = ""
        for peep in people:
            info_parts = ""
            if hasattr(peep, 'Person'):
                info_parts += peep.Person
            
            if hasattr(peep, 'Email'):
                info_parts += peep.Email
            
            if info_parts:
                speaker_info += " " + info_parts
        
        return ", ".join(speaker_info) if speaker_info else ""
        
    except Exception as e:
        return f"Error occurred: {e}"

# Call the function with the current row's linked references
get_speakers_from_event($Linked_Sessions, $Linked_Camp_Events)
