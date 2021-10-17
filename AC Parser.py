import pdfplumber
import re

with pdfplumber.open(r'AC List.pdf') as pdf:
    content = []
    regs = {"pages": [], "variances": [], "regs": []}
    pages = pdf.pages
    terms = ['departure', 'alternate', 'alternate compliance',
             'AC', 'A/C', 'variance' 'alt compliance']
    for i, page in enumerate(pages):
        content = page.extract_text()
        hits = 0
        for term in terms:
            for word in content.split(' '):
                if term in word:
                    hits += 1

        reg = re.findall('250\.(.+?)\s', content)
        regs["pages"].append(page)
        regs["variances"].append(hits)
        regs["regs"].append(reg)

        print(
            f"Found {hits} variance(s) and {len(reg)} regulation(s) on {page}.")
        if reg:
            print(f'\t {reg}\n')
        else:
            print(f'\t')

    print("Summary:")
    print(f"Pages = {len(regs['pages'])}")
    print(f"Variances = {sum(regs['variances'])}")
    regs_set = []
    for v in regs["regs"]:
        for inner_v in v:
            if inner_v not in regs_set:
                regs_set.append(inner_v)
    print(f"Regulations = {set(regs_set)}")
