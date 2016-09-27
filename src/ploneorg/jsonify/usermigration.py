import json


def export_userdb(site):
    pas = site.acl_users
    users = pas.source_users
    passwords = users._user_passwords
    thefile = open('userdb.txt', 'w')
    thefile.write(json.dumps(dict(passwords)))
    thefile.close()
