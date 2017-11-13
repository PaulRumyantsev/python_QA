*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***

Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  lastname1  id1  address1
    Create Contact  $(contact)
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  $(contact)
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  get From List  ${old_list}  ${index}
    Modify Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  $(contact)
    Contact Lists Should Be Equal  ${new_list}  ${old_list}