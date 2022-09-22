"""https://stackabuse.com/creating-a-form-in-a-pdf-document-in-python-with-borb/
https://github.com/jorisschellekens/borb-examples"""
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout

from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.forms.text_field import TextField
from borb.pdf.canvas.color.color import HexColor
from decimal import Decimal
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.forms.drop_down_list import DropDownList

from borb.pdf.canvas.layout.forms.country_drop_down_list import CountryDropDownList

import typing
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.page.page_size import PageSize
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
from borb.pdf.canvas.layout.image.shape import Shape

from borb.pdf.pdf import PDF


def create_pdf():
    # Create empty Document
    pdf = Document()

    # Create empty Page
    page = Page()

    # Add Page to Document
    pdf.append_page(page)

    # Create PageLayout
    layout: PageLayout = SingleColumnLayout(page)


    # Let's start by adding a heading
    layout.add(Paragraph("Patient Information:", font="Helvetica-Bold"))

    # Use a table to lay out the form
    table: FixedColumnWidthTable = FixedColumnWidthTable(
        number_of_rows=5, number_of_columns=2)

    # Name
    table.add(Paragraph("Name : ", horizontal_alignment=Alignment.LEFT,
            font_color=HexColor("56cbf9")))
    table.add(TextField(value="Doe", font_color=HexColor(
        "56cbf9"), font_size=Decimal(20)))

    # Surname
    table.add(Paragraph("Surname : ", horizontal_alignment=Alignment.LEFT,
            font_color=HexColor("56cbf9")))
    table.add(TextField(value="John", font_color=HexColor(
        "56cbf9"), font_size=Decimal(20)))

    # Sex
    table.add(Paragraph("Gender : ", horizontal_alignment=Alignment.LEFT))
    table.add(DropDownList(
        possible_values=[
            "Female",
            "Male",
        ]
    ))

    # Country of Residence
    table.add(Paragraph("Country of Residence : ",
            horizontal_alignment=Alignment.RIGHT))
    table.add(CountryDropDownList(value="Belgium"))

    # Nationality
    table.add(Paragraph("Nationality : ", horizontal_alignment=Alignment.RIGHT))
    table.add(CountryDropDownList(value="Belgium"))

    # Set some properties on the table to make the layout prettier
    table.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))
    table.no_borders()

    # Adding Table to PageLayout
    layout.add(table)

    # Data protection policy
    layout.add(Paragraph("Data Protection Policy",
                        font="Helvetica-Bold"))

    # Dummy text
    layout.add(Paragraph(
        """
        ** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
        font="Helvetica-Oblique"
    ))

    ps: typing.Tuple[Decimal, Decimal] = PageSize.A4_PORTRAIT.value

    r: Rectangle = Rectangle(Decimal(0), Decimal(32), ps[0], Decimal(8))
    Shape(points=LineArtFactory.rectangle(r), stroke_color=HexColor(
        "56cbf9"), fill_color=HexColor("56cbf9")).layout(page, r)

    # Store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)
