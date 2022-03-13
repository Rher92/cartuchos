from django.db import models
from cartuchos.utils.models import BaseCreatedUpdatedModel


# store report requests for testing, used by ReportBro Designer
# for preview of pdf and xlsx
class ReportRequest(BaseCreatedUpdatedModel):
    key = models.CharField(max_length=36)
    report_definition = models.TextField()
    data = models.TextField()
    is_test_data = models.BooleanField()
    pdf_file = models.BinaryField(null=True)
    pdf_file_size = models.IntegerField(null=True)
    created_on = models.DateTimeField()


# report definition for our album report which is used for printing
# the pdf with the album list. When the report is saved
# in ReportBro Designer it will be stored in this table.
class ReportDefinition(BaseCreatedUpdatedModel):
    report_definition = models.TextField()
    report_type = models.CharField(max_length=100, unique=True)
    remark = models.TextField(null=True, blank=True)
    last_modified_at = models.DateTimeField()

    def __str__(self):
        desc = self.report_type
        if self.remark:
            desc += ', ' + self.remark
        desc += ' (' + str(self.last_modified_at) + ')'
        return desc
