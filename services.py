# hullo  too!

import settings as st

def authorizeCreds(givenUsername, givenPassword):
    if givenUsername != st.storeUsername or givenPassword != st.storePassword:
        return False
    else:
        return True