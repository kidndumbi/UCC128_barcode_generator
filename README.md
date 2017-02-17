##Tote Barcode Generator._beta_0_1##
###About:###
    This is a small but mighty application that will generate Tote barcode labels.

###How to install:###
    If python installed just run a WHTOT_generator_b_0_3.py.
    If working on the machine without python installed. Run an executable file.
    To build it in executable application run: "pyinstaller C:\path_to_the_file\alpha_0_2.py"

###How to Use:###
    Run the program.
    Application will welcome you and ask for required data:
      - Start Tote number - Type the number and press Enter.
      - End Tote number - Type the number and press Enter.
    After generation is complete:
      1. application will return you the information about location of the labels. Follow the provided directions to retrieve it.
      2. application will save a log about the last operation in format: date: current date, start: start_tote, end: end_tote, requester: Eli, warehouse: NJ3, comments: Blah

###Limitations:###
    1. System will automatically cut batches in 500 labels.(to support printing on the slow machines)
    2. All labels will start from 'WHTOT' prefix. (If you need another labels contact WMS Support)
    3. To avoid overloading of application it limited to generate 3000 labels at the session. To generate more that 3000 labels just run the application again.
