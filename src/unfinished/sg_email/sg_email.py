#!/usr/bin/python2

import os
import sendgrid


def main():
    s = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_KEY'], secure=True)

    message = sendgrid.Mail(from_email='', subject='', text='', to=[''])
    
    # Attachments must be under 7MB in size each, and under 20MB total
    # Should add a check eventually
    # for filepath in args.attachments:
        # message.add_attachment(os.path.basename(filepath), filepath)
    s.send(message)

if __name__ == '__main__':
    main()