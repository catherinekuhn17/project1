# write tests for parsers
from typing import Tuple, Union
from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    
    # Generating FastaParser instance, and itterating it into a list
    parser_obj = FastaParser('./data/test.fa')
    record_list=[]
    for record in parser_obj:
        record_list.append(record)
    # Check if first record is what is expected from test file
    assert record_list[0] == ('>seq0','TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA')
    # Check if last record is what is expected from test file
    assert record_list[99] == ('>seq99',
'CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA')
    # Check if length of individual record is what is expected
    assert len(record_list[0]) == 2
    # Check if all records are read
    assert len(record_list) == 100
    
    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    # Generating FastqParser instance, and itterating it into a list
    parser_obj = FastqParser('./data/test.fq')
    record_list=[]
    for record in parser_obj:
        record_list.append(record)
    # Check if first record is what is expected from test file (in this case I didn't include the quaility
    # measure in the check, so spliced the tuple - I was having trouble inserting the quality measure as a string
    # on the right side of the equal sign
    assert record_list[0][0:2] == ('@seq0',
'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG')
    # Check if last record is what is expected from test file
    assert record_list[99][0:2] == ('@seq99',
'CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG')
    # Check if length of individual record is what is expected
    assert len(record_list[0]) == 3
    # Check if all records are read
    assert len(record_list) == 100
    
    pass
