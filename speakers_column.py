def get_speakers_from_event(linked_session, linked_camp_event):
    try:
        # Get the appropriate people list
        people = []
        
        if linked_session:
            people = getattr(linked_session, 'Speakers', "")
            #return "linked"
        elif linked_camp_event:
            fac = getattr(linked_camp_event, 'Facilitators', None)
            if fac: 
              people = [getattr(f, 'Person') for f in fac if hasattr(f, 'Person')]
        
        if not people: 
          return "" # No people so skip
        # Process each person
        speaker_info = []
        for person in people:
            info_parts = ""
            if hasattr(person, 'Person'):
                info_parts = person.Person
            if hasattr(person, 'Email'):
                info_parts += person.Email
            
            if info_parts:
                speaker_info.append(" ".join(info_parts))
             
        return ", ".join(speaker_info) if speaker_info else ""

    except Exception as e:
        return f"Error occurred: {e}"
        
# Call the function
get_speakers_from_event($Linked_Sessions, $Linked_Camp_Events)
