from pdf_annotate import PdfAnnotator, Location, Appearance


def update_pdf():
    # 826/1166 (environ)

    print("Updating PDF")
    folder = './pdf_files/'
    file_name = 'wtc.pdf'
    new_file = 'wtc_new.pdf'
    pdf = PdfAnnotator(folder + file_name)
    (w, h) = (827, 1169)
    pdf.set_page_dimensions((w, h), 0)

    company_name = 'Table ronde'
    company_address = 'Kaamelott, Royaume de Logres'
    pin_lible = '1234567890876'
    pin_withheld = '9876543210254'
    payer_name = 'Merlin l\'enchanteur'
    payer_address = 'Le labo, Kaamelott, Royaume de Logres'

    """
    +x1 -> push right
    +y1 -> push up
    +x2 -> increase square width (if < x1, invisible)

    """
    data = [
        {
            'text': company_name,
            'location': Location(x1=180, y1=h-130, x2=300, y2=h-115, page=0),
        },
        {
            'text': company_address,
            'location': Location(x1=180, y1=h-155, x2=500, y2=h-140, page=0),
        },
        {
            'text': payer_name,
            'location': Location(x1=180, y1=h-195, x2=500, y2=h-180, page=0),
        },
        {
            'text': payer_address,
            'location': Location(x1=180, y1=h-220, x2=500, y2=h-205, page=0),
        },
    ]

    for item in data:
        pdf.add_annotation(
            'text',
            item['location'],
            Appearance(fill=[0, 0, 0], content=item['text'], font_size=9),
        )

    pdf.write(folder + new_file)
