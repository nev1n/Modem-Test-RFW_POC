*** Settings ***
Library    NetcatLibrary.py

*** Variables ***
${modem_host}    127.0.0.1
${modem_port}    12345

*** Test Cases ***
Connect to Modem and Send Command
    Connect To Modem    ${modem_host}    ${modem_port}
    Send Command    +++AT?BV
    ${response} =    Read Response
    Log    Modem Response: ${response}
    Close Connection