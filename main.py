from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dna/transcription")
async def transcription(sequence):
    transcript = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'U '
        elif nucleotide == 'T':
            nucleotide = 'A '
        elif nucleotide == 'C':
            nucleotide = 'G '
        elif nucleotide == 'G':
            nucleotide = 'C '
        else:
            break
        transcript+=nucleotide
    return transcript

@app.get("/dna/translation")
async def translation(sequence):
    sequence2 = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            nucleotide = 'U'
        elif nucleotide == 'T':
            nucleotide = 'A'
        elif nucleotide == 'C':
            nucleotide = 'G'
        elif nucleotide == 'G':
            nucleotide = 'C'
        sequence2 += nucleotide

    RNA_sequence = []
    n = 0
    k = 1
    for seq in sequence2:
        RNA_sequence.append(sequence2[n]+sequence2[n+1]+sequence2[n+2])
        if len(sequence2)//3 > k:
            n += 3
            k += 1
        else:
            break

    amino_sequence = ''
    for codon in RNA_sequence:
        if codon == 'UUU' or codon == 'UUC':
            codon = 'Phe-'
        elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
            codon = 'Leu-'
        elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
            codon = 'Ile-'
        elif codon == 'AUG':
            codon = 'Met-'
        elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
            codon = 'Val-'
        elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
            codon = 'Ser-'
        elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            codon = 'Pro-'
        elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            codon = 'Thr-'
        elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            codon = 'Ala-'
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            codon = 'STOP'
            break
        elif codon == 'UAU' or codon == 'UAC':
            codon = 'Tyr-'
        elif codon == 'CAU' or codon == 'CAC':
            codon = 'His-'
        elif codon == 'CAA' or codon == 'CAG':
            codon = 'Gln-'
        elif codon == 'AAU' or codon == 'AAC':
            codon = 'Asn-'
        elif codon == 'AAA' or codon == 'AAG':
            codon = 'Lys-'
        elif codon == 'GAU' or codon == 'GAC':
            codon = 'Asp-'
        elif codon == 'GAA' or codon == 'GAG':
            codon = 'Glu-'
        elif codon == 'UGU' or codon == 'UGC':
            codon = 'Cys-'
        elif codon == 'UGG':
            codon = 'Trp-'
        elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            codon = 'Arg-'
        elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            codon = 'Gly-'
        amino_sequence+=codon
    return amino_sequence

@app.get("/dna/gc_content")
async def gc(sequence):
    gc = sequence.count('G') + sequence.count('C')
    total = len(sequence)
    content = ''
    try:
        content = str(int(gc/total*100))+'%'
    except ZeroDivisionError:
        pass
    return content

@app.get("/dna/total_count")
async def total_count(sequence):
    duuh = str(len(sequence))
    return duuh

@app.get("/dna/restriction_siter")
async def restriction_siter(restriction_site, sequence):
    motif_count = sequence.count(restriction_site) or  sequence.count(reverse(restriction_site)) 
    return motif_count

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)