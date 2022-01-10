# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    nuc_dict = {
        'A' : 'U',
        'T' : 'A',
        'G' : 'C',
        'C' : 'G'
    }
    out_seq = ''
    for nuc in seq:
        out_seq = out_seq + nuc_dict[nuc]
    return out_seq


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    out_seq = transcribe(seq)
    rev_out_seq = out_seq[::-1]
    return rev_out_seq
