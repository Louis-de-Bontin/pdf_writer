from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.constants import FieldDictionaryAttributes
from PyPDF2.generic import NameObject, TextStringObject
from pprint import pprint

"""
'0': tax ID
'1': branch
'2': company name
'3': address
"""

file_name = "./pdf_files/pnd1.pdf"


def read_fields():
    reader = PdfReader(file_name)
    fields = reader.getFields()
    # page = reader.pages[0]
    # for j in range(len(page["/Annots"])):  # type: ignore
    #     writer_annot = page["/Annots"][j].get_object()  # type: ignore
    #     pprint(writer_annot)
    # try:
    #     pprint(f"{writer_annot['/T']}")
    # except:
    #     pass
    # pprint(page)
    return fields
    # pprint(fields)
    # fields_dict = {}
    # for key, value in fields.items():
    # fields_dict[key] = ""


#  'payer': {'/FT': '/Btn',
#            '/Ff': 32768,
#            '/Kids': [IndirectObject(1744, 0, 140487597669392),
#                      IndirectObject(1774, 0, 140487597669392),
#                      IndirectObject(1788, 0, 140487597669392),
#                      IndirectObject(1801, 0, 140487597669392)],
#            '/Opt': ['Yes', 'Yes', 'Yes', 'Yes'],
#            '/T': 'payer',
#            '/V': '/2'},


def update_form():
    reader = PdfReader(file_name)
    writer = PdfWriter()
    fields = reader.getFields()

    page = reader.getPage(0)
    # pprint(fields)

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

    # print(fields["payer"])
    for i in range(len(page["/Annots"])):  # type: ignore
        writer_annot = page["/Annots"][i].get_object()
        # if writer_annot.get(FieldDictionaryAttributes.T) == "payer":
        try:
            pprint(writer_annot["payer"])
        except:
            pass
        # fields["payer"].get_object().update(
        #     {
        #         NameObject("/V"): [
        #             TextStringObject("/1"),
        #         ]
        #     }
        # )
    # fields = reader.getFields()
    # print(fields["payer"])

    # for j in range(0, len(page["/Annots"])):
    #     writer_annot = page["/Annots"][j].getObject()
    #     for field in fields:
    #         payer_field = writer_annot.get("/T")
    #         # print(payer_field)
    #         if payer_field == "payer":
    #             print("Bonjour")
    #             writer_annot[payer_field].update(
    #                 {
    #                     NameObject("/Opt"): [
    #                         TextStringObject("Yes"),
    #                         TextStringObject("No"),
    #                         TextStringObject("No"),
    #                         TextStringObject("No"),
    #                     ]
    #                 }
    #             )
    #     print(f'Match : {writer_annot.get("/T")}')
    #     writer_annot.update({NameObject("/V"): TextStringObject("salut")})
    # else:
    #     print(f'No match : {writer_annot.get("/T")} != {field}')

    # for field_name, value in data.items():
    for i in range(1, 13):
        writer.updatePageFormFieldValues(page, {f"month_{i}": "/Yes"})
    #     )

    # write "output" to PyPDF2-output.pdf
    with open("./pdf_files/bonjour.pdf", "wb") as output_stream:
        writer.write(output_stream)
