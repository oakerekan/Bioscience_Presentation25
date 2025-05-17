# bio_utils.py

def gc_content(seq):
    """Return GC percentage of a DNA sequence."""
    return 100 * (seq.count("G") + seq.count("C")) / len(seq)

def rev_comp(seq):
    """Return the reverse complement of a DNA sequence."""
    comp = seq.translate(str.maketrans("ACGT", "TGCA"))
    return comp[::-1]
