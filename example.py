from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    
    
    # Create instance of FastaParser
    fastaparser_obj = FastaParser('./data/test.fa')
    # Create instance of FastqParser
    fastqparser_obj = FastqParser('./data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for record in fastaparser_obj:
        print(record)
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for record in fastqparser_obj:
        print(record)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fastaparser_obj:
        print(reverse_transcribe(record[1]))
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fastqparser_obj:
        print(reverse_transcribe(record[1]))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
