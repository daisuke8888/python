#! python3
# config: utf-8

testall = [{
    'scenarioName': '0001',
    'scenarioLog' : 'C:\\logdir\\logfile1.log'
    'checkLogs': [
        '<ERROR> Invalid argment.',
        '<INFO> Add IP address 192.168.0.1/24'
    ]},{
    'scenarioName': '0002',
    'scenarioLog' : 'C:\\logdir\\logfile2.log'
    'checkLogs': [
        '<DEBUG> Call validate().'
    ]}
]

