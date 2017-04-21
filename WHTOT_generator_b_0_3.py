
import code128
import os
import datetime

print("Hello \nPlease input start and end numbers for the totes.\nMax number of labels 3000.\n"
      "System will truncate everything after this point.\n"
      ".........................................................")

timestamp = '{:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())

prefix = input('Enter the prefix of the barcode. (e.g WHTOT): ')
start = int(input('Enter Start Tote Number: '))
end = int(input('Enter End Tote Number: '))
requester = input('Who requested? ')
warehouse = input('For which Warehouse? ')
comments = input('Comments? ')

if end - start > 3000:
    end = start + 3000
    q = input("You requested more than 3000 labels.\n"
              "System will generate only first 3000 labels\n"
              "From {} to {} \n"
              ".........................................................\n"
              "Continue?(Y/N)".format(start, end))
    if q == 'Y' or q == 'y':
        pass
    else:
        quit()
# test comment
if start > end:
    print('Start number has to be less\equal then end number')
    input('please click Enter and re-start the application')
    quit()

path = 'C:\\Totes\\{}-{}\\'.format(start, end)
history_path = 'C:\\Totes\\'

blank_start = "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN'\
 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>\
<html xmlns='http://www.w3.org/1999/xhtml'><head><meta http-equiv='Content-Type' content='text/html;\
 charset=UTF-8'> <title>'WMS:: Print barcodes'</title> \
     <link id='Link1' href='_WMSTheme1.css' rel='stylesheet' type='text/css'> </head> <body>"

blank_end = " </body> </html>"
tote_html = "<div id='divUPC' style='width: 708px; height: 165px'> \
<table border='0' cellpadding='0' cellspacing='0' style='width: 334px; height: 86px'> <tr> \
<td style='width: 355px; height: 19px; text-align: center;' valign='middle'> \
<span class='txthdr_18'>{0}</span> \
</td> </tr> <tr> <td style='width: 500px; height: 160px'> \
<img src='{0}.png' style='width: 360px; height: 130px;'> \
</td> </tr> <tr> <td style='width: 340px; height: 19px; text-align: center;' valign='middle'> \
<span class='txthdr_18'>{0}</span> \
</td> </tr> </table> </div> <p STYLE='page-break-after: always'>&nbsp;</p>"


def create_path():
    if not os.path.exists(path):
        os.makedirs(path)

# generate and save images
def generate_labels(prefix, start, end):
    for image in range(start, end+1):
        code128.image(prefix.format(image), height=238, thickness=7, quiet_zone=True).save("{0}{1}{2}.png".format(prefix, path, image), compress_level = 6)

start_list = []
end_list = []

def generate_lists(start,end):
    while end - start > 500:
        start_list.append(start)
        end_list.append(start + 499)
        start += 500
    start_list.append(start)
    end_list.append(end)


# generate and save html
def create_html(start, end):
    for s in range(len(start_list)):
        f = open('{}{}-{}.html'.format(path, start_list[s], end_list[s]), 'w')
        f.write(blank_start)
        for x in range(start_list[s], end_list[s]+1):
            f.write(tote_html.format(x))
        f.write(blank_end)
        f.close()


def create_history_file(start, end, requester, warehouse, comments):
    try:
        f = open('{}history.csv'.format(history_path), 'a')
        f.write('Date:,{0},Start:,{1},End:,{2},Requester:,{3},Warehouse:,{4}, Comments:,{5}\n'
                ''.format(timestamp, start, end, requester, warehouse, comments))
        f.close()
    except PermissionError:
        input("Please close opened 'history.csv' file and click Enter...")
        create_history_file(start, end, requester, warehouse, comments)

create_path()
generate_labels(prefix, start, end)
generate_lists(start, end)
create_html(start, end)
create_history_file(start, end, requester, warehouse, comments)

print("\n"
      "Barcodes generated SUCCESSFULLY. \n"
      "Please find them in {} folder".format(path))

input('.........................................................\n'
      'To close this window press ENTER...')


