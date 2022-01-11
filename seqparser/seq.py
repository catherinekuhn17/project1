# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # transcription dictionary containing mapping of compliment bases.
    nuc_dict = {
        'A' : 'U',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G'
    }
    # initializing compliment sequence string
    comp_seq = ''
    # for each base in original sequence, find compliment and add it to output sequence
    for nuc in seq:
        comp_seq = comp_seq + nuc_dict[nuc]
    return comp_seq


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    # start by transcribing the sequence
    comp_seq = transcribe(seq)
    # reversing the previously created compliment strand
    rev_out_seq = comp_seq[::-1]
    return rev_out_seq
