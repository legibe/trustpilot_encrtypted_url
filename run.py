import sys
from csv_reader import CSVReader
from csv_writer import CSVWriter
from trustpilot_url_encrypt import TrustPilotURLEncryption
from config import Config

if len(sys.argv) < 2:
    print('Requires at least one filename')
    exit()

for filename in sys.argv[1:]:
    input_file = filename
    output_file = filename.replace('.csv', '_links.csv')
    print('reading', input_file)
    config = Config('config.yaml')
    reader = CSVReader(input_file)
    writer = CSVWriter(output_file)
    # write the header only once in the output file
    write_header = True
    # go through the source csv
    for row in reader():
        # build the record for trust pilot we get something like
        record = {}
        for field in ('name', 'email', 'ref'):
            record[field] = row[config['fields'][field]]
        url = TrustPilotURLEncryption.encrypt(record)
        new_row = []
        for key in reader.header:
            new_row.append(row[key])
        new_row.append(url)
        if write_header:
            write_header = False
            writer.write_row(reader.header + ['Trustpilot_Link'])
        else:
            writer.write_row(new_row)
    print('output:', output_file, 'written')
