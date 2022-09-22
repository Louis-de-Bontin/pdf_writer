from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, TextStringObject
from pprint import pprint

"""
'0': tax ID
'1': branch
'2': company name
'3': address
"""

file_name = "./pdf_files/pnd1_with_form.pdf"


def read_fields():
    reader = PdfFileReader(file_name)
    fields = reader.getFields()
    return fields
    pprint(fields)
    # fields_dict = {}
    # for key, value in fields.items():
    # fields_dict[key] = ""


def update_form():
    reader = PdfFileReader(file_name)
    writer = PdfFileWriter()

    page = reader.getPage(0)
    print(page)

    writer.addPage(page)

    # data = {
    #     "company_pid": "9 9999 95999 99 9",
    #     "company_tin": "9 9999 9999 9",
    #     "tax_withheld_business_profit": 1500,
    #     "tax_withheld_commissions": 400,
    #     "tax_withheld_dividen30": "bonjour",
    #     "tax_withheld_dividend20": "au revoir",
    #     # "tax_withheld_5": 65,
    #     # "tax_withheld_6": 6578.8785,
    #     # "tax_withheld_7": 6873.8,
    # }

    for j in range(0, len(page["/Annots"])):
        writer_annot = page["/Annots"][j].getObject()
        for field in read_fields():
            writer_annot.pop(NameObject("/Kid"), None)
            if writer_annot.get("/T") == field:
                print(f'Match : {writer_annot.get("/T")}')
                writer_annot.update({NameObject("/V"): TextStringObject("salut")})
            else:
                print(f'No match : {writer_annot.get("/T")} != {field}')

    # for field_name, value in data.items():
    #     writer.updatePageFormFieldValues(
    #         page,
    #         {field_name: value},
    #     )

    # write "output" to PyPDF2-output.pdf
    with open("./pdf_files/bonjour.pdf", "wb") as output_stream:
        writer.write(output_stream)
