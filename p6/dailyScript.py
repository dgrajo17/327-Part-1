import tempfile
import pytest
from importlib import reload
import os
import io
import sys
import backendSourceCode
import frontendSourceCode
#from subprocess import Popen, PIPE
import subprocess

path = os.path.dirname(os.path.abspath(__file__))

#subprocess.call(["frontendSourceCode.py", "vaf.txt"])
#subprocess.call(["python", "frontendSourceCode.py vaf.txt TTSF.txt"])


def dailyScript(
        test_id):
    """ a helper function that test requirements for the example app

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # locate test case folder:
    case_folder = os.path.join(path, test_id)

    # concatenate test_id with .txt
    test_id_txt = test_id + ".txt"

    # concatenate test_id_txt with o
    out_test_id_txt = "o" + test_id_txt

    # read terminal input:
    with open(
            os.path.join(
                case_folder, test_id_txt)) as rf:  # REPLACE NAME HERE
        terminal_input = rf.read().splitlines()

    # read expected tail portion of the terminal output:
    with open(
            os.path.join(
                case_folder, out_test_id_txt)) as rf:  # REPLACE NAME HERE
        terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # prepare program parameters
    sys.argv = ['frontendSourceCode.py',
                os.path.join(case_folder, 'vaf.txt'),
                transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    # app.main()

    frontendSourceCode.main()

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)

dailyScript(
        test_id='1a'
    )