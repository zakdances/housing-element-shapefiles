import boto3
import json
import os
import logging
from botocore.exceptions import ClientError
from ctypes.util import find_library
# import tkinter
import camelot
import tabula
import pdfplumber
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env.local'))

logger = logging.getLogger(__name__)

class TextractWrapper:
    """Encapsulates Textract functions."""
    def __init__(self, textract_client, s3_resource, sqs_resource):
        """
        :param textract_client: A Boto3 Textract client.
        :param s3_resource: A Boto3 Amazon S3 resource.
        :param sqs_resource: A Boto3 Amazon SQS resource.
        """
        self.textract_client = textract_client
        self.s3_resource = s3_resource
        self.sqs_resource = sqs_resource

    def analyze_file(
            self, feature_types, *, document_file_name=None, document_bytes=None):
        """
        Detects text and additional elements, such as forms or tables, in a local image
        file or from in-memory byte data.
        The image must be in PNG or JPG format.

        :param feature_types: The types of additional document features to detect.
        :param document_file_name: The name of a document image file.
        :param document_bytes: In-memory byte data of a document image.
        :return: The response from Amazon Textract, including a list of blocks
                 that describe elements detected in the image.
        """
        if document_file_name is not None:
            with open(document_file_name, 'rb') as document_file:
                document_bytes = document_file.read()
        try:
            response = self.textract_client.analyze_document(
                Document={'Bytes': document_bytes}, FeatureTypes=feature_types)
            logger.info(
                "Detected %s blocks.", len(response['Blocks']))
        except ClientError:
            logger.exception("Couldn't detect text.")
            raise
        else:
            return response


TEST_FILE_PATH_1 = os.getenv('TEST_FILE_PATH_1')

def main():
    # find_library("gs")
    # tables = camelot.read_pdf(test_file_path)
    # print("Total tables extracted:", tables.n)
    # tables = tabula.read_pdf(test_file_path, pages="all")

    with pdfplumber.open(TEST_FILE_PATH_1) as pdf:
        page = pdf.pages[611]
        table = page.extract_table()  # Extract the table as a list of lists
        print(table)
        # print(first_page.chars[0])
    return

if __name__ == '__main__':
    main()