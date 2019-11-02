import pytest
import tempfile
from importlib import reload
import os
import io
import sys
from p3 import SourceCode

path = os.path.dirname(os.path.abspath(__file__))


# def test_r1a(capsys):
#     """Testing r2. All required information stored in folder r2. 

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='1a'
#     )

# def test_r1b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='1b'
#     )


# def test_r2a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='2a'
#     )


# def test_r3a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='3a'
#     )


# def test_r3b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='3b'
#     )


# def test_r3c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='3c'
#     )


# def test_r4a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='4a'
#     )


# def test_r4b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='4b'
#     )


# def test_r4c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='4c'
#     )


# def test_r5a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='5a'
#     )


# def test_r5b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='5b'
#     )


# def test_r6a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='6a'
#     )


# def test_r7a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='7a'
#     )


# def test_r7b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='7b'
#     )



# def test_r8a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='8a'
#     )


# def test_r9a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9a'
#     )


# def test_r9b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9b'
#     )


# def test_r9c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9c'
#     )

# def test_r9d(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9d'
#     )

# def test_r9e(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9e'
#     )

# def test_r9f(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='9f'
#     )

# def test_r10a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='10a'
#     )

# def test_r10b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='10b'
#     )

# def test_r10c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='10c'
#     )

# def test_r10e(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='10e'
#     )

# def test_r11a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='11a'
#     )

# def test_r11b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='11b'
#     )

# def test_r12a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='12a'
#     )

# def test_r13a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='13a'
#     )

# def test_r13b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='13b'
#     )

# def test_r14a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='14a'
#     )

# def test_r14b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='14b'
#     )

def test_r15a(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        test_id='15a'
    )

# def test_r15b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='15b'
#     )

# def test_r16a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='16a'
#     )

# def test_r16b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='16b'
#     )

# def test_r17a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='17a'
#     )

# def test_r17b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='17b'
#     )

# def test_r17c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='17c'
#     )

# def test_r18a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='18a'
#     )

# def test_r18b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='18b'
#     )

# def test_r18c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='18c'
#     )

# def test_r19a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='19a'
#     )

# def test_r19b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='19b'
#     )

# def test_r20a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='20a'
#     )

# def test_r20b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='20b'
#     )

# def test_r21a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='21a'
#     )

# def test_r21b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='21b'
#     )

# def test_r21c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='21c'
#     )

# def test_r22a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='22a'
#     )

# def test_r22b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='22b'
#     )

# def test_r22c(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helperNoTSF(
#         capsys=capsys,
#         test_id='22c'
#     )

# def test_r23a(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='23a'
#     )

# def test_r23b(capsys):
#     """Testing r2. All required information stored in folder r2.

#     Arguments:
#         capsys -- object created by pytest to capture stdout and stderr
#     """
#     helper(
#         capsys=capsys,
#         test_id='23b'
#     )
def test_r24a(capsys):
    """Testing r2. All required information stored in folder r2. 

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='24a'
    )

def test_r24b(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='24b'
    )

def test_r25a(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='25a'
    )
	
def test_r25b(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='25b'
    )

def test_r26a(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='26a'
    )

def test_r26b(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='26b'
    )
	
def test_r26c(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='26c'
    )
	
def test_r26d(capsys):
    """Testing r2. All required information stored in folder r2.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helperNoTSF(
        capsys=capsys,
        test_id='26d'
    )

# def r32a(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='32a'
    # )
	
# def test_r33a(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='33a'
    # )
# def test_r33b(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='33b'
    # )
# def test_r34a(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='34a'
    # )	
# def r34b(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='34b'
    # )
	
# def test_r35a(capsys):
    # """Testing r2. All required information stored in folder r2.

    # Arguments:
        # capsys -- object created by pytest to capture stdout and stderr
    # """
    # helperNoTSF(
        # capsys=capsys,
        # test_id='35a'
    # )	
#def test_r35b(capsys):
#    """Testing r2. All required information stored in folder r2.
#
#    Arguments:
#        capsys -- object created by pytest to capture stdout and stderr
#    """
#    helperNoTSF(
#        capsys=capsys,
#        test_id='35b'
#    )	

	

def helper(
        capsys,
        test_id):
    """ a helper function that test requirements for the example app

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # cleanup package
    #reload(app)

    # locate test case folder:
    case_folder = os.path.join(path, test_id)

    # concatenate test_id with .txt
    test_id_txt = test_id + ".txt"

    # concatenate test_id_txt with o
    out_test_id_txt = "o" + test_id_txt

    # concatenate test_id with o, _TSF and .txt
    out_tsf_test_id_txt = "o" + test_id + "_TSF.txt"

    # read terminal input:
    with open(
        os.path.join(
            case_folder, test_id_txt)) as rf:  # REPLACE NAME HERE
        terminal_input = rf.read().splitlines()

    # read expected tail portion of the terminal output:
    with open(
        os.path.join(
            case_folder, out_test_id_txt)) as rf:  #REPLACE NAME HERE
        terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file


    # prepare program parameters
    sys.argv = ['SourceCode.py',
        os.path.join(case_folder, 'vaf.txt'),
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    #app.main()
	
    SourceCode.main()
    #os.system("python ImprovedCodeWithClasses.py " + sys.argv[1] + " "+ sys.argv[2])
    #subprocess.run("python ImprovedCodeWithClasses.py " + sys.argv[1] + " "+ sys.argv[2])
    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    
    # compare terminal outputs at the end.`
    for i in range(1, len(terminal_output_tail)+1):
        index = i * -1
        print(index)
        print("What we expect")
        print(terminal_output_tail[index])
        print(out_lines[index])
        assert terminal_output_tail[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, out_tsf_test_id_txt), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            print("Content")
            print(content)
            print("expected")
            print(expected_content)
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)


def helperNoTSF(
        capsys,
        test_id):
    """ a helper function that test requirements for the example app

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # cleanup package
    # reload(app)

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
    sys.argv = ['SourceCode.py',
                os.path.join(case_folder, 'vaf.txt'),
                transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    # app.main()

    SourceCode.main()
    # os.system("python ImprovedCodeWithClasses.py " + sys.argv[1] + " "+ sys.argv[2])
    # subprocess.run("python ImprovedCodeWithClasses.py " + sys.argv[1] + " "+ sys.argv[2])
    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.`
    for i in range(1, len(terminal_output_tail) + 1):
        index = i * -1
        print(index)
        print("What we expect")
        print(terminal_output_tail[index])
        print(out_lines[index])
        assert terminal_output_tail[index] == out_lines[index]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
