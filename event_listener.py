# LISTENERS:: event listener for custom forms. event.py#289

@event.listens_for(Event, 'after_insert')
def receive_init(mapper, conn, target):
    custom_form = CustomForms(
        event_id=target.id,
        session_form=session_form_str,
        speaker_form=speaker_form_str
    )
    target.custom_forms.append(custom_form)
