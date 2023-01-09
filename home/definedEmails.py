from django.core.mail import EmailMultiAlternatives


def notify_user_registration(username, email):
    subject, from_email, to = 'Registration Confirmed !', 'dronza@dronza.org', email
    text_content = ''
    html_content = '<div style="margin: 50px; width: 80%; padding: 10px;">' \
                   '<img src="https://i.ibb.co/McTGgc7/dronza-red.png" border="0" />' \
                   f'<br> <p style="font-size:20px;font-weight:normal;"> <strong>Greetings!</strong></p>' \
                   f'<p style="font-size:18px;font-weight:normal;">Hi, {username} welcome to your new account and ' \
                   f'the beginning of your <strong style="color:#d72323;">DRONZA</strong> experience!</p>' \
                   '<p>We are excited to have you join us! I am <strong>Sohaib</strong> your Account Manager and ' \
                   'Support Representative. I am available to answer questions, provide technical assistance and' \
                   ' guide you through your setup. It is a quick ' \
                   'and easy process, and if you require assistance you can mail us or join the live chat.</p>' \
                   '<br><strong>Customer Support</strong> <br>Ph+: 92 344 427 6747 <br>' \
                   '<i>44000, ISLAMABAD</i>' \
                   '<hr><p> <span style="font-size:16px;color:#999; margin:0;">If you have any questions, ' \
                   'please contact us at </span><br>' \
                   '<a href="mailto:info@dronza.org" style="color:#d72323; text-decoration:none">' \
                   'Customer_support@dronza.org</a><p></div>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def notify_contact_us(username, email, message):
    subject, from_email, to = f'Hi, {username} Thank you for contact !', 'dronza@dronza.org', email
    text_content = ''
    html_content = '<div style="margin: 50px; width: 80%; padding: 10px;">' \
                   '<img src="https://i.ibb.co/McTGgc7/dronza-red.png" border="0" />' \
                   '<br> <p style="font-size:24px;font-weight:normal;">Thank you for reaching out to us !</p>' \
                   f'<p style="font-size:16px;color:#777; margin:0;">Hi, {username} We will appreciate your patience ' \
                   f'and gladly will respond to any question We will notify you once the following issue resolved:</p>' \
                   f'<div style=" background-color:#ddffdd;margin-bottom: 15px;border-left: 6px solid #04AA6D;' \
                   f' padding: 4px 12px;"><blockquote>{message}</blockquote></div><br>' \
                   '<strong>Info Center</strong> <br>Ph+: 92 344 427 6747 <br>' \
                  '<i>44000, ISLAMABAD</i>' \
                   '<hr><p> <span style="font-size:16px;color:#999; margin:0;">If you have any questions, ' \
                   'please contact us at </span><br>' \
                   '<a href="mailto:info@dronza.org" style="color:#d72323; text-decoration:none">' \
                   'info@dronza.org</a><p></div>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def notify_order_confirmation(c_name, c_email, c_phone, c_city, c_zip, c_country, c_address1, c_address2, p_grand_total):
    subject, from_email, to = 'Order confirmed !', 'dronza@dronza.org', c_email
    text_content = ''
    html_content = '<div style="margin: 50px; width: 80%; padding: 10px;">' \
                   '<img src="https://i.ibb.co/McTGgc7/dronza-red.png" border="0" />' \
                   '<br> <p style="font-size:24px;font-weight:normal;">Thank you for your purchase!</p>' \
                   f'<p style="font-size:16px;color:#777; margin:0;">Hi {c_name}, we are getting your order ' \
                   f'ready to be shipped we will notify you <br>' \
                   'when it has been sent.</p> <p><a href="https://dronza.org/track_order">' \
                   '<button style="border-color: #d72323;background: #c6192a;border-radius: 4px;color: white;' \
                   'padding: 15px 8px;  font-size: 16px; cursor: pointer;">' \
                   'View your order</button></a> or ' \
                   '<a href="https://dronza.org/" style="color:#d72323;">Visit our store</a></p><br><br>' \
                   f'<p style="font-size:20px;">Order summary</p>' \
                   f'<p style="font-size:17px; color:#555;">Total: <span style="margin-left:20px;">{p_grand_total}' \
                   f'</span> PKR</p><br>' \
                   f'<p style="font-size:26px;">Customer information</p>' \
                   f'<p>Name: <span style="font-weight:500; font-size:16px;color:#777;">{c_name}</span></p>' \
                   f'<p>Email: <span style="font-weight:500; font-size:16px;color:#777; text-decoration:none;">' \
                   f'{c_email}</span></p>' \
                   f'<p>Phone: <span style="font-weight:500; font-size:16px;color:#777;">{c_phone}</span></p>' \
                   f'<p>City: <span style="font-weight:500; font-size:16px;color:#777;">{c_city}</span></p>' \
                   f'<p>Country: <span style="font-weight:500; font-size:16px;color:#777;">{c_zip}, {c_country}' \
                   f'</span></p>' \
                   f'<p>Address 1: <span style="font-weight:500; font-size:16px;color:#777;">{c_address1}' \
                   f'</span></p>' \
                   f'<p>Address 2: <span style="font-weight:500; font-size:16px;color:#777;">{c_address2}' \
                   f'</span></p>' \
                   '<br><hr><p> <span style="font-size:16px;color:#999; margin:0;">If you have any questions, ' \
                   'please contact us at </span><br> ' \
                   '<a href="mailto:info@dronza.org" style="color:#d72323; text-decoration:none">' \
                   'Customer_support@dronza.org</a><p>' \
                   '</div>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

