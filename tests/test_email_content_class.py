from mordormail.EmailContentClass import EmailContentClass


def test_initialization():
    email = EmailContentClass("Hello, World!", "Test Subject")
    assert email.msg == "Hello, World!"
    assert email.subject == "Test Subject"
    assert email.tag is None
    assert email.attachments is None
    assert email.template_name == "default.html"
    assert email.template_vars == {
        "message": "Hello, World!",
        "signature": "The MordorMail Utility",
    }
    assert email.signature == "The MordorMail Utility"


def test_initialization_with_tag():
    email = EmailContentClass(
        "Hello, World!",
        "Test Subject",
        tag="TestTag",
    )
    assert email.subject == "[TestTag]: Test Subject"


def test_initialization_with_template_vars():
    template_vars = {"message": "New Message", "signature": "New Signature"}
    email = EmailContentClass(
        "Hello, World!", "Test Subject", template_vars=template_vars
    )
    assert email.msg == "New Message"
    assert email.signature == "New Signature"
    assert email.template_vars == template_vars


def test_add_attachments_to_mime_msg(sample_mime_message):
    email = EmailContentClass(
        "Hello, World!",
        "Test Subject",
        attachments=["./tests/test_files/test1.txt", "./tests/test_files/test2.json"],
    )
    result_msg = email.add_attachments_to_mime_msg(sample_mime_message)
    assert len(result_msg.get_payload()) == 2


def test_overwriting_message_and_signature():
    email = EmailContentClass(
        "Will be overwritten",
        "Test Subject",
        signature="Not the final signature",
        template_vars={"message": "Final Message", "signature": "Final Signature"},
    )
    assert email.msg == "Final Message"
    assert email.signature == "Final Signature"
