"""Tests for the pdf_merge tool."""

import os
import shutil
import sys
import tempfile
from unittest.mock import patch

import pytest
from pypdf import PdfWriter

from sst import pdf_merge


@pytest.fixture
def sample_pdfs():
    """Create temporary PDF files for testing."""
    temp_dir = tempfile.mkdtemp()
    pdf_files = []
    
    # Create two simple PDF files
    for i in range(2):
        pdf_path = os.path.join(temp_dir, f"test_{i}.pdf")
        writer = PdfWriter()
        writer.add_blank_page(width=612, height=792)  # Standard letter size
        with open(pdf_path, "wb") as f:
            writer.write(f)
        writer.close()
        pdf_files.append(pdf_path)
    
    yield temp_dir, pdf_files
    
    # Cleanup - remove entire temp directory
    shutil.rmtree(temp_dir, ignore_errors=True)


def test_main_successful_merge(sample_pdfs):
    """Test successful PDF merge."""
    temp_dir, pdf_files = sample_pdfs
    output_path = os.path.join(temp_dir, "merged.pdf")
    
    test_args = ["sst.pdf-merge", "--input"] + pdf_files + ["--output", output_path]
    
    with patch.object(sys, "argv", test_args):
        pdf_merge.main()
    
    assert os.path.exists(output_path)


def test_main_missing_input_file():
    """Test that missing input file causes exit."""
    test_args = ["sst.pdf-merge", "--input", "nonexistent.pdf", "--output", "out.pdf"]
    
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc_info:
            pdf_merge.main()
        assert exc_info.value.code == 1


def test_main_missing_arguments():
    """Test that missing required arguments cause exit."""
    test_args = ["sst.pdf-merge"]
    
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc_info:
            pdf_merge.main()
        assert exc_info.value.code == 2  # argparse exits with 2 for missing args
