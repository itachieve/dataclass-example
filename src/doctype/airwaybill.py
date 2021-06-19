from dataclasses import dataclass

from doctype.base import DocType
from field.base import CertainDateTimeField, IntField

@dataclass
class AirwayBill(DocType):
    file_name: str
    page_number: str
    dc_number: IntField
    dc_issue_date: CertainDateTimeField



if __name__ == "__main__":

    awb = AirwayBill(
        "NPG BI_8902",
        "TM00002",
        IntField("dc-number", "00050275"),
        CertainDateTimeField("dc-issue-date",None))
    print(awb.dc_number.name)
