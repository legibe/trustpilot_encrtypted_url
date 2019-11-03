## Trustpilot encrypted url to allow identified users to add a review.

First use 'pip install -r requirements.txt ' to install all required modules.

* uses the Trust Pilot library to encrypt the url (in the requirement file)
* take one or more intput CSV file(s) passed to the command line (python run.py input1, inout2, ...)
* generate an output file for each input file in the same directory with _links appended before .csv. The output files have an extra column called Trustpilot_Link

See example_config.yaml for more info about configuration that should be stored in a file config.yaml
The encryption library used is pyca/cryptography that can be installed using 'pip install cryptography'. It is a requirement for trustpilot/python-authenticated-encryption used to create the encrypterf URLs.


