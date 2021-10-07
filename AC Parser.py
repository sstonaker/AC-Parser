import pdfplumber
import re

with pdfplumber.open(r'AC List3.pdf') as pdf:
    content = []
    regs = {}
    pages = pdf.pages
    terms = ['departure', 'alternate', 'alternate compliance',
             'AC', 'A/C', 'variance' 'alt compliance']
    for i, page in enumerate(pages):
        content = page.extract_text()
        hits = 0
        for term in terms:
            if term in content:
                hits += 1

        reg = re.findall('250\.(.+?)\s', content)
        regs.update({page: reg})
        if hits > 0:
            print(f"Found {hits} variance(s) on {page}.")
            print(f'\t {reg}\n')
        else:
            print(f'{hits} variance(s) on {page}\n')
    print("Summary:")
    for k, v in regs.items():
        print(k, v)
