def invalid(entry):
    if entry == '':
        return True
    if ' ' in entry:
        return True
    if len(entry) < 3:
        return True
    if len(entry) > 20:
        return True

def check_entries(username, password, vpassword, email):
    errors = {}
    errors['username'] = ''
    errors['password'] = ''
    errors['vpassword'] = ''
    errors['email'] = ''

    if invalid(username):
        errors['username'] ='Username is not valid! Please try again.'
    if invalid(password):
        errors['password'] ='Password is not valid! Please try again.'
    if vpassword != password:
        errors['vpassword'] ='Passwords do not match! Please try again.'
    if email_invalid(email):
        errors['email'] ='Email entered is not valid! Please try again.'
    return errors
    
def email_invalid(email):
    if email == '':
        return False
    else:
        if email.count('.') == 0 or email.count('.') > 1:
            return True
        if email.count('@') == 0 or email.count('@') > 1:
            return True
        if len(email) < 3 or len(email) > 20:
            return True

