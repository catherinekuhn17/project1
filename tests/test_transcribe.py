# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    # test of trancription using example of transcription provided
    assert transcribe('ACTGAACCC') == 'UGACUUGGG'
    pass


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    # test of reverse trancription using example of reverse transcription provided
    assert reverse_transcribe('ACTGAACCC') == 'GGGUUCAGU'
    pass
